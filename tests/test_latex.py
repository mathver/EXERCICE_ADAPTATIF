import pytest
from sympy import Symbol
from adap_exercice.class_define import Profit
from adap_exercice.latex_q1 import question_1
from adap_exercice.latex_q2 import question_2
from adap_exercice.latex_q3 import question_3
from adap_exercice.latex_q4 import question_4
from adap_exercice.latex_q5 import question_5
from adap_exercice.latex_q6 import question_6

profit = Profit()
p_2 = Symbol("p_2")


def test_latex_q_1():
    observe = question_1()
    attendu = "\\section{Exercice}\n\\subsection{Question 1}\n\\begin{flushleft}We write the second period profit :\\newline $$q_{2} \\left(\\gamma q_{1} + p_{2} - 1\\right) = \\left(- p_{2} + s_{2}\\right) \\left(\\gamma q_{1} + p_{2} - 1\\right)$$\\newline\n$CN1 : \\; - \\gamma q_{1} - 2 p_{2} + s_{2} + 1 = 0 \\newline\\newline \\Rightarrow \\; p_2(s_2) = - \\frac{\\gamma q_{1}}{2} + \\frac{s_{2}}{2} + \\frac{1}{2}$\\newline\n\n$CS2 : \\; -2 < 0 $, so we have a maximum\\newline\n\n$q_2 = s_2 - - \\frac{\\gamma q_{1}}{2} + \\frac{s_{2}}{2} + \\frac{1}{2}\\newline\\newline \\Rightarrow q_2(s_2) = \\frac{\\gamma q_{1}}{2} + \\frac{s_{2}}{2} - \\frac{1}{2}$\\newline\n\nWe integrate the two version of $p_2(s_2)$ and $q_2(s_2)$ we found in the preceding profit form\n\n$$\\tilde\\pi_2 = \\frac{\\left(\\gamma q_{1} + s_{2} - 1\\right)^{2}}{4}$$\\newline\n\nAfter that, we differentiate by quality $s_2$ to obtain these two equations :\\newline\n\n$$\\tilde\\pi_2^H(q_1) = \\frac{\\left(q_{1} + 12\\right)^{2}}{64}$$\n\n$$\\tilde\\pi_2^L(q_1) = \\frac{\\left(q_{1} + 2\\right)^{2}}{16}$$\\newline\n\\end{flushleft}"
    assert observe == attendu


def test_latex_q_2():
    observe = question_2()
    attendu = "\\newpage\\subsection{Question 2}\n\\begin{flushleft}\n\nWe have 4 cases to study there with $\\gamma_h = 1/4$ and $\\gamma_l = 1/2$ :\n \\newline\\newline\n\\underline{\\nth{1} Case} : $s_1 = 4$ \\& $s_2 = 4$\\newline Here, customers believe quality is high and perceive it well in \\nth2 period.\\newline\\newline\nWe have the monopoly profit in \\nth{1} period :\\newline\\newline$\\pi_1(p_1) = q_{1} \\left(p_{1} - 1\\right) = \\left(- p_{1} + s_{1}\\right) \\left(p_{1} - 1\\right) = \\left(4 - p_{1}\\right) \\left(p_{1} - 1\\right)$\\newline\\newline\nSo we obtain the form of profit below \\newline\n$$\\pi_1^H(p_1)=\\left( - p_{1}^{2} + 5 p_{1} - 4\\right)$$\\newline\\newline\nWe take the profit of the \\nth{2} period we found before and substitute with $q_1$ to obtain :\\newline\\newline\n$$\\pi_2^H(p_1)=\\left( \\frac{p_{1}^{2}}{64} - \\frac{p_{1}}{2} + 4\\right)$$\nFinnaly, we sum the two profit found before to obtain the total profit below : \\newline\\newline\n$$\\pi(p_1;4,4)=\\left( - \\frac{63 p_{1}^{2}}{64} + \\frac{9 p_{1}}{2}\\right)$$\n\\underline{\\nth{2} Case} : $s_1 = 4$ \\& $s_2 = 2$\\newline Here, customers believe quality is high and it wasn't, so they adapt their believes in \\nth2 period.\\newline\\newline\nWe have the monopoly profit in \\nth{1} period :\\newline\\newline$\\pi_1(p_1) = q_{1} \\left(p_{1} - 1\\right) = \\left(- p_{1} + s_{1}\\right) \\left(p_{1} - 1\\right) = \\left(4 - p_{1}\\right) \\left(p_{1} - 1\\right)$\\newline\nSo we obtain the form of profit below \\newline\n$$\\pi_1^H(p_1)=\\left( - p_{1}^{2} + 5 p_{1} - 4\\right)$$\nWe take the profit of the \\nth{2} period we found before and substitute with $q_1$ to obtain :\\newline\\newline\n$$\\pi_2^L(p_1)=\\left( \\frac{p_{1}^{2}}{16} + \\frac{p_{1}}{16} + \\frac{1}{64}\\right)$$\nFinnaly, we sum the two profit found before to obtain the total profit below : \\newline\\newline\n$$\\pi(p_1;4,2)=\\left( - \\frac{15 p_{1}^{2}}{16} + \\frac{17 p_{1}}{4} - \\frac{7}{4}\\right)$$\n\\underline{\\nth{3} Case} : $s_1 = 2$ \\& $s_2 = 4$\\newline Here, customers believe quality is low and it wasn't, so they adapt their believes in \\nth2 period.\\newline\\newline\nWe have the monopoly profit in \\nth{1} period :\\newline$\\pi_1(p_1) = q_{1} \\left(p_{1} - 1\\right) = \\left(- p_{1} + s_{1}\\right) \\left(p_{1} - 1\\right) = \\left(2 - p_{1}\\right) \\left(p_{1} - 1\\right)$\\newline\nSo we obtain the form of profit below \\newline\n$$\\pi_1^L(p_1)=\\left( - p_{1}^{2} + 3 p_{1} - 2\\right)$$\nWe take the profit of the \\nth{2} period we found before and substitute with $q_1$ to obtain :\\newline\\newline\n$$\\pi_2^H(p_1)=\\left( \\frac{p_{1}^{2}}{64} - \\frac{49 p_{1}}{128} + \\frac{2401}{1024}\\right)$$\nFinnaly, we sum the two profit found before to obtain the total profit below : \\newline\\newline\n$$\\pi(p_1;2,4)=\\left( - \\frac{63 p_{1}^{2}}{64} + \\frac{41 p_{1}}{16} + \\frac{17}{16}\\right)$$\n\\underline{\\nth{4} Case} : $s_1 = 2$ \\& $s_2 = 2$\\newline Here, customers believe quality is low and perceive it well in \\nth2 period.\\newline\\newline\nWe have the monopoly profit in \\nth{1} period :\\newline$\\pi_1(p_1) = q_{1} \\left(p_{1} - 1\\right) = \\left(- p_{1} + s_{1}\\right) \\left(p_{1} - 1\\right) = \\left(2 - p_{1}\\right) \\left(p_{1} - 1\\right)$\\newline\nSo we obtain the form of profit below \\newline\n$$\\pi_1^L(p_1)=\\left( - p_{1}^{2} + 3 p_{1} - 2\\right)$$\nWe take the profit of the \\nth{2} period we found before and substitute with $q_1$ to obtain :\\newline\\newline\n$$\\pi_2^L(p_1)=\\left( \\frac{p_{1}^{2}}{16} - \\frac{p_{1}}{2} + 1\\right)$$\nFinnaly, we sum the two profit found before to obtain the total profit below : \\newline\\newline\n$$\\pi(p_1;2,2)=\\left( - \\frac{15 p_{1}^{2}}{16} + \\frac{5 p_{1}}{2} - 1\\right)$$\n\n\n\\end{flushleft}"
    assert observe == attendu


def test_latex_q_3():
    observe = question_3()
    attendu = "\\newpage\n\\subsection{Question 3}\n\\begin{flushleft}\n\nWe have here to find the optimal strategy for a low type quality monopole in separating equilibrium. We know that in separating equilibrium, the level of advertising $A$ will be 0.\\newline\nSo we have the following program :\\newline\\newline $$\\pi(p_1;2,2) = \\left( - \\frac{15 p_{1}^{2}}{16} + \\frac{5 p_{1}}{2} - 1\\right)$$\\newline\\newline\nCN1 : $\\frac{5}{2} - \\frac{15 p_{1}}{8}$\\newline\\newline\nCS2 : $- \\frac{15}{8} < 0$\\newline\\newline\nIf we solve by $p_1$ the CN1, we obtain the equilibrium price : \\newline\\newline\n$\\Rightarrow p_L^*= \\frac{4}{3}$\\newline\\newline\nWe obtain the equilibrium profit : \\newline\\newline\n$$\\pi(\\frac{4}{3}; 2,2) = \\frac{2}{3}$$\n\\end{flushleft}"
    assert observe == attendu


def test_latex_q_4():
    observe = question_4()
    attendu = "\n\\subsection{Question 4}\n\\begin{flushleft}\n\nWe're looking here for the expression of $A(p_1)$, thus that the consummer believe the product to be high quality. But we need to find a level which discourage low quality firm to mimic.\\newline\nSo, we have the following equation : \\newline\\newline $$\\pi(p_1;2, 2) \\geq \\pi(p_1;4, 2) - A$$\\newline\\newline\n$$\\Leftrightarrow\\frac{2}{3}\\geq- A - \\frac{15 p_{1}^{2}}{16} + \\frac{17 p_{1}}{4} - \\frac{7}{4}$$\n$$\\Leftrightarrow A \\geq - \\frac{15 p_{1}^{2}}{16} + \\frac{17 p_{1}}{4} - \\frac{7}{4} - \\frac{2}{3}$$\nFinnaly, we obtain :\\newline\\newline\n$$A(p_1)=- \\frac{15 p_{1}^{2}}{16} + \\frac{17 p_{1}}{4} - \\frac{29}{12}$$\\newline\\newpage\n\n\n\\includegraphics{graph.png}\n\nThere are two roots to $A(p_1)$, he makes advertising only inside the interval formed by the two roots :$\\frac{2}{3}$ and $\\frac{58}{15}$\n\\end{flushleft}"
    assert attendu == observe


def test_latex_q_5():
    observe = question_5()
    attendu = "\n\\subsection{Question 5}\n\\begin{flushleft}\n\nHere, we try to find the strategy of a high quality monopoly in a separating equilibrium, which is given by :\\newline\\newline\n$$\\max \\; \\pi(p_1;4,4)-A$$\\newline\nIf wer replacing by the value of profit and $A$ we found previously, we obtain : \\newline\\newline\n$$\\pi(p_1;4,4)-A=- \\frac{63 p_{1}^{2}}{64} + \\frac{9 p_{1}}{2}-- \\frac{15 p_{1}^{2}}{16} + \\frac{17 p_{1}}{4} - \\frac{29}{12}$$\n$$\\pi(p_1;4,4)-A=- \\frac{3 p_{1}^{2}}{64} + \\frac{p_{1}}{4} + \\frac{29}{12}$$\\newline\\newline\nCN1 : $\\frac{1}{4} - \\frac{3 p_{1}}{32}$\\newline\\newline\nCS2 : $- \\frac{3}{32}<0$\\newline\\newline\n$\\Rightarrow p_1^*=\\frac{8}{3}$\\newline\\newline\nWith the value of $p_1$, we can rewrite the optimal amount of advertising as :\\newline\\newline\n$A(\\frac{8}{3})=\\frac{9}{4}$\n\\end{flushleft}"
    assert observe == attendu


def test_latex_q_6():
    observe = question_6()
    attendu = "\n\\subsection{Question 6}\n\\begin{flushleft}\n\nIn full information market, the monopoly don't need to advertise and set $A=0$ and we have to maximize the following profit :\\newline\\newline\n$$\\max \\; \\pi(p_1;4,4) = - \\frac{63 p_{1}^{2}}{64} + \\frac{9 p_{1}}{2}$$\\newline\\newline\nCN1 : $\\frac{9}{2} - \\frac{63 p_{1}}{32}$\\newline\\newline\nCS2 : $- \\frac{63}{32}<0$\\newline\\newline\n$p_H^* = \\left( \\frac{16}{7}\\right)$\\newline\\newline\nWe can see that the price is less than in separating equilibrium, so we understand that the monopoly separates itself by overpricing and advertising.\n\\end{flushleft}"
    assert observe == attendu
