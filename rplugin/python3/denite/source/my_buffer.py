# ============================================================================
# FILE: my_buffer.py
# AUTHOR: delphinus <delphinus@remora.cx>
# License: MIT license
# ============================================================================

import sys
from os.path import dirname

sys.path.append(dirname(dirname(__file__)))

from denite.source.buffer import Source as Base
from denite.util import Nvim
from my_util import NO_NAME, abbr, icon, highlight
from time import localtime, strftime
from typing import Any, Dict


class Source(Base):
    def __init__(self, vim: Nvim):
        super().__init__(vim)
        self.name = "my_buffer"
        sys.path.append(dirname(dirname(__file__)))

    def _convert(
        self, buffer_attr: Dict[str, Any], rjust: int, ljustnm: int, rjustft: int
    ) -> Dict[str, Any]:
        if buffer_attr["name"] == "":
            name = NO_NAME
            path = ""
        else:
            name = self.vim.call("fnamemodify", buffer_attr["name"], ":~:.")
            path = self.vim.call("fnamemodify", buffer_attr["name"], ":p")
        return {
            "bufnr": buffer_attr["number"],
            "word": name,
            "abbr": " {0} {1}{2} {3}{4} {5}".format(
                icon(self.vim, name),
                str(buffer_attr["number"]).rjust(rjust, " "),
                buffer_attr["status"],
                abbr(self.vim, name),
                " [{}]".format(buffer_attr["filetype"])
                if buffer_attr["filetype"] != ""
                else "",
                strftime(
                    "(" + self.vars["date_format"] + ")",
                    localtime(buffer_attr["timestamp"]),
                )
                if self.vars["date_format"] != ""
                else "",
            ),
            "action__bufnr": buffer_attr["number"],
            "action__path": path,
            "timestamp": buffer_attr["timestamp"],
        }

    def highlight(self) -> None:
        highlight(self.vim, self.syntax_name)
