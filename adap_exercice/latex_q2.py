from sympy import Symbol, latex, decompose, Rational, simplify
from .resolution import (resol_prof1_H, resol_prof1_L,
resol_prof2subq_HH, resol_prof_HH,
resol_prof2subq_HL, resol_prof_HL,
resol_prof_LH, resol_prof2subq_LH,
resol_prof_LL, resol_prof2subq_LL)
from .class_define import Profit

profit = Profit()
p_2 = Symbol('p_2')

def question_2(h: int = 4, l: int = 2, gh: Rational = Rational(1,4), gl: Rational = Rational(1,2)):
    titre_section_2 = "\\subsection{Question 2}\n\\begin{flushleft}\n"
    text1 = f"We have 4 cases to study there with $\\gamma_h = {gh}$ and $\\gamma_l = {gl}$ :\n \\newline\\newline"
    cas1 = "\\underline{\\nth{1} Case} : " + f"$s_1 = {h}$ \\& $s_2 = {h}$\\newline Here, customers believe quality is high and perceive it well in \\nth{2} period.\\newline\\newline"
    textc1 = ("We have the monopoly profit in \\nth{1} period :\\newline\\newline" +
    f"$\\pi_1(p_1) = {latex(profit.profit_1_NDV())} = {latex(profit.profit_1())} = {latex(resol_prof1_H(profit, h))}$\\newline\\newline")
    text2c1 = "So we obtain the form of profit below \\newline"
    prof1HH = f"$$\\pi_1^H(p_1)={latex(decompose(resol_prof1_H(profit, h))).replace('[', '(').replace(']', ')')}$$\\newline\\newline"
    text3c1 = "We take the profit of the \\nth{2} period we found before and substitute with $q_1$ to obtain :\\newline\\newline"
    prof2HH = f"$$\\pi_2^H(p_1)={latex(decompose(resol_prof2subq_HH(profit, p_2, h, gh))).replace('[', '(').replace(']', ')')}$$"
    text4c1 = "Finnaly, we sum the two profit found before to obtain the total profit below : \\newline\\newline"
    profHH = f"$$\\pi(p_1;{h},{h})={latex(decompose(resol_prof_HH(profit, p_2, h, gh))).replace('[', '(').replace(']', ')')}$$"

    cas2 = "\\underline{\\nth{2} Case} : " + f"$s_1 = {h}$ \\& $s_2 = {l}$\\newline Here, customers believe quality is high and it wasn't, so they adapt their believes in \\nth{2} period.\\newline\\newline"
    textc2 = ("We have the monopoly profit in \\nth{1} period :\\newline\\newline" + 
    f"$\\pi_1(p_1) = {latex(profit.profit_1_NDV())} = {latex(profit.profit_1())} = {latex(resol_prof1_H(profit, h))}$\\newline")
    text2c2 = "So we obtain the form of profit below \\newline"
    prof1HL = f"$$\\pi_1^H(p_1)={latex(decompose(resol_prof1_H(profit, h))).replace('[', '(').replace(']', ')')}$$"
    text3c2 = "We take the profit of the \\nth{2} period we found before and substitute with $q_1$ to obtain :\\newline\\newline"
    prof2HL = f"$$\\pi_2^L(p_1)={latex(decompose(resol_prof2subq_HL(profit, p_2, l, gl))).replace('[', '(').replace(']', ')')}$$"
    text4c2 = "Finnaly, we sum the two profit found before to obtain the total profit below : \\newline\\newline"
    profHL = f"$$\\pi(p_1;{h},{l})={latex(decompose(resol_prof_HL(profit, p_2, h, l, gl))).replace('[', '(').replace(']', ')')}$$"

    cas3 = "\\underline{\\nth{3} Case} : " + f"$s_1 = {l}$ \\& $s_2 = {h}$\\newline Here, customers believe quality is low and it wasn't, so they adapt their believes in \\nth{2} period.\\newline\\newline"
    textc3 = ("We have the monopoly profit in \\nth{1} period :\\newline" +
    f"$\\pi_1(p_1) = {latex(profit.profit_1_NDV())} = {latex(profit.profit_1())} = {latex(resol_prof1_L(profit, l))}$\\newline")
    text2c3 = "So we obtain the form of profit below \\newline"
    prof1LH = f"$$\\pi_1^L(p_1)={latex(decompose(resol_prof1_L(profit, l))).replace('[', '(').replace(']', ')')}$$"
    text3c3 = "We take the profit of the \\nth{2} period we found before and substitute with $q_1$ to obtain :\\newline\\newline"
    prof2LH = f"$$\\pi_2^H(p_1)={latex(decompose(resol_prof2subq_LH(profit, p_2, h, gh))).replace('[', '(').replace(']', ')')}$$"
    text4c3 = "Finnaly, we sum the two profit found before to obtain the total profit below : \\newline\\newline"
    profLH = f"$$\\pi(p_1;{l},{h})={latex(decompose(resol_prof_LH(profit, p_2, h, l, gh))).replace('[', '(').replace(']', ')')}$$"

    cas4 = "\\underline{\\nth{4} Case} : " + f"$s_1 = {l}$ \\& $s_2 = {l}$\\newline Here, customers believe quality is low and perceive it well in \\nth{2} period.\\newline\\newline"
    textc4 = ("We have the monopoly profit in \\nth{1} period :\\newline" +
    f"$\\pi_1(p_1) = {latex(profit.profit_1_NDV())} = {latex(profit.profit_1())} = {latex(resol_prof1_L(profit, l))}$\\newline")
    text2c4 = "So we obtain the form of profit below \\newline"
    prof1LL = f"$$\\pi_1^L(p_1)={latex(decompose(resol_prof1_L(profit, l))).replace('[', '(').replace(']', ')')}$$"
    text3c4 = "We take the profit of the \\nth{2} period we found before and substitute with $q_1$ to obtain :\\newline\\newline"
    prof2LL = f"$$\\pi_2^H(p_1)={latex(decompose(resol_prof2subq_LL(profit, p_2, l, gl))).replace('[', '(').replace(']', ')')}$$"
    text4c4 = "Finnaly, we sum the two profit found before to obtain the total profit below : \\newline\\newline"
    profLL = f"$$\\pi(p_1;{l},{l})={latex(decompose(resol_prof_LL(profit, p_2, l, gl))).replace('[', '(').replace(']', ')')}$$"




    section_2 = ("\\newpage"+ titre_section_2 + "\n"+ text1 + "\n" + 
    cas1 + "\n" +textc1 + "\n" + text2c1 + "\n" + prof1HH + "\n"+ text3c1 + "\n" + prof2HH + "\n" + text4c1 + "\n" + profHH + "\n"+
    cas2 + "\n" +textc2 + "\n" + text2c2 + "\n" + prof1HL + "\n"+ text3c2 + "\n" + prof2HL + "\n" + text4c2 + "\n" + profHL + "\n"+
    cas3 + "\n" +textc3 + "\n" + text2c3 + "\n" + prof1LH + "\n"+ text3c3 + "\n" + prof2LH + "\n" + text4c3 + "\n" + profLH + "\n"+
    cas4 + "\n" +textc4 + "\n" + text2c4 + "\n" + prof1LL + "\n"+ text3c4 + "\n" + prof2LL + "\n" + text4c4 + "\n" + profLL + "\n"+
    "\n" +"\n\end{flushleft}")
    return section_2