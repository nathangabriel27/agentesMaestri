# Agentes

Configuração dos agentes do Maestri, reutilizável em qualquer projeto.

## Estrutura
| Caminho | O que é |
|---|---|
| `00-base-comum.md` | Regras que todo agente lê ao iniciar |
| `responsabilidades/*.md` | Texto de cada Responsabilidade do Maestri (fonte única) |
| `responsabilidades/_ids.json` | Liga cada arquivo ao id e nome da Responsabilidade no Maestri |
| `gerar-responsabilidades.py` | Gera `.maestri/roles/` e compara com o que está no Maestri |
| `modelos/` | Arquivos para copiar em cada projeto novo |

## Para alterar uma Responsabilidade
1. Edite o `.md` em `responsabilidades/`.
2. Rode `python3 gerar-responsabilidades.py`. Ele mostra quais estão diferentes no Maestri.
3. Atualize no Maestri: pelo "Descobrir Responsabilidades" apontando para esta pasta, ou com `python3 gerar-responsabilidades.py --copiar <Nome>` e colando em Instruções.
4. Faça o commit.

## Para preparar um projeto novo
1. Copie `modelos/AGENTS.md` e `modelos/CLAUDE.md` para a raiz e preencha o `AGENTS.md`.
2. Acrescente o conteúdo de `modelos/gitignore.txt` ao `.gitignore`.

## Permissões do Claude Code (uma vez por máquina)
Junte `modelos/claude-settings-usuario.json` ao seu `~/.claude/settings.json`. Itens em `deny` são bloqueados; itens em `ask` fazem o Claude Code pedir sua confirmação no terminal antes de executar. É uma rede de segurança: o bloqueio definitivo continua sendo o ruleset do GitHub.
