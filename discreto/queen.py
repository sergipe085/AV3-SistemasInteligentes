from random import randrange
import numpy as np

queens = [0, 0, 0, 0, 0, 0, 0, 0]
t = 0
n = 10
probabilidade_mutacao = 0.5
probabilidade_de_recombinacao = 0.95;
taxa_mutacao          = 0.01


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
                n = np.random.uniform(0, 1)
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

parar = False
while t <= 100 and parar == False:   
    aptidaoArr = [None] * n
    for i in range(n):
        aptidaoArr[i] = aptidao(population[i])
    t+=1

    nova_populacao = [None] * n 
    for i in range(n):
        nova_populacao[i] = population[proportion_selection(aptidaoArr)]
        # nova_populacao[i] = population[i]
        

    for i in range(len(nova_populacao) - 1):
        recombinar(nova_populacao[i], nova_populacao[i + 1])
    print("==ANTES DA MUTACAO==")
    imprimir_populacao(nova_populacao)
    mutacao(nova_populacao)
    print("==DEPOIS DA MUTACAO==")
    imprimir_populacao(nova_populacao)

    for i in range(len(nova_populacao)):
        if aptidao(nova_populacao[i]) == 28:
            print("ACHOUUUU")
            parar = True
            

    imprimir_populacao(nova_populacao)

    population = nova_populacao.copy();


# A rainha da coluna 1 esta na linha 5

print(aptidao([4, 2, 5, 7, 1, 3, 0, 6]))

# Funcao aptidao Ψ(x) = 28 − h(x)
# Objetivo: Maximizar a funcao aptidao            