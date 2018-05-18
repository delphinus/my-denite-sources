import os.path

NO_NAME = 'NoName'

def word(vim, x):
    return vim.funcs.fnamemodify(x, ':~:.')


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
    def name(x):
        return syntax_name + '_' + x

    com = vim.command
    com(r'syntax match {0} /\v\d+\s[\ ahu%#]+/ contained containedin={1}'.
        format(name('Prefix'), syntax_name))
    com(r'syntax match {0} /\v[^/ \[\]]+\ze(\s(\[|\()|\n)/ contained containedin={1}'.
        format(name('File'), syntax_name))
    com(r'syntax match {0} /\v\[[^]]*\]/ contained containedin={1}'.
        format(name('Info'), syntax_name))
    com(r'syntax match {0} /\v\([^)]*\)/ contained containedin={1}'.
        format(name('Time'), syntax_name))
    com(r'syntax match {0} /\$[A-Z]\+/ contained containedin={1}'.
        format(name('Special'), syntax_name))

    com(r'syntax match {0} /\v\].\[/ contained containedin={1}'.
        format(name('Icon'), syntax_name))
    com(r'syntax match {0} /[[\]]/ conceal contained containedin={1}'.
        format(name('Sep'), name('Icon')))

    com('highlight default link {0} Constant'.format(name('Prefix')))
    com('highlight default link {0} String'.format(name('Icon')))
    com('highlight default link {0} Function'.format(name('File')))
    com('highlight default link {0} PreProc'.format(name('Info')))
    com('highlight default link {0} Statement'.format(name('Time')))
    com('highlight default link {0} WildMenu'.format(name('Special')))
