# ============================================================================
# FILE: my_file.py
# AUTHOR: delphinus <delphinus@remora.cx>
# License: MIT license
# ============================================================================

import sys
from os.path import dirname

sys.path.append(dirname(dirname(__file__)))

from denite.source.file.rec import Source as Base
from denite.util import Candidate, Candidates, Nvim, UserContext
from my_util import icon_abbr, highlight


class Source(Base):
    def __init__(self, vim: Nvim):
        super().__init__(vim)
        self.name = "my_file_rec"

    def gather_candidates(self, context: UserContext) -> Candidates:
        def filter_abbr(x: Candidate) -> Candidate:
            x["abbr"] = icon_abbr(self.vim, x["action__path"])
            return x

        return list(map(filter_abbr, super().gather_candidates(context)))

    def highlight(self) -> None:
        highlight(self.vim, self.syntax_name)
