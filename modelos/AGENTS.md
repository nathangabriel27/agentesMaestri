# AGENTS.md — <nome do projeto>

Contexto deste projeto para o time de agentes. As regras gerais estão em `/Users/nathanoliveiradev/Code/agentes/00-base-comum.md`; o que está aqui substitui os padrões de lá quando houver conflito. Portões humanos só podem ser acrescentados, nunca removidos.

## Projeto
- Cliente / produto: <nome e uma frase sobre o que é>
- Owner: <nome> (aprova os portões humanos)
- Repositório: <usuario/repo> · GitHub Project: <link ou "não usa">
- Documentos de referência: <links para spec, protótipo, handoff>

## Stack
<ex.: site estático em HTML/CSS/JS · React + Vite + TypeScript · Next.js + Supabase>

## Comandos
| Ação | Comando |
|---|---|
| Rodar localmente | <...> |
| Lint | <... ou "não se aplica"> |
| Typecheck | <...> |
| Testes | <...> |
| Build | <...> |

## Branches
- Principais: `main` (produção) e `develop` (desenvolvimento) <ajuste se o projeto usar outras>
- Destino dos PRs: `develop`
- Ambiente de preview / homologação: <URL ou "não há">

## Regras específicas do projeto
- <ex.: usar apenas os tokens de cor definidos em :root>
- <ex.: não alterar textos aprovados pelo cliente sem OK do Owner>

## Áreas sensíveis
<pastas ou arquivos que exigem Tech Lead ou cuidado extra: ex. supabase/migrations, auth, workflows>

## Portões humanos extras
- <ex.: qualquer mudança em textos, contatos ou preços exibidos ao cliente>

## Memória do projeto (X9)
- Passagem de conhecimento: `docs/passagem-de-conhecimento.md`
- Decisões: `docs/decisoes/`
