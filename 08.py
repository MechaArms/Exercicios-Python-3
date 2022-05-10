#Exercicio 8
#Faça um programa que leia 5 números e informe a soma e a média dos números.

lista = []
soma = 0

for casa in range(5):
    num = int(input('Digite o Numero: '))
    lista.append(num)
    soma = soma + num

print(lista)

print(f'A Soma é: {soma}')

media = soma / 5
print(f'A Media é: {media}')