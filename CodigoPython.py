´´´!pip install pulp
from pulp import *

Problema1 = LpProblem('Produção',LpMinimize)
x11 = LpVariable('x11', lowBound = 0)
x12 = LpVariable('x12', lowBound = 0)
x13 = LpVariable('x13', lowBound = 0)
x14 = LpVariable('x14', lowBound = 0)
x15 = LpVariable('x15', lowBound = 0)
x21 = LpVariable('x21', lowBound = 0)
x22 = LpVariable('x22', lowBound = 0)
x23 = LpVariable('x23', lowBound = 0)
x24 = LpVariable('x24', lowBound = 0)
x25 = LpVariable('x25', lowBound = 0)
x35 = LpVariable('x35', lowBound = 0)

Problema1 += 0.56*x11+0.46*x12+0.42*x13+0.44*x14+0.47*x15+0.4*x21+0.36*x22+0.36*x23+0.38*x24+0.38*x25+0.26*x35

Problema1 += x11 + x12 + x13 + x14 + x15 == 2635200
Problema1 += x21 + x22 + x23 + x24 + x25 == 10311000
Problema1 += x35 == 1116900

Problema1

problema1.solve()
for v in problema1.variables(): print (v.name, "=", v.varValue)
print('resultado do custo minimo =', value(problema1.objective))´´´
