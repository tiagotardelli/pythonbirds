# Classe é a base da orientacao objetos, ela é a forma que define como nossos objetos se comportam
# Classe também é usado como sinônimo de tipo
# Método, é uma função que pertence a uma classe. Sempre está relacionado a um objeto
# self = em java e C# usamos this
class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    luciano = Pessoa(nome='Luciano')
    tiago = Pessoa(luciano, nome='Tiago')
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
    print(tiago.__dict__)
    print(luciano.__dict__)

