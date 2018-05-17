# ============================================================================
# FILE: my_file.py
# AUTHOR: delphinus <delphinus@remora.cx>
# License: MIT license
# ============================================================================

import sys
from os.path import dirname
sys.path.append(dirname(dirname(__file__)))

from my_util import abbr, add_icon, highlight
from denite.source.file import Source as Base


class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'my_file'

    def gather_candidates(self, context):
        def filter_abbr(x):
            abb = abbr(self.vim, x['abbr'])
            x['abbr'] = add_icon(self.vim, abb, x['action__path'])
            return x
        return list(map(filter_abbr, super().gather_candidates(context)))

    def highlight(self):
        highlight(self.vim, self.syntax_name)
