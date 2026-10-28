# Base comum dos agentes

Vale para todos os agentes, em qualquer projeto. Esta base traz os padrões; o `AGENTS.md` (ou `CLAUDE.md`) na raiz de cada repositório traz o contexto do projeto e pode substituir qualquer padrão daqui.

## Prioridade das fontes

1. Instrução explícita do Owner nesta sessão
2. Briefing da Issue e a Issue no GitHub
3. `AGENTS.md` / `CLAUDE.md` do projeto
4. Esta base
5. Documentos antigos: servem de histórico e nunca prevalecem sobre o código atual

O Owner é a pessoa definida no `AGENTS.md` do projeto. Se o projeto não definir, o Owner é o Nathan.

## Antes de agir

- Rode `maestri list` para ver o time, seu nome e suas conexões.
- Leia o `AGENTS.md` do projeto, a Issue e o briefing por completo.
- Confira o estado real na fonte: código, `git status`, branch atual, GitHub, CI.
- Ambíguo ou contraditório? Pergunte ao PO antes de implementar, numa única mensagem com perguntas numeradas.

## Comunicação

- Fale com o PO. Só fale direto com outro agente se o PO conectar vocês para isso.
- Mantenha o status do seu Andar atualizado com `maestri floor status` (Trabalhando, Bloqueado, Pronto para revisão, Concluído). Use `maestri <comando> --help` se precisar.
- Toda entrega termina com um handoff neste formato, curto, sem repetir o briefing:

```
HANDOFF #<issue> — <seu papel> → PO
Resultado: concluído | bloqueado | precisa de decisão
Feito:
- ...
Evidências:
- [verificado] ...   (você executou ou viu agora)
- [relatado] ...     (outra fonte informou)
- [planejado] ...    (ainda não feito)
Branch / SHA: ...
Pendências e riscos: ...
Próximo passo sugerido: ...
```

## Evidência

Teste local, CI verde, PR mesclado, deploy e funcionalidade homologada são coisas diferentes. Nunca afirme um pelo outro.

## Git (padrão, quando o projeto não definir outro fluxo)

- Nunca trabalhe no Térreo nem direto nas branches principais (`main`, `develop` ou as que o projeto definir). Trabalhe na branch do seu Andar.
- Branches: `feature/<nº-issue>-descricao-kebab`, `fix/<nº-issue>-...`, `bugfix/<nº-issue>-...`, `hotfix/<descricao>`, `release/vX.Y.Z`, `docs/<descricao>`.
- Commits: Conventional Commits em pt-BR (`feat:`, `fix:`, `hotfix:`, `chore:`, `refactor:`, `docs:`, `test:`).
- PR para `develop` com `Related to #N`. Nunca use `Closes`, `Fixes` ou `Resolves`.
- Antes do PR, atualize a branch com a branch de destino.
- Proibido: `push --force`, apagar branch alheia, reescrever histórico publicado.
- Mesclar PR: só o PO, com `gh pr merge`, depois do OK explícito do Owner e com o SHA aprovado pelo QA.

## Código (padrão)

- Siga os padrões já existentes no projeto. Dependência, biblioteca ou stack nova só com decisão do PO.
- TypeScript estrito; `any` só com justificativa em comentário.
- Não use `switch`; prefira `const` e objetos de mapeamento.
- Altere apenas a área de arquivos declarada no briefing. Precisa sair dela? Pare e avise o PO.
- Arquivos globais (`package.json`, lockfile, configs de build, migrations, tokens de design, workflows) só com autorização do PO.
- Antes de entregar: lint, typecheck, testes e build, com os comandos do `AGENTS.md` do projeto.

## Segurança

- Nunca leia, imprima ou faça commit de `.env`, secrets, tokens, chaves, `service_role` ou links de convite.
- Nunca confie em identidade, permissão, tenant ou status vindos do navegador.
- Não copie dados reais de clientes para logs, notas ou prompts.

## Portões humanos: só o Owner aprova

Pare, avise com `maestri notify` e espere OK explícito do Owner antes de:

- mesclar nas branches principais ou publicar em qualquer ambiente público;
- aplicar migration em banco remoto;
- criar ou alterar secrets, DNS, domínio, Auth ou serviços externos;
- gerar custo novo (serviço ou plano pago);
- mudar escopo, prioridade, arquitetura ou stack;
- apagar dados, branches ou Andares com trabalho não pousado.

OK de outro agente não substitui o OK do Owner. O projeto pode acrescentar portões no `AGENTS.md`, nunca remover estes.

## Economia de tokens

- Leia só o necessário; não varra o repositório inteiro sem motivo.
- Mensagens e handoffs curtos. Referencie arquivos e links em vez de colar conteúdo.
- No máximo 2 rodadas de correção com o QA. Na terceira, o PO decide.

## Quando parar

Incerteza sobre regra, portão ou escopo, ou bloqueio sem saída clara: marque o Andar como Bloqueado, explique em até 3 linhas ao PO e aguarde.
