#Exercicio 25
#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

lista = []
soma = 0
n = int(input("Digite quantas pessoas na turma: "))

for casa in range(n):
    num = int(input('Digite a idade: '))

    while num <= 0 or num > 150:
        print('Valor invalido! Por favor digite apenas números da idade entre 1 a 150')
        num = int(input('Digite a idade: '))

    lista.append(num)
    soma = soma + num

print("As idades são:",lista)
media = soma / n

if media > 0 and media <= 25:
    print('A turma é jovem. A Media é: ', media)
elif media > 26 and media <= 60:
    print('A turma é adulta. A Media é: ', media)
elif media > 60:
    print('A turma é idosa. A Media é: ', media)
else:
    print('erro')