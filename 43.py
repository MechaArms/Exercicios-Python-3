#Exercicio 43
'''
O cardápio de uma lanchonete é o seguinte:

Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
Considere que o cliente deve informar quando o pedido deve ser encerrado.
'''

codigos = [100, 101, 102, 103, 104, 105]
comidas = ['Cachorro Quente', 'Bauru Simples', 'Bauru com ovo', 'Hamburguer', 'ChesseBurguer', 'Refrigerante']
precos = [1.20, 1.30, 1.50, 1.20, 1.30, 1.0]
codigo = True
n_pedido = 1
pedido = []

while codigo != 0:
    print("\nPedido n°", n_pedido)
    codigo = int(input("Digite o código do alimento: "))
    if codigo == 0:
        break
    else:
        while codigo not in codigos:
            print("[Este código não corresponde a nenhum alimento.]")
            codigo = int(input("Digite o código do alimento: "))

        indice = codigos.index(codigo)
        quantidade = int(input("Digite a quantidade: "))
        valor_pedido = precos[indice] * quantidade
        pedido.append(valor_pedido)
    n_pedido += 1

pedido_nota = 0
print("\n" * 2)
for i in range(n_pedido - 1):
    print("Pedido n°", pedido_nota + 1, "= R$", round(pedido[pedido_nota], 2))
    pedido_nota += 1
print("Total: R$", round(sum(pedido), 2))