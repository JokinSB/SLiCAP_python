# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 13:53:46 2025

@author: joba138
"""

import textwrap as tw
import pytest
from SLiCAP.formatting import latex

OUTFILE = "latex_output"


def test_netlist():
    lf = latex.LaTeXFormatter()
    snippet = tw.dedent("""\
        \\textbf{{Netlist: dummy}}

        \\lstinputlisting[language=ltspice, numbers=left{0}{1}]{{cir/dummy}}

        """)
    latex.LaTeXFormatter(autosave=False)
    assert snippet.format("", "") == lf.netlist("dummy")
    assert snippet.format(", linerange={1-99}", "") == lf.netlist("dummy", lineRange="1-99")
    assert snippet.format("", ", firstnumber=42") == lf.netlist("dummy", firstNumber=42)
    assert snippet.format(", linerange={1-99}", ", firstnumber=42") == lf.netlist("dummy", lineRange="1-99", firstNumber=42)



