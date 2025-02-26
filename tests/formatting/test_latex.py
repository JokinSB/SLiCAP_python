# import pytest
import textwrap as tw
from SLiCAP.formatting import latex

OUTFILE = "latex_output"


def test_netlist():
    lf = latex.LaTeXFormatter()
    snippet = tw.dedent("""\
        \\textbf{{Netlist: dummy}}

        \\lstinputlisting[language=ltspice, numbers=left{0}{1}]{{cir/dummy}}

        """)
    assert snippet.format("", "") == lf.netlist("dummy").snippet
    assert snippet.format(", linerange={1-99}", "") == lf.netlist("dummy", lineRange="1-99").snippet
    assert snippet.format("", ", firstnumber=42") == lf.netlist("dummy", firstNumber=42).snippet
    assert snippet.format(", linerange={1-99}", ", firstnumber=42") == lf.netlist("dummy", lineRange="1-99", firstNumber=42).snippet



