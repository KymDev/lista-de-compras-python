class CompraLista:

    #Método construtor
    def __init__(self,lista,valor):
        self.lista = lista
        self.valor = valor

    #Função Listagem
    def Listagem(self):
        for intem, preco in zip(self.lista,self.valor):
            print(f'{item:.<20} R${preco:.2f}', end='\n')

    #Função Total
    def Total(self):
        soma = sum(self.valor)
        print(f"O valor total da lista é {soma:.2f}")

#Lista de compras e peços vazias
itens = []
precos = []

#lopp em while para adicionar valores
continuar = 'S'
while continuar == 'S':
    item = input('Digite um item para a lista: ')
    preco = float(input('Digite o valor do item: '))
    itens.append(item)
    precos.append(preco)
    continuar = input("Deseja acrescentar mais algum item a lista?(S/N) ").upper()

#Instancia da classe CompraLista
compras = CompraLista(itens,precos)

#Chamando os métodos
compras.Listagem()
compras.Total()