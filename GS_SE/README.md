# Neighborhood Action Dashboard — GS2026.2

**CitizenTech para Gestão Colaborativa de Demandas Urbanas**

Entrega da **Global Solution GS2026.2** da disciplina de **Engenharia de Software**
da FIAP: concepção arquitetural de uma plataforma digital para registro,
organização e acompanhamento de demandas de melhoria de bairros e comunidades.

| | |
|---|---|
| **Curso** | Ciência da Computação — FIAP |
| **Disciplina** | Engenharia de Software |
| **Professor** | Prof. Dr. Leandro Ramos da Silva |
| **Entrega** | Documento único em PDF, padrão ABNT |
| **Versão** | 1.0 — 06/11/2026 |

## Integrantes

| Nome completo | RM |
|---|---|
| Lincoln Simão Pereira | RM567284 |
| Miguel Silva Bezerra | RM566763 |
| Nicolas Sakaue Nishimura | RM567752 |

## Entregável

📄 **[docs/GS2026.2_Neighborhood_Action_Dashboard.pdf](docs/GS2026.2_Neighborhood_Action_Dashboard.pdf)**
— 29 páginas, 5 figuras e 21 tabelas.

## Escolhas da equipe

| Decisão | Opção adotada |
|---|---|
| Abordagem arquitetural | **Arquitetura Hexagonal** (portas e adaptadores) |
| Visões arquiteturais | **Modelo C4** — diagramas de Contexto e de Containers |
| Cenário crítico modelado | **Registrar ocorrência** |

Conforme o enunciado, apenas **uma** abordagem arquitetural e **um** conjunto de
visões foram entregues. As alternativas avaliadas (Camadas, Clean e Onion) estão
no documento com o motivo do descarte.

## Como o documento atende a cada etapa

| Etapa | Valor | Onde está |
|---|---|---|
| 1 — Visão do Negócio | 2,0 | Seção 2: objetivo, problema, público-alvo, benefícios, As-Is/To-Be, papéis, 9 RF e 7 RNF |
| 2 — Arquitetura da Solução | 2,0 | Seção 3: Hexagonal, com motivação, benefícios, limitações e alternativas descartadas |
| 3 — Visões Arquiteturais | 2,5 | Seção 4: C4 contexto e containers, com rastreabilidade até os requisitos |
| 4 — Cenário Crítico e Sequência | 1,5 | Seção 5: fluxo principal (10 mensagens) e 3 fluxos alternativos |
| 5 — Decisões Arquiteturais | 1,5 | Seção 6: ADR-001 (+ ADR-002 no Apêndice A, adicional) |
| 6 — Qualidade e Testes | 0,5 | Seção 7: pirâmide, 3 níveis de teste e Definition of Done |

## A proposta em uma frase

O problema do Neighborhood Action Dashboard não é falta de canais para o cidadão
reclamar — canais existem e se multiplicam. É a **ausência de um fluxo único,
padronizado e transparente** que transforme relato disperso em demanda rastreável,
priorizada por critério e verificável por quem reclamou.

A arquitetura responde ao traço mais marcante desse contexto: a **instabilidade das
bordas**. Canais de entrada se multiplicam e fornecedores municipais mudam, enquanto
a regra de negócio permanece. Daí a escolha pela Arquitetura Hexagonal — a
volatilidade fica confinada aos adaptadores.

## Diagramas

| Diagrama | Conteúdo |
|---|---|
| [Arquitetura Hexagonal](diagramas/arquitetura_hexagonal.png) | Núcleo de domínio, portas de entrada e de saída, adaptadores primários e secundários |
| [C4 — Contexto](diagramas/c4_contexto.png) | Pessoas, o sistema e os cinco sistemas externos |
| [C4 — Containers](diagramas/c4_containers.png) | Portal, app móvel, API, workers, banco e fila, com os protocolos |
| [Sequência — Registrar ocorrência](diagramas/sequencia_registrar_ocorrencia.png) | Fluxo principal e os alternativos A1, A2 e A3 |
| [Pirâmide de testes](diagramas/piramide_de_testes.png) | Unitários, integração e end-to-end aplicados ao NAD |

## Estrutura do repositório

```
GS_SE/
├── docs/        documento final em PDF (entregável da GS)
├── diagramas/   figuras em PNG (alta resolução)
└── src-doc/     fontes: LaTeX do documento e scripts que geram as figuras
```

## Como reconstruir o PDF

Requer `pdflatex` (TeX Live), `python3` e `cairosvg`.

```bash
cd src-doc
pip install cairosvg
python3 figuras.py        # gera os .png a partir dos .svg
pdflatex principal.tex
pdflatex principal.tex    # segunda passada: sumário e referências cruzadas
```

## Observação sobre os números

Trata-se de **concepção arquitetural, não de implementação**. Não há código, não há
medição de desempenho, e os valores dos requisitos não funcionais são metas de
projeto — não resultados. A validação depende de protótipo executável e uso real.
