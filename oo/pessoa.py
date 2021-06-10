#Classe é a base da orientacao objetos, ela é a forma que define como nossos objetos se comportam
#Classe também é usado como sinônimo de tipo
#Método, é uma função que pertence a uma classe. Sempre está relacionado a um objeto
#self = em java e C# usamos this
class Pessoa:
    def __init__(self, nome=None, idade=35):
        self.idade = idade
        self.nome = nome


    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('João')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Tiago'
    print(p.nome)
    print(p.idade)