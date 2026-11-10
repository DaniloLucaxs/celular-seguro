# Registro de revisão — edição 1.0

Revisão editorial em 09/11/2026, America/Sao_Paulo. Execução técnica na sessão de geração (host UTC em 10/11/2026). Responsável pela autoria declarada: Danilo Lucas dos Santos. Este registro descreve o material produzido, não uma ação comunitária realizada.

## Editorial e técnica

- [x] Estrutura de 16 páginas conforme o briefing, nas duas edições.
- [x] Português brasileiro revisado, com exemplos cotidianos e sem estatísticas não verificadas.
- [x] Identidade do autor limitada aos dados fornecidos, sem informações privadas adicionais.
- [x] Comunidade e autonomia no centro da mensagem, sem estereótipos.
- [x] Variações de sistema, fabricante e menus sinalizadas.
- [x] Transição do WhatsApp de PIN para senha contemplada, conforme página oficial consultada.
- [x] PIN/senha de tela, código de registro e verificação em duas etapas diferenciados.
- [x] Resposta a roubo prioriza segurança física e não incentiva confronto.
- [x] Localização remota apresentada com dependências e sem prometer recuperação.
- [x] MED apresentado com análise e sem promessa de devolução.
- [x] Publicação diferenciada do programa governamental de mesmo nome.
- [x] Fontes e URLs oficiais conferidas por páginas e/ou resultados oficiais de busca; ver limitações em FONTES.md.
- [x] Sem repositório fictício, QR code inventado ou publicação em nome do autor.
- [x] Roteiro de 25 minutos e modelo de relatório em branco, sem participantes ou resultados inventados.

## PDFs e inspeção visual

- [x] Cada arquivo abre corretamente e contém exatamente 16 páginas A4 verticais (595,276 × 841,89 pontos).
- [x] Todas as 32 páginas finais foram renderizadas em PNG e inspecionadas individualmente, em comparações lado a lado por número de página.
- [x] Capa ajustada para separar o aparelho da linha editorial inferior.
- [x] Rodapé da página 15 ajustado para acomodar a assinatura e o canal oficial.
- [x] Setas de referência substituídas por marcadores compatíveis com a fonte incorporada.
- [x] Títulos, cards, quadros, caixas e rodapés sem cortes ou sobreposições observadas.
- [x] Edição econômica elimina fundos escuros, reduz preenchimentos e preserva o mesmo texto e paginação.
- [x] Contraste e tamanho de corpo conferidos visualmente em renderização A4; notas e referências usam corpo menor.
- [x] Fontes Noto Sans incorporadas e licença incluída.
- [x] Texto selecionável, pesquisável e extraível, sem caracteres de substituição detectados.
- [x] 16 marcadores de navegação e 15 links oficiais em cada PDF.
- [x] 23 caixas de seleção em cada PDF (8 no diagnóstico, 5 no desafio, 10 no checklist).
- [x] Marcação e persistência de uma caixa testadas em cópia separada com PyMuPDF.
- [x] Conteúdo acessível em Markdown estruturado incluído como alternativa de leitura.

## Código e organização

- [x] Geração completa com Python/ReportLab executada.
- [x] Geração repetida em cópia independente da pasta, sem depender do caminho original.
- [x] As 32 páginas regeneradas resultaram em pixels idênticos às versões revisadas.
- [x] `src/validate.py` executado: contagem, dimensões, texto, margens, links, campos, marcadores e equivalência textual entre edições aprovados.
- [x] `requirements.txt` corresponde à versão efetivamente utilizada do ReportLab.
- [x] Conferidos PDFs, README, src, assets, dependências, roteiro, modelo de relatório e este checklist.
- [x] Pacote ZIP preparado para transferência; sem arquivos de participantes ou credenciais.

## Verificações não realizadas / limites

- [ ] Impressão física e prova em gráfica: não realizadas. A legibilidade para impressão foi avaliada nas renderizações. Recomenda-se uma prova antes de uma tiragem grande.
- [ ] Testes em aparelhos físicos Android/iPhone, contas reais e aplicativos bancários: não realizados. Menus foram conferidos na documentação, com ressalvas de versão.
- [ ] Compatibilidade das caixas em todos os leitores PDF: não testada; alguns navegadores podem não salvar formulários.
- [ ] Ensaio com leitor de tela e auditoria PDF/UA: não realizados. Os PDFs não são semanticamente marcados para conformidade PDF/UA. Há alternativa em Markdown.
- [ ] Leitura integral de todos os artigos Apple: limitada por respostas HTTP 429; títulos, URLs e trechos oficiais foram confirmados na busca. A consulta web não equivale a teste físico de todos os caminhos.
- [ ] Disponibilidade futura de sites externos: não garantida. Confira as fontes ao atualizar a edição.
- [ ] Instalação de dependências em máquina nova e testes em Windows/macOS: não realizados. A regeneração usou uma cópia limpa da pasta no mesmo ambiente Python.
- [ ] Oficina, comprovação de extensão, aprovação institucional e carga horária: não realizadas/atribuídas por esta produção.
- [x] Pacote preparado para publicação em https://github.com/DaniloLucaxs/celular-seguro, por solicitação do autor.
- [ ] Definição de licença geral pelo autor: pendente. A licença das fontes já está incluída.

