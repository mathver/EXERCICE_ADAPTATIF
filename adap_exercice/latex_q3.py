from sympy import Symbol, latex, decompose, Rational, simplify
from .resolution import resol_prof_LL, cn1_profLL, cs2_profLL, prix_equilibre_LL, profit_equilibre_LL
from .class_define import Profit

profit = Profit()
p_2 = Symbol('p_2')

def question_3(h: int = 4, l: int = 2, gh: Rational = Rational(1,4), gl: Rational = Rational(1,2)):
    titre_section_3 = "\\newpage\n\\subsection{Question 3}\n\\begin{flushleft}\n"
    text_1 = "We have here to find the optimal strategy for a low type quality monopole in separating equilibrium. We know that in separating equilibrium, the level of advertising $A$ will be 0.\\newline"
    text_2 = f"So we have the following program :\\newline\\newline $$\\pi(p_1;{l},{l}) = {latex(decompose(resol_prof_LL(profit, p_2, l, gl))).replace('[', '(').replace(']', ')')}$$\\newline\\newline"
    cn1 = f"CN1 : ${latex(cn1_profLL(profit))}$\\newline\\newline"
    cs2 = f"CS2 : ${latex(cs2_profLL(profit))} < 0$\\newline\\newline"
    text_3 = "If we solve by $p_1$ the CN1, we obtain the equilibrium price : \\newline\\newline"
    p1 = f"$\\Rightarrow p_L^*= {latex(prix_equilibre_LL(profit))}$\\newline\\newline"
    profit_LL = "We obtain the equilibrium profit : \\newline\\newline"
    eq_pro = f"$$\\pi({latex(prix_equilibre_LL(profit))}; {l},{l}) = {latex(profit_equilibre_LL(profit))}$$"






    section_3 = (titre_section_3 + "\n" + text_1 + "\n" + text_2 + "\n" + cn1 + "\n" + cs2 + "\n" + text_3 + "\n" + p1 + "\n" + profit_LL + "\n" + eq_pro + "\n" + "\\end{flushleft}")
    return section_3