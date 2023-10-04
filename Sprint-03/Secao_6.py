# Exercícios 21

class Passaro:  # Definindo a classe Passaro
    def voar(self): # Definindo o método voar
        print('Voando...')
    
    def som(self): # Definindo o método som
        pass

class Pato(Passaro):
    def __init__(self): # Definindo o método inícial
        print('Pato')

    def som(self): # Editando o método herdado
        print('Pato emitindo som...') 
        print('Quack Quack')

class Pardal(Passaro):
    def __init__(self): # Definindo o método inícial
        print('Pardal')

    def som(self): # Editando o método herdado
        print('Pardal emitindo som...')
        print('Piu Piu')

pato = Pato() # O objeto Pato
pato.voar()
pato.som()

pardal = Pardal() # O objeto Pardal
pardal.voar()
pardal.som()

# Exercícios 22

class Pessoa: # Definindo a classe Passoa
    def __init__(self, id) -> None: # Definindo o método inícial, e o atribito id
        self.id = id 
        self.__nome = None

    @property # Um decorator transforma o metodo nome em um getter
    def nome(self):
        return self.__nome 
    
    @nome.setter # Um decorator que transforma o metedo nome em um setter
    def nome(self, nome): # Aqui entra o atributo nome
        self.__nome = nome
    
pessoa = Pessoa(0) # O objeto Pessoa
pessoa.nome = 'Fulano De Tal'
print(pessoa.nome)

# Exercícios 23

class Calculo: # Definindo a classe Calculo
    def soma(self, X, Y): # Aqui chama o metodo soma, com os atributos X e Y
        self.X = X
        self.Y = Y
        print(f'Somando: {X}+{Y} = {X + Y}')

    def sub(self, X, Y): # Aqui chama o metodo subtração, com os atributos X e Y
        self.X = X
        self.Y = Y
        print(f'Subtraindo: {X}-{Y} = {X - Y}')

calculo = Calculo() # O objeto Calculo
calculo.soma(4,5)
calculo.sub(4,5)

# Exercícios 24

class Ordenadora: # Definindo a classe Ordenadora
    listaBaguncada = [] # Criando a variável listaBagunçada para definir o tipo da variavel

    def __init__(self, listaBaguncada) -> None: # Definindo o método inícial, e o atribito listaBaguncada
        self.listaBaguncada = listaBaguncada

    def ordenacaoCrescente(self): # Definindo o método para ordenar crescentemente
        return sorted(self.listaBaguncada)

    def ordenacaoDecrescente(self): # Definindo o método para ordenar decrescentemente
        return sorted(self.listaBaguncada, reverse=True)

crescente = Ordenadora([1, 2, 3, 4, 5]) # O objeto crescente com a primeira lista
ordenacao_crescente = crescente.ordenacaoCrescente()

decrescente = Ordenadora([9, 8, 7, 6]) # O objeto decrescente com a segunda lista
ordenacao_decrescente = decrescente.ordenacaoDecrescente()

print(ordenacao_crescente)
print(ordenacao_decrescente)

# Exercícios 25

class Aviao: # Definindo a classe Avião
    cor = 'Azul' # Definindo o atributo cor como padrão
    def __init__(self, modelo, velocidade_maxima, capacidade) -> None: # Definindo o método inícial, e os atribitos modelo, velocidade_maxima, capacidade
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade

avioes = [] # Uma lista para acrescentar os atribitos modelo, velocidade_maxima, capacidade 
avioes.append(Aviao("BOIENG456", "1500 km/h", 400))
avioes.append(Aviao("Embraer Praetor 600", "863 km/h", 14))
avioes.append(Aviao("Antonov An-2", "258 km/h", 12))

for aviao in avioes: # Mostra o print da lista avião
    print(f"O avião de modelo {aviao.modelo} possui uma velocidade máxima de {aviao.velocidade_maxima}, capacidade para {aviao.capacidade} passageiros e é da cor {aviao.cor}.")