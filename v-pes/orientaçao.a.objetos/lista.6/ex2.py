class Carro:
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor

    def pintar(self, nova_cor):
        self.cor = nova_cor

    def mostrar_cor(self):
        return self.cor

carro = Carro("Mazda Rx7 Fc3s", "Branco")

carro.pintar("Preto")

print(carro.mostrar_cor())
