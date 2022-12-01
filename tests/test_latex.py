import pytest
from sympy import Symbol, latex, Rational
from adap_exercice.resolution import cn1_prof2, resolution_2, cs2_prof2, substitute_q2, profit_equilibre, resol_prof2_H, resol_prof2_L
from adap_exercice.class_define import Profit
from adap_exercice.latex_q1 import question_1

profit = Profit()
p_2 = Symbol('p_2')

def test_latex_q_1():
    observe = question_1()
    attendu = '\\section{Exercice}\n\\subsection{Question 1}\n\\begin{flushleft}We write the second period profit :\\newline $$q_{2} \\left(\\gamma q_{1} + p_{2} - 1\\right) = \\left(- p_{2} + s_{2}\\right) \\left(\\gamma q_{1} + p_{2} - 1\\right)$$\\newline\n$CN1 : \\; - \\gamma q_{1} - 2 p_{2} + s_{2} + 1 = 0 \\newline\\newline \\Rightarrow \\; p_2(s_2) = - \\frac{\\gamma q_{1}}{2} + \\frac{s_{2}}{2} + \\frac{1}{2}$\\newline\n\n$CS2 : \\; -2 < 0 $, so we have a maximum\\newline\n\n$q_2 = s_2 - - \\frac{\\gamma q_{1}}{2} + \\frac{s_{2}}{2} + \\frac{1}{2}\\newline\\newline \\Rightarrow q_2(s_2) = \\frac{\\gamma q_{1}}{2} + \\frac{s_{2}}{2} - \\frac{1}{2}$\\newline\n\nWe integrate the two version of $p_2(s_2)$ and $q_2(s_2)$ we found in the preceding profit form\n\n$$\\tilde\\pi_2 = \\frac{\\left(\\gamma q_{1} + s_{2} - 1\\right)^{2}}{4}$$\\newline\n\nAfter that, we differentiate by quality $s_2$ to obtain these two equations :\\newline\n\n$$\\tilde\\pi_2^H(q_1) = \\frac{\\left(q_{1} + 12\\right)^{2}}{64}$$\n\n$$\\tilde\\pi_2^L(q_1) = \\frac{\\left(q_{1} + 2\\right)^{2}}{16}$$\\newline\n\\end{flushleft}'
    assert observe == attendu