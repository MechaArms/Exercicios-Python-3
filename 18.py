#Exercicio 18
#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

lista = []
soma = 0
cont = int(input('Favor informe quantos numeros serão avaliados: '))

for casa in range(cont):
    num = int(input('Digite o Numero: '))
    lista.append(num)
    soma = soma + num
lista.sort(reverse = True)

print(lista)
print(f'O maior é {lista[0]}')
print(f'O menor é {lista[-1]}')
print(f'A Soma é: {soma}')