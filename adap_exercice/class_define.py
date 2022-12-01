

from dataclasses import dataclass
import sympy as sp

@dataclass
class Profit : 
    p_1 : sp.core = sp.symbols("p_1")
    p_2 : sp.core = sp.symbols("p_2")
    s_1 : sp.core = sp.symbols("s_1")
    s_2 : sp.core = sp.symbols("s_2")
    q_1_NDV : sp.core = sp.symbols("q_1")
    q_2_NDV : sp.core = sp.symbols("q_2")
    gamma : sp.core = sp.symbols("gamma")
    A : sp.core = sp.symbols("A")
    c_1 : int = 1
    
    def quantity_1(self):
        return self.s_1 - self.p_1

    def quantity_2(self):
        return self.s_2 - self.p_2

    def cost_2_NDV(self) -> sp.core: 
        return 1 - self.gamma * self.q_1_NDV

    def cost_2(self) -> sp.core: 
        return 1 - self.gamma * self.quantity_1()
        
    def profit_1(self) -> sp.core:
        return  self.quantity_1()*(self.p_1 - self.c_1)

    def profit_1_NDV(self) -> sp.core:
        return self.q_1_NDV*(self.p_1 - self.c_1)

    def profit_2(self):
        return self.quantity_2()*(self.p_2 - self.cost_2_NDV())

    def profit_2_NDV(self) -> sp.core:
        return self.q_2_NDV*(self.p_2 - self.cost_2_NDV())

    def profit_2_FULL(self):
        return self.quantity_2()*(self.p_2 - self.cost_2())
