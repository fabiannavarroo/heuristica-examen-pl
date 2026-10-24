from pathlib import Path
import re,json,random,html,hashlib
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether, Flowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.shapes import Drawing,Line,PolyLine,Polygon,String,Rect,Circle
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'output/pdf/guia-programacion-lineal.pdf'
import os
normal_font=os.environ.get('GUIDE_FONT','/System/Library/Fonts/Supplemental/Arial Unicode.ttf')
bold_font=os.environ.get('GUIDE_BOLD_FONT','/System/Library/Fonts/Supplemental/Arial Bold.ttf')
if not Path(normal_font).exists():normal_font='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
if not Path(bold_font).exists():bold_font='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
pdfmetrics.registerFont(TTFont('Study',normal_font))
pdfmetrics.registerFont(TTFont('StudyBold',bold_font))
pdfmetrics.registerFontFamily('Study',normal='Study',bold='StudyBold',italic='Study',boldItalic='StudyBold')
INK=colors.HexColor('#142d3f'); ACCENT=colors.HexColor('#087e8b'); LIGHT=colors.HexColor('#edf5f6')
styles={
 'body':ParagraphStyle('body',fontName='Study',fontSize=11.2,leading=16,spaceAfter=10,textColor=INK),
 'h1':ParagraphStyle('h1',fontName='StudyBold',fontSize=21,leading=26,spaceAfter=18,textColor=INK),
 'h2':ParagraphStyle('h2',fontName='StudyBold',fontSize=13.5,leading=18,spaceBefore=7,spaceAfter=8,textColor=ACCENT),
 'formula':ParagraphStyle('formula',fontName='Study',fontSize=11.2,leading=17,leftIndent=10,rightIndent=6,borderColor=ACCENT,borderWidth=1,borderPadding=7,backColor=LIGHT,spaceAfter=13),
 'small':ParagraphStyle('small',fontName='Study',fontSize=9.2,leading=12.4,textColor=INK,spaceAfter=5),
 'question':ParagraphStyle('question',fontName='StudyBold',fontSize=10.3,leading=13.5,textColor=INK,spaceAfter=4),
 'option':ParagraphStyle('option',fontName='Study',fontSize=10,leading=13,leftIndent=12,spaceAfter=2,textColor=INK),
 'answer':ParagraphStyle('answer',fontName='Study',fontSize=9.7,leading=13.3,spaceAfter=4,textColor=INK),
 'table':ParagraphStyle('table',fontName='Study',fontSize=9.4,leading=12.8,textColor=INK),
}
SUBS=dict(zip('₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎ᵢⱼₖₗₘₙₚₛₜₓᵧ','0123456789+-=()ijkl mnpstxy'.replace(' ','')))
SUPS={'ᵀ':'T','⁻':'-','⁺':'+','⁰':'0','¹':'1','²':'2','³':'3','⁴':'4','⁵':'5','⁶':'6','⁷':'7','⁸':'8','⁹':'9'}
def fmt(text):
 text=html.escape(text)
 text=re.sub('['+''.join(SUBS)+']+',lambda m:'<sub>'+''.join(SUBS[c] for c in m[0])+'</sub>',text)
 text=re.sub('['+''.join(SUPS)+']+',lambda m:'<super>'+''.join(SUPS[c] for c in m[0])+'</super>',text)
 return re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',text)
def para(t,key='body'):return Paragraph(fmt(t),styles[key])

def chart(kind):
 d=Drawing(470,205)
 if kind=='tree':
  nodes=[(235,178,'Raíz: (4/3,4/3), UB=20/3'),(115,110,'x≤1: (1;1,5), UB=6'),(355,110,'x≥2: (2,0), z=6'),(65,40,'y≤1: (1,1), z=5'),(205,40,'y≥2: (0,2), z=4')]
  for a,b in [(0,1),(0,2),(1,3),(1,4)]:
   x,y,_=nodes[a];xx,yy,_=nodes[b];d.add(Line(x,y-10,xx,yy+15,strokeColor=ACCENT))
  for ni,(x,y,t) in enumerate(nodes):
   width=260 if ni==0 else 205 if ni<3 else 130
   d.add(Rect(x-width/2,y-14,width,30,rx=6,fillColor=LIGHT,strokeColor=ACCENT));d.add(String(x,y-2,t,fontName='Study',fontSize=8.5,textAnchor='middle',fillColor=INK))
  return d
 ox,oy=45,25;sx=55;sy=35
 def xy(x,y):return ox+x*sx,oy+y*sy
 d.add(Line(*xy(0,0),*xy(6.5,0),strokeColor=INK));d.add(Line(*xy(0,0),*xy(0,4.7),strokeColor=INK))
 for n in range(1,7):d.add(String(*xy(n,-.35),str(n),fontName='Study',fontSize=8,textAnchor='middle'))
 for n in range(1,5):d.add(String(*xy(-.25,n),str(n),fontName='Study',fontSize=8,textAnchor='middle'))
 if kind=='basic':
  coords=[xy(0,0),xy(3,0),xy(3,1),xy(0,4)]
  d.add(Polygon([v for pt in coords for v in pt],fillColor=colors.HexColor('#cce9e5'),strokeColor=ACCENT))
  d.add(Line(*xy(0,4),*xy(4,0),strokeColor=ACCENT));d.add(Line(*xy(3,0),*xy(3,4.5),strokeColor=colors.HexColor('#c47735')))
  d.add(Line(*xy(1.4,4.2),*xy(3.5,0),strokeColor=INK,strokeDashArray=[4,3]))
  d.add(Circle(*xy(3,1),r=4,fillColor=INK));d.add(String(*xy(3.15,1.2),'(3,1), z=7',fontName='Study',fontSize=10,fillColor=INK))
  d.add(String(300,176,'x+y≤4; x≤3',fontName='Study',fontSize=10,fillColor=INK))
 else:
  d.add(Rect(*xy(2,0),width=4.3*sx,height=4.2*sy,fillColor=colors.HexColor('#e2f1ed'),strokeColor=None))
  d.add(Line(*xy(2,0),*xy(2,4.2),strokeColor=ACCENT,strokeWidth=2));d.add(String(*xy(2.2,3.8),'x≥2, y≥0',fontName='Study',fontSize=11,fillColor=INK))
  d.add(String(*xy(2.2,2.8),'min x = 2',fontName='StudyBold',fontSize=12,fillColor=INK));d.add(String(*xy(2.2,2),'Óptimo finito; región ilimitada',fontName='Study',fontSize=10,fillColor=INK))
 return d

bank=json.loads((ROOT/'study/questions.json').read_text()); snapshot=ROOT/'study/pdf-questions.json'
byid={q['id']:q for q in (json.loads(snapshot.read_text()) if snapshot.exists() else bank['questions'])}
exam_pages=[];exams_meta=[]
for e,ids in enumerate(bank['pdfExams']):
 rng=random.Random(841+e);slots=[i for i in range(3) for _ in range(6+int(i!=e))];rng.shuffle(slots);items=[]
 for qid,slot in zip(ids,slots):
  q=byid[qid];wrong=[o for o in q['options'] if o['id']!=q['correctId']];rng.shuffle(wrong)
  opts=wrong[:];opts.insert(slot,next(o for o in q['options'] if o['id']==q['correctId']))
  items.append({'question':q,'options':opts,'letter':'ABC'[slot]})
 for start in [0,10]:
  block=[f'# Simulacro {e+1} · preguntas {start+1}–{start+10}']
  for j,item in enumerate(items[start:start+10],start+1):
   q=item['question'];block.append(f"Q {j}. {q['prompt']}")
   for letter,o in zip('ABC',item['options']):block.append(f"O {letter}) {o['text']}")
  exam_pages.append('\n\n'.join(block))
 exams_meta.append(items)
# Todos los enunciados aparecen antes que cualquier solucionario.
for e,items in enumerate(exams_meta):
 for start in [0,5,10,15]:
  block=[f'# Solucionario {e+1} · preguntas {start+1}–{start+5}']
  for j,item in enumerate(items[start:start+5],start+1):
   q=item['question'];block.append(f"Q {j}. Correcta: {item['letter']}. {q['prompt']}")
   block.append(q['explanation'])
   for letter,o in zip('ABC',item['options']):
    if o['id']==q['correctId']:msg='Correcta: '+o['text']+'.'
    else:msg='Incorrecta: «'+o['text']+'». '+q['explanation']
    block.append('A '+letter+') '+msg)
   block.append('A '+q['reference']+'.')
  exam_pages.append('\n\n'.join(block))
(ROOT/'study/simulacros.md').write_text('\n---PAGE---\n'.join(exam_pages))
raw=(ROOT/'study/guia.md').read_text().replace('[[EXAMS]]','\n---PAGE---\n'.join(exam_pages))
raw=re.sub(r'(?m)^(#{1,2} .+)\n(?!\n)',r'\1\n\n',raw)
pages=[p.strip() for p in raw.split('---PAGE---')]
assert len(pages)==65,len(pages)
titles=[re.search(r'^# (.+)$',p,re.M).group(1) for p in pages]
contents=[(t,i+1) for i,t in enumerate(titles) if i>1 and not (t.startswith('R') or t.startswith('P') or t.startswith('Soluciones') or t.startswith('Simulacro') or t.startswith('Solucionario'))]
contents += [('Ejercicios resueltos R01–R16',titles.index('R01. Parcial de refrescos (2021, modelo 81)')+1),('Ejercicios propuestos P01–P16',37),('Soluciones de los propuestos',41),('Tres simulacros: 60 preguntas',46),('Solucionarios razonados',52)]
contents.sort(key=lambda x:x[1])
class GuideDoc(SimpleDocTemplate):
 def afterFlowable(self,flow):
  if isinstance(flow,Paragraph) and flow.style.name=='h1':
   t=flow.getPlainText();key='h'+hashlib.sha1(t.encode()).hexdigest()[:12];self.canv.bookmarkPage(key);self.canv.addOutlineEntry(t,key,level=0)

def footer(c,doc):
 c.setStrokeColor(ACCENT);c.setLineWidth(.7);c.line(44,43,551,43)
 c.setFont('Study',8);c.setFillColor(INK);c.drawString(44,30,'HEURÍSTICA Y OPTIMIZACIÓN · PROGRAMACIÓN LINEAL');c.drawRightString(551,30,f'{doc.page} / 65')
 c.setFont('Study',8);c.setFillColor(ACCENT);c.drawString(44,810,'ESTUDIO · PRÁCTICA · COMPRENSIÓN')

story=[]
for pi,p in enumerate(pages):
 if pi:story.append(PageBreak())
 for block in re.split(r'\n\s*\n',p):
  block=block.strip()
  if not block:continue
  # Encabezados seguidos por texto en la misma sección.
  if block.startswith('#') and '\n' in block:
   lines=block.splitlines();parts=[]
   for line in lines:
    if line.startswith('# '):story.append(para(line[2:],'h1'))
    elif line.startswith('## '):story.append(para(line[3:],'h2'))
    else:parts.append(line)
   if parts:story.append(para(' '.join(parts)))
  elif block.startswith('# '):story.append(para(block[2:],'h1'))
  elif block.startswith('## '):story.append(para(block[3:],'h2'))
  elif block=='[[CONTENTS]]':
   for t,n in contents:story.append(para(f'{n:02}   {t}','small'))
  elif block.startswith('[[GRAPH:'):story.append(chart(block[8:-2]));story.append(Spacer(1,12))
  elif block.startswith('>'):
   story.append(para('<br/>'.join([]))) if False else None
   story.append(Paragraph('<br/>'.join(fmt(l.lstrip('> ').strip()) for l in block.splitlines()),styles['formula']))
  elif block.startswith('|'):
   rows=[[para(cell.strip(),'table') for cell in l.strip('|').split('|')] for l in block.splitlines()]
   n=len(rows[0]);width=507
   if n==2:widths=[width*.33,width*.67]
   else:widths=[width/n]*n
   table=Table(rows,colWidths=widths,hAlign='LEFT')
   table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),LIGHT),('VALIGN',(0,0),(-1,-1),'TOP'),('BOX',(0,0),(-1,-1),.5,colors.HexColor('#bdd3d9')),('LINEBELOW',(0,0),(-1,0),1,ACCENT),('INNERGRID',(0,1),(-1,-1),.3,colors.HexColor('#d5e1e5')),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
   story.append(table);story.append(Spacer(1,12))
  elif re.match(r'^[1-5]\. ',block):
   for line in block.splitlines():story.append(para(line))
  elif block.startswith('Q '):story.append(para(block[2:],'question'))
  elif block.startswith('O '):story.append(para(block[2:],'option'))
  elif block.startswith('A '):story.append(para(block[2:],'answer'))
  else:
   style='answer' if titles[pi].startswith('Solucionario') else 'body'
   story.append(para(' '.join(block.splitlines()),style))
OUT.parent.mkdir(parents=True,exist_ok=True)
doc=GuideDoc(str(OUT),pagesize=(595.276,841.89),rightMargin=44,leftMargin=44,topMargin=53,bottomMargin=55,title='Programación lineal · guía de estudio',author='Material de estudio preparado para el examen',allowSplitting=1)
def check_glyphs(flow):
 if isinstance(flow,Paragraph):
  for frag in flow.frags:
   if not hasattr(frag,'text'):continue
   face=pdfmetrics.getFont(frag.fontName).face
   missing=[c for c in frag.text if ord(c)>32 and ord(c) not in face.charToGlyph]
   assert not missing,(frag.fontName,missing,frag.text)
 elif isinstance(flow,Table):
  for row in flow._cellvalues:
   for cell in row:
    if isinstance(cell,list):
     for child in cell:check_glyphs(child)
    else:check_glyphs(cell)
for flow in story:check_glyphs(flow)
print('Cobertura de glifos: todas las fórmulas, tablas y párrafos comprobados')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
from pypdf import PdfReader
r=PdfReader(OUT);print('PDF:',len(r.pages),'páginas')
actual=[]
for i,p in enumerate(r.pages):
 txt=p.extract_text();actual.append((i+1,txt[:150]))
assert len(r.pages)==65,f'Desbordamiento: {len(r.pages)} páginas, previstas 65'
# Detecta secciones partidas o encabezados desplazados comparando título en su página.
for i,t in enumerate(titles):
 text=r.pages[i].extract_text()
 normalize=lambda s:re.sub(r'\s+','',s)
 assert normalize(t) in normalize(text),(i+1,t)
(ROOT/'tmp/pdfs/page-titles.json').write_text(json.dumps(titles,ensure_ascii=False,indent=2))
print('65 páginas y encabezados verificados; 16 resueltos, 16 propuestos, 60 preguntas')
