#Classe é a base da orientacao objetos, ela é a forma que define como nossos objetos se comportam
#Classe também é usado como sinônimo de tipo
#Método, é uma função que pertence a uma classe. Sempre está relacionado a um objeto
#self = em java e C# usamos this
class Pessoa:
    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())