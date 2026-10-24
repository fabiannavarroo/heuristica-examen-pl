"""Comprobación opcional contra los PDF locales, sin publicarlos."""
from pathlib import Path
import re,json
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1]
coverage=json.loads((ROOT/'study/past-exam-coverage.json').read_text())
for doc,meta in coverage['documents'].items():
 path=ROOT.parent/'parciales'/meta['file']
 if not path.exists():
  assert doc=='C',path
  print('C: inventario de 60 preguntas de la lectura completa previa; PDF actualmente ausente (declarado en cobertura).')
  continue
 actual=[];extras=False
 for page_number,page in enumerate(PdfReader(path).pages,1):
  if page_number==1:continue
  text=(page.extract_text() or '').split('Reservados todos los derechos')[0]
  marker='Otras preguntas únicamente dando la respuesta correcta:'
  chunks=text.split(marker)
  for chunk_index,chunk in enumerate(chunks):
   if chunk_index:extras=True
   for match in re.finditer(r'(?m)^\s*(\d{1,2})\.\s+',chunk):
    actual.append((int(match[1]),page_number,'extras' if extras else 'principal'))
 expected=[(e['printedNumber'],e['page'],e['section']) for e in coverage['coverage'] if e['document']==doc]
 assert actual==expected,(doc,actual,expected)
 print(doc,':',len(actual),'apariciones cotejadas contra número impreso, página y sección del PDF')
