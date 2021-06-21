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
        # return f'Olá {id(self)}'
        return f'Olá meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        # cumprimentar_da_classe=self.cumprimentar() - Errado, gera recursão
        # cumprimentar_da_classe=Pessoa.cumprimentar() - Abordagem ruim, tem que ficar mudando a classe
        cumprimentar_da_classe=super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'


class Mutante(Pessoa):
    olhos = 3


def imprimir(list: []):
    for item in list:
        print(item)


if __name__ == '__main__':
    luciano = Mutante(nome='Luciano')
    # luciano = Homem(nome='Luciano')
    # luciano = Pessoa(nome='Luciano')
    tiago = Homem(luciano, nome='Tiago')
    # tiago = Pessoa(luciano, nome='Tiago')
    imprimir([
        Pessoa.cumprimentar(tiago),
        id(tiago),
        tiago.cumprimentar(),
        tiago.nome,
        tiago.idade,
    ])

    for filho in tiago.filhos:
        print(filho.nome)
    tiago.sobrenome = 'Tardelli'
    imprimir([tiago.sobrenome])
    del tiago.filhos
    luciano.olhos = 1
    del luciano.olhos
    print(tiago.__dict__)
    print(luciano.__dict__)
    # Pessoa.olhos = 3
    imprimir([
        Pessoa.olhos,
        tiago.olhos,
        luciano.olhos,
        (id(Pessoa.olhos), id(luciano.olhos), id(tiago.olhos)),
        (Pessoa.metodo_estatico(), luciano.metodo_estatico()),
        (Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())
    ])
    pessoa = (Pessoa('Anonimo'))
    imprimir([
        isinstance(pessoa, Pessoa),
        isinstance(pessoa, Homem),
        isinstance(tiago, Pessoa),
        isinstance(tiago, Homem),
        luciano.olhos,
        tiago.cumprimentar(),
        luciano.cumprimentar()
    ])
