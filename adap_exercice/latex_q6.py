from sympy import Symbol, latex, Rational, diff, solve
from .resolution import resol_prof_HH
from .class_define import Profit

profit = Profit()
p_2 = Symbol("p_2")


def question_6(
    h: int = 4, l: int = 2, gh: Rational = Rational(1, 4), gl: Rational = Rational(1, 2)
):
    """It takes the parameters of the model and returns the LaTeX code for the sixth question.

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
        The latex code of the sith question of the report.

    """
    titre_section_6 = "\n\\subsection{Question 6}\n\\begin{flushleft}\n"
    text_1 = f"In full information market, the monopoly don't need to advertise and set $A=0$ and we have to maximize the following profit :\\newline\\newline"
    eq_1 = f"$$\\max \\; \\pi(p_1;{h},{h}) = {latex(resol_prof_HH(profit, p_2, h ,gh))}$$\\newline\\newline"
    cn1 = f"CN1 : ${latex(diff(resol_prof_HH(profit, p_2, h ,gh), profit.p_1))}$\\newline\\newline"
    cs2 = f"CS2 : ${latex(diff(diff(resol_prof_HH(profit, p_2, h ,gh), profit.p_1), profit.p_1))}<0$\\newline\\newline"
    prix_opt = f"$p_H^* = {latex(solve(diff(resol_prof_HH(profit, p_2, h ,gh), profit.p_1), profit.p_1)).replace('[','(').replace(']',')')}$\\newline\\newline"
    text_2 = "We can see that the price is less than in separating equilibrium, so we understand that the monopoly separates itself by overpricing and advertising."
    section_6 = (
        titre_section_6
        + "\n"
        + text_1
        + "\n"
        + eq_1
        + "\n"
        + cn1
        + "\n"
        + cs2
        + "\n"
        + prix_opt
        + "\n"
        + text_2
        + "\n"
        + "\\end{flushleft}"
    )
    return section_6
