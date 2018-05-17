import os.path

ICON_SEP = '{0}_i_{0}'.format(chr(0xa0))
FILE_SEP = '{0}_f_{0}'.format(chr(0xa0))
SEP_RE = '{0}_._{0}'.format(chr(0xa0))
NO_NAME = 'No Name'


def word(vim, x):
    return vim.funcs.fnamemodify(x, ':~:.')


def abbr(vim, x):
    if x != NO_NAME:
        x = vim.funcs.fnamemodify(x, ':p:~')
        x = x.replace('~/.cache/dein/repos', '$DEIN')
        x = x.replace('~/.go/src', '$GO')
    icon = vim.funcs.WebDevIconsGetFileTypeSymbol(
        x, os.path.isdir(x))
    icon = ' {0}  '.format(icon)
    if x == NO_NAME:
        directory = ''
        filename = x
    else:
        directory = vim.funcs.fnamemodify(x, ':.:h') + '/'
        filename = vim.funcs.fnamemodify(x, ':t')
    return icon + ICON_SEP + directory + FILE_SEP + filename


def highlight(vim, syntax_name):
    def name(x):
        return syntax_name + '_' + x

    com = vim.command
    com(r'syntax match {0} /\v\d+\s[\ ahu%#]+/ contained containedin={1}'.
        format(name('Prefix'), syntax_name))
    com(r'syntax match {0} /\v\S+\s*({1})@=/ contained containedin={2}'.
        format(name('Icon'), ICON_SEP, syntax_name))
    com(r'syntax match {0} /\v({1})@<=.*/ contained containedin={2}'.
        format(name('File'), FILE_SEP, syntax_name))
    com(r'syntax match {0} /\v\[[^]]*\]/ contained containedin={1}'.
        format(name('Info'), name('File')))
    com(r'syntax match {0} /\v\([^)]*\)/ contained containedin={1}'.
        format(name('Time'), name('File')))
    com(r'syntax match {0} /\$[A-Z]\+/ contained containedin={1}'.
        format(name('Special'), syntax_name))
    com('syntax match {0} /{1}/ conceal contained containedin={2}'.
        format(name('Sep'), SEP_RE, syntax_name))

    com('highlight default link {0} Constant'.format(name('Prefix')))
    com('highlight default link {0} Function'.format(name('Icon')))
    com('highlight default link {0} Directory'.format(name('File')))
    com('highlight default link {0} PreProc'.format(name('Info')))
    com('highlight default link {0} Statement'.format(name('Time')))
    com('highlight default link {0} WildMenu'.format(name('Special')))
