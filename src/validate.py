"""Validação técnica opcional: requer PyMuPDF (requirements-dev.txt)."""
import json
from pathlib import Path
import fitz
ROOT=Path(__file__).resolve().parents[1]

def validate(root=ROOT):
    report=[]
    expected=[0]*16
    expected[3]=8;expected[12]=5;expected[14]=10
    for name in ['Celular_Seguro_Cartilha.pdf','Celular_Seguro_Impressao.pdf']:
        doc=fitz.open(root/name)
        assert len(doc)==16, name
        assert not doc.is_encrypted
        assert len(doc.get_toc())==16
        assert len(doc[-1].get_links())==15
        for i,page in enumerate(doc):
            assert abs(page.rect.width-595.276)<.1 and abs(page.rect.height-841.89)<.1
            assert len(page.get_text().strip())>150
            assert len(list(page.widgets() or []))==expected[i]
            for block in page.get_text('dict')['blocks']:
                for line in block.get('lines',[]):
                    for span in line['spans']:
                        assert '\ufffd' not in span['text'],(name,i,span)
                        box=fitz.Rect(span['bbox'])
                        assert box.x0>=20 and box.x1<=page.rect.width-20,(name,i,box)
                        assert box.y0>=15 and box.y1<=page.rect.height-15,(name,i,box)
        report.append({'arquivo':name,'paginas':len(doc),'tamanho':'A4 vertical','campos':sum(expected),'links':15,'texto_extraivel':True,'marcadores':16})
    a=fitz.open(root/'Celular_Seguro_Cartilha.pdf');b=fitz.open(root/'Celular_Seguro_Impressao.pdf')
    assert [p.get_text() for p in a]==[p.get_text() for p in b]
    print(json.dumps(report,ensure_ascii=False,indent=2))
    return report
if __name__=='__main__':validate()
