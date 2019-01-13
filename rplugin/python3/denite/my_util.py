import os.path

NO_NAME = 'NoName'
HIGHLIGHT_SYNTAX = [
    {'name': 'Prefix', 'link': 'Constant', 're': r'\v\d+\s[\ ahu%#+]+'},
    {'name': 'Info', 'link': 'PreProc', 're': r'\v\[[^]]*\]'},
    {'name': 'Modified', 'link': 'Statement', 're': '+', 'in': 'Prefix'},
    {'name': 'Time', 'link': 'Statement', 're': r'\v\([^)]*\)'},
    {'name': 'File', 'link': 'Function', 're': r'\v[^/ [\]]+\ze\s(\[|\()'},
    {'name': 'File', 'link': 'Function', 're': r'\v[^/ [\]]+\ze\n'},
    {'name': 'Special', 'link': 'WildMenu', 're': r'\v\$[A-Z]+'},
    {'name': 'Icon', 'link': 'String', 're': r'\].\['},
    {'name': 'IconConceal', 'is_conceal': True, 'in': 'Icon', 're': r'[[\]]'},
]

def abbr(vim, x):
    if x != NO_NAME:
        x = vim.funcs.fnamemodify(x, ':p:~')
        x = x.replace('~/.cache/dein/repos', '$DEIN')
        x = x.replace('~/.go/src', '$GO')
    return x


def icon(vim, path):
    return ']{0}['.format(
        vim.funcs.WebDevIconsGetFileTypeSymbol(path, os.path.isdir(path)))


def icon_abbr(vim, x):
    return ' {0}  {1}'.format(icon(vim, x), abbr(vim, x))


def highlight(vim, syntax_name):
    for syn in HIGHLIGHT_SYNTAX:
        conceal = 'conceal ' if syn.get('is_conceal') else ''
        containedin = syntax_name + ('_' + syn['in'] if 'in' in syn else '')
        vim.command(
            'syntax match {0}_{1} /{2}/ {3}contained containedin={4}'.format(
                syntax_name, syn['name'], syn['re'], conceal, containedin))
        if not syn.get('is_conceal'):
            vim.command(
                'highlight default link {0}_{1} {2}'.format(
                    syntax_name, syn['name'], syn['link']))
