import numpy as np

#************************************************************
#Configurações dos parâmetros gamma e alpha para o Q-Learning
#************************************************************

#fator de desconto
gamma = 0.75
#taxa de aprendizagem
alpha = 0.9

#************************************************************
# Parte 1 - Definição do ambiente 
#************************************************************

subfases = {'ferrovia': 0,
            'hidro_alt': 1,
            'via_deslocamento': 2,
            'elementos_varios': 3,
            'limites_especiais': 4,
            'toponimos': 5,
            'area_edificada': 6,
            'planimetria': 7,
            'vegetacao': 8,
            'cq_tematico':  9,
            'validacao': 10,
            'edicao': 11           
        }

acoes = [0,1,2,3,4,5,6,7,8,9,10,11]

r = np.array([[0,1,1,0,0,0,0,0,0,0,0,0],
              [1,0,1,1,1,1,1,0,0,0,0,0],
              [0,1,0,1,1,1,1,0,0,0,0,0],
              [0,0,0,0,1,1,1,1,1,0,0,0],
              [0,0,0,1,0,1,1,1,1,0,0,0],
              [1,0,1,1,1,0,1,1,1,0,0,0],
              [0,0,0,1,1,1,0,0,1,0,0,0],
              [0,0,0,1,1,1,0,0,1,0,0,0],
              [0,0,0,1,1,1,0,1,0,0,0,0],
              [0,0,0,0,0,0,0,1,1,0,0,0],
              [0,0,0,0,0,0,0,0,0,1,100,0],
              [0,0,0,0,0,0,0,0,0,0,0,1000]])

#************************************************************
# Parte 2 - Construção da solução de ia com Q-Learning 
#************************************************************

Q = np.array(np.zeros([12,12]))

#inicializacao random
for i in range(0,10000):
    estado_atual = np.random.randint(0, 2)
    acao_possivel = []
    for j in range(12):
        if r[estado_atual, j] > 0:
            acao_possivel.append(j)
    proximo_estado = np.random.choice(acao_possivel)
    
    #Diferença temporal
    TD = r[estado_atual, proximo_estado] + gamma*Q[proximo_estado, np.argmax(Q[proximo_estado])] - Q[estado_atual, proximo_estado]
    
    #Atualizacao de Q pela equacao de Bellman
    Q[estado_atual,proximo_estado] = Q[estado_atual,proximo_estado] + alpha*TD
