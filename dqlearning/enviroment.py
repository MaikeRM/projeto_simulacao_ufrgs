# Criação do ambieante

import numpy as np

# Criando o Ambiente
class Enviroment(object):

    #Definição e inicialização de todos os parâmentros e variáveis do ambiente
    def __init__(self, tipo_1 = 208, tipo_2 = 52):
        self.tipo_1 = tipo_1
        self.tipo_2 = tipo_2
        self.ferrovia = {'media_horas':1,'std_horas': 4, 'tipo': self.tipo_1, 'autorizado': 0, 'finalizado':0}
        self.hidro_alt = {'media_horas':28,'std_horas': 7, 'tipo': self.tipo_1, 'autorizado': 0, 'finalizado':0}
        self.via_deslocamento = {'media_horas':18,'std_horas': 4, 'tipo': self.tipo_1, 'autorizado': 0, 'finalizado':0}
        self.elementos_varios = {'media_horas':3,'std_horas': 1, 'tipo': self.tipo_1, 'autorizado': 0, 'finalizado':0}
        self.limites_especiais = {'media_horas':1,'std_horas': 3, 'tipo': self.tipo_2, 'autorizado': 0, 'finalizado':0}
        self.toponimos = {'media_horas':4,'std_horas': 1, 'tipo': self.tipo_2, 'autorizado': 0, 'finalizado':0}
        self.area_edificada = {'media_horas':1,'std_horas': 4, 'tipo': self.tipo_1, 'autorizado': 0, 'finalizado':0}
        self.planimetria = {'media_horas':15,'std_horas': 5, 'tipo': self.tipo_1, 'autorizado': 0, 'finalizado':0}
        self.vegetacao = {'media_horas':32,'std_horas': 5, 'tipo': self.tipo_1, 'autorizado': 0, 'finalizado':0}
        self.cq_tematico = {'media_horas':14,'std_horas': 4, 'tipo': self.tipo_2, 'autorizado': 0, 'finalizado':0}
        self.validacao = {'media_horas':9,'std_horas': 3, 'tipo': self.tipo_2, 'autorizado': 0, 'finalizado':0}
        self.edicao = {'media_horas':18,'std_horas': 3, 'tipo': self.tipo_2, 'autorizado': 0, 'finalizado':0}
        self.tarefas_iniciais = self.ferrovia, self.hidro_alt
        self.tempo_total = 0.0
        self.reward = 0.0
        self.train = 1
        self.terminou = 0
    
    def update_enviroment(self, tempo_ai):

        #Calculo da Recompensa
        self.reward = tempo_ai

        #Escalonamento de recompensa
        self.reward = 1e-3*self.reward

        #Nó 1___________________________________________
        if self.ferrovia['finalizado'] == 1:
            self.via_deslocamento['autorizado'] = 1
        
        elif self.hidro_alt['finalizado'] == 1:
            self.toponimos['autorizado'] = 1

        #Nó 2___________________________________________
        elif self.via_deslocamento['finalizado'] == 1 and self.hidro_alt['finalizado'] == 1:
            self.area_edificada['autorizado'] = 1
            self.elementos_varios['autorizado'] = 1
            self.limites_especiais['autorizado'] = 1
        
        elif self.area_edificada['finalizado'] == 1:
            self.planimetria['autorizado'] = 1
            self.vegetacao['autorizado'] = 1
        
        elif (self.elementos_varios['finalizado']==1 and self.limites_especiais['finalizado'] == 1 and 
            self.toponimos['finalizado']==1 and self.planimetria['finalizado']==1 and self.vegetacao['finalizado']):
            self.cq_tematico['autorizado'] = 1
            
        #Nó 3___________________________________________
        elif self.cq_tematico['finalizado'] == 1:
            self.validacao['autorizado'] == 1
        
        elif self.validacao['finalizado'] == 1:
            self.edicao['autorizado'] == 1
