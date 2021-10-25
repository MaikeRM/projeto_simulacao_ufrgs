# Criação do ambieante

import numpy as np

# Criando o Ambiente
class Enviroment(object):

    #Definição e inicialização de todos os parâmentros e variáveis do ambiente
    def __init__(self, tipo_1 = 208, tipo_2 = 52):
        self.tipo_1 = tipo_1
        self.tipo_2 = tipo_2
        self.ferrovia = {'media_horas':1,'std_horas': 4, 'tipo': self.tipo_1, 'autorizado': 1, 'finalizado':0}
        self.hidro_alt = {'media_horas':28,'std_horas': 7, 'tipo': self.tipo_1, 'autorizado': 1, 'finalizado':0}
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
        self.subfases = {'ferrovia':0,
                         'hidrografia':1,
                         'via_deslocamento':2,
                         'elementos_varios':3,
                         'limites_especiais':4,
                         'toponimos':5,
                         'area_edificada':6,
                         'planimetria':7,
                         'vegetacao':8,
                         'cq_tematica':9,
                         'validacao':10,
                         'edicao':11}

        self.funcionarios = [{'nome': 'Danilo','numero': 0, 'habilidades': [1,3,4,5,6,7,9]},
                        {'nome': 'Paulo', 'numero': 1, 'habilidades': [1,3,4,5,6,7,9]},
                        {'nome': 'Andre', 'numero': 2, 'habilidades': [2,8,9]},
                        {'nome': 'Castro', 'numero': 3, 'habilidades': [0,3,4,5,6,7,9,10]},
                        {'nome': 'Gustavo Ramos', 'numero':4, 'habilidades': [1,2,8,9,10]},
                        {'nome': 'Henrique Pires', 'numero':5, 'habilidades': [2,8]},
                        {'nome': 'Viana', 'numero': 6,'habilidades': [1,2,8]},
                        {'nome': 'Mendonca', 'numero': 7, 'habilidades': [2,8]},
                        {'nome': 'Rute Daniela', 'numero': 8, 'habilidades': [1,2,8]},
                        {'nome': 'Cialla', 'numero': 9, 'habilidades': [1,2,8]},
                        {'nome': 'Colleto', 'numero': 10, 'habilidades': [1,2]},
                        {'nome': 'Fachi', 'numero': 11, 'habilidades': [10,11]},
                        {'nome': 'Ana Luiza', 'numero': 12, 'habilidades': [10,11]}]
    
    def update_enviroment(self, tempo_ai):

        #Calculo da Recompensa
        self.reward = tempo_ai

        #Escalonamento de recompensa
        self.reward = 1e-3*self.reward

        #Iniciando o processo
        if self.ferrovia['autorizado'] == 1:
            escalados_ferrovia = []
            for i in range(len(self.funcionarios)):
                if self.subfases['ferrovia'] in self.funcionarios[i]['habilidades']:
                    escalados_ferrovia.append(self.funcionarios[i]['numero'])

        if self.hidro_alt['autorizado'] == 1:
            escalados_hidrovia = []
            for i in range(len(self.funcionarios)):
                if self.subfases['hidrografia'] in self.funcionarios[i]['habilidades']:
                    escalados_hidrovia.append(self.funcionarios[i]['numero'])

        #Obtenção do próximo estado
        if self.ferrovia['finalizado'] == 1:
            self.via_deslocamento['autorizado'] = 1
        
        elif self.hidro_alt['finalizado'] == 1:
            self.toponimos['autorizado'] = 1

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

        elif self.cq_tematico['finalizado'] == 1:
            self.validacao['autorizado'] == 1
        
        elif self.validacao['finalizado'] == 1:
            self.edicao['autorizado'] == 1

