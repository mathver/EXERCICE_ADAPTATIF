"""
Module de résolution permettant de trouver la solution optimale au programme du producteur.
"""

import sympy as sp
from .class_define import Profit
from sympy import Rational


def cn1_prof2(obj: Profit, var):
    """The function `cn1_prof2` takes in an object of the class `Profit` and a variable, and returns the
    first derivative of the profit function with respect to the variable.

    Parameters
    ----------
    obj : Profit
        Profit
    var
        the variable that we want to differentiate with respect to

    Returns
    -------
        The derivative of the profit function with respect to the variable.

    """
    prof = obj.profit_2()
    return sp.diff(prof, var)


def cs2_prof2(obj: Profit, var):
    """The function `cs2_prof2` takes in an object of the class `Profit` and a variable, and returns the
    second derivative of the profit function with respect to the variable.

    Parameters
    ----------
    obj : Profit
        Profit
    var
        the variable that we are differentiating with respect to.

    Returns
    -------
        The derivative of the constraint with respect to the variable.

    """
    cn = cn1_prof2(obj, var)
    return sp.diff(cn, var)


def resolution_2(obj: Profit, var):
    """The function `resolution_2` takes in an object of the class `Profit` and a variable, and returns
    the solution to the constraint `cn1_prof2` with respect to the variable

    Parameters
    ----------
    obj : Profit
        Profit
    var
        the variable to solve for

    Returns
    -------
        The solution of the equation.

    """
    return sp.solve(cn1_prof2(obj, var), var)[0]


def substitute_q2(obj: Profit, var):
    """It takes in an object of the class Profit and a variable, and returns the quantity of the
    good produced, after substituting the variable with its solution

    Parameters
    ----------
    obj : Profit
        Profit
    var
        the variable to be solved for

    Returns
    -------
        The quantity of the second good.

    """
    sol = resolution_2(obj, var)
    quant = obj.quantity_2()
    return quant.subs(var, sol)


def profit_equilibre(obj: Profit, var):
    """It takes a Profit object and a variable, and returns the profit function with the variable replaced
    by the solution to the equation that the variable is equal to

    Parameters
    ----------
    obj : Profit
        Profit
    var
        the variable to be solved for

    Returns
    -------
        The profit function is being returned.

    """
    profit = obj.profit_2()
    return sp.simplify(profit.subs(var, resolution_2(obj, var)))


def resol_prof2_H(obj: Profit, var, h: int = 4, gh: Rational = Rational(1, 4)):
    """It solves the equilibrium of the game for a given value of quality and gamma ofgr high quality.

    Parameters
    ----------
    obj : Profit
        Profit
    var
        the variable to be solved for
    h : int, optional
        The value of high quality
    gh : Rational
        The value of gamma for high quality

    Returns
    -------
        The equilibrium price and quantity for a given level of h and gh.

    """
    sol = profit_equilibre(obj, var)
    return sp.simplify(sol.subs([(obj.s_2, h), (obj.gamma, gh)]))


def resol_prof2_L(obj: Profit, var, l: int = 2, gl: Rational = Rational(1, 2)):
    """It solves the equilibrium of the game for a given value of quality and gamma for low quality.

    Parameters
    ----------
    obj : Profit
        Profit
    var
        the variable to be solved for
    l :
        The value of low quality
    gl : Rational
        The value of gamma for low quality

    Returns
    -------
        The equilibrium price and quantity for a given level of l and gl.

    """
    sol = profit_equilibre(obj, var)
    return sp.simplify(sol.subs([(obj.s_2, l), (obj.gamma, gl)]))


def resol_prof2subq_LL(obj: Profit, var, l: int = 2, gl: Rational = Rational(1, 2)):
    """Return the solution of the profit for low quality cas with the price as variable.

    Parameters
    ----------
    obj : Profit
        Profit
    var
        the variable to solve for
    l :
        The value of low quality
    gl : Rational
        The value of gamma for low quality

    Returns
    -------
        The profit function for low quality firm.

    """
    sol = profit_equilibre(obj, var)
    return sp.simplify(
        sol.subs(
            [
                (obj.s_2, l),
                (obj.gamma, gl),
                (obj.q_1_NDV, obj.quantity_1()),
                (obj.s_1, l),
            ]
        )
    )


def resol_prof2subq_HH(obj: Profit, var, h: int = 4, gh: Rational = Rational(1, 4)):
    """Return the solution of the profit for high quality cas with the price as variable

    Parameters
    ----------
    obj : Profit
        Profit
    var
        the variable to be solved for
    h : int, optional
        The value of high quality
    gh : Rational
        The value of gamma for high quality

    Returns
    -------
        The profit function for high quality firm.

    """
    sol = profit_equilibre(obj, var)
    return sp.simplify(
        sol.subs(
            [
                (obj.s_2, h),
                (obj.gamma, gh),
                (obj.q_1_NDV, obj.quantity_1()),
                (obj.s_1, h),
            ]
        )
    )


def resol_prof2subq_LH(
    obj: Profit, var, h: int = 4, l: int = 2, gh: Rational = Rational(1, 4)
):
    """It takes a profit object, a variable, and some parameters, and returns the value of the profit in
    the profit equilibrium for low in 1st and high in 2nd period.

    Parameters
    ----------
    obj : Profit
        Profit
    var
        the variable to be solved for
    h : int, optional
        The value of high quality
    l : int, optionnal
        The value of low quality
    gh : Rational
        The value of gamma for high quality

    Returns
    -------
        The equilibrium profit for LH firm.

    """
    sol = profit_equilibre(obj, var)
    return sp.simplify(
        sol.subs(
            [
                (obj.s_2, h),
                (obj.gamma, gh),
                (obj.q_1_NDV, obj.quantity_1()),
                (obj.s_1, l),
            ]
        )
    )


def resol_prof2subq_HL(
    obj: Profit, var, h: int = 4, l: int = 2, gh: Rational = Rational(1, 2)
):
    """It takes a profit object, a variable, and some parameters, and returns the value of the profit in
    the profit equilibrium for high in 1st and low in 2nd period.

    Parameters
    ----------
    obj : Profit
        Profit
    var
        the variable to be solved for
    h : int, optional
        The value of high quality
    l : int, optionnal
        The value of low quality
    gh : Rational
        The value of gamma for high quality

    Returns
    -------
        The equilibrium profit for HL firm.

    """
    sol = profit_equilibre(obj, var)
    return sp.simplify(
        sol.subs(
            [
                (obj.s_2, l),
                (obj.gamma, gh),
                (obj.q_1_NDV, obj.quantity_1()),
                (obj.s_1, l),
            ]
        )
    )


def resol_prof1_H(obj: Profit, h: int = 4):
    """It takes a Profit object and an integer, and returns the high firm profit function for the 1st period.

    Parameters
    ----------
    obj : Profit
        Profit
    h : int, optional
        The value of high quality

    Returns
    -------
        Profit for high firm in 1st period.

    """
    fct = obj.profit_1()
    return fct.subs(obj.s_1, h)


def resol_prof1_L(obj: Profit, l: int = 2):
    """It takes a Profit object and an integer, and returns the low firm profit function for the 1st period.

    Parameters
    ----------
    obj : Profit
        Profit
    l : int, optional
        The value of low quality

    Returns
    -------
        Profit for low firm in 1st period.

    """
    fct = obj.profit_1()
    return fct.subs(obj.s_1, l)


def resol_prof_HH(obj: Profit, var, h: int = 4, gh: Rational = Rational(1, 4)):
    """It computes the profit function for a firm of high quality in both periods.

    Parameters
    ----------
    obj : Profit
        Profit
    var
        the variable to be maximized
    h : int, optional
        The value of high quality
    gh : Rational
        The value of gamma for high quality

    Returns
    -------
        The profit function of HH firm.

    """
    prof1 = resol_prof1_H(obj, h)
    prof2 = resol_prof2_H(obj, var, h, gh)
    prof2_DV = prof2.subs(obj.q_1_NDV, obj.quantity_1())
    prof2_FIN = prof2_DV.subs(obj.s_1, h)
    return sp.decompose(prof1 + prof2_FIN)[0]


def resol_prof_LL(obj: Profit, var, l: int = 2, gl: Rational = Rational(1, 2)):
    """It computes the profit function for a firm of low quality in both periods.

    Parameters
    ----------
    obj : Profit
        Profit
    var
        the variable to be maximized
    l : int, optional
        The value of low quality
    gl : Rational
        The value of gamma for low quality

    Returns
    -------
        The profit function of LL firm.
    """
    prof1 = resol_prof1_L(obj, l)
    prof2 = resol_prof2_L(obj, var, l, gl)
    prof2_DV = prof2.subs(obj.q_1_NDV, obj.quantity_1())
    prof2_FIN = prof2_DV.subs(obj.s_1, l)
    return sp.simplify(prof1 + prof2_FIN)


def resol_prof_HL(
    obj: Profit, var, h: int = 4, l: int = 2, gl: Rational = Rational(1, 2)
):
    """It computes the profit function for a firm which is high quality in 1st period and low on the 2nd.

    Parameters
    ----------
    obj : Profit
        Profit
    var
        the variable to be maximized
    h : int, optional
        The value of high quality
    l : int, optional
        The value of low quality
    gl : Rational
        The value of gamma for low quality

    Returns
    -------
        The profit function of HL firm..
    """
    prof1 = resol_prof1_H(obj, h)
    prof2 = resol_prof2_L(obj, var, l, gl)
    prof2_DV = prof2.subs(obj.q_1_NDV, obj.quantity_1())
    prof2_FIN = prof2_DV.subs(obj.s_1, h)
    return sp.simplify(prof1 + prof2_FIN)


def resol_prof_LH(
    obj: Profit, var, h: int = 4, l: int = 2, gh: Rational = Rational(1, 4)
):
    """It computes the profit function for a firm which is low quality in 1st period and high on the 2nd.

    Parameters
    ----------
    obj : Profit
        Profit
    var
        the variable to be maximized
    h : int, optional
        The value of high quality
    l : int, optional
        The value of low quality
    gh : Rational
        The value of gamma for high quality

    Returns
    -------
        The profit function of LH firm.

    """
    prof1 = resol_prof1_L(obj, l)
    prof2 = resol_prof2_H(obj, var, h, gh)
    prof2_DV = prof2.subs(obj.q_1_NDV, obj.quantity_1())
    prof2_FIN = prof2_DV.subs(obj.s_1, l)
    return sp.simplify(prof1 + prof2_FIN)


def cn1_profLL(obj: Profit):
    """It solves the CN1 in the case of LL firm profit.

    Parameters
    ----------
    obj : Profit
        Profit

    Returns
    -------
        The derivative of the profit function with respect to p_1.

    """
    prof_LL = resol_prof_LL(obj, obj.p_2)
    return sp.diff(prof_LL, obj.p_1)


def cs2_profLL(obj: Profit):
    """It solves the CS2 in the case of LL firm profit.

    Parameters
    ----------
    obj : Profit
        Profit

    Returns
    -------
        The second derivative of the profit function with respect to p_1.

    """
    cn = cn1_profLL(obj)
    return sp.diff(cn, obj.p_1)


def prix_equilibre_LL(obj: Profit):
    """It solves the equilibrium price for a LL firm.

    Parameters
    ----------
    obj : Profit
        Profit

    Returns
    -------
        The value of the equilibrium price.

    """
    cn = cn1_profLL(obj)
    return sp.solve(cn, obj.p_1)[0]


def profit_equilibre_LL(obj: Profit):
    """It solves the equilibrium profit for a LL firm.

    Parameters
    ----------
    obj : Profit
        Profit

    Returns
    -------
        The value of the equilibrium profit.

    """
    prof_LL = resol_prof_LL(obj, obj.p_2)
    px = prix_equilibre_LL(obj)
    return prof_LL.subs(obj.p_1, px)


def prof_HL_A(obj: Profit, var, h: int = 4, l: int = 2, gl: Rational = Rational(1, 2)):
    """It solves the form of the profit of HL firm with advertising A.

    Parameters
    ----------
    obj : Profit
        Profit

    Returns
    -------
        The form of the profit function.

    """
    prof_A = resol_prof_HL(obj, var, h, l, gl) - obj.A
    return prof_A


def form_A(obj: Profit, var, h: int = 4, l: int = 2, gl: Rational = Rational(1, 2)):
    """It solves the form of the advertising funtion.

    Parameters
    ----------
    obj : Profit
        Profit
    var
        the variable to be maximized
    h : int, optional
        The value of high quality
    l : int, optional
        The value of low quality
    gl : Rational
        The value of gamma for low quality

    Returns
    -------
        The value of the equilibrium price.

    """
    A = sp.solve(profit_equilibre_LL(obj) > prof_HL_A(obj, var, h, l, gl), obj.A).rhs
    return A


def val_A(obj: Profit, var, h: int = 4, l: int = 2, gl: Rational = Rational(1, 2)):
    """It solves the polynomial form of avertising function.

    Parameters
    ----------
    obj : Profit
        Profit
    var
        the variable to be maximized
    h : int, optional
        The value of high quality
    l : int, optional
        The value of low quality
    gl : Rational
        The value of gamma for low quality

    Returns
    -------
        The value of the roots of the polynomial form of advertising function.

    """
    roots = form_A(obj, var, h, l, gl)
    a, b = sp.solve(roots)
    return a, b


def opt_A(
    obj: Profit,
    var,
    h: int = 4,
    l: int = 2,
    gh: Rational = Rational(1, 4),
    gl: Rational = Rational(1, 2),
):
    """It solves the optimal value of advertising for the firm.

    Parameters
    ----------
    obj : Profit
        Profit
    var
        the variable to be maximized
    h : int, optional
        The value of high quality
    l : int, optional
        The value of low quality
    gl : Rational
        The value of gamma for low quality

    Returns
    -------
        The optimal value of advertising.
    """
    return sp.solve(
        sp.diff(resol_prof_HH(obj, var, h, gh) - form_A(obj, var, h, l, gl), obj.p_1),
        obj.p_1,
    )[0]


def graph_A(obj: Profit, var, h: int = 4, l: int = 2, gl: Rational = Rational(1, 2)):
    """It plots the graph of the function of advertising.

    Parameters
    ----------
    obj : Profit
        Profit
    var
        the variable to be maximized
    h : int, optional
        The value of high quality
    l : int, optional
        The value of low quality
    gl : Rational
        The value of gamma for low quality
    """
    graph = sp.plot(
        form_A(obj, var, h, l, gl),
        xlim=(0, h + 2),
        ylim=(0, h + 2),
        ylabel="$A(p_1)$",
        show=False,
    )
    graph.save("./graph.png")
