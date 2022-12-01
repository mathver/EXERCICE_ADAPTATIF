from sympy import Symbol, latex, Rational
from .resolution import (
    prof_HL_A,
    form_A,
    profit_equilibre_LL,
    resol_prof_HL,
    graph_A,
    roots_A
)
from .class_define import Profit

profit = Profit()
p_2 = Symbol("p_2")


def question_4(
    h: int = 4, l: int = 2, gh: Rational = Rational(1, 4), gl: Rational = Rational(1, 2)
):
    """It takes the parameters of the model and returns the LaTeX code for the fourth question.

    Parameters
    ----------
     h : int, optional
        The value of high quality, default value = 4
    l : int, optional
        The value of low quality, default value = 2
    gh : Rational
        The value of gamma for high quality quality, default value = Rational(1,4)
    gl : Rational
        The value of gamma for high quality quality, default value = Rational(1,2)


    Returns
    -------
        The latex code of the fourth question of the report.

    """
    titre_section_4 = "\n\\subsection{Question 4}\n\\begin{flushleft}\n"
    text_1 = f"We're looking here for the expression of $A(p_1)$, thus that the consummer believe the product to be high quality. But we need to find a level which discourage low quality firm to mimic.\\newline"
    eq_1 = f"So, we have the following equation : \\newline\\newline $$\\pi(p_1;{l}, {l}) \\geq \\pi(p_1;{h}, {l}) - A$$\\newline\\newline"
    eq_2 = f"$$\\Leftrightarrow{latex(profit_equilibre_LL(profit))}\\geq{latex(prof_HL_A(profit, p_2, h, l , gl))}$$"
    eq_3 = f"$$\\Leftrightarrow A \geq {latex(resol_prof_HL(profit, p_2, h, l , gl))} - {latex(profit_equilibre_LL(profit))}$$"
    text_2 = "Finnaly, we obtain :\\newline\\newline"
    eq_4 = f"$$A(p_1)={latex(form_A(profit, p_2, h, l, gl))}$$\\newline\\newpage"
    root = roots_A(profit, p_2, h, l, gl)
    graph_A(profit, p_2, h, l, gl)
    fig = "\n\\includegraphics{graph.png}\n"
    text_3 = "\\newline\\newline A is the minimum advertising level that the high-quality firm must sets to respect the incentive constraint of low quality firm." 
    section_4 = (
        titre_section_4
        + "\n"
        + text_1
        + "\n"
        + eq_1
        + "\n"
        + eq_2
        + "\n"
        + eq_3
        + "\n"
        + text_2
        + "\n"
        + eq_4
        + "\n"
        + "\n"
        + fig
        + "\n"
        + root
        + "\n"
        + "\\end{flushleft}"
    )
    return section_4
