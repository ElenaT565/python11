from sympy.plotting import plot
from sympy import Symbol, solve, diff, solveset, S, pprint, sin, cos
# import matplotlib.pyplot as plt

x = Symbol('x')
f = sin(x)**2 - cos(x)**2
plot(f)

# px = [i for i in range(-10, 10)]
# fx = lambda x: 5*x**2 + 10*x - 30
# py = list(map(fx, range(-10, 10)))
# plt.plot(px, py, 'r')
# plt.show()

print(solve(f,x))

pprint(solve(f > 0,x))
pprint(solve(f < 0,x))

diff_f = diff(f,x)
print(diff_f)
print(solve(diff_f))
pprint(solveset(diff_f > 0, x))
print(solve(diff_f < 0, x))