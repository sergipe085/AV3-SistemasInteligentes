import numpy as np
import matplotlib.pyplot as plt
from functions import *

def hill_climbing(f, x1_range, x2_range, ax, min = False):
    x1 = x1_range[0]
    x2 = x2_range[0]
    x1_best = x1
    x2_best = x2
    y_best = f(x1_best, x2_best)
    e = 0.1
    maxit = 10000
    maxn = 100

    ax.scatter3D(x1_best, x2_best, y_best, color="yellow", s=50, marker="X")

    i = 0
    melhoria = True
    while i < maxit and melhoria:
        j = 0;
        while j < maxn:

            cand1 = candidato(x1_best)
            while cand1 < x1_range[0] or cand1 > x1_range[1]:
                cand1 = candidato(x1_best)

            cand2 = candidato(x2_best)
            while cand2 < x2_range[0] or cand2 > x2_range[1]:
                cand2 = candidato(x2_best)

            melhoria = False
            y = f(cand1, cand2)
            cond = y > y_best
            if (min):
                cond = y < y_best
            if cond:
                x1_best = cand1
                x2_best = cand2
                y_best = y
                melhoria = True
                ax.scatter3D(x1_best, x2_best, y_best, color="red")
                break
            j+=1
        i+=1

    ax.scatter3D(x1_best, x2_best, y_best, color="green", s=50, marker="X")
    print(f"X1: {x1_best}, X2: {x2_best}, Y: {y_best}")



def candidato(x):
    E = 0.1
    return np.random.uniform(low=x-E,high=x+E)

# Acha o maximo ou minimo local
# Mas nao acha o global
   
# ax = plot_function(funcao_01, [-100, 100], [-100, 100], "Hill Climbing Funcao 01")
# hill_climbing(funcao_01, [-100, 100], [-100, 100], ax, min=True)

ax = plot_function(funcao_02, [-2, 4], [-2, 5], "Hill Climbing Funcao 02")
hill_climbing(funcao_02, [-2, 4], [-2, 5], ax, min=False)

# ax = plot_function(funcao_03, [-8, 8], [-8, 8], "Hill Climbing Funcao 03")
# hill_climbing(funcao_03, [-8, 8], [-8, 8], ax, min=True)

# ax = plot_function(funcao_04, [-5.12, 5.12], [-5.12, 5.12], "Hill Climbing Funcao 04")
# hill_climbing(funcao_04, [-5.12, 5.12], [-5.12, 5.12], ax, min=True)

# ax = plot_function(funcao_05, [-2, 2], [-1, 3], "Hill Climbing Funcao 05")
# hill_climbing(funcao_05, [-2, 2], [-1, 3], ax, min=True)

# ax = plot_function(funcao_06, [-1, 3], [-1, 3], "Hill Climbing Funcao 06")
# hill_climbing(funcao_06, [-1, 3], [-1, 3], ax, min=False)

# ax = plot_function(funcao_07, [0, np.pi], [0, np.pi], "Hill Climbing Funcao 07")
# hill_climbing(funcao_07, [0, np.pi], [0, np.pi], ax, min=True)

ax = plot_function(funcao_08, [-200, 20], [-200, 20], "Hill Climbing Funcao 08")
hill_climbing(funcao_08, [-200, 20], [-200, 20], ax, min=True)
plt.show()
# plot_function(funcao_01)



