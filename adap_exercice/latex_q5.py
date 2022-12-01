from sympy import Symbol, latex, Rational, simplify, diff
import sympy 
from .resolution import form_A, val_A, opt_A, resol_prof_HH
from .class_define import Profit

profit = Profit()
p_2 = Symbol('p_2')

def question_5(h: int = 4, l: int = 2, gh: Rational = Rational(1,4), gl: Rational = Rational(1,2)):
    titre_section_5 = "\n\\subsection{Question 5}\n\\begin{flushleft}\n"
    text_1 = f"Here, we try to find the strategy of a high quality monopoly in a separating equilibrium, which is given by :\\newline\\newline"
    eq_1 = f"$$\\max \\; \\pi(p_1;{h},{h})-A$$\\newline"
    text_2 = "If wer replacing by the value of profit and $A$ we found previously, we obtain : \\newline\\newline"
    eq_2 = f"$$\\pi(p_1;{h},{h})-A={latex(resol_prof_HH(profit, p_2, h ,gh))}-{latex(form_A(profit, p_2, h, l, gl))}$$"
    eq_3 = f"$$\\pi(p_1;{h},{h})-A={latex(simplify(resol_prof_HH(profit, p_2, h ,gh)-form_A(profit, p_2, h, l, gl)))}$$\\newline\\newline"
    cn1 = f"CN1 : ${latex(diff(resol_prof_HH(profit, p_2, h ,gh)-form_A(profit, p_2, h, l, gl),profit.p_1))}$\\newline\\newline"
    cs2 = f"CS2 : ${latex(diff(diff(resol_prof_HH(profit, p_2, h ,gh)-form_A(profit, p_2, h, l, gl),profit.p_1), profit.p_1))}<0$\\newline\\newline"
    prof_opt = f"$\\Rightarrow p_1^*={latex(opt_A(profit, p_2, h, l, gh, gl))}$\\newline\\newline"
    text_3 = f"With the value of $p_1$, we can rewrite the optimal amount of advertising as :\\newline\\newline"
    ammount_A = f"$A({latex(opt_A(profit, p_2, h, l, gh, gl))})={latex(form_A(profit, p_2, h, l, gl).subs(profit.p_1, opt_A(profit, p_2, h, l, gh, gl)))}$"
    section_5 = (titre_section_5 + "\n" + text_1 + "\n" + eq_1 + "\n" + text_2 + "\n"
    + eq_2+ "\n" + eq_3 + "\n"+ cn1 + "\n"+ cs2 + "\n" + prof_opt+ "\n" + text_3 + "\n" + ammount_A + "\n" +"\end{flushleft}")
    return section_5