"""LaTeX formatter class."""

from ._common import Snippet, BaseFormatter
import SLiCAP.SLiCAPlatex as sl


class LaTeXFormatter(BaseFormatter):
    """
    LaTeX Formatter, inherited from the base formatter.
    Implements the LaTeX version of the functionality.
    Extra functionality is always allowed.
    """

    def __init__(self):
        super().__init__()

    def netlist(self, netlistFile, lineRange=None, firstNumber=None):
        return Snippet(sl.netlist2TEX(netlistFile, lineRange, firstNumber))

    def specs(self, specs, specType, label='', caption=''):
        return Snippet(sl.specs2TEX(specs, specType, label, caption))

    def elementData(self, circuitObject, label='', append2caption=''):
        return Snippet(sl.elementData2TEX(circuitObject, label, append2caption))

    def eqn(self, LHS, RHS, units='', label='', multiline=0):
        return Snippet(sl.eqn2TEX(LHS, RHS, units, label, multiline))
