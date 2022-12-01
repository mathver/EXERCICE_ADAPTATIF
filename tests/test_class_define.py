"""Description.

Tests automatiques associés à la librairie class_define.

"""
import pytest
import sympy as sp
from adap_exercice.class_define import Profit

def test_quantity_1():
    quantity = Profit().quantity_1()
    qualite_1 = sp.symbols("s_1")
    prix_1 = sp.symbols("p_1")
    attendu = qualite_1 - prix_1
    assert quantity == attendu

def test_quantity_2():
    quantity = Profit().quantity_2()
    qualite_2 = sp.symbols("s_2")
    prix_2 = sp.symbols("p_2")
    attendu = qualite_2 - prix_2
    assert quantity == attendu
    
def test_cost_2_NDV():
    cost_2_NDV = Profit().cost_2_NDV() 
    gamma = sp.symbols("gamma") 
    quantite_1 = sp.symbols("q_1")
    attendu = 1 - gamma*quantite_1
    assert cost_2_NDV == attendu

def test_cost_2():
    cost_2 = Profit().cost_2()
    gamma = sp.symbols("gamma") 
    qualite_1 = sp.symbols("s_1")
    prix_1 = sp.symbols("p_1")
    attendu = 1 - gamma*(qualite_1 - prix_1)
    assert cost_2 == attendu

def test_profit_1():
    profit = Profit().profit_1()
    qualite_1 = sp.symbols("s_1")
    prix_1 = sp.symbols("p_1")
    attendu = (qualite_1 - prix_1)*(prix_1 - 1)
    assert profit == attendu

def test_profit_1_NDV():
    profit = Profit().profit_1_NDV()
    quantite_1 = sp.symbols("q_1")
    prix_1 = sp.symbols("p_1")
    attendu = (quantite_1)*(prix_1 - 1)
    assert profit == attendu

def test_profit_2():
    profit = Profit().profit_2()
    quantite_1 = sp.symbols("q_1")
    qualite_2 = sp.symbols("s_2")
    prix_2 = sp.symbols("p_2")
    gamma = sp.symbols("gamma")
    attendu = (qualite_2 - prix_2)*(prix_2 - (1- gamma*quantite_1))
    assert profit == attendu

def test_profit_2_NDV():
    profit = Profit().profit_2_NDV()
    quantite_1 = sp.symbols("q_1")
    quantite_2 = sp.symbols("q_2")
    prix_2 = sp.symbols("p_2")
    gamma = sp.symbols("gamma")
    attendu = quantite_2*(prix_2 - (1- gamma*quantite_1))
    assert profit == attendu

def test_profit_2_FULL():
    profit = Profit().profit_2_FULL()
    quantite_2 = sp.symbols("q_2")
    prix_2 = sp.symbols("p_2")
    gamma = sp.symbols("gamma")
    qualite_1 = sp.symbols("s_1")
    prix_1 = sp.symbols("p_1")
    qualite_2 = sp.symbols("s_2")
    attendu = attendu = (qualite_2 - prix_2)*(prix_2 - (1- gamma*(qualite_1-prix_1)))
    assert profit == attendu