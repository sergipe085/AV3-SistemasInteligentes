from random import randrange
import numpy as np
from time import time

queens = [0, 0, 0, 0, 0, 0, 0, 0]
t = 0
n = 100
probabilidade_mutacao = 0.05
probabilidade_de_recombinacao = 0.85;
taxa_mutacao          = 0.2

def h(x):
    m = [None]*8
    for i in range(8):
        m[i] = [None] * 8


    for i in range(len(m)):
        for j in range(len(m[i])):
            if (x[i] > 7):
                x[i] = 7
            if (x[i] < 0):
                x[i] = 0

            if (j == x[i]):
                m[j][i] = 1
            else:
                m[j][i] = 0

    pares_que_se_atacam = 0

    # Verificar mesma linha
    for i in range(len(m)):
        quant = 0
        for j in range(len(m[i])):
            if (m[i][j] == 1):
                quant += 1
        if (quant >= 2):
            pares_que_se_atacam += quant - 1

    # Verificar mesma disgonal
    for i in range(len(m)):
        quant = 0
        for j in range(i + 1):
            _i = i - j
            _j = j
            if (m[_i][_j] == 1):
                quant += 1
        if (quant >= 2):
            pares_que_se_atacam += quant - 1

    for i in range(len(m) - 1):
        quant = 0
        for j in range(i + 1):
            _i = 7 -(i - j)
            _j = 7 - j
            if(m[_i][_j] == 1):
                quant += 1
        if (quant >= 2):
            pares_que_se_atacam += quant - 1 

    for i in range(len(m)):
        quant = 0
        for j in range(i + 1):
            _i = j
            _j = 7 - (i-j)
            if (m[_i][_j] == 1):
                quant += 1
        if (quant >= 2):
            pares_que_se_atacam += quant - 1

    for i in range(len(m)):
        quant = 0
        for j in range(i):
            _i = i - j
            _j = j
            if (m[_i][_j] == 1):
                quant += 1
        if (quant >= 2):
            pares_que_se_atacam += quant - 1
        

    return pares_que_se_atacam      

def aptidao(x):
    return 28 - h(x)

def proportion_selection(aptidaoArr):
    aptidaoArr = np.array(aptidaoArr)
    aptidaoArr = (aptidaoArr / aptidaoArr.sum())
    i = 0
    Soma = aptidaoArr[i]
    r = np.random.uniform(0, 1)
    while Soma < r:
        i += 1
        Soma += aptidaoArr[i]
    
    return i

def mutacao(populacao):
    for i in range(len(populacao)):
        for j in range(len(populacao[i])):
            p = np.random.uniform(0, 1);
            if (p < probabilidade_mutacao):
                xu = 7
                xl = 0
                n = np.random.uniform(-1, 1)
                populacao[i][j] = round(populacao[i][j] + taxa_mutacao * (xu-xl) * n)

                if (populacao[i][j] > 7):
                    populacao[i][j] = 7
                elif populacao[i][j] < 0:
                    populacao[i][j] = 0
 
def recombinar(x1, x2):
    p = np.random.uniform(0, 1);
    if (p < probabilidade_de_recombinacao):
        mascara = [0, 0, 0, 0, 0, 0, 0, 0]

        p = randrange(0, len(mascara))

        for i in range(len(mascara)):
            if i >= p:
                mascara[i] = 1

        _x1 = x1.copy()
        _x2 = x2.copy()

        for i in range(len(mascara)):
            if (mascara[i] == 1):
                x1[i] = _x2[i]
                x2[i] = _x1[i]

population = [None] * n
for i in range(n):
    population[i] = [None] * 8
    for j in range(8):
        population[i][j] = randrange(0, 8)


def imprimir_populacao(population): 
    print("===============")
    for i in population:
        print(f"({i}): {aptidao(i)}")
    print("===============")
    pass

print(f"POPULACAO INICIAL")
imprimir_populacao(population)

solucoes = []



def reiniciar():
    population = [None] * n
    for i in range(n):
        population[i] = [None] * 8
        for j in range(8):
            population[i][j] = randrange(0, 8)
parar = False
t1 = time()
t2 = time()
while len(solucoes) < 98:   

    if (t >= 30):
        t = 0
        reiniciar()

    aptidaoArr = [None] * n
    for i in range(n):
        aptidaoArr[i] = aptidao(population[i])
    t+=1

    nova_populacao = [None] * n 
    for i in range(n):
        nova_populacao[i] = population[proportion_selection(aptidaoArr)].copy()
        # nova_populacao[i] = population[i].copy()
        

    for i in range(len(nova_populacao) - 1):
        recombinar(nova_populacao[i], nova_populacao[i + 1])
    mutacao(nova_populacao)

    for i in range(len(nova_populacao)):
        if aptidao(nova_populacao[i]) == 28:
            if ((nova_populacao[i] in solucoes) == False):
                print(f"ACHOUUUU GERACAO: {t}")
                print(nova_populacao[i])
                solucoes.append(nova_populacao[i])
                t3 = time() - t2;
                print(f"{len(solucoes)}/98 SOLUCOES ENCONTRADAS EM {t3:.2f} SEGUNDOS FALTAM {98 - len(solucoes)}")  
                reiniciar();
                t2 = time()
    

    population = nova_populacao.copy();

t_total = time()-t1

for i in solucoes:
    print(f"{i}: {aptidao(i)}")      
print(f"{len(solucoes)} SOLUCOES ENCONTRADAS EM {t_total:.2f} SEGUNDOS")  


# SOLUCOES
# [0, 3, 4, 5, 1, 6, 7, 2]: 28
# [1, 5, 3, 0, 4, 6, 7, 2]: 28
# [2, 6, 4, 1, 5, 0, 7, 3]: 28
# [0, 3, 5, 2, 6, 1, 7, 4]: 28
# [1, 2, 5, 3, 6, 0, 7, 4]: 28
# [1, 2, 3, 5, 6, 4, 7, 0]: 28
# [1, 2, 4, 5, 7, 0, 6, 3]: 28
# [4, 2, 5, 3, 6, 0, 7, 1]: 28
# [1, 2, 6, 3, 5, 0, 7, 4]: 28
# [1, 2, 6, 4, 5, 0, 7, 3]: 28
# [2, 3, 7, 4, 6, 0, 5, 1]: 28
# [0, 3, 6, 2, 5, 1, 7, 4]: 28
# [1, 2, 5, 6, 4, 0, 7, 3]: 28
# [0, 2, 3, 5, 6, 1, 7, 4]: 28
# [1, 2, 7, 5, 3, 0, 6, 4]: 28
# [1, 2, 6, 4, 7, 0, 3, 5]: 28
# [2, 3, 1, 7, 5, 0, 6, 4]: 28
# [2, 3, 5, 6, 7, 0, 4, 1]: 28
# [2, 3, 4, 7, 5, 0, 6, 1]: 28
# [1, 2, 4, 7, 5, 3, 6, 0]: 28
# [3, 0, 4, 7, 5, 2, 6, 1]: 28
# [3, 4, 2, 5, 6, 1, 7, 0]: 28
# [1, 2, 3, 5, 7, 4, 6, 0]: 28
# [2, 0, 3, 5, 6, 1, 7, 4]: 28
# [2, 3, 1, 5, 6, 0, 7, 4]: 28
# [4, 2, 3, 5, 7, 1, 6, 0]: 28
# [4, 0, 3, 7, 5, 2, 6, 1]: 28
# [4, 0, 3, 5, 7, 1, 6, 2]: 28
# [4, 2, 3, 5, 6, 1, 7, 0]: 28
# [4, 0, 3, 5, 6, 1, 7, 2]: 28
# [3, 0, 2, 5, 6, 1, 7, 4]: 28
# [2, 4, 1, 7, 5, 3, 6, 0]: 28
# [3, 5, 2, 4, 6, 0, 7, 1]: 28
# [1, 2, 3, 6, 4, 7, 5, 0]: 28
# [1, 3, 4, 7, 5, 6, 2, 0]: 28
# [0, 2, 3, 4, 5, 6, 7, 1]: 28
# [1, 4, 2, 5, 6, 7, 3, 0]: 28
# [2, 4, 1, 5, 6, 7, 3, 0]: 28
# [2, 3, 1, 5, 6, 7, 0, 4]: 28
# [1, 4, 2, 7, 3, 6, 0, 5]: 28
# [1, 5, 0, 6, 3, 7, 2, 4]: 28
# [1, 3, 0, 4, 6, 7, 5, 2]: 28
# [1, 2, 4, 5, 6, 7, 3, 0]: 28
# [1, 3, 4, 6, 7, 5, 2, 0]: 28
# [3, 1, 4, 7, 5, 6, 2, 0]: 28
# [4, 0, 5, 7, 2, 6, 3, 1]: 28
# [4, 1, 3, 7, 5, 6, 2, 0]: 28
# [1, 2, 6, 3, 5, 7, 4, 0]: 28
# [2, 3, 4, 0, 5, 6, 7, 1]: 28
# [2, 3, 5, 0, 6, 4, 7, 1]: 28
# [1, 4, 5, 0, 6, 3, 7, 2]: 28
# [1, 4, 6, 0, 3, 5, 7, 2]: 28
# [1, 4, 5, 0, 2, 6, 7, 3]: 28
# [1, 3, 5, 0, 4, 6, 7, 2]: 28
# [2, 0, 5, 1, 4, 6, 7, 3]: 28
# [1, 4, 2, 0, 5, 6, 7, 3]: 28
# [2, 3, 4, 0, 6, 7, 5, 1]: 28
# [1, 3, 4, 2, 5, 6, 7, 0]: 28
# [0, 3, 4, 2, 5, 6, 7, 1]: 28
# [1, 6, 3, 0, 4, 7, 5, 2]: 28
# [2, 6, 3, 0, 5, 7, 4, 1]: 28
# [0, 2, 4, 1, 5, 6, 7, 3]: 28
# [1, 3, 4, 0, 6, 7, 5, 2]: 28
# [2, 5, 3, 0, 6, 4, 7, 1]: 28
# [2, 0, 3, 4, 5, 6, 7, 1]: 28
# [3, 0, 2, 4, 5, 6, 7, 1]: 28
# [3, 0, 5, 1, 4, 6, 7, 2]: 28
# [2, 0, 4, 1, 5, 6, 7, 3]: 28
# [3, 1, 4, 2, 5, 6, 7, 0]: 28
# [4, 1, 5, 0, 6, 3, 7, 2]: 28
# [1, 4, 5, 0, 7, 3, 6, 2]: 28
# [2, 5, 3, 1, 7, 4, 6, 0]: 28
# [2, 5, 3, 0, 7, 4, 6, 1]: 28
# [4, 1, 3, 5, 6, 7, 0, 2]: 28
# [1, 4, 6, 3, 0, 7, 5, 2]: 28
# [2, 0, 4, 5, 1, 6, 7, 3]: 28
# [0, 2, 4, 5, 1, 6, 7, 3]: 28
# [1, 2, 4, 5, 0, 7, 3, 6]: 28
# [1, 2, 3, 5, 0, 7, 4, 6]: 28
# [1, 2, 3, 5, 0, 6, 4, 7]: 28
# [1, 2, 4, 7, 0, 6, 3, 5]: 28
# [1, 2, 4, 5, 0, 6, 3, 7]: 28
# [1, 2, 3, 4, 0, 6, 7, 5]: 28
# [1, 2, 4, 6, 0, 3, 5, 7]: 28
# [1, 2, 6, 3, 0, 4, 7, 5]: 28
# [3, 0, 4, 5, 1, 6, 7, 2]: 28
# [2, 3, 4, 6, 1, 5, 7, 0]: 28
# [4, 1, 3, 5, 2, 6, 7, 0]: 28
# [2, 3, 4, 5, 1, 6, 7, 0]: 28
# [3, 1, 4, 5, 0, 6, 7, 2]: 28
# [1, 2, 3, 6, 0, 5, 7, 4]: 28
# [4, 0, 3, 6, 2, 5, 7, 1]: 28
# [4, 0, 5, 3, 1, 6, 7, 2]: 28
# [3, 0, 6, 4, 1, 5, 7, 2]: 28
# [2, 3, 4, 6, 1, 7, 5, 0]: 28
# [2, 5, 3, 6, 0, 7, 4, 1]: 28
# [0, 3, 6, 4, 1, 7, 5, 2]: 28
# [0, 2, 6, 4, 1, 7, 5, 3]: 28