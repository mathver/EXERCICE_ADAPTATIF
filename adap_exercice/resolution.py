"""
Module de résolution permettant de trouver la solution optimale au programme du producteur.
"""

import sympy as sp
from .class_define import Profit
from sympy import Rational
    

def cn1_prof2(obj: Profit, var):
    prof = obj.profit_2()
    return sp.diff(prof, var)

def cs2_prof2(obj: Profit, var):
    cn = cn1_prof2(obj, var)
    return sp.diff(cn, var)

def resolution_2(obj: Profit, var):
    return sp.solve(cn1_prof2(obj, var),var)[0]

def substitute_q2(obj: Profit, var):
    sol = resolution_2(obj, var)
    quant = obj.quantity_2()
    return quant.subs(var, sol)

def profit_equilibre(obj: Profit, var):
    profit = obj.profit_2()
    return sp.simplify(profit.subs(var, resolution_2(obj, var)))


def resol_prof2_H(obj: Profit, var, h: int = 4, gh: Rational = Rational(1,4)):
    sol = profit_equilibre(obj, var)
    return sp.simplify(sol.subs([(obj.s_2, h), (obj.gamma, gh)]))

def resol_prof2_L(obj: Profit, var, l: int = 2, gl: Rational = Rational(1,2)):
    sol = profit_equilibre(obj, var)
    return sp.simplify(sol.subs([(obj.s_2, l), (obj.gamma, gl)]))

def resol_prof2subq_LL(obj: Profit, var, l: int = 2, gl: Rational = Rational(1,2)):
    sol = profit_equilibre(obj, var)
    return sp.simplify(sol.subs([(obj.s_2, l), (obj.gamma, gl), (obj.q_1_NDV, obj.quantity_1()), (obj.s_1, l)]))

def resol_prof2subq_HH(obj: Profit, var, h: int = 4, gh: Rational = Rational(1,4)):
    sol = profit_equilibre(obj, var)
    return sp.simplify(sol.subs([(obj.s_2, h), (obj.gamma, gh), (obj.q_1_NDV, obj.quantity_1()), (obj.s_1, h)]))

def resol_prof2subq_LH(obj: Profit, var, h: int = 4, l: int = 2, gh: Rational = Rational(1,4)):
    sol = profit_equilibre(obj, var)
    return sp.simplify(sol.subs([(obj.s_2, h), (obj.gamma, gh), (obj.q_1_NDV, obj.quantity_1()), (obj.s_1, l)]))

def resol_prof2subq_HL(obj: Profit, var, h: int = 4, l: int = 2, gh: Rational = Rational(1,2)):
    sol = profit_equilibre(obj, var)
    return sp.simplify(sol.subs([(obj.s_2, l), (obj.gamma, gh), (obj.q_1_NDV, obj.quantity_1()), (obj.s_1, l)]))

def resol_prof1_H(obj: Profit, h: int = 4):
    fct = obj.profit_1()
    return fct.subs(obj.s_1, h)

def resol_prof1_L(obj: Profit, l: int = 2):
    fct = obj.profit_1()
    return fct.subs(obj.s_1, l)


def resol_prof_HH(obj: Profit, var, h: int = 4, gh: Rational = Rational(1,4)):
    prof1 = resol_prof1_H(obj, h)
    prof2 = resol_prof2_H(obj,var, h, gh)
    prof2_DV = prof2.subs(obj.q_1_NDV, obj.quantity_1())
    prof2_FIN = prof2_DV.subs(obj.s_1, h)
    return sp.decompose(prof1 + prof2_FIN)[0]

def resol_prof_LL(obj: Profit, var, l:int = 2, gl: Rational = Rational(1,2)):
    prof1 = resol_prof1_L(obj, l)
    prof2 = resol_prof2_L(obj,var, l, gl)
    prof2_DV = prof2.subs(obj.q_1_NDV, obj.quantity_1())
    prof2_FIN = prof2_DV.subs(obj.s_1, l)
    return sp.simplify(prof1 + prof2_FIN)

def resol_prof_HL(obj: Profit, var, h: int = 4, l:int = 2, gl: Rational = Rational(1,2)):
    prof1 = resol_prof1_H(obj, h)
    prof2 = resol_prof2_L(obj,var, l, gl)
    prof2_DV = prof2.subs(obj.q_1_NDV, obj.quantity_1())
    prof2_FIN = prof2_DV.subs(obj.s_1, h)
    return sp.simplify(prof1 + prof2_FIN)

def resol_prof_LH(obj: Profit, var,  h: int = 4, l:int = 2, gh: Rational = Rational(1,4)):
    prof1 = resol_prof1_L(obj, l)
    prof2 = resol_prof2_H(obj, var, h, gh)
    prof2_DV = prof2.subs(obj.q_1_NDV, obj.quantity_1())
    prof2_FIN = prof2_DV.subs(obj.s_1, l)
    return sp.simplify(prof1 + prof2_FIN)

def cn1_profLL(obj: Profit):
    prof_LL = resol_prof_LL(obj, obj.p_2)
    return sp.diff(prof_LL, obj.p_1)

def cs2_profLL(obj: Profit):
    cn = cn1_profLL(obj)
    return sp.diff(cn, obj.p_1)

def prix_equilibre_LL(obj: Profit):
    cn = cn1_profLL(obj)
    return sp.solve(cn, obj.p_1)[0]

def profit_equilibre_LL(obj: Profit):
    prof_LL = resol_prof_LL(obj, obj.p_2)
    px = prix_equilibre_LL(obj)
    return prof_LL.subs(obj.p_1, px)

def prof_HL_A(obj: Profit, var,  h: int = 4, l:int = 2, gl: Rational = Rational(1,2)):
    prof_A = resol_prof_HL(obj, var, h, l, gl) - obj.A
    return prof_A

def form_A(obj: Profit, var,  h: int = 4, l:int = 2, gl: Rational = Rational(1,2)):
    A = sp.solve(profit_equilibre_LL(obj) > prof_HL_A(obj, var, h, l, gl), obj.A).rhs
    return A

def val_A(obj: Profit, var,  h: int = 4, l:int = 2, gl: Rational = Rational(1,2)):
    roots = form_A(obj, var, h, l, gl)
    a, b = sp.solve(roots)
    return a, b

def opt_A(obj: Profit, var,  h: int = 4, l:int = 2, gh:  Rational = Rational(1,4), gl: Rational = Rational(1,2)):
    return sp.solve(sp.diff(resol_prof_HH(obj, var, h, gh) - form_A(obj, var, h, l, gl), obj.p_1), obj.p_1)[0]

def graph_A(obj: Profit, var,  h: int = 4, l:int = 2, gl: Rational = Rational(1,2)):
    graph = sp.plot(form_A(obj, var, h, l, gl), xlim =(0,h+2), ylim =(0,h+2), ylabel = "$A(p_1)$", show = False)
    graph.save('./graph.png')