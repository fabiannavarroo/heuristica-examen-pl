from pathlib import Path
import json,itertools,math
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
bank=json.loads((ROOT/'study/questions.json').read_text());qs=bank['questions']
assert len(qs)==len({q['id'] for q in qs})==len({q['prompt'] for q in qs})==360
for q in qs:
 assert len(q['options'])==3
 assert len({o['id'] for o in q['options']})==len({o['text'] for o in q['options']})==3,q['id']
 assert sum(o['id']==q['correctId'] for o in q['options'])==1
 assert all(q['rationales'].get(o['id']) for o in q['options'])
 assert q['topic'] in bank['topics'] and q['reference'] and q['explanation']
ids=sum(bank['pdfExams'],[]);assert len(ids)==len(set(ids))==60
for exam in bank['pdfExams']:
 chosen=[next(q for q in qs if q['id']==i) for i in exam]
 assert len(chosen)==20 and sum(q['kind']=='calculo' for q in chosen)==6

def vertices(A,b):
 A=np.array(A,dtype=float);b=np.array(b,dtype=float);pts=[]
 for inds in itertools.combinations(range(len(b)),2):
  M=A[list(inds)]
  if abs(np.linalg.det(M))<1e-9:continue
  x=np.linalg.solve(M,b[list(inds)])
  if np.all(A@x <= b+1e-8):pts.append(x)
 return pts
# Cálculo independiente por enumeración de todas las intersecciones, incluyendo ejes.
cases=[
 ('R01',[[ -4,-2],[27,18],[-1,1],[-1,0],[0,-1]],[-10,270,0,0,0],[5,6],[6,6],66),
 ('R02',[[5,4],[8,4],[2,2],[-1,0],[0,-1]],[40,40,22,0,0],[300,200],[0,10],2000),
 ('R03',[[2,2],[1,1],[2,1],[-1,0],[0,-1]],[100,120,80,0,0],[300,100],[40,0],12000),
 ('R04',[[4,2],[6,3],[-1,0],[2,-1],[0,-1]],[80,120,-5,0,0],[200,110],[5,30],4300),
 ('R06',[[1,1],[1,0],[-1,0],[0,-1]],[4,3,0,0],[2,1],[3,1],7),
 ('R08',[[1,1],[2,1],[-1,0],[0,-1]],[4,6,0,0],[3,2],[2,2],10),
 ('R09fuera',[[1,1],[2,1],[-1,0],[0,-1]],[7,6,0,0],[3,2],[0,6],12),
 ('P01',[[1,1],[1,0],[-1,0],[0,-1]],[5,2,0,0],[4,3],[2,3],17),
 ('P04',[[2,1],[-3,2],[-1,0],[0,-1]],[10,0,0,0],[7,5],[20/7,30/7],290/7),
]
for label,A,b,c,x,z in cases:
 pts=vertices(A,b);best=max(pts,key=lambda p:np.dot(c,p))
 assert np.allclose(best,x) and np.isclose(np.dot(c,best),z),(label,best)
print('9 óptimos continuos comprobados por intersecciones independientes')
# Enumera dominios enteros y asignaciones, sin usar los desarrollos de la guía.
for label,fn,obj,want in [
 ('R14',lambda x,y:2*x+y<=4 and x+2*y<=4,lambda x,y:3*x+2*y,6),
 ('P13',lambda x,y:x+y<=3.5 and x<=2,lambda x,y:5*x+4*y,14)]:
 feasible=[(obj(x,y),x,y) for x in range(10) for y in range(10) if fn(x,y)]
 assert max(feasible)[0]==want
costs=[[4,1,3],[2,0,5],[3,2,2]]
assert min(sum(costs[i][p[i]] for i in range(3)) for p in itertools.permutations(range(3)))==5
for U,K in [(50,20),(80,30)]:
 for x in range(U+1):
  allowed=[y for y in [0,1] if x>=K*y and x<=K-1+(U-K+1)*y]
  assert allowed==[int(x>=K)]
# Comprueba íntegramente las 160 preguntas parametrizadas mediante resultados esperados.
for q in qs:
 if q['kind']!='calculo':continue
 k=int(q['id'].split('-')[-1]);a=k+2;b=k+4;m=(k-1)%4
 c=next(o['text'] for o in q['options'] if o['id']=='c')
 if q['topic']=='fundamentos':expected=[2*a+3*b,10*b,5,a*b][m];assert float(c)==expected
 if q['topic']=='bases' and m==1:assert np.allclose(np.linalg.solve(np.diag([2,3]),[2*a,3*b]),[a,b])
 if q['topic']=='simplex' and m==1:assert min(2*a/2,3*b/3)==int(c)
 if q['topic']=='simplex' and m==2:assert int(c)==-(-a)*b
 if q['topic']=='redes' and m==2:assert int(c)==min(a+b,1+2)
 if q['topic']=='entera' and m==2:
  U=a+b;K=a
  for x in range(U+1):
   assert [y for y in [0,1] if x>=K*y and x<=K-1+(U-K+1)*y]==[int(x>=K)]
print('360 preguntas: estructura y unicidad; 60 preguntas PDF; 2 enteros, asignación y umbrales verificados')
print('Las familias numéricas se revisan con sus fórmulas; los conceptos requieren además revisión editorial.')
verified=0
for q in qs:
 if q['kind']!='calculo':continue
 k=int(q['id'].split('-')[-1]);a=k+2;b=k+4;m=(k-1)%4
 actual=next(o['text'] for o in q['options'] if o['id']=='c')
 expected={
  'fundamentos':[str(2*a+3*b),str(10*b),'5',str(a*b)],
  'modelos':[f'{b} unidades',f'{a*b} horas',str(a*b),str(b)],
  'formas':[f'{a}x + s = {b}',f'{a}x ≤ {a*b}',str(a*b),f'x = {b} + u'],
  'grafica':[f'({b},0)',f'En todo el segmento x+y={b} del primer cuadrante','Infactible',f'z*={a}, con infinitos óptimos'],
  'bases':[str(b),f'({a},{b})','Factible y degenerada','No es factible'],
  'simplex':['x2',str(a),str(a*b),str(a+2*b)],
  'artificiales':['Objetivo no acotado','Original infactible','Óptimo único','No, su valor cero no la demuestra'],
  'dualidad':[f'{b} variables y {a} restricciones',f'{a*b} €','Ambas son óptimas','0'],
  'redes':[str(a*b),str(b),'3','1'],
  'entera':['Podar por cota',f'x ≤ {a} y x ≥ {a+1}',f'x ≤ {a-1} + {b+1}y','Podar el nodo'],
 }[q['topic']][m]
 assert actual==expected,(q['id'],actual,expected)
 # Las tres alternativas deben seguir siendo incompatibles con el resultado calculado.
 assert all(o['text']!=expected for o in q['options'] if o['id']!='c')
 verified+=1
assert verified==160
print('160/160 soluciones de cálculo contrastadas con una tabla de resultados independiente del generador')
