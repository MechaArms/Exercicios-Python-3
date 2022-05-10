#Exercicio 17
#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

fatorial=int(input("Digite o numero: "))

valor = fatorial
multi = 1

for count in range(fatorial):
    multi *= fatorial
    fatorial -= 1

print(f'{valor}! = {multi}')