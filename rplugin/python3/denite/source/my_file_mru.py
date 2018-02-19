# ============================================================================
# FILE: my_file_mru.py
# AUTHOR: delphinus <delphinus@remora.cx>
# License: MIT license
# ============================================================================

import sys
from os.path import dirname
sys.path.append(dirname(dirname(__file__)))

from my_util import word, abbr, highlight
from denite.source.file_mru import Source as Base


class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'my_file_mru'

    def gather_candidates(self, context):
        return [{
            'word': word(self.vim, x),
            'abbr': abbr(self.vim, x),
            'action__path': x,
        } for x in self.vim.eval(
            'neomru#_get_mrus().file.'
            + 'gather_candidates([], {"is_redraw": 0})')]

    def highlight(self):
        highlight(self.vim, self.syntax_name)
