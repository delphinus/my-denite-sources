# ============================================================================
# FILE: my_file_mru.py
# AUTHOR: delphinus <delphinus@remora.cx>
# License: MIT license
# ============================================================================

import importlib
from denite.source.file_mru import Source as Base


class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'my_file_mru'
        self.__util = importlib.import_module('..my_util')

    def gather_candidates(self, context):
        return [{
            'word': self.__util.word(self.vim, x),
            'abbr': self.__util.abbr(self.vim, x),
            'action__path': x,
        } for x in self.vim.eval(
            'neomru#_get_mrus().file.'
            + 'gather_candidates([], {"is_redraw": 0})')]

    def highlight(self):
        self.__util.highlight(self.vim, self.syntax_name)
