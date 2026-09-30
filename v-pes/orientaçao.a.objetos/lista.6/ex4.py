class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def esta_disponivel(self):
        return self.quantidade > 0

    def vender(self):
        if self.esta_disponivel():
            self.quantidade -= 1

produto = Produto("Caneta", 2)

print("Disponível:", produto.esta_disponivel())

produto.vender()
print("Quantidade após uma venda:", produto.quantidade)
print("Disponível:", produto.esta_disponivel())

produto.vender()
print("Quantidade após outra venda:", produto.quantidade)
print("Disponível:", produto.esta_disponivel())

produto.vender()
print("Quantidade após tentar vender sem estoque:", produto.quantidade)
print("Disponível:", produto.esta_disponivel())
