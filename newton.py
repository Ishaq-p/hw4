import math
Digits = 7



f = lambda x: x ** 3 - x ** 2 + 7*x - 6   # function whose root we're approximating
g = lambda x: x - f(x) / (3*x ** 2 - 2* x  + 7)  # the iteration function, g(x) = x - f(x) / f'(x)


p0 = 1.632653
epsilon = 10**(-7)
RE = 1

n = 1
while RE >= epsilon:
    p = g(p0)
    RE = abs((p - p0) / p)
    print(n,"\t||\t",round(p0,7),"\t||\t", round(p,7),"\t||\t", RE)
    p0 = p
    n += 1

print('Approximation of the fixed point is', p)

