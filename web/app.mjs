import {freshProgress,eligible,createSession,answer,finish,summary,validSession,metrics} from './engine.mjs';
const KEY='criterio-pl-v1';
const main=document.getElementById('main');
const notice=document.getElementById('notice');
const escape=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const difficulty={1:'Fundamentos',2:'Aplicación',3:'Reto'};
let bank,progress=freshProgress(),session=null,screen='home';
let config={mode:'practice',topic:'all',difficulty:'all',count:20};
let reviewOnlyWrong=false,canStore=true;
function message(text){notice.hidden=!text;notice.textContent=text;}
function save(){
 try{localStorage.setItem(KEY,JSON.stringify({progress,session}));}
 catch{canStore=false;message('El navegador no permite guardar el historial. Puedes seguir practicando durante esta visita.');}
}
function load(){
 try{
  const raw=localStorage.getItem(KEY);if(!raw)return;
  const data=JSON.parse(raw);
  if(data.progress?.version===1 && data.progress.questions && typeof data.progress.questions==='object' && !Array.isArray(data.progress.questions)){
   const p=freshProgress();p.sessions=Number.isInteger(data.progress.sessions)?Math.max(0,data.progress.sessions):0;
   const ids=new Set(bank.questions.map(q=>q.id));
   for(const [id,q] of Object.entries(data.progress.questions)){
    if(ids.has(id)&&Number.isInteger(q?.attempts)&&q.attempts>=0&&Number.isInteger(q.correct)&&q.correct>=0&&q.correct<=q.attempts)
     p.questions[id]={attempts:q.attempts,correct:q.correct,wrong:!!q.wrong,lastAt:Number(q.lastAt)||0};
   }progress=p;
  }
  if(validSession(bank,data.session))session=data.session;
 }catch{message('No se ha podido leer el historial anterior. Puedes empezar una sesión nueva.');}
}
function focusMain(){main.focus({preventScroll:true});window.scrollTo({top:0,behavior:'instant'});}
function navigate(next){screen=next;render();focusMain();}
function el(id){return document.getElementById(id);}
const graph=`<svg class="hero-figure" viewBox="0 0 240 180" role="img" aria-label="Región factible y un vértice óptimo de ejemplo"><path d="M24 146H224M24 146V12" fill="none" stroke="currentColor" stroke-width=".8" opacity=".45"/><path d="M24 146H162V92L24 30Z" fill="#e1e9dc" stroke="currentColor" stroke-width="1.2"/><path d="M162 146V25M24 30L219 119M85 28L185 146" fill="none" stroke="currentColor" stroke-width=".7" opacity=".4" stroke-dasharray="4 4"/><circle cx="162" cy="92" r="4" fill="currentColor"/><path d="M168 87L194 60" fill="none" stroke="currentColor" stroke-width=".8"/><text x="194" y="51" font-family="Georgia,serif" font-size="16" fill="currentColor">x*</text><text x="211" y="162" font-family="Georgia,serif" font-size="12" fill="currentColor">x₁</text><text x="10" y="18" font-family="Georgia,serif" font-size="12" fill="currentColor">x₂</text><text x="64" y="125" font-family="Georgia,serif" font-size="13" fill="currentColor">Ax ≤ b</text><text x="61" y="177" font-family="monospace" font-size="8" fill="currentColor" opacity=".7">ENCUENTRA TU PUNTO ÓPTIMO</text></svg>`;
function home(){
 const m=metrics(progress);const pool=eligible(bank,progress,config);
 const pending=session&&!session.finished;
 const description={practice:'Responde y entiende la explicación al momento. Puedes elegir un tema o mezclar todo el bloque.',exam:'Como en un test: responde, revisa tus elecciones y consulta la corrección al finalizar.',mistakes:'Vuelve a las preguntas que fallaste. Un acierto las retira de tus pendientes.'}[config.mode];
 main.innerHTML=`
 <section class="hero" aria-labelledby="home-title"><div><p class="eyebrow">Tu mesa de estudio · Programación lineal</p><h1 id="home-title">Una sesión para<br><em>entenderlo mejor.</em></h1><p>360 preguntas explicadas, desde el primer modelo hasta la última cota.<br>Elige tu ritmo. Cada respuesta tiene algo que enseñarte.</p></div>${graph}</section>
 <div class="stats-strip" aria-label="Tu progreso"><div class="stat"><strong>${m.seen}<span style="display:inline;font-size:14px"> / 360</span></strong><span>preguntas practicadas</span></div><div class="stat"><strong>${m.attempts?m.accuracy+' %':'—'}</strong><span>aciertos históricos</span></div><div class="stat"><strong>${m.mistakes}</strong><span>fallos por repasar</span></div><button class="small-link" id="reset">Reiniciar historial</button></div>
 ${pending?`<div class="resume"><p><strong>Tu sesión sigue aquí</strong>${session.mode==='exam'?'Simulacro':'Práctica'} · pregunta ${session.index+1} de ${session.items.length} · orden conservado</p><button class="button small" id="resume">Continuar →</button></div>`:''}
 <div class="workspace"><section class="sheet" aria-labelledby="session-title"><p class="section-label">01 · Prepara tu sesión</p><h2 id="session-title">¿Qué quieres practicar?</h2>
 <div class="mode-tabs" role="group" aria-label="Modo de estudio">${[['practice','Práctica libre'],['exam','Simulacro'],['mistakes','Mis fallos']].map(([v,t])=>`<button class="mode-tab" data-mode="${v}" aria-pressed="${v===config.mode}">${t}${v==='mistakes'&&m.mistakes?' · '+m.mistakes:''}</button>`).join('')}</div>
 <p class="mode-description">${description}</p>
 <fieldset class="field"><legend>Contenido</legend><div class="topic-pills"><button class="pill" data-topic="all" aria-pressed="${config.topic==='all'}">Todo el bloque</button>${Object.entries(bank.topics).map(([id,name])=>`<button class="pill" data-topic="${id}" aria-pressed="${config.topic===id}">${escape(name)}</button>`).join('')}</div></fieldset>
 <div class="controls-row"><fieldset class="field"><legend>Preguntas</legend><div class="segmented">${(config.mode==='exam'?[20,30]:[10,20,30,60]).map(n=>`<button data-count="${n}" aria-pressed="${config.count===n}">${n}</button>`).join('')}</div></fieldset><fieldset class="field"><legend>Dificultad</legend><div class="segmented">${[['all','Todas'],['1','Base'],['2','Media'],['3','Reto']].map(([id,t])=>`<button data-difficulty="${id}" aria-pressed="${String(config.difficulty)===id}">${t}</button>`).join('')}</div></fieldset></div>
 <p class="available">${pool.length?`${pool.length} disponibles · sesión de ${Math.min(config.count,pool.length)} · sin repeticiones`:config.mode==='mistakes'?'No hay fallos pendientes con estos filtros. Prueba otros temas o vuelve a práctica libre.':'No hay preguntas con esta combinación. Cambia el tema o la dificultad.'}</p>
 <button class="button wide" id="start" ${!pool.length?'disabled':''}><span>${pending?'Empezar una sesión nueva':config.mode==='mistakes'?'Repasar mis fallos':config.mode==='exam'?'Empezar simulacro':'Empezar a practicar'}</span><span aria-hidden="true">↗</span></button>
 <p class="focus-note">${pending?'Empezar otra sesión sustituirá la que tienes guardada. El historial de respuestas se conserva.':'Las preguntas menos practicadas tienen prioridad. Las opciones cambian de posición en cada sesión.'}</p>
 </section>
 <aside class="aside" aria-label="Mapa de estudio"><p class="section-label">02 · Tu recorrido</p><h2>Concepto a concepto</h2>
 ${Object.entries(bank.topics).map(([id,name])=>{const all=bank.questions.filter(q=>q.topic===id);const seen=all.filter(q=>progress.questions[q.id]?.attempts).length;return `<div class="topic-row"><div class="topic-info"><span>${escape(name)}</span><small>${seen} / ${all.length}</small></div><div class="topic-track" role="progressbar" aria-label="${escape(name)} practicadas" aria-valuenow="${seen}" aria-valuemin="0" aria-valuemax="${all.length}"><span style="width:${seen/all.length*100}%"></span></div></div>`;}).join('')}
 <p class="aside-note">El recorrido cuenta preguntas distintas respondidas. Los fallos pendientes se retiran al acertarlos en un nuevo intento.</p>
 <div class="pdf-card"><div class="pdf-icon" aria-hidden="true">PDF</div><div><h3>Tu guía, de principio a fin</h3><p>65 páginas · teoría · 32 ejercicios · 3 tests</p><a href="./guia-programacion-lineal.pdf" download>Descargar guía de estudio ↗</a></div></div>
 </aside></div>`;
 el('start').onclick=()=>{session=createSession(bank,progress,config);if(session){save();navigate('session');}};
 if(pending)el('resume').onclick=()=>navigate('session');
 el('reset').onclick=()=>el('reset-dialog').showModal();
 main.querySelectorAll('[data-mode]').forEach(b=>b.onclick=()=>{config.mode=b.dataset.mode;if(config.mode==='exam'&&![20,30].includes(config.count))config.count=20;home();});
 main.querySelectorAll('[data-topic]').forEach(b=>b.onclick=()=>{config.topic=b.dataset.topic;home();});
 main.querySelectorAll('[data-count]').forEach(b=>b.onclick=()=>{config.count=Number(b.dataset.count);home();});
 main.querySelectorAll('[data-difficulty]').forEach(b=>b.onclick=()=>{config.difficulty=b.dataset.difficulty;home();});
}
function currentQuestion(){return bank.questions.find(q=>q.id===session.items[session.index].questionId);}
function reference(q){const sec=Number(q.reference.match(/apartado (\d+)/)?.[1]||3);const page={3:5,4:6,5:7,6:8,7:10,8:11,10:13,11:14,13:16,14:17}[sec]||5;return `<a class="reference" href="./guia-programacion-lineal.pdf#page=${page}" target="_blank" rel="noopener">${escape(q.reference)} · abrir PDF ↗</a>`;}
function sessionView(){
 if(!session){navigate('home');return;}if(session.finished){screen='results';results();return;}
 const q=currentQuestion(),item=session.items[session.index],selected=session.answers[q.id],checked=session.mode!=='exam'&&session.checked[q.id];
 const options=item.optionIds.map(id=>q.options.find(o=>o.id===id));
 const responded=Object.keys(session.answers).length;
 main.innerHTML=`<div class="session-top"><button class="small-link" id="save-exit">← Guardar y salir</button><span class="session-label">${session.mode==='exam'?'Simulacro · corrección al finalizar':session.mode==='mistakes'?'Repaso de fallos':'Práctica libre'}</span></div>
 <progress max="${session.items.length}" value="${responded}" aria-label="Preguntas respondidas"></progress>
 <div class="session-layout"><div><article class="sheet question-sheet" aria-labelledby="question-title"><div class="question-meta"><span>${escape(bank.topics[q.topic])}</span><span>${difficulty[q.difficulty]} · ${session.index+1} / ${session.items.length}</span></div><h1 id="question-title">${escape(q.prompt)}</h1>
 <fieldset class="options"><legend>Elige una respuesta</legend><div role="radiogroup" aria-labelledby="question-title">${options.map((o,i)=>{
 const isCorrect=o.id===q.correctId;const chosen=o.id===selected;let state=checked?(isCorrect?'correct':chosen?'incorrect':''):'';
 return `<button class="option ${state}" style="margin-bottom:12px" role="radio" aria-checked="${chosen}" data-answer="${o.id}" ${checked?'disabled':''}><span class="option-letter">${'ABC'[i]}</span><span>${escape(o.text)}</span>${checked&&isCorrect?'<span class="result-symbol" aria-label="Correcta">✓</span>':checked&&chosen?'<span class="result-symbol" aria-label="Incorrecta">×</span>':''}</button>`;
 }).join('')}</div></fieldset>
 ${checked?`<section class="feedback" role="status" aria-label="Corrección"><h2>${selected===q.correctId?'✓ Bien razonado.':'Vamos a aclararlo.'}</h2><p>${escape(q.explanation)}</p>${reference(q)}<details class="rationales"><summary>Por qué se descarta cada opción</summary>${options.map((o,i)=>`<p><strong>${'ABC'[i]}.</strong> ${escape(q.rationales[o.id])}</p>`).join('')}</details></section>`:session.mode==='exam'?'<p class="focus-note">Puedes cambiar tu respuesta. Las soluciones se muestran al terminar.</p>':''}
 </article><div class="session-actions"><button class="button secondary" id="prev" ${!session.index?'disabled':''}>← Anterior</button><div class="right">${session.index<session.items.length-1?'<button class="button secondary" id="end-early">Terminar</button>':''}<button class="button" id="next">${session.index===session.items.length-1?'Ver resultados':selected?'Siguiente →':'Dejar en blanco →'}</button></div></div></div>
 <aside><section class="sheet navigator"><h2>Tu hoja de respuestas</h2><div class="question-grid">${session.items.map((it,i)=>{
  const chosen=session.answers[it.questionId];const question=bank.questions.find(q=>q.id===it.questionId);const iswrong=session.mode!=='exam'&&session.checked[it.questionId]&&chosen!==question.correctId;
  return `<button data-index="${i}" class="${i===session.index?'current ':''}${chosen?'answered ':''}${iswrong?'wrong':''}" aria-label="Pregunta ${i+1}${chosen?', respondida':', en blanco'}" ${i===session.index?'aria-current="step"':''}>${i+1}</button>`;
 }).join('')}</div><p><strong>${responded} de ${session.items.length}</strong> respondidas.<br>Puedes volver a cualquier pregunta desde aquí.</p><p>${session.mode==='exam'?'El color indica que has respondido, sin revelar si has acertado.':'Verde: acertada. Rojo: fallada. Sin color: pendiente.'}</p></section><div class="scratch">${session.mode==='exam'?'Lee las hipótesis.<br>Comprueba las unidades.<br>Revisa antes de terminar.':'rⱼ = zⱼ − cⱼ<br>Δz = −rⱼ · θ<br>Una regla, un paso cada vez.'}</div></aside></div>`;
 el('save-exit').onclick=()=>{save();navigate('home');};
 el('prev').onclick=()=>{session.index--;save();sessionView();focusMain();};
 el('next').onclick=()=>{if(session.index===session.items.length-1){finish(bank,progress,session);save();navigate('results');}else{session.index++;save();sessionView();focusMain();}};
 if(el('end-early'))el('end-early').onclick=()=>showFinishCheck();
 main.querySelectorAll('[data-answer]').forEach(b=>b.onclick=()=>{
   if(answer(bank,progress,session,b.dataset.answer)){save();sessionView();const chosen=main.querySelector(`[data-answer="${b.dataset.answer}"]`);if(session.mode==='exam')chosen?.focus();else el('next').focus({preventScroll:true});}
 });
 // Teclado de grupos radio: flechas recorren opciones; Enter/Espacio responden.
 main.querySelectorAll('[data-answer]').forEach((b,i,buttons)=>b.onkeydown=event=>{
  if(['ArrowDown','ArrowRight','ArrowUp','ArrowLeft'].includes(event.key)){
   event.preventDefault();const step=['ArrowDown','ArrowRight'].includes(event.key)?1:-1;buttons[(i+step+buttons.length)%buttons.length].focus();
  }
 });
 main.querySelectorAll('[data-index]').forEach(b=>b.onclick=()=>{session.index=Number(b.dataset.index);save();sessionView();focusMain();});
}
function showFinishCheck(){
 const blank=session.items.length-Object.keys(session.answers).length;
 const old=el('finish-check');if(old){old.remove();return;}
 const section=document.createElement('section');section.id='finish-check';section.className='resume';section.setAttribute('aria-label','Confirmar finalización');
 section.innerHTML=`<p><strong>Terminar esta sesión</strong>${blank?`Quedan ${blank} preguntas sin responder. Se contarán como blancas.`:'Ya has respondido todas las preguntas.'}</p><button class="button small" id="finish-now">Terminar y corregir</button>`;
 main.prepend(section);el('finish-now').onclick=()=>{finish(bank,progress,session);save();navigate('results');};el('finish-now').focus();
}
function results(){
 if(!session?.finished){navigate(session?'session':'home');return;}
 const s=summary(bank,session);
 const errors=session.items.filter(it=>session.answers[it.questionId]!==bank.questions.find(q=>q.id===it.questionId).correctId);
 const shown=reviewOnlyWrong?errors:session.items;
 main.innerHTML=`<section class="result-heading"><p class="eyebrow">Sesión completada</p><h1>${s.correct===s.total?'Todo encaja.':s.wrong?'Ya sabes por dónde seguir.':'Un paso más en tu recorrido.'}</h1><p>${s.correct} aciertos de ${s.total} preguntas. Revisa el razonamiento y vuelve a las ideas que aún te cuestan.</p></section>
 <div class="result-stats"><div><strong>${s.correct}</strong><span>Aciertos</span></div><div><strong>${s.wrong}</strong><span>Fallos</span></div><div><strong>${s.blank}</strong><span>En blanco</span></div><div><strong>${Math.round(100*s.correct/s.total)} %</strong><span>Sobre el total</span></div></div>
 <p class="focus-note">Esta cifra es de repaso. No aplica una penalización ni una nota oficial que no se ha confirmado.</p>
 <div class="session-actions"><button id="back-home" class="button secondary">← Volver al estudio</button><button id="retry-mistakes" class="button" ${!metrics(progress).mistakes?'disabled':''}>Repasar fallos pendientes →</button></div>
 <div class="result-by-topic" aria-label="Resultados por tema">${Object.entries(s.topics).map(([t,v])=>`<span>${escape(bank.topics[t])} · ${v.correct}/${v.correct+v.wrong+v.blank}</span>`).join('')}</div>
 <div class="result-toolbar"><h2>Lo que te llevas de esta sesión</h2><button id="toggle-review" class="pill" aria-pressed="${reviewOnlyWrong}">${reviewOnlyWrong?'Mostrar todas':'Solo fallos y blancos'} · ${errors.length}</button></div>
 ${shown.length?shown.map(it=>{
  const q=bank.questions.find(q=>q.id===it.questionId);const chosen=session.answers[q.id];const number=session.items.indexOf(it)+1;
  return `<article class="sheet review-card"><div class="question-meta"><span>${number}. ${escape(bank.topics[q.topic])}</span><span>${!chosen?'En blanco':chosen===q.correctId?'✓ Acertada':'× Fallada'}</span></div><h3>${escape(q.prompt)}</h3>${it.optionIds.map((id,i)=>{
   const o=q.options.find(o=>o.id===id);return `<div class="review-option ${id===q.correctId?'correct':id===chosen?'incorrect':''}"><strong>${'ABC'[i]}.</strong> ${escape(o.text)} ${id===q.correctId?' · ✓ Correcta':''}${id===chosen?' · Tu respuesta':''}</div>`;
  }).join('')}<p class="explanation">${escape(q.explanation)}</p><details class="rationales"><summary>Explicación de las tres opciones</summary>${it.optionIds.map((id,i)=>`<p><strong>${'ABC'[i]}.</strong> ${escape(q.rationales[id])}</p>`).join('')}</details>${reference(q)}</article>`;
 }).join(''):'<p class="empty">No hay fallos ni blancos en esta sesión. Puedes seguir con otro tema.</p>'}`;
 el('back-home').onclick=()=>navigate('home');
 el('retry-mistakes').onclick=()=>{config={mode:'mistakes',topic:'all',difficulty:'all',count:20};session=createSession(bank,progress,config);if(session){save();navigate('session');}};
 el('toggle-review').onclick=()=>{reviewOnlyWrong=!reviewOnlyWrong;results();};
}
function render(){if(screen==='session')sessionView();else if(screen==='results')results();else home();}
el('nav-study').onclick=()=>{save();navigate('home');};
el('cancel-reset').onclick=()=>el('reset-dialog').close();
el('confirm-reset').onclick=()=>{progress=freshProgress();session=null;config={mode:'practice',topic:'all',difficulty:'all',count:20};save();el('reset-dialog').close();message(canStore?'Historial reiniciado. Tienes toda la práctica por delante.':'');navigate('home');};
try{
 const response=await fetch('./questions.json');if(!response.ok)throw new Error('HTTP '+response.status);
 bank=await response.json();if(!Array.isArray(bank.questions)||bank.questions.length!==360)throw new Error('Banco incompleto');
 load();render();
}catch{
 main.innerHTML='<section class="sheet"><h1>No se ha podido cargar la práctica</h1><p>Comprueba tu conexión y vuelve a intentarlo. La guía de estudio sigue disponible.</p><button class="button" id="reload">Volver a cargar</button> <a class="button secondary" href="./guia-programacion-lineal.pdf">Abrir PDF</a></section>';
 el('reload').onclick=()=>location.reload();
}
