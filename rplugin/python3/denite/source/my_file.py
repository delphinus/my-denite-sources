# ============================================================================
# FILE: my_file.py
# AUTHOR: delphinus <delphinus@remora.cx>
# License: MIT license
# ============================================================================

import sys
from os.path import dirname
sys.path.append(dirname(dirname(__file__)))

from my_util import abbr, highlight
from denite.source.file import Source as Base


class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'my_file'

    def gather_candidates(self, context):
        def filter_abbr(x):
            x['abbr'] = abbr(self.vim, x['abbr'])
            return x
        return list(map(filter_abbr, super().gather_candidates(context)))

    def highlight(self):
        highlight(self.vim, self.syntax_name)
