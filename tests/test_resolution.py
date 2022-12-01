"""Description.

Tests automatiques associés à la librairie resolution.
"""

import pytest
import sympy as sp
from sympy import Rational
from adap_exercice.class_define import Profit
from adap_exercice.resolution import (
    cn1_prof2,
    cs2_prof2,
    resolution_2,
    substitute_q2,
    profit_equilibre,
    resol_prof2_H,
    resol_prof2_L,
    resol_prof2subq_LL,
    resol_prof2subq_HH,
    resol_prof2subq_LH,
    resol_prof2subq_HL,
    resol_prof1_H,
    resol_prof1_L,
    resol_prof_HH,
    resol_prof_LL,
    resol_prof_HL,
    resol_prof_LH,
    cn1_profLL,
    cs2_profLL,
    prix_equilibre_LL,
    profit_equilibre_LL,
    prof_HL_A,
    form_A,
    opt_A,
    graph_A,
    roots_A,
)
from unittest.mock import patch
from matplotlib.testing.decorators import image_comparison


def test_cn1_prof2():
    profit = Profit()
    observe = sp.latex(cn1_prof2(profit, profit.p_2))
    attendu = "- \\gamma q_{1} - 2 p_{2} + s_{2} + 1"
    assert observe == attendu


def test_cs2_prof2():
    profit = Profit()
    observe = sp.latex(cs2_prof2(profit, profit.p_2))
    attendu = "-2"
    assert observe == attendu


def test_resolution_2():
    profit = Profit()
    observe = sp.latex(resolution_2(profit, profit.p_2))
    attendu = "- \\frac{\\gamma q_{1}}{2} + \\frac{s_{2}}{2} + \\frac{1}{2}"
    assert observe == attendu


def test_substitute_q2():
    profit = Profit()
    observe = sp.latex(substitute_q2(profit, profit.p_2))
    attendu = "\\frac{\\gamma q_{1}}{2} + \\frac{s_{2}}{2} - \\frac{1}{2}"
    assert observe == attendu


def test_profit_equilibre():
    profit = Profit()
    observe = sp.latex(profit_equilibre(profit, profit.p_2))
    attendu = "\\frac{\\left(\\gamma q_{1} + s_{2} - 1\\right)^{2}}{4}"
    assert observe == attendu


def test_resol_prof2_H():
    profit = Profit()
    observe = sp.latex(resol_prof2_H(profit, profit.p_2))
    attendu = "\\frac{\\left(q_{1} + 12\\right)^{2}}{64}"
    assert attendu == observe


def test_resol_prof2_L():
    profit = Profit()
    observe = sp.latex(resol_prof2_L(profit, profit.p_2))
    attendu = "\\frac{\\left(q_{1} + 2\\right)^{2}}{16}"
    assert attendu == observe


def test_resol_prof2subq_LL():
    profit = Profit()
    observe = sp.latex(resol_prof2subq_LL(profit, profit.p_2))
    attendu = "\\frac{\\left(p_{1} - 4\\right)^{2}}{16}"
    assert observe == attendu


def test_resol_prof2subq_HH():
    profit = Profit()
    observe = sp.latex(resol_prof2subq_HH(profit, profit.p_2))
    attendu = "\\frac{\\left(p_{1} - 16\\right)^{2}}{64}"
    assert observe == attendu


def test_resol_prof2subq_LH():
    profit = Profit()
    observe = sp.latex(resol_prof2subq_LH(profit, profit.p_2))
    attendu = "\\frac{\\left(p_{1} - 14\\right)^{2}}{64}"
    assert observe == attendu


def test_resol_prof2subq_HL():
    profit = Profit()
    observe = sp.latex(resol_prof2subq_HL(profit, profit.p_2))
    attendu = "\\frac{\\left(p_{1} - 4\\right)^{2}}{16}"
    assert observe == attendu


def test_resol_prof1_H():
    profit = Profit()
    observe = sp.latex(resol_prof1_H(profit, profit.q_1_NDV))
    attendu = "\\left(- p_{1} + q_{1}\\right) \\left(p_{1} - 1\\right)"
    assert observe == attendu


def test_resol_prof1_L():
    profit = Profit()
    observe = sp.latex(resol_prof1_L(profit, profit.q_1_NDV))
    attendu = "\\left(- p_{1} + q_{1}\\right) \\left(p_{1} - 1\\right)"
    assert observe == attendu


def test_resol_prof_HH():
    profit = Profit()
    observe = sp.latex(resol_prof_HH(profit, profit.p_2))
    attendu = "- \\frac{63 p_{1}^{2}}{64} + \\frac{9 p_{1}}{2}"
    assert observe == attendu


def test_resol_prof_LL():
    profit = Profit()
    observe = sp.latex(resol_prof_LL(profit, profit.p_2))
    attendu = "- \\frac{15 p_{1}^{2}}{16} + \\frac{5 p_{1}}{2} - 1"
    assert observe == attendu


def test_resol_prof_HL():
    profit = Profit()
    observe = sp.latex(resol_prof_HL(profit, profit.p_2))
    attendu = "- \\frac{15 p_{1}^{2}}{16} + \\frac{17 p_{1}}{4} - \\frac{7}{4}"
    assert observe == attendu


def test_resol_prof_LH():
    profit = Profit()
    observe = sp.latex(resol_prof_LH(profit, profit.p_2))
    attendu = "- \\frac{63 p_{1}^{2}}{64} + \\frac{41 p_{1}}{16} + \\frac{17}{16}"
    assert observe == attendu


def test_cn1_profLL():
    profit = Profit()
    observe = sp.latex(cn1_profLL(profit))
    attendu = "\\frac{5}{2} - \\frac{15 p_{1}}{8}"
    assert observe == attendu


def test_cs2_profLL():
    profit = Profit()
    observe = sp.latex(cs2_profLL(profit))
    attendu = "- \\frac{15}{8}"
    assert observe == attendu


def test_profit_equilibre_LL():
    profit = Profit()
    observe = sp.latex(profit_equilibre_LL(profit))
    attendu = "\\frac{2}{3}"
    assert observe == attendu


def test_prix_equilibre_LL():
    profit = Profit()
    observe = sp.latex(prix_equilibre_LL)
    attendu = "\\frac{8}{3}"


def test_prof_HL_A():
    profit = Profit()
    observe = sp.latex(prof_HL_A(profit, profit.p_2))
    attendu = "- A - \\frac{15 p_{1}^{2}}{16} + \\frac{17 p_{1}}{4} - \\frac{7}{4}"
    assert observe == attendu


def test_form_A():
    profit = Profit()
    observe = sp.latex(form_A(profit, profit.p_2))
    attendu = "- \\frac{15 p_{1}^{2}}{16} + \\frac{17 p_{1}}{4} - \\frac{29}{12}"
    assert observe == attendu


def test_opt_A():
    profit = Profit()
    observe = sp.latex(opt_A(profit, profit.p_2))
    attendu = "\\frac{8}{3}"
    assert observe == attendu


def test_graph_A():
    profit = Profit()
    graph_A(profit, profit.p_2)


def test_roots_A():
    profit = Profit()
    observe = roots_A(profit, profit.p_2)
    attendu = "There are two roots to $A(p_1)$, he makes advertising only inside the interval formed by the two roots :$\\frac{2}{3}$ and $\\frac{58}{15}$"
    assert observe == attendu
