# ============================================================================
# FILE: my_file.py
# AUTHOR: delphinus <delphinus@remora.cx>
# License: MIT license
# ============================================================================

import sys
from os.path import dirname
sys.path.append(dirname(dirname(__file__)))

from my_util import icon_abbr, highlight
from denite.source.file.rec import Source as Base


class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'my_file_rec'

    def gather_candidates(self, context):
        def filter_abbr(x):
            x['abbr'] = icon_abbr(self.vim, x['action__path'])
            return x
        return list(map(filter_abbr, super().gather_candidates(context)))

    def highlight(self):
        highlight(self.vim, self.syntax_name)
