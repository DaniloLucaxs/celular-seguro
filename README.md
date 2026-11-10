# CELULAR SEGURO

**Sua vida é digital. Sua proteção também precisa ser.**

Cartilha educativa independente sobre tecnologia, proteção e autonomia nas periferias. Autoria: **Danilo Lucas dos Santos**, estudante do último semestre de Análise e Desenvolvimento de Sistemas na Universidade Paulista — UNIP, com vivência no Capão Redondo, Zona Sul de São Paulo.

Segurança digital não pode ser privilégio. O projeto aproxima orientações práticas da rotina de quem usa o celular para trabalhar, estudar, conversar, pagar e acessar serviços. A comunidade ocupa o centro: aprender, fazer e compartilhar, sem infantilização ou discurso de medo.

## Entregas

| Arquivo | Uso |
|---|---|
| [Celular_Seguro_Cartilha.pdf](Celular_Seguro_Cartilha.pdf) | Edição colorida, 16 páginas A4 verticais |
| [Celular_Seguro_Impressao.pdf](Celular_Seguro_Impressao.pdf) | Edição econômica, mesmo conteúdo e paginação |
| [CONTEUDO_ACESSIVEL.md](CONTEUDO_ACESSIVEL.md) | Conteúdo em texto estruturado, para leitura e adaptação |
| [ROTEIRO_APRESENTACAO.md](ROTEIRO_APRESENTACAO.md) | Encontro presencial de 25 minutos, adaptável a 20–30 |
| [MODELO_RELATORIO_EXTENSAO.md](MODELO_RELATORIO_EXTENSAO.md) | Modelo em branco para preencher após a execução real |
| [CHECKLIST_REVISAO.md](CHECKLIST_REVISAO.md) | Verificações realizadas e limites da validação |
| [FONTES.md](FONTES.md) | Referências completas e observações sobre consulta |
| `src/` | Gerador modular Python/ReportLab e validação opcional |
| `assets/` | Vetores próprios, fontes incorporadas e licença das fontes |
| `requirements.txt` | Dependência de geração |
| `requirements-dev.txt` | Dependência opcional de validação |

## Público e objetivos

Pessoas da comunidade externa à universidade, de diferentes idades e níveis de familiaridade com tecnologia. Ao usar o material, o participante poderá conferir bloqueio de tela, atualizações, conta e privacidade do WhatsApp, permissões, cuidados financeiros, localização/bloqueio remoto, backup e recuperação.

Não é necessário ter aparelho recente ou internet ilimitada. A prática respeita as escolhas de cada pessoa e pode continuar em casa. Ninguém deve fornecer senhas, códigos ou dados bancários ao educador.

## Leitura em 16 páginas

1. Capa — identidade do projeto.
2. Manifesto — proteção digital para todos.
3. Por que proteger — trabalho, família e dinheiro.
4. Diagnóstico individual sem pontuação.
5. Bloqueio de tela — PIN, senha, biometria e tempo automático.
6. Atualizações — sistema e aplicativos.
7. WhatsApp — verificação em duas etapas e recuperação.
8. WhatsApp — privacidade e grupos.
9. Aplicativos — permissões necessárias.
10. Dinheiro — Pix, autenticação e reação a fraude.
11. Perda ou roubo — plano de resposta.
12. Backup e recuperação de contas.
13. Desafio com cinco conferências.
14. Seis mitos e verdades.
15. Checklist destacável com dez cuidados.
16. Encerramento e fontes oficiais.

## Gerar os PDFs

Requer Python 3.10 ou posterior. Não precisa de rede depois de instalar a dependência. As fontes estão incluídas no projeto.

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python src/build.py
```

Também é possível gerar uma edição por vez:

```bash
python src/build.py --edition principal
python src/build.py --edition impressao
```

Os dois PDFs são gravados na raiz do projeto, independentemente do diretório de onde o comando é chamado. Executar novamente substitui esses dois arquivos gerados.

Validação técnica opcional:

```bash
python -m pip install -r requirements-dev.txt
python src/validate.py
```

A validação confere páginas, tamanho A4, texto extraível, margens de texto, marcadores, links de referência, quantidade de campos e equivalência textual entre as edições. Ela não substitui inspeção visual nem verifica a disponibilidade futura dos sites.

## Arquitetura e edição

- `src/content.py`: conteúdo das páginas 2–15, organizado por componentes.
- `src/references.py`: títulos e URLs oficiais.
- `src/components.py`: tipografia, cabeçalhos, rodapés, cards, dicas, caixas e ilustração vetorial original.
- `src/build.py`: capa, composição das páginas, encerramento e seleção de edição.
- `src/validate.py`: verificações estruturais.

Ao mudar o texto, confira as duas edições. O gerador acusa excesso de texto nos cards e limites físicos; isso não detecta todos os problemas de composição. Renderize e examine novamente todas as páginas. Mantenha as 16 páginas e atualize a data de consulta após conferir fontes.

## Distribuição e impressão

Para celular e computador, use a edição colorida. O PDF tem texto selecionável, marcadores de navegação, 15 links e 23 caixas interativas nas páginas 4, 13 e 15. As caixas dependem do leitor de PDF; salve uma cópia para preservar suas marcas. Elas não enviam respostas a um servidor.

Para impressão, use a edição econômica em A4, orientação vertical, tamanho real/100%. Pode ser impressa frente e verso, virando pela borda longa. A página 15 pode ser impressa sozinha para consulta. A numeração é de páginas, não de folhas. Os PDFs não estão impostos em cadernos de gráfica e não possuem sangria; todos os elementos úteis respeitam margens internas. Faça uma prova antes de imprimir em grande volume. A versão econômica elimina os fundos escuros e reduz preenchimentos; também funciona em escala de cinza.

Há metadados de idioma e fontes incorporadas. Não se declara conformidade PDF/UA: o PDF não possui estrutura completa de marcação semântica. Para tecnologias assistivas ou adaptação de tamanho de texto, prefira o arquivo Markdown acessível. Não houve ensaio com leitor de tela nem impressão física.

## Fontes e manutenção

As orientações foram conferidas em páginas oficiais de Google/Android, Apple, WhatsApp, Banco Central e MJSP em 09/11/2026. Alguns artigos Apple limitaram acesso direto (HTTP 429); nesses casos, a identificação e os trechos foram conferidos pelo índice de busca oficial. Veja `FONTES.md` para os detalhes. Menus variam com sistema, modelo e versão. Em especial, o WhatsApp está migrando a verificação em duas etapas de PIN para senha; o material explica as duas situações.

Esta publicação **não é o programa Celular Seguro do governo**, não possui vínculo institucional com ele e não representa Google, Apple, WhatsApp ou bancos. O programa oficial é citado somente como recurso público. Não há estatísticas inventadas nem promessa de segurança total. Repositório do projeto: https://github.com/DaniloLucaxs/celular-seguro. Os PDFs desta primeira edição foram preparados antes da criação do repositório e não contêm QR code.

Este repositório reúne os PDFs, código-fonte e recursos do projeto. O README usa links relativos para abrir os materiais diretamente no GitHub. Não envie listas de presença, imagens identificáveis ou relatórios privados ao repositório público.

## Uso comunitário e autoria

O roteiro e o relatório são materiais de preparação. Nenhuma oficina, participação, autorização, resultado ou carga horária foi presumida. Aprovação e validação acadêmica dependem das regras e avaliação da UNIP.

A licença das fontes acompanha os arquivos de fonte. Não foi atribuída uma licença geral ao texto/código em nome do autor: a autorização pública de reutilização e adaptação deverá ser definida por Danilo antes da publicação. Os arquivos estão organizados para consulta, impressão e manutenção do projeto; marcas mencionadas pertencem aos respectivos titulares.
