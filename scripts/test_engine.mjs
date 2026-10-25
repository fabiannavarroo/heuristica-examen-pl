import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createSession,freshProgress,answer,finish,summary,validSession,eligible,metrics} from '../web/engine.mjs';
const bank=JSON.parse(readFileSync(new URL('../web/questions.json',import.meta.url)));
const seed=n=>()=>{n=(Math.imul(n,1664525)+1013904223)>>>0;return n/4294967296;};
for(const count of [1,2,3,10,20,30,60,359,360,bank.questions.length]){
 for(let i=1;i<=50;i++){
  const s=createSession(bank,freshProgress(),{count},seed(i));assert.equal(s.items.length,count);assert(validSession(bank,s));
  assert.equal(new Set(s.items.map(x=>x.questionId)).size,count);
  const letters=[0,0,0];for(const item of s.items){const q=bank.questions.find(q=>q.id===item.questionId);letters[item.optionIds.indexOf(q.correctId)]++;}
  assert(Math.max(...letters)-Math.min(...letters)<=1);
 }
}
const p=freshProgress();let s=createSession(bank,p,{count:20,mode:'exam'},seed(3));
const q=bank.questions.find(q=>q.id===s.items[0].questionId);const wrong=q.options.find(o=>o.id!==q.correctId).id;
assert(answer(bank,p,s,wrong));assert.equal(metrics(p).attempts,0,'No revelar ni calificar antes de terminar');
assert(answer(bank,p,s,q.correctId));s=JSON.parse(JSON.stringify(s));assert(validSession(bank,s));assert.equal(s.answers[q.id],q.correctId);
finish(bank,p,s);assert.deepEqual([summary(bank,s).correct,summary(bank,s).wrong,summary(bank,s).blank],[1,0,19]);assert.equal(p.sessions,1);finish(bank,p,s);assert.equal(p.sessions,1);assert.equal(metrics(p).attempts,1);
let practice=createSession(bank,p,{count:10,mode:'practice'},seed(4));const pq=bank.questions.find(q=>q.id===practice.items[0].questionId);const pw=pq.options.find(o=>o.id!==pq.correctId).id;
answer(bank,p,practice,pw);assert(p.questions[pq.id].wrong);assert(!answer(bank,p,practice,pq.correctId),'No modificar una práctica ya corregida');
let retry=createSession(bank,p,{count:20,mode:'mistakes'},seed(9));assert.equal(retry.items.length,1);answer(bank,p,retry,pq.correctId);assert.equal(eligible(bank,p,{mode:'mistakes'}).length,0);
for(const topic of Object.keys(bank.topics)){
 const topicSession=createSession(bank,p,{topic,count:60},seed(7));assert.equal(topicSession.items.length,Math.min(60,bank.questions.filter(q=>q.topic===topic).length));assert(topicSession.items.every(i=>bank.questions.find(q=>q.id===i.questionId).topic===topic));
}
const seen=freshProgress();for(const q of bank.questions.slice(0,350))seen.questions[q.id]={attempts:3,correct:1,wrong:false};
const unseen=createSession(bank,seen,{count:10},seed(7));assert(unseen.items.every(i=>!seen.questions[i.questionId]),'Priorizar preguntas nuevas');
const broken=structuredClone(unseen);broken.items[0].optionIds=['c','c','a'];assert(!validSession(bank,broken));
const different=Array.from({length:30},(_,i)=>JSON.stringify(createSession(bank,freshProgress(),{count:20},seed(i+1)).items));assert.equal(new Set(different).size,30);
console.log('Motor: 500 sesiones de equilibrio, identidad al barajar, guardado/reanudación, corrección diferida, blancos, idempotencia, filtros y repaso verificados.');

for(const count of [20,30]){
 const exam=createSession(bank,freshProgress(),{count,mode:'exam'},seed(count));
 const counts={};let numeric=0;
 for(const item of exam.items){const q=bank.questions.find(q=>q.id===item.questionId);counts[q.topic]=(counts[q.topic]||0)+1;numeric+=Number(q.kind==='calculo');}
 assert.equal(Object.keys(counts).length,10);assert(Object.values(counts).every(n=>n===count/10));assert.equal(numeric,Math.floor(.3*count));
}
console.log('Simulacros generales: cobertura de los 10 temas y 70 % concepto / 30 % aplicación.');

const past=eligible(bank,freshProgress(),{mode:'past'});
assert.equal(past.length,60);
assert(past.every(q=>q.pastExam&&q.sources.length));
const coverage=bank.pastExams.coverage;
assert.equal(coverage.length,147);
assert.equal(new Set(coverage.map(e=>e.key)).size,147);
assert.equal(new Set(coverage.map(e=>e.questionId)).size,60);
for(const [document,count] of Object.entries({A:20,B:37,C:60,D:30})){
 const entries=coverage.filter(e=>e.document===document);assert.equal(entries.length,count);
 const principal=entries.filter(e=>e.section==='principal');
 assert.deepEqual(principal.map(e=>e.number),Array.from({length:document==='B'?20:count},(_,i)=>i+1));
 if(document==='B')assert.deepEqual(entries.filter(e=>e.section==='extras').map(e=>e.number),Array.from({length:17},(_,i)=>i+1));
}
for(const entry of coverage){
 const q=bank.questions.find(q=>q.id===entry.questionId);
 assert(q?.pastExam&&q.sources.some(s=>s.key===entry.key));assert(q.revisionNote&&q.explanation);
}
for(let i=0;i<50;i++){
 const allPast=createSession(bank,freshProgress(),{mode:'past',count:'all'},seed(i));
 assert.equal(allPast.items.length,60);assert(validSession(bank,allPast));
 assert.deepEqual(new Set(allPast.items.map(i=>i.questionId)),new Set(past.map(q=>q.id)));
 const slots=[0,0,0];for(const item of allPast.items)slots[item.optionIds.indexOf(bank.questions.find(q=>q.id===item.questionId).correctId)]++;
 assert.deepEqual(slots,[20,20,20]);
}
const pastTopic=createSession(bank,freshProgress(),{mode:'past',topic:'dualidad',count:'all'},seed(3));
assert(pastTopic.items.every(it=>bank.questions.find(q=>q.id===it.questionId).topic==='dualidad'));
const savedPast=JSON.parse(JSON.stringify(createSession(bank,freshProgress(),{mode:'past',count:20},seed(11))));
const legacyProgress=freshProgress();assert(validSession(bank,savedPast));
const firstPast=bank.questions.find(q=>q.id===savedPast.items[0].questionId);
answer(bank,legacyProgress,savedPast,firstPast.correctId);
assert.equal(legacyProgress.questions[firstPast.id].correct,1,'Corrección inmediata en exámenes anteriores');
assert(validSession(bank,JSON.parse(JSON.stringify(savedPast))),'Reanudar el nuevo modo');
assert(bank.questions.filter(q=>!q.id.startsWith('anterior-')).length===360,'No eliminar IDs del banco previo');
console.log('Exámenes anteriores: 147 apariciones, 60 únicas, cobertura íntegra y 50 sesiones con todas, sin duplicados ni preguntas ajenas. Historial compatible.');

// La práctica completa ignora cualquier filtro o tamaño heredado y conserva el banco entero.
const fullProgress=freshProgress();
for(const q of bank.questions)fullProgress.questions[q.id]={attempts:2,correct:1,wrong:false};
assert.equal(eligible(bank,fullProgress,{mode:'complete',topic:'dualidad',difficulty:3}).length,bank.questions.length);
const full=createSession(bank,fullProgress,{mode:'complete',topic:'dualidad',difficulty:3,count:20},seed(2026));
assert.equal(full.items.length,bank.questions.length);
assert.equal(full.topic,'all');assert.equal(full.difficulty,'all');
assert.deepEqual(new Set(full.items.map(i=>i.questionId)),new Set(bank.questions.map(q=>q.id)));
assert.equal(full.items.filter(i=>bank.questions.find(q=>q.id===i.questionId).pastExam).length,60);
const fullLetters=[0,0,0];
for(const i of full.items)fullLetters[i.optionIds.indexOf(bank.questions.find(q=>q.id===i.questionId).correctId)]++;
assert.deepEqual(fullLetters,[124,124,124]);
const fullFirst=bank.questions.find(q=>q.id===full.items[0].questionId);
assert(answer(bank,fullProgress,full,fullFirst.correctId));
assert(full.checked[fullFirst.id],'Corrección inmediata, sin esperar al final');
assert.equal(fullProgress.questions[fullFirst.id].attempts,3);
assert(!answer(bank,fullProgress,full,fullFirst.options.find(o=>o.id!==fullFirst.correctId).id));
full.index=360;
const savedFull=JSON.parse(JSON.stringify(full));assert(validSession(bank,savedFull));
assert.equal(savedFull.index,360);assert.deepEqual(savedFull.items,full.items);
assert.equal(savedFull.answers[fullFirst.id],fullFirst.correctId);
finish(bank,fullProgress,savedFull);
assert.deepEqual([summary(bank,savedFull).correct,summary(bank,savedFull).blank],[1,371]);
console.log('Práctica completa: 372 preguntas, 60 anteriores incluidas, ninguna repetida, letras 124/124/124, corrección inmediata y reanudación.');
