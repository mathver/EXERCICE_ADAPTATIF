from sympy import Symbol, latex, Rational
from .resolution import cn1_prof2, resolution_2, cs2_prof2, substitute_q2, profit_equilibre, resol_prof2_H, resol_prof2_L
from .class_define import Profit

profit = Profit()
p_2 = Symbol('p_2')

def question_1(h: int = 4, l: int = 2, gh: Rational = Rational(1,4), gl: Rational = Rational(1,2)):
    titre_section_1 = "\\section{Exercice}\n\\subsection{Question 1}\n\\begin{flushleft}"
    question_1 = f"We write the second period profit :\\newline $${latex(profit.profit_2_NDV())} = {latex(profit.profit_2())}$$\\newline"
    cn1 = f"$CN1 : \\; {latex(cn1_prof2(profit, p_2))} = 0 \\newline\\newline \\Rightarrow \; p_2(s_2) = {latex(resolution_2(profit, p_2))}$\\newline"
    cs2 = f"$CS2 : \\; {latex(cs2_prof2(profit, p_2))} < 0 $, so we have a maximum\\newline"
    q2 = f"$q_2 = s_2 - {latex(resolution_2(profit, p_2))}\\newline\\newline \\Rightarrow q_2(s_2) = {latex(substitute_q2(profit, p_2))}$\\newline"

    text1 = "We integrate the two version of $p_2(s_2)$ and $q_2(s_2)$ we found in the preceding profit form"
    prof_eq = f"$$\\tilde\\pi_2 = {latex(profit_equilibre(profit, p_2))}$$\\newline" 
    text2 = "After that, we differentiate by quality $s_2$ to obtain these two equations :\\newline"
    prof_eq_H = f"$$\\tilde\\pi_2^H(q_1) = {latex(resol_prof2_H(profit, p_2, h, gh))}$$"
    prof_eq_L = f"$$\\tilde\\pi_2^L(q_1) = {latex(resol_prof2_L(profit, p_2, l, gl))}$$\\newline"

    section_1 = titre_section_1 + question_1 +"\n"+ cn1 + "\n\n" + cs2 + "\n\n" + q2 + "\n\n" + text1 + "\n\n" + prof_eq + "\n\n"+ text2 + "\n\n" + prof_eq_H + "\n\n" + prof_eq_L + "\n\end{flushleft}"
    return section_1
