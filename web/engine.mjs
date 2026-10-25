export const VERSION = 1;
export const freshProgress = () => ({ version: VERSION, questions: {}, sessions: 0 });
export function shuffle(items, random = Math.random) {
  const a = [...items];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}
export function eligible(bank, progress, { mode = 'practice', topic = 'all', difficulty = 'all' } = {}) {
  return bank.questions.filter(q => (mode === 'complete' || topic === 'all' || q.topic === topic) &&
    (mode === 'complete' || difficulty === 'all' || q.difficulty === Number(difficulty)) &&
    (mode !== 'mistakes' || progress.questions[q.id]?.wrong) &&
    (mode !== 'past' || q.pastExam === true));
}
export function createSession(bank, progress, config = {}, random = Math.random) {
  const mode = config.mode || 'practice';
  if (mode === 'complete') config = {...config, topic:'all', difficulty:'all', count:'all'};
  const pool = eligible(bank, progress, config);
  if (!pool.length) return null;
  const size = Math.min(Math.max(1, (config.count === 'all' ? pool.length : Number(config.count)) || 20), pool.length);
  // Primero las menos practicadas; Fisher–Yates rompe empates sin sesgo estable.
  const prioritized = shuffle(pool, random).sort((a,b) =>
    (progress.questions[a.id]?.attempts || 0) - (progress.questions[b.id]?.attempts || 0));
  let chosen = prioritized.slice(0,size);
  // Un simulacro general de 20/30 cubre los diez temas: 2/3 por tema.
  if (mode === 'exam' && (config.topic || 'all') === 'all' && [20,30].includes(size)) {
    const topics = shuffle(Object.keys(bank.topics),random);
    const perTopic = size / topics.length;
    if (Number.isInteger(perTopic) && topics.every(t=>pool.filter(q=>q.topic===t).length>=perTopic)) {
      const calculationTopics = new Set(topics.slice(0,Math.floor(size*.3)));
      chosen = topics.flatMap(t=>{
        const list = prioritized.filter(q=>q.topic===t);
        if ((config.difficulty || 'all') !== 'all') return list.slice(0,perTopic);
        const nCalc = calculationTopics.has(t) ? 1 : 0;
        return [...list.filter(q=>q.kind==='concepto').slice(0,perTopic-nCalc),
          ...list.filter(q=>q.kind==='calculo').slice(0,nCalc)];
      });
    }
  }
  const extras = shuffle([0,1,2],random).slice(0,size%3);
  const positions = shuffle(Array.from({length:size}, (_,i) => i < size - size%3 ? i%3 : extras[i-(size-size%3)]),random);
  const items = shuffle(chosen,random).map((q,i) => {
    const options = shuffle(q.options.filter(o => o.id !== q.correctId),random);
    options.splice(positions[i],0,q.options.find(o => o.id===q.correctId));
    return { questionId: q.id, optionIds: options.map(o=>o.id) };
  });
  return { version:VERSION, mode, topic:config.topic||'all', difficulty:config.difficulty||'all',
    id:`session-${Date.now()}-${Math.floor(random()*1e9)}`, items, answers:{}, checked:{},
    index:0, finished:false, counted:false, startedAt:Date.now() };
}
export function recordQuestion(progress, session, q, choice) {
  if (session.checked[q.id]) return;
  if (choice) {
    const old = progress.questions[q.id] || { attempts:0, correct:0, wrong:false };
    const correct = choice === q.correctId;
    progress.questions[q.id] = { attempts:old.attempts+1, correct:old.correct+Number(correct),
      wrong:!correct, lastAt:Date.now() };
  }
  session.checked[q.id] = true;
}
export function answer(bank, progress, session, optionId) {
  if (session.finished) return false;
  const q = bank.questions.find(q=>q.id===session.items[session.index].questionId);
  if (!q.options.some(o=>o.id===optionId)) return false;
  if (session.mode !== 'exam' && session.checked[q.id]) return false;
  session.answers[q.id] = optionId;
  if (session.mode !== 'exam') recordQuestion(progress,session,q,optionId);
  return true;
}
export function finish(bank, progress, session) {
  if (session.finished) return;
  for (const item of session.items) {
    const q = bank.questions.find(q=>q.id===item.questionId);
    recordQuestion(progress,session,q,session.answers[q.id]);
  }
  session.finished=true;
  session.finishedAt=Date.now();
  if (!session.counted) { progress.sessions++; session.counted=true; }
}
export function summary(bank,session) {
  let correct=0,wrong=0,blank=0;
  const topics={};
  for (const {questionId} of session.items) {
    const q=bank.questions.find(q=>q.id===questionId);const selected=session.answers[q.id];
    const state=!selected?'blank':selected===q.correctId?'correct':'wrong';
    if(state==='correct')correct++;else if(state==='wrong')wrong++;else blank++;
    topics[q.topic] ||= {correct:0,wrong:0,blank:0};topics[q.topic][state]++;
  }
  return {correct,wrong,blank,total:session.items.length,topics};
}
export function validSession(bank,s) {
  if(!s || s.version!==VERSION || !['practice','exam','mistakes','past','complete'].includes(s.mode) || !Array.isArray(s.items) || !s.items.length || s.items.length>bank.questions.length) return false;
  if(!Number.isInteger(s.index) || s.index<0 || s.index>=s.items.length || !s.answers || !s.checked) return false;
  const map=new Map(bank.questions.map(q=>[q.id,q]));const ids=new Set();
  return s.items.every(item=>{
    const q=map.get(item.questionId);if(!q || ids.has(q.id))return false;ids.add(q.id);
    const opts=item.optionIds;
    return Array.isArray(opts) && opts.length===3 && new Set(opts).size===3 && opts.every(id=>q.options.some(o=>o.id===id)) &&
      (!s.answers[q.id] || opts.includes(s.answers[q.id]));
  });
}
export function metrics(progress) {
  const entries=Object.values(progress.questions);
  const attempts=entries.reduce((s,q)=>s+q.attempts,0),correct=entries.reduce((s,q)=>s+q.correct,0);
  return {seen:entries.filter(q=>q.attempts>0).length, attempts, correct,
    accuracy:attempts?Math.round(correct*100/attempts):0, mistakes:entries.filter(q=>q.wrong).length};
}
