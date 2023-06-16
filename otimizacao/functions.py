import matplotlib.pyplot as plt
import numpy as np

def plot_function(f, x1_range, x2_range, name):
    x1 = np.linspace(x1_range[0], x1_range[1], 30)
    x2 = np.linspace(x2_range[0], x2_range[1], 30)
    X1, X2 = np.meshgrid(x1, x2)
    Y = f(X1, X2)
    fig = plt.figure(figsize=(10, 10))
    ax = plt.axes(projection='3d')
    ax.contour3D(X1, X2, Y, 50, cmap='coolwarm',alpha=0.5)
    ax = plt.axes(projection='3d')
    ax.plot_surface(X1, X2, Y, rstride=1, cstride=1,
    cmap='winter', edgecolor='none', alpha=0.5)
    ax.set_title(name, fontsize=18)
    ax.set_xlabel('Eixo X1', fontsize=15)
    ax.set_ylabel('Eixo X2', fontsize=15)
    ax.set_zlabel('Eixo Y', fontsize=15)
    ax.view_init(70, 35)
    return ax

def funcao_01(x1, x2):
    return x1 ** 2 + x2 ** 2

def funcao_02(x1, x2):
    termo1 = np.exp(-(x1**2 + x2**2))
    termo2 = 2 * np.exp(-((x1 - 1.7)**2 + (x2 - 1.7)**2))
    resultado = termo1 + termo2
    return resultado

def funcao_03(x1, x2):
    termo1 = -20 * np.exp(-0.2 * np.sqrt(0.5 * (x1**2 + x2**2)))
    termo2 = np.exp(0.5 * (np.cos(2 * np.pi * x1) + np.cos(2 * np.pi * x2))) + 20 + np.exp(1)
    resultado = termo1 - termo2
    return resultado

def funcao_04(x1, x2):
    termo1 = (x1**2 - 10 * np.cos(2 * np.pi * x1) + 10)
    termo2 = (x2**2 - 10 * np.cos(2 * np.pi * x2) + 10)
    resultado = termo1 + termo2
    return resultado

def funcao_05(x1, x2):
    termo1 = (x1 - 1)**2
    termo2 = 100 * (x2 - x1**2)**2
    resultado = termo1 + termo2
    return resultado

def funcao_06(x1, x2):
    termo1 = x1 * np.sin(4 * np.pi * x1)
    termo2 = x2 * np.sin(4 * np.pi * x2 + np.pi)
    resultado = termo1 - termo2 + 1
    return resultado

def funcao_07(x1, x2):
    termo1 = -np.sin(x1) * np.sin((x1**2 / np.pi)**2) * (2 * 10)
    termo2 = -np.sin(x2) * np.sin((2 * x2**2 / np.pi)**2) * (2 * 10)
    resultado = termo1 + termo2
    return resultado

def funcao_08(x1, x2):
    termo1 = -(x2 + 47) * np.sin(np.sqrt(abs(x1/2 + (x2 + 47))))
    termo2 = -x1 * np.sin(np.sqrt(abs(x1 - (x2 + 47))))
    resultado = termo1 - termo2
    return resultado