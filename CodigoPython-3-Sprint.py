!pip install pulp

from pulp import *

problema1 = LpProblem('produção',LpMinimize)


x11 = LpVariable('x11', lowBound=0)
x12 = LpVariable('x12', lowBound=0)
x13 = LpVariable('x13', lowBound=0)
x14 = LpVariable('x14', lowBound=0)
x15 = LpVariable('x15', lowBound=0)
x16 = LpVariable('x16', lowBound=0)
x17 = LpVariable('x17', lowBound=0)
x18 = LpVariable('x18', lowBound=0)
x19 = LpVariable('x19', lowBound=0)
x110 = LpVariable('x110', lowBound=0)
x111 = LpVariable('x111', lowBound=0)
x112 = LpVariable('x112', lowBound=0)
x113 = LpVariable('x113', lowBound=0)
x114 = LpVariable('x114', lowBound=0)
x115 = LpVariable('x115', lowBound=0)
x116 = LpVariable('x116', lowBound=0)
x117 = LpVariable('x117', lowBound=0)
x118 = LpVariable('x118', lowBound=0)
x119 = LpVariable('x119', lowBound=0)
x120 = LpVariable('x120', lowBound=0)
x121 = LpVariable('x121', lowBound=0)
x122 = LpVariable('x122', lowBound=0)
x123 = LpVariable('x123', lowBound=0)
x124 = LpVariable('x124', lowBound=0)
x125 = LpVariable('x125', lowBound=0)
x126 = LpVariable('x126', lowBound=0)
x127 = LpVariable('x127', lowBound=0)
x128 = LpVariable('x128', lowBound=0)
x129 = LpVariable('x129', lowBound=0)
x130 = LpVariable('x130', lowBound=0)
x131 = LpVariable('x131', lowBound=0)
x132 = LpVariable('x132', lowBound=0)
x133 = LpVariable('x133', lowBound=0)
x134 = LpVariable('x134', lowBound=0)
x135 = LpVariable('x135', lowBound=0)
x139 = LpVariable('x139', lowBound=0)
x140 = LpVariable('x140', lowBound=0)
x141 = LpVariable('x141', lowBound=0)
x142 = LpVariable('x142', lowBound=0)
x143 = LpVariable('x143', lowBound=0)
x144 = LpVariable('x144', lowBound=0)
x145 = LpVariable('x145', lowBound=0)
x146 = LpVariable('x146', lowBound=0)
x147 = LpVariable('x147', lowBound=0)
x148 = LpVariable('x148', lowBound=0)
x149 = LpVariable('x149', lowBound=0)
x150 = LpVariable ('x150', lowBound=0)
x151 = LpVariable('x151', lowBound=0)
x21 = LpVariable('x21', lowBound=0)
x22 = LpVariable('x22', lowBound=0)
x23 = LpVariable('x23', lowBound=0)
x24 = LpVariable('x24', lowBound=0)
x25 = LpVariable('×25', lowBound=0)
x26 = LpVariable('x26', lowBound=0)
x27 = LpVariable('x27', lowBound=0)
x28 = LpVariable('x28', lowBound=0)
x29 = LpVariable('×29', lowBound=0)
x210 = LpVariable ('x210', lowBound=0)
x211 = LpVariable('x211', lowBound=0)
x219 = LpVariable('x219', lowBound=0)
x220 = LpVariable('x220', lowBound=0)
x221 = LpVariable('x221', lowBound=0)
x222 = LpVariable('x222', lowBound=0)
x223 = LpVariable('x223', lowBound=0)
x224 = LpVariable('x224', lowBound=0)
x225 = LpVariable('x225', lowBound=0)
x226 = LpVariable('x226', lowBound=0)
x227 = LpVariable('x227', lowBound=0)
x228 = LpVariable('x228', lowBound=0)
x229 = LpVariable('x229', lowBound=0)
x230 = LpVariable('x230', lowBound=0)
x231 = LpVariable('x231', lowBound=0)
x232 = LpVariable('x232', lowBound=0)
x233 = LpVariable('x233', lowBound=0)
x234 = LpVariable('x234', lowBound=0)
x235 = LpVariable('x235', lowBound=0)
x236 = LpVariable('x236', lowBound=0)
x237 = LpVariable('x237', lowBound=0)
x238 = LpVariable('x238', lowBound=0)
x244 = LpVariable('x244', lowBound=0)
x245 = LpVariable('x245', lowBound=0)
x246 = LpVariable('x246', lowBound=0)
x247 = LpVariable('x247', lowBound=0)
x248 = LpVariable('x248', lowBound=0)
x249 = LpVariable('x249', lowBound=0)
x250 = LpVariable('x250', lowBound=0)
x251 = LpVariable('x251', lowBound=0)
x35 = LpVariable('x35', lowBound=0)
x38 = LpVariable('x38', lowBound=0)
x39 = LpVariable('x39', lowBound=0)
x310 = LpVariable('x310', lowBound=0)
x311 = LpVariable('x311', lowBound=0)
x324 = LpVariable('x324', lowBound=0)
x325 = LpVariable('x325', lowBound=0)
x326 = LpVariable('x326', lowBound=0)
x327 = LpVariable('x327', lowBound=0)
x328 = LpVariable('x328', lowBound=0)
x329 = LpVariable('x329', lowBound=0)
x330 = LpVariable('x330', lowBound=0)
x331 = LpVariable('x331', lowBound=0)
x332 = LpVariable('x332', lowBound=0)
x333 = LpVariable('x333', lowBound=0)
x334 = LpVariable('x334', lowBound=0)
x335 = LpVariable('x335', lowBound=0)
x336 = LpVariable('x336', lowBound=0)
x337 = LpVariable('x337', lowBound=0)
x338 = LpVariable('x338', lowBound=0)
x339 = LpVariable('x339', lowBound=0)
x340 = LpVariable('x340', lowBound=0)
x341 = LpVariable('x341', lowBound=0)
x342 = LpVariable('x342', lowBound=0)
x343 = LpVariable('x343', lowBound=0)
x347 = LpVariable('x347', lowBound=0)
x348 = LpVariable('x348', lowBound=0)
x349 = LpVariable('x349', lowBound=0)
x350 = LpVariable('x350', lowBound=0)
x351 = LpVariable('x351', lowBound=0)


problema1 += 0.61*x11 + 0.56*x12 + 0.48*x13 + 0.52*x14 + 0.55*x15 + 0.60*x16 + 0.58*x17 + 0.60*x18 + 0.48*x19 + 0.76*x110 + 0.42*x111 + 0.84*x112 + 0.82*x113 + 0.76*x114 + 0.89*x115 + 0.89*x116 + 0.89*x117 + 0.89*x118 + 0.75*x119 + 0.78*x120 + 0.82*x121 + 0.74*x122 + 0.80*x123 + 0.76*x124 + 0.68*x125 + 0.75*x126 + 0.77*x127 + 0.77*x128 + 0.81*x129 + 0.81*x130 + 0.75*x131 + 0.74*x132 + 0.72*x133 + 0.74*x134 + 0.74*x135 + 0.92*x139 + 1.02*x140 + 0.97*x141 + 0.96*x142 + 1.04*x143 + 0.68*x144 + 0.69*x145 + 0.69*x146 + 0.33*x147 + 0.33*x148 + 0.35*x149 + 0.41*x150 + 0.46*x151 + 0.47*x21 + 0.43*x22 + 0.42*x23 + 0.45*x24 + 0.45*x25 + 0.42*x26 + 0.48*x27 + 0.42*x28 + 0.53*x29 + 0.33*x210 + 0.61*x211 + 0.34*x219 + 0.33*x220 + 0.33*x221 + 0.34*x222 + 0.30*x223 + 0.34*x224 + 0.32*x225 + 0.33*x226 + 0.26*x227 + 0.36*x228 + 0.32*x229 + 0.34*x230 + 0.33*x231 + 0.32*x232 + 0.32*x233 + 0.34*x234 + 0.34*x235 + 0.77*x236 + 0.75*x237 + 0.75*x238 + 0.53*x244 + 0.54*x245 + 0.52*x246 + 0.95*x247 + 1.01*x248 + 1.10*x249 + 1.07*x250 + 1.14*x251 + 0.31*x35 + 0.31*x38 + 0.32*x39 + 0.34*x310 + 0.31*x311 + 0.33*x324 + 0.3*x325 + 0.34*x326 + 0.33*x327 + 0.36*x328 + 0.37*x329 + 0.48*x330 + 0.34*x331 + 0.39*x332 + 0.65*x333 + 0.32*x334 + 0.32*x335 + 0.53*x336 + 0.51*x337 + 0.51*x338 + 0.6*x339 + 0.66*x340 + 0.63*x341 + 0.62*x342 + 0.66*x343 + 0.73*x347 + 0.77*x348 + 0.66*x349 + 0.73*x350 + 0.68*x351



problema1 += x11 + x12 + x13 + x14 + x15 + x16 + x17 + x18 + x19 + x110 + x111 + x112 + x113 + x114 + x115 + x116 + x117 + x118 + x119 + x120 + x121 + x122 + x123 + x124 + x125 + x126 + x127 + x128 + x129 + x130 + x131 + x132 + x133 + x134 + x135 + x139 + x140 + x141 + x142 + x143 + x144 + x145 + x146 + x147 + x148 + x149 + x150 + x151 <= 90000000
problema1 += x21 + x22 + x23 + x24 + x25 + x26 + x27 + x28 + x29 + x210 + x211 + x219 + x220 + x221 + x222 + x223 + x224 + x225 + x226 + x227 + x228 + x229 + x230 + x231 + x232 + x233 + x234 + x235 + x236 + x237 + x238 + x244 + x245 + x246 + x247 + x248 + x249 + x250 + x251 <= 90000000
problema1 += x35 + x38 + x39 + x310 + x311 + x324 + x325 + x326 + x326 + x327 + x328 + x329 + x330 + x331 + x332 + x333 + x334 + x335 + x336 + x337 + x338 + x339 + x340 + x341 + x342 + x343 + x344 + x347 + x348 + x349 + x350 + x351 <= 56000000

problema1 += x11 + x21 == 5973721
problema1 += x12 + x22 == 1778080
problema1 += x13 + x23 == 5958798
problema1 += x14 + x24 == 896173
problema1 += x15 + x25 + x35 == 3241494
problema1 += x16 + x26 == 3244827
problema1 += x17 + x27 == 12738726
problema1 += x18 + x28 + x38 == 6792503
problema1 += x19 + x29 + x39 == 7471374
problema1 += x110 + x210 + x310 == 2098730
problema1 += x111 + x211 + x311 == 7295028
problema1 += x112 == 1350774
problema1 += x113 == 1439856
problema1 += x114 == 3977784
problema1 += x115 == 3666906
problema1 += x116 == 271034
problema1 += x117 == 1272373
problema1 += x118 == 569236
problema1 += x119 + x219 == 1589336
problema1 += x120 + x220 == 5063433
problema1 += x121 + x221 == 10686204
problema1 += x122 + x222 == 2495205
problema1 += x123 + x223 == 1753764
problema1 += x124 + x224 + x324 == 20427048
problema1 += x125 + x225 + x325 == 7828763
problema1 += x126 + x226 + x326 == 5788209
problema1 += x127 + x227 + x327 == 11836544
problema1 += x128 + x228 + x328 == 6145143
problema1 += x129 + x229 + x329 == 13860432
problema1 += x130 + x230 + x330 == 3482379
problema1 += x131 + x231 + x331 == 4084642
problema1 += x132 + x232 + x332 == 10839219
problema1 += x133 + x233 + x333 == 1336988
problema1 += x134 + x234 + x334 == 1898750
problema1 += x135 + x235 + x335 == 14197671
problema1 += x236 + x336 == 1716192
problema1 += x237 + x337 == 827342
problema1 += x238 + x338 == 2539443
problema1 += x139 + x339 == 1789064
problema1 += x140 + x340 == 973767
problema1 += x141 + x341 == 5304924
problema1 += x142 + x342 == 838856
problema1 += x143 + x343 == 8150094
problema1 += x144 + x244 == 678417
problema1 += x145 + x245 == 3600095
problema1 += x146 + x246 == 3522678
problema1 += x147 + x247 + x347 == 3675315
problema1 += x148 + x248 + x348 == 1310374
problema1 += x149 + x249 + x349 == 1761137
problema1 += x150 + x250 + x350 == 4402893
problema1 += x151 + x251 + x251 == 1331761

problema1

problema1.solve()

for v in problema1.variables():
  print(v.name,"=",v.varValue)
