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
        self.reward = 0.0
        self.train = 1
        self.terminou = 0
        self.tempo_total = {'ferrovia': 0,
                         'hidrografia': 0,
                         'via_deslocamento': 0,
                         'elementos_varios': 0,
                         'limites_especiais': 0,
                         'toponimos': 0,
                         'area_edificada': 0,
                         'planimetria': 0,
                         'vegetacao': 0,
                         'cq_tematica': 0,
                         'validacao': 0,
                         'edicao': 0}

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

<<<<<<< HEAD
        #Nó 1___________________________________________
=======
        #Iniciando o processo

        #___________________________________FERROVIA________________________________________
        if self.ferrovia['autorizado'] == 1:
            escalados_ferrovia = []
            for i in range(len(self.funcionarios)):
                if self.subfases['ferrovia'] in self.funcionarios[i]['habilidades']:
                    escalados_ferrovia.append(self.funcionarios[i]['numero'])
            qtd_escalados = 1
            # qtd_escalados = np.random.choice(escalados_ferrovia, size=np.random.randint(len(escalados_ferrovia)), replace=False)
            mu, sigma = self.ferrovia['media_horas'], self.ferrovia['std_horas']
            tempo_ferrovia = self.ferrovia['tipo']*abs(np.random.normal(mu, sigma, 1))/len(qtd_escalados)

            #Atualizando tempos
            self.tempo_total['ferrovia'] = tempo_ferrovia

            #Atualizando estados
            self.ferrovia['finalizado'] = 1

        #___________________________________HIDROGRAFIA________________________________________
        if self.hidro_alt['autorizado'] == 1:
            escalados_hidrovia = []
            for i in range(len(self.funcionarios)):
                if self.subfases['hidrografia'] in self.funcionarios[i]['habilidades']:
                    escalados_hidrovia.append(self.funcionarios[i]['numero'])
            qtd_escalados = np.random.choice(escalados_hidrovia, size=np.random.randint(0, len(escalados_hidrovia)), replace=False)
            mu, sigma = self.hidro_alt['media_horas'], self.hidro_alt['std_horas']
            tempo_hidrovia = self.hidro_alt['tipo']*abs(np.random.normal(mu, sigma, 1))/len(qtd_escalados)        
           
           #Atualizando tempos
            self.tempo_total['hidrovia'] = tempo_hidrovia

            #Atualizando estados
            self.hidro_alt['finalizado'] = 1

        #___________________________________VIA DESLOCAMENTO________________________________________
        
        if self.via_deslocamento['autorizado'] == 1:
            escalados_via = []
            for i in range(len(self.funcionarios)):
                if self.subfases['via_deslocamento'] in self.funcionarios[i]['habilidades']:
                    escalados_via.append(self.funcionarios[i]['nome'])
            qtd_escalados = np.random.choice(escalados_via, size=np.random.randint(1, len(escalados_via)), replace=False)
            print('\nvia_deslocamento', escalados_via, '\nescalados', qtd_escalados)
            mu, sigma = self.via_deslocamento['media_horas'], self.via_deslocamento['std_horas']
            tempo_via = self.via_deslocamento['tipo']*abs(np.random.normal(mu, sigma, 1))/len(qtd_escalados)    
            
            #Atualizando tempos
            self.tempo_total['via_deslocamento'] = tempo_via[0]

            #Atualizando estados
            self.via_deslocamento['finalizado'] = 1
                
        #___________________________________AREA EDIFICADA________________________________________
        if self.area_edificada['autorizado'] == 1:
            escalados_area_edificada = []
            for i in range(len(self.funcionarios)):
                if self.subfases['area_edificada'] in self.funcionarios[i]['habilidades']:
                    escalados_area_edificada.append(self.funcionarios[i]['nome'])
            qtd_escalados = np.random.choice(escalados_area_edificada, size=np.random.randint(1, len(escalados_area_edificada)), replace=False)
            print('\nvarea edificada', escalados_area_edificada, '\nescalados', qtd_escalados)
            mu, sigma = self.area_edificada['media_horas'], self.area_edificada['std_horas']
            tempo_area_edificada = self.area_edificada['tipo']*abs(np.random.normal(mu, sigma, 1))/len(qtd_escalados)    
            
            #Atualizando tempos
            self.tempo_total['area_edificada'] = tempo_area_edificada[0]

            #Atualizando estados
            self.area_edificada['finalizado'] = 1

        #___________________________________ELEMENTOS VARIOS________________________________________
        if self.elementos_varios['autorizado'] == 1:
            escalados_elementos = []
            for i in range(len(self.funcionarios)):
                if self.subfases['elementos_varios'] in self.funcionarios[i]['habilidades']:
                    escalados_elementos.append(self.funcionarios[i]['nome'])
            qtd_escalados = np.random.choice(escalados_elementos, size=np.random.randint(1, len(escalados_area_edificada)), replace=False)
            print('\nElementos varios', escalados_elementos, '\nescalados', qtd_escalados)
            mu, sigma = self.elementos_varios['media_horas'], self.elementos_varios['std_horas']
            tempo_elementos = self.elementos_varios['tipo']*abs(np.random.normal(mu, sigma, 1))/len(qtd_escalados)    
            
            #Atualizando tempos
            self.tempo_total['elementos_varios'] = tempo_elementos[0]

            #Atualizando estados
            self.elementos_varios['finalizado'] = 1
    
        #___________________________________LIMITES ESPECIAS________________________________________
        if self.limites_especiais['autorizado'] == 1:
            escalados_limites = []
            for i in range(len(self.funcionarios)):
                if self.subfases['limites_especiais'] in self.funcionarios[i]['habilidades']:
                    escalados_limites.append(self.funcionarios[i]['nome'])
            qtd_escalados = np.random.choice(escalados_limites, size=np.random.randint(1, len(escalados_area_edificada)), replace=False)
            print('\nLimites especiais', escalados_limites, '\nescalados', qtd_escalados)
            mu, sigma = self.escalados_limites['media_horas'], self.escalados_limites['std_horas']
            tempo_limites = self.limites_especiais['tipo']*abs(np.random.normal(mu, sigma, 1))/len(qtd_escalados)    
            
            #Atualizando tempos
            self.tempo_total['limites_especiais'] = tempo_limites[0]

            #Atualizando estados
            self.limites_especiais['finalizado'] = 1

        #___________________________________TOPONIMOS________________________________________
        if self.toponimos['autorizado'] == 1:
            escalados_toponimos = []
            for i in range(len(self.funcionarios)):
                if self.subfases['toponimos'] in self.funcionarios[i]['habilidades']:
                    escalados_limites.append(self.funcionarios[i]['nome'])
            qtd_escalados = np.random.choice(escalados_toponimos, size=np.random.randint(1, len(escalados_area_edificada)), replace=False)
            print('\nToponimos', escalados_toponimos, '\nescalados', qtd_escalados)
            mu, sigma = self.toponimos['media_horas'], self.toponimos['std_horas']
            tempo_toponimos = self.toponimos['tipo']*abs(np.random.normal(mu, sigma, 1))/len(qtd_escalados)    
            
            #Atualizando tempos
            self.tempo_total['toponimos'] = tempo_toponimos[0]

            #Atualizando estados
            self.toponimos['finalizado'] = 1





    def check_env(self):
>>>>>>> d41d165471f9ba7d4c21e3e0cfdc9450b1019df3
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

