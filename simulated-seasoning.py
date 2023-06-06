import numpy as np
import matplotlib.pyplot as plt
from functions import *
from random import randrange

def simulated_seasoning(f, x1_range, x2_range, ax, min = False):
    maxit = 1000

    if (x2_range == None):
        x2_range = x1_range

    x_best = np.array([randrange(x1_range[0], x1_range[1]), randrange(x2_range[0], x2_range[1])])
    y_best = f(x_best[0], x_best[1]);

    ax.scatter3D(x_best[0], x_best[1], y_best, color="yellow", s=50, marker="X")

    i = 0
    T = 1000
    while i < maxit:
         
        x_cand = candidato(x_best, x1_range, x2_range, T)
        y_cand = f(x_cand[0], x_cand[1])

        cond = y_best < y_cand
        if (min == True):
            cond = y_best > y_cand
        if cond:
            y_best = y_cand
            x_best = x_cand
            ax.scatter3D(x_best[0], x_best[1], y_best, color="red", s=5, alpha=0.5)
        else:
            Pij = np.exp(-(y_cand - y_best)/T)
            if (Pij >= np.random.uniform(0.0, 1.0)):
                y_best = y_cand
                x_best = x_cand
        i+=1
        T = escalona(T)

    ax.scatter3D(x_best[0], x_best[1], y_best, color="green", s=50, marker="X")
    print(f"X1: {x_best[0]}, X2: {x_best[1]}, Y: {y_best}")


def escalona(T):
    return 0.99 * T

def candidato(x_best, x_range, x2_range, lbda):
    x1 = np.random.uniform(low=x_best[0]-lbda,high=x_best[0]+lbda)
    x2 = np.random.uniform(low=x_best[1]-lbda,high=x_best[1]+lbda)

    if (x1 <= x_range[0]):
        x1 = x_range[0]
    if (x2 <= x2_range[0]):
        x2 = x2_range[0]
    if (x2 >= x2_range[1]):
        x2 = x2_range[1]
    if (x1 >= x_range[1]):
        x1 = x_range[1]


    return [x1, x2]

# Acha o maximo ou minimo local
# Mas nao acha o global
   
ax = plot_function(funcao_01, [-100, 100], [-100, 100], "Simulated Seasoning Funcao 01")
simulated_seasoning(funcao_01, [-100, 100], [-100, 100], ax, min=True)

# ax = plot_function(funcao_02, [-2, 4], [-2, 5], "Simulated Seasoning Funcao 02")
# global_random_search(funcao_02, [-2, 4], [-2, 5], ax, min=False)

# ax = plot_function(funcao_03, [-8, 8], [-8, 8], "Simulated Seasoning Funcao 03")
# global_random_search(funcao_03, [-8, 8], [-8, 8], ax, min=True)

# ax = plot_function(funcao_04, [-5.12, 5.12], [-5.12, 5.12], "Simulated Seasoning Funcao 04")
# global_random_search(funcao_04, [-5.12, 5.12], [-5.12, 5.12], ax, min=True)

# ax = plot_function(funcao_05, [-2, 2], [-1, 3], "Simulated Seasoning Funcao 05")
# global_random_search(funcao_05, [-2, 2], [-1, 3], ax, min=True)

# ax = plot_function(funcao_06, [-1, 3], [-1, 3], "Simulated Seasoning Funcao 06")
# global_random_search(funcao_06, [-1, 3], [-1, 3], ax, min=True)

# ax = plot_function(funcao_07, [0, np.pi], [0, np.pi], "Simulated Seasoning Funcao 07")
# global_random_search(funcao_07, [0, np.pi], [0, np.pi], ax, min=True)

# ax = plot_function(funcao_08, [-200, 20], [-200, 20], "Simulated Seasoning Funcao 08")
# random_search(funcao_08, [-200, 20], ax, min=True)
plt.show()
# plot_function(funcao_01)



