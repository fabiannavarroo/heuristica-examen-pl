import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createSession,freshProgress,answer,finish,summary,validSession,eligible,metrics} from '../web/engine.mjs';
const bank=JSON.parse(readFileSync(new URL('../web/questions.json',import.meta.url)));
const seed=n=>()=>{n=(Math.imul(n,1664525)+1013904223)>>>0;return n/4294967296;};
for(const count of [1,2,3,10,20,30,60,359,360]){
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
 const topicSession=createSession(bank,p,{topic,count:60},seed(7));assert.equal(topicSession.items.length,36);assert(topicSession.items.every(i=>bank.questions.find(q=>q.id===i.questionId).topic===topic));
}
const seen=freshProgress();for(const q of bank.questions.slice(0,350))seen.questions[q.id]={attempts:3,correct:1,wrong:false};
const unseen=createSession(bank,seen,{count:10},seed(7));assert(unseen.items.every(i=>!seen.questions[i.questionId]),'Priorizar preguntas nuevas');
const broken=structuredClone(unseen);broken.items[0].optionIds=['c','c','a'];assert(!validSession(bank,broken));
const different=Array.from({length:30},(_,i)=>JSON.stringify(createSession(bank,freshProgress(),{count:20},seed(i+1)).items));assert.equal(new Set(different).size,30);
console.log('Motor: 450 sesiones de equilibrio, identidad al barajar, guardado/reanudación, corrección diferida, blancos, idempotencia, filtros y repaso verificados.');

for(const count of [20,30]){
 const exam=createSession(bank,freshProgress(),{count,mode:'exam'},seed(count));
 const counts={};let numeric=0;
 for(const item of exam.items){const q=bank.questions.find(q=>q.id===item.questionId);counts[q.topic]=(counts[q.topic]||0)+1;numeric+=Number(q.kind==='calculo');}
 assert.equal(Object.keys(counts).length,10);assert(Object.values(counts).every(n=>n===count/10));assert.equal(numeric,Math.floor(.3*count));
}
console.log('Simulacros generales: cobertura de los 10 temas y 70 % concepto / 30 % aplicación.');
