import numpy as np
from random import randrange
import math

def gerar_pontos3D(N:int)->np.ndarray:
    '''
    Esta função gera pontos aleatórios em um espaço tridimensional.
    Desta massa de pontos, um destes é selecionado e removido para ser o ponto inicial da rota.
    
    '''
    x_partition = np.random.uniform(-10, 10, size=(N,3))
    y_partition = np.random.uniform(0, 20, size=(N,3))
    z_partition = np.random.uniform(-20, 0, size=(N,3))
    w_partition = np.random.uniform(0, 20, size=(N,3))

    x1 = np.array([[20,-20,-20]])
    x1 = np.tile(x1,(N,1))
    x_partition = x_partition+x1

    x1 = np.array([[-20,20,20]])
    x1 = np.tile(x1,(N,1))
    y_partition = y_partition+x1

    x1 = np.array([[-20,20,-20]])
    x1 = np.tile(x1,(N,1))
    z_partition = z_partition+x1

    x1 = np.array([[20,20,-20]])
    x1 = np.tile(x1,(N,1))
    w_partition = w_partition+x1 
    Pontos = np.concatenate((x_partition,y_partition,z_partition,w_partition), axis=0)
    I = np.random.permutation(N*4)
    inicial = I[0]
    ponto_inicial = Pontos[inicial,:].reshape(1,3)
    Pontos = np.delete(Pontos,inicial,axis=0)
    return ponto_inicial,Pontos

def gerar_individuo(pontos):
    tamanho = len(pontos)
    individuo = [0]
    genes = list(range(1, len(pontos), 1))
    jafoiindex = []
    i=0
    while i < len(genes):
        index =  randrange(0, len(genes))
        while index in jafoiindex:
            index =  randrange(0, len(genes))
        individuo.append(genes[index])
        jafoiindex.append(index)
        i+=1
    individuo.append(0)
    return individuo

def gerar_populacao(pontos, n):
    populacao = []
    i = 0
    while i < n:
        populacao.append(gerar_individuo(pontos))
        i+=1

    return populacao


def distancia_entre_2_pontos(x1, x2):
    distancia = math.sqrt((x2[0] - x1[0]) ** 2 + (x2[1] - x1[1]) ** 2 + (x2[2] - x1[2]) ** 2)
    return distancia;

def aptidao(individuo, pontos):
    i = 0
    soma = 0
    while i < len(individuo) - 1:
        soma += distancia_entre_2_pontos(pontos[individuo[i]], pontos[individuo[i + 1]])
        
        i+=1
    return float(soma)

def aptidao_populacao(populacao, pontos):
    menor = 99999
    soma = 0
    for i in populacao:
        _i = aptidao(i, pontos)
        if (_i < menor):
            menor = _i
        soma += _i

    return (soma/len(populacao), menor)

def recombinar(x1, x2):
    p = np.random.uniform(0, 1);
    probabilidade_de_recombinacao = 0.95;
    if (p < probabilidade_de_recombinacao):
        mascara = [0] * len(x1)

        p = randrange(0, len(mascara))
        p2 = randrange(0, len(mascara))

        if (p2 < p):
            p,p2 = p2,p

        for i in range(len(mascara)):
            if i >= p and i < p2:
                mascara[i] = 1

        x1_trocou = []
        x2_trocou = []
        for i in range(1, len(mascara) - 1, 1):
            if (mascara[i] == 1):
                x1_trocou.append(x1[i])
                x2_trocou.append(x2[i])

                tmp = x1[i]
                x1[i] = x2[i]
                x2[i] = tmp
            pass

        for i in range(1, len(mascara) - 1, 1):
            if (mascara[i] == 0):
                if (x1[i] in x2_trocou):
                    for j in range(len(x1_trocou)):
                        if ((x1_trocou[j] in x1) == False):
                            x1[i] = x1_trocou[j]
                            x1_trocou.remove(x1_trocou[j])
                            break;
        
                if (x2[i] in x1_trocou):
                    for j in range(len(x2_trocou)):
                        if ((x2_trocou[j] in x2) == False):
                            x2[i] = x2_trocou[j]
                            x2_trocou.remove(x2_trocou[j])
                            break;

        # for i in range(1, len(mascara) - 1, 1):
        #     if (mascara[i] == 1):
        #         x1_trocou.append(x1[i])
        #         x2_trocou.append(_x2[i])
        #         tmp = _x1[i]
        #         _x1[i] = _x2[i]
        #         _x2[i] = tmp

        # _x1i = 0
        # _x2i = 0
        # for i in range(1, len(mascara)-1, 1):
        #     if (mascara[i] == 0):
        #         if (_x1i < len(x1_trocou) and _x1[i] in x2_trocou):
        #             _x1[i] = x1_trocou[_x1i]
        #             _x1i+=1
        #         if (_x2i < len(x2_trocou) and _x2[i] in x1_trocou):
        #             _x2[i] = x2_trocou[_x2i]
        #             _x2i+=1
                

def recombinar_populacao(populacao):
    new_population = populacao.copy()
    for i in range(len(new_population) - 1):
        recombinar(new_population[i], new_population[i+1])

    return new_population


        

def selecao_por_torneio(populacao, pontos):
    N = len(populacao)
    populacao = populacao.copy()
    new_population = []
    for i in range(N):
        n = randrange(1, 5);
        grupo = []
        grupo_index = []
        for _ in range(n):
            index = randrange(0, N)
            while index in grupo_index:
                index = randrange(0, N)
            grupo.append(populacao[index])   
            grupo_index.append(index)  
        max_index = grupo_index[0]
        max_aptidao = aptidao(populacao[max_index], pontos)
        
        for j in range(len(grupo_index)):
            aptidao_atual = aptidao(populacao[grupo_index[j]], pontos)
            if (aptidao_atual < max_aptidao):
                max_aptidao = aptidao_atual
                max_index = grupo_index[j]
        new_population.append(populacao[max_index])
    return new_population

def get_pontos():
    ponto_inicial, pontos = gerar_pontos3D(4);
    pontos = list(pontos)
    pontos.insert(0, ponto_inicial[0])
    return pontos


def melhor_individuo(populacao, pontos):
    _individuo = []
    menor_index = 0
    menor = aptidao(populacao[0], pontos)
    for i in range(len(populacao)):
        cand = aptidao(populacao[i], pontos)
        if (cand < menor):
            menor = cand
            menor_index = i

    return populacao[i]
        

def mutar(populacao):
    new_population = []
    for i in range(len(populacao)):

        n = randrange(0, 6)
        
        for _ in range(n):
            p = np.random.uniform(0, 1)

            if (mutacao_p > p):
                _from = randrange(1, len(populacao[i])-1)
                _to = randrange(1, len(populacao[i])-1)

                tmp = populacao[i][_to]
                populacao[i][_to] = populacao[i][_from]
                populacao[i][_from] = tmp

        new_population.append(populacao[i].copy())
    return new_population

def imprimir_populacao(populacao, pontos):
    print("==================")
    for i in range(len(populacao)):
        print(f"Individuo: {populacao[i]}:   {aptidao(populacao[i], pontos):.2f}")
    print("==================")

n = 50
t_max = 999999;

pontos = get_pontos()


populacao = gerar_populacao(pontos, n)
mutacao_p = 0.01
t = 0
epocas_sem_melhorar = 0
new_population = populacao
melhorou = True
while t < t_max and melhorou == True:

    media_aptidao, menor_aptidao = aptidao_populacao(new_population, pontos)

    new_population = selecao_por_torneio(new_population, pontos)

    recombinar_populacao(new_population)
    # imprimir_populacao(new_population, pontos)
    new_population = mutar(new_population)
    # imprimir_populacao(new_population, pontos)

    print(f"APTIDAO POPULACAO: {aptidao_populacao(new_population,pontos)}")

    new_media_aptidao, new_menor_aptidao = aptidao_populacao(new_population, pontos)
    
    if (new_menor_aptidao >= menor_aptidao):
        epocas_sem_melhorar += 1
    else:
        epocas_sem_melhorar = 0

    if (epocas_sem_melhorar > 30):
        melhorou = False

    t+=1
    bp = 1

print(melhor_individuo(new_population, pontos))