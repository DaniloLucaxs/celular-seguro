"""Componentes editoriais vetoriais, texto selecionável e caixas interativas."""
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor, Color, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

ROOT = Path(__file__).resolve().parents[1]
W,H = A4
M=44
CW=W-2*M
NAVY='#101E32'; BLUE='#2563EB'; LIME='#C9F36B'; INK='#172333'; GRAY='#EDF2F7'
for name, fname in [('Body','NotoSans-Regular.ttf'),('Bold','NotoSans-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(ROOT/'assets/fonts'/fname)))
pdfmetrics.registerFontFamily('Body', normal='Body',bold='Bold',italic='Body',boldItalic='Bold')

class Editor:
    def __init__(self,path,economy=False):
        self.c=canvas.Canvas(str(path),pagesize=A4,pageCompression=1)
        self.c.setTitle('CELULAR SEGURO — Cartilha educativa')
        self.c.setAuthor('Danilo Lucas dos Santos')
        self.c.setSubject('Tecnologia, proteção e autonomia nas periferias')
        self.c.setCreator('Celular Seguro / ReportLab')
        self.c.setViewerPreference('DisplayDocTitle','true')
        self.c._doc.Catalog.Lang='pt-BR'
        self.eco=economy; self.dark=False; self.n=0
    def color(self,s):
        if self.eco:
            if s==LIME:return HexColor('#F5F5F5')
            if s==GRAY:return HexColor('#FAFAFA')
            if s==BLUE:return HexColor('#222222')
        return HexColor(s)
    def rect(self,x,y,w,h,fill,stroke=None,r=0):
        self.c.setFillColor(self.color(fill)); self.c.setStrokeColor(self.color(stroke or fill))
        if r:self.c.roundRect(x,H-y-h,w,h,r,stroke=bool(stroke),fill=1)
        else:self.c.rect(x,H-y-h,w,h,stroke=bool(stroke),fill=1)
    def line(self,x,y,x2,y2,color=BLUE,width=1):
        self.c.setStrokeColor(self.color(color));self.c.setLineWidth(width)
        self.c.line(x,H-y,x2,H-y2)
    def text(self,txt,x,y,w=CW,size=12,bold=False,color=None,leading=None):
        color=color or ('#FFFFFF' if self.dark else INK)
        style=ParagraphStyle('p',fontName='Bold' if bold else 'Body',fontSize=size,leading=leading or size*1.43,textColor=self.color(color),spaceAfter=0)
        # Text is plain author content; explicit newlines become line breaks.
        p=Paragraph(escape(txt.replace('→','•')).replace('\n','<br/>'),style)
        _,h=p.wrap(w,1000)
        if y+h>H-15:raise ValueError(f'Texto ultrapassa limite p.{self.n}: {txt[:40]} em {y+h}')
        p.drawOn(self.c,x,H-y-h)
        return y+h
    def start(self,n,section='',title='',dark=False):
        self.n=n;self.dark=dark and not self.eco
        if self.dark:self.rect(0,0,W,H,NAVY)
        self.c.bookmarkPage(f'p{n}'); self.c.addOutlineEntry(title.replace('\n',' ') or 'Capa',f'p{n}',level=0)
        band=n in (6,10,13) and not self.eco
        if band:self.rect(0,0,W,183,NAVY)
        color='#FFFFFF' if self.dark or band else NAVY
        self.text('CELULAR SEGURO',M,30,300,9,True,color)
        self.text(section,M,77,CW,10,True,LIME if self.dark or band else BLUE)
        if title:self.text(title,M,104,CW,31,True,color,35)
        self.line(M,H-43,W-M,H-43,'#8290A0' if self.dark else '#CBD2DA',.5)
        self.text('EDUCAÇÃO DIGITAL • COMUNIDADE • AUTONOMIA',M,H-33,CW-35,7,color='#FFFFFF' if self.dark else NAVY)
        self.text(f'{n:02d}',W-M-25,H-36,25,10,True,'#FFFFFF' if self.dark else NAVY)
    def end(self):self.c.showPage()
    def card(self,title,body,y,h=125,num=None):
        self.rect(M,y,CW,h,GRAY, '#D4DAE1' if self.eco else None,8)
        self.rect(M,y,4,h,BLUE)
        self.text(title,M+18,y+11,CW-36,11.5 if h<110 else 13,True,INK)
        bottom=self.text(body,M+18,y+(31 if h<110 else 39),CW-36,11 if h<110 else 11.5,color=INK,leading=15 if h<110 else 16)
        if bottom>y+h-9:raise ValueError(f'Card p{self.n} {title} {bottom-y}>{h}')
        return y+h+12
    def callout(self,title,body,y,h=95):
        self.rect(M,y,CW,h,LIME if self.n in (2,4,7,11,15) else GRAY,'#B9C1CB' if self.eco else None,7)
        self.text(title,M+16,y+12,CW-32,10,True,INK)
        bottom=self.text(body,M+16,y+33,CW-32,11.5,color=INK,leading=16)
        if bottom>y+h-8:raise ValueError(f'Callout p{self.n}: {bottom-y}>{h}')
        return y+h+12
    def check(self,body,y,i,h=48):
        self.c.acroForm.checkbox(name=f'p{self.n}_{i}',tooltip=body,x=M+1,y=H-y-16,size=14,borderWidth=1,borderColor=self.color(INK),fillColor=white,textColor=self.color(INK),buttonStyle='check',checked=False,forceBorder=True)
        bottom=self.text(body,M+29,y-2,CW-29,11.5,leading=16)
        if bottom>y+h-5:raise ValueError(f'Checkbox p{self.n} overflow')
        self.line(M+29,y+h-9,W-M,y+h-9,'#D5DAE0',.45)
        return y+h
    def phone(self,x,y,scale=1):
        """Desenho educativo próprio: aparelho, segredo de tela e escudo."""
        c=self.c;c.saveState();c.translate(x,H-y);c.scale(scale,scale)
        c.setStrokeColor(self.color('#FFFFFF' if self.dark else NAVY));c.setLineWidth(3)
        c.setFillColor(self.color(NAVY if not self.eco else '#FFFFFF'))
        c.roundRect(0,-240,132,240,19,stroke=1,fill=1)
        c.setFillColor(self.color('#EDF2F7'));c.roundRect(10,-225,112,206,11,stroke=0,fill=1)
        c.setFillColor(self.color(NAVY));c.roundRect(45,-16,42,5,2,stroke=0,fill=1)
        c.setStrokeColor(self.color(BLUE));c.setLineWidth(5)
        c.arc(47,-90,85,-48,0,180); c.setFillColor(self.color(BLUE));c.roundRect(40,-105,52,38,7,stroke=0,fill=1)
        c.setFillColor(white);c.circle(66,-84,3,stroke=0,fill=1)
        for k in range(6):c.setFillColor(self.color(NAVY));c.circle(31+14*k,-135,3,stroke=0,fill=1)
        for row in range(3):
            for col in range(3):
                c.setFillColor(self.color('#BAC7D9'));c.circle(39+27*col,-158-21*row,7,stroke=0,fill=1)
        p=c.beginPath();p.moveTo(92,-107);p.lineTo(144,-123);p.lineTo(144,-162);p.curveTo(144,-187,119,-207,118,-207);p.curveTo(116,-207,92,-187,92,-162);p.close()
        c.setFillColor(self.color(LIME));c.setStrokeColor(self.color(NAVY));c.setLineWidth(2);c.drawPath(p,stroke=1,fill=1)
        c.setLineWidth(4);c.line(104,-158,115,-170);c.line(115,-170,134,-143)
        c.restoreState()
