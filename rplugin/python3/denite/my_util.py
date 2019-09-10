from os import environ
from pathlib import Path
from typing import List, Dict, Union

from denite.util import Nvim

NO_NAME = "NoName"
HIGHLIGHT_SYNTAX: List[Dict[str, Union[str, bool]]] = [
    {"name": "Prefix", "link": "Constant", "re": r"\v\d+\s[\ ahu%#+]+"},
    {"name": "Info", "link": "PreProc", "re": r"\v\[[^]]*\]"},
    {"name": "Modified", "link": "Statement", "re": "+", "in": "Prefix"},
    {"name": "Time", "link": "Statement", "re": r"\v\([^)]*\)"},
    {"name": "File", "link": "Function", "re": r"\v[^/ [\]]+\ze\s(\[|\()"},
    {"name": "File", "link": "Function", "re": r"\v[^/ [\]]+\ze\n"},
    {"name": "Special", "link": "Special", "re": r"\v\$[A-Z]+"},
    {"name": "Icon", "link": "String", "re": r"\].\["},
    {"name": "IconConceal", "is_conceal": True, "in": "Icon", "re": r"[[\]]"},
]
PATH_REPLACES = [
    {
        # TODO: detect vim?
        "path": str(Path("~/.cache/dein/.cache/init.vim/.dein")),
        "text": "$INIT",
    },
    {"path": str(Path("~/.cache/dein/repos")), "text": "$DEIN"},
    {"path": str(Path("~/.go/src")), "text": "$GO"},
    {"path": str(Path(environ["VIMRUNTIME"])), "text": "$VIMRUNTIME"},
    {"path": str(Path(environ["VIM"])), "text": "$VIM"},
]


def abbr(vim: Nvim, x: str) -> str:
    """
    abbr() makes shortened paths. It replaces paths by PATH_REPLACES config.

    And also it replaces path parts into the head character until the length is
    under winwidth.

    path/to/long/long/filenames.txt
    <---- winwidth ---->
    p/t/l/long/filenames.txt

    The last two part will be not cut even if it is over the width.
    """
    if x == NO_NAME:
        return x

    x = vim.funcs.fnamemodify(x, ":~:.")
    for p in PATH_REPLACES:
        x = x.replace(vim.funcs.fnamemodify(p["path"], ":~:."), p["text"])
    width = vim.funcs.winwidth(0)
    if len(x) <= width:
        return x

    xp = Path(x)

    def cut(n: int = 0) -> str:
        y = Path(*[part[0:1] if i <= n else part for i, part in enumerate(xp.parts)])
        return str(y) if len(str(y)) < width or n < len(xp.parts) - 3 else cut(n + 1)

    return cut() if len(xp.parts) > 2 else x


def icon(vim: Nvim, path: str) -> str:
    icon_str = vim.funcs.WebDevIconsGetFileTypeSymbol(path, Path(path).is_dir())
    return f"]{icon_str}["


def icon_abbr(vim: Nvim, x: str) -> str:
    return f" {icon(vim,x)}  {abbr(vim,x)}"


def highlight(vim: Nvim, syntax_name: str) -> None:
    for syn in HIGHLIGHT_SYNTAX:
        conceal = "conceal " if syn.get("is_conceal") else ""
        containedin = syntax_name + ("_" + str(syn["in"]) if "in" in syn else "")
        vim.command(
            "syntax match {0}_{1} /{2}/ {3}contained containedin={4}".format(
                syntax_name, syn["name"], syn["re"], conceal, containedin
            )
        )
        if not syn.get("is_conceal"):
            vim.command(
                "highlight default link {0}_{1} {2}".format(
                    syntax_name, syn["name"], syn["link"]
                )
            )
