# ============================================================================
# FILE: my_file_old.py
# AUTHOR: delphinus <delphinus@remora.cx>
# License: MIT license
# ============================================================================

import sys
from os.path import dirname

sys.path.append(dirname(dirname(__file__)))

from my_util import icon_abbr, highlight
from denite.source.file_old import Source as Base


class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = "my_file_old"

    def gather_candidates(self, context):
        return [
            {"word": x, "abbr": icon_abbr(self.vim, x), "action__path": x}
            for x in self.vim.call("denite#helper#_get_oldfiles")
        ]

    def highlight(self):
        highlight(self.vim, self.syntax_name)
