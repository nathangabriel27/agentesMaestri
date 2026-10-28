#!/usr/bin/env python3
"""Gera as Responsabilidades do Maestri a partir de responsabilidades/*.md.

Uso:
  python3 gerar-responsabilidades.py              gera .maestri/roles/<id>/ e mostra o que difere do Maestri
  python3 gerar-responsabilidades.py --copiar PO  copia o texto da Responsabilidade para a área de transferência

O script só LÊ ~/.maestri/preferences.json (para manter ícone e cor e comparar o texto).
Ele nunca escreve nos arquivos do Maestri.
"""
import json
import pathlib
import subprocess
import sys

RAIZ = pathlib.Path(__file__).resolve().parent
PASTA_MD = RAIZ / "responsabilidades"
PREFERENCIAS = pathlib.Path.home() / ".maestri" / "preferences.json"
ICONE_PADRAO = "sparkles"
COR_PADRAO = "#007AFF"


def responsabilidades_do_maestri():
    encontradas = {}

    def percorrer(obj):
        if isinstance(obj, dict):
            if "id" in obj and "prompt" in obj and "name" in obj:
                encontradas[str(obj["id"]).upper()] = obj
            for valor in obj.values():
                percorrer(valor)
        elif isinstance(obj, list):
            for valor in obj:
                percorrer(valor)

    try:
        percorrer(json.loads(PREFERENCIAS.read_text(encoding="utf-8")))
    except (OSError, ValueError):
        print(f"Aviso: não consegui ler {PREFERENCIAS}. Ícone e cor usarão o padrão.")
    return encontradas


def carregar():
    ids = json.loads((PASTA_MD / "_ids.json").read_text(encoding="utf-8"))
    return [
        {**meta, "arquivo": arquivo, "prompt": (PASTA_MD / arquivo).read_text(encoding="utf-8").strip()}
        for arquivo, meta in ids.items()
    ]


def copiar(nome, itens):
    alvo = next((i for i in itens if i["name"].lower() == nome.lower()), None)
    if alvo is None:
        nomes = ", ".join(i["name"] for i in itens)
        sys.exit(f"Responsabilidade '{nome}' não encontrada. Opções: {nomes}")
    subprocess.run(["pbcopy"], input=alvo["prompt"].encode("utf-8"), check=True)
    print(f"Texto de '{alvo['name']}' copiado. Cole no campo Instruções do Maestri.")


def gerar(itens):
    no_maestri = responsabilidades_do_maestri()
    print(f"{'Responsabilidade':<12} {'Situação no Maestri'}")
    for item in itens:
        atual = no_maestri.get(item["id"].upper(), {})
        papel = {
            "color": atual.get("color", COR_PADRAO),
            "icon": atual.get("icon", ICONE_PADRAO),
            "id": item["id"],
            "name": item["name"],
            "prompt": item["prompt"],
            "schemaVersion": 1,
        }
        destino = RAIZ / ".maestri" / "roles" / item["id"].lower()
        destino.mkdir(parents=True, exist_ok=True)
        (destino / "role.json").write_text(
            json.dumps(papel, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        for nome_arquivo in ("CLAUDE.md", "AGENTS.md"):
            (destino / nome_arquivo).write_text(item["prompt"] + "\n", encoding="utf-8")

        situacoes = {
            True: "igual",
            False: "DIFERENTE: atualize (--copiar " + item["name"] + ")",
        }
        situacao = "não encontrada no Maestri" if not atual else situacoes[atual.get("prompt", "").strip() == item["prompt"]]
        print(f"{item['name']:<12} {situacao}")
    print(f"\nArquivos gerados em {RAIZ / '.maestri' / 'roles'}")


if __name__ == "__main__":
    itens = carregar()
    argumentos = sys.argv[1:]
    if argumentos[:1] == ["--copiar"] and len(argumentos) == 2:
        copiar(argumentos[1], itens)
    elif not argumentos:
        gerar(itens)
    else:
        sys.exit(__doc__)
