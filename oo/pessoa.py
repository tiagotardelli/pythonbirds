# Classe é a base da orientacao objetos, ela é a forma que define como nossos objetos se comportam
# Classe também é usado como sinônimo de tipo
# Método, é uma função que pertence a uma classe. Sempre está relacionado a um objeto
# self = em java e C# usamos this
class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    pass

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    luciano = Mutante(nome='Luciano')
    #luciano = Homem(nome='Luciano')
    # luciano = Pessoa(nome='Luciano')
    tiago = Homem(luciano, nome='Tiago')
    # tiago = Pessoa(luciano, nome='Tiago')
    print(Pessoa.cumprimentar(tiago))
    print(id(tiago))
    print(tiago.cumprimentar())
    print(tiago.nome)
    print(tiago.idade)
    for filho in tiago.filhos:
        print(filho.nome)
    tiago.sobrenome = 'Tardelli'
    print(tiago.sobrenome)
    del tiago.filhos
    luciano.olhos = 1
    del luciano.olhos
    print(tiago.__dict__)
    print(luciano.__dict__)
    # Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(tiago.olhos)
    print(luciano.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(tiago.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())
    pessoa = (Pessoa('Anonimo'))
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(tiago, Pessoa))
    print(isinstance(tiago, Homem))
    print(luciano.olhos)



