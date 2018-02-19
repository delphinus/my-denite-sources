# ============================================================================
# FILE: my_file.py
# AUTHOR: delphinus <delphinus@remora.cx>
# License: MIT license
# ============================================================================

import importlib
from denite.source.file import Source as Base


class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'my_file'
        self.__util = importlib.import_module('..my_util')

    def gather_candidates(self, context):
        def filter_abbr(x):
            x['abbr'] = self.__util.abbr(self.vim, x['abbr'])
            return x
        return list(map(filter_abbr, super().gather_candidates(context)))

    def highlight(self):
        self.__util.highlight(self.vim, self.syntax_name)
