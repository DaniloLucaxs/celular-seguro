"""Execute: python src/build.py [--edition principal|impressao|ambas]."""
import argparse
from components import *
from content import PAGES
from references import SOURCES

def cover(e):
    e.start(1,dark=True)
    e.text('TECNOLOGIA, PROTEÇÃO E AUTONOMIA NAS PERIFERIAS',M,83,CW,9,True,LIME if e.dark else BLUE)
    e.text('CELULAR\nSEGURO',M,121,CW,64,True,leading=68)
    e.text('Sua vida é digital.\nSua proteção também precisa ser.',M,284,CW,20,leading=28)
    e.phone(350,410,1.05)
    e.text('PROTEÇÃO\nQUE CABE\nNA ROTINA.',M,449,265,27,True,leading=34)
    e.text('Aprenda no seu aparelho.\nCompartilhe na comunidade.',M,572,260,12)
    e.line(M,683,W-M,683,LIME if e.dark else BLUE,2)
    e.text('Uma iniciativa de educação e inclusão digital.',M,705,CW,12)
    e.text('Danilo Lucas dos Santos',M,731,CW,13,True)
    e.text('EDIÇÃO 1.0 • NOVEMBRO DE 2026',M,759,CW,8)
    e.end()

def regular(e,p,n):
    kind=p.get('kind','regular')
    e.start(n,p['section'],p['title'],dark=kind=='manifesto')
    y=195
    if 'intro' in p:
        y=e.text(p['intro'],M,y,CW,18 if kind=='manifesto' else 12.5,bold=kind=='manifesto',leading=25 if kind=='manifesto' else 18)+20
    if kind=='manifesto':
        for body in p['body']:y=e.text(body,M,y,CW,13,leading=20)+19
        e.callout(*p['callout'],y,105)
    elif kind in ('diagnostic','challenge','takeaway'):
        h={'diagnostic':43,'challenge':68,'takeaway':39}[kind]
        for i,body in enumerate(p['checks']):y=e.check(body,y,i,h)
        y+=8
        y=e.callout(*p['callout'],y,101 if kind!='takeaway' else 105)
        if p.get('bottom'):e.text(p['bottom'],M,y+2,CW,9.5,leading=15)
        if kind=='diagnostic':
            e.line(M,y+65,W-M,y+65,'#A9B2C0',.8)
    elif kind=='myths':
        for title,body in p['cards']:y=e.card(title,body,y,78)
        e.text(p['bottom'],M,y+4,CW,10.5)
    else:
        if p.get('steps'):
            for i,(title,body) in enumerate(p['steps'],1):y=e.card(f'{i:02d}  {title}',body,y,85)
        else:
            for title,body in p['cards']:y=e.card(title,body,y,119)
        if 'callout' in p:y=e.callout(*p['callout'],y,95)
        if p.get('bottom'):e.text(p['bottom'],M,y,CW,9,leading=13)
    e.end()

def closing(e):
    e.start(16,'CONTINUE ESSA CONVERSA','Conhecimento\nque circula')
    e.text('Compartilhe uma orientação, ajude alguém a encontrar uma configuração e respeite as escolhas de cada pessoa. A comunidade também produz tecnologia quando aprende e ensina.',M,192,CW,12,leading=18)
    e.text('Danilo Lucas dos Santos',M,262,CW,12,True)
    e.text('Estudante do último semestre de Análise e Desenvolvimento de Sistemas na UNIP, com vivência no Capão Redondo, Zona Sul de São Paulo. Projeto educativo de inclusão e proteção digital.',M,284,CW,10.5,leading=15)
    e.text('REFERÊNCIAS OFICIAIS',M,344,CW,10,True,BLUE)
    e.text('Consulta: 09/11/2026. Toque no título para abrir. No papel, use o endereço-base e procure o título no suporte oficial.',M,365,CW,9,leading=13)
    y=402
    for i,(title,url) in enumerate(SOURCES,1):
        e.text(f'[{i:02d}]  {title}',M,y,CW,9.3,leading=12)
        e.c.linkURL(url,(M,H-y-13,W-M,H-y+1),relative=0,thickness=0)
        y+=18
    e.text('support.google.com/android • support.apple.com/pt-br • faq.whatsapp.com\nwhatsapp.com/privacy • bcb.gov.br • gov.br/mj',M,y+3,CW,8,leading=12)
    e.text('Publicação independente, sem vínculo com o programa governamental Celular Seguro. Menus e recursos variam. Não há garantia de segurança total. Aprovação e carga horária de extensão dependem da avaliação institucional.',M,y+40,CW,8.5,leading=12)
    e.end()

def build(edition):
    eco=edition=='impressao'
    path=ROOT/('Celular_Seguro_Impressao.pdf' if eco else 'Celular_Seguro_Cartilha.pdf')
    e=Editor(path,eco);cover(e)
    for n,p in enumerate(PAGES,2):regular(e,p,n)
    closing(e);e.c.save();print(path)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--edition',choices=['principal','impressao','ambas'],default='ambas');args=parser.parse_args()
    for edition in (['principal','impressao'] if args.edition=='ambas' else [args.edition]):build(edition)
