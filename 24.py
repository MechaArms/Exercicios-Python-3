#Exercicio 24
#Faça um programa que calcule o mostre a média aritmética de N notas.

lista = []
soma = 0
n = int(input("Verificar a media de até quantas notas? "))

for casa in range(n):
    num = int(input('Digite o Numero: '))
    lista.append(num)
    soma = soma + num

print("As notas são:",lista)
media = soma / n
print(f'A Media é: {media}')