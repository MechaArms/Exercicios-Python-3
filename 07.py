#Exercício 7
#Faça um programa que leia 5 números e informe o maior número

lista = []

for casa in range(5):
    num = int(input('Digite o Numero: '))
    lista.append(num)
lista.sort(reverse = True)
print(lista)
print(f'O maior é {lista[0]}')