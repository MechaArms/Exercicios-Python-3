#Exercicio 42
'''
Faça um programa que leia uma quantidade indeterminada de números positivos e 
conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. 
A entrada de dados deverá terminar quando for lido um número negativo.
'''
repet = 0
cont = 0
lista_25 = []
lista_50 = []
lista_75 = []
lista_100 = []

while repet == 0:
    cont += 1
    print('numero ',cont)

    num = int(input('digite o numero: '))
    if num < 0:
        print('numero abaixo de 0')
        break
    elif num >= 0 and num <= 25:
        lista_25.append(num)
    elif num >= 26 and num <= 50:
        lista_50.append(num)
    elif num >= 51 and num <= 75:
        lista_75.append(num)
    elif num >= 76 and num <= 100:
        lista_100.append(num)
    else:
        print('numero acima de 100')
        break

print("\n" * 2)
print('numeros entre 0-25: ',len(lista_25))
print('numeros entre 26-50: ',len(lista_50))
print('numeros entre 51-75: ',len(lista_75))
print('numeros entre 76-100: ',len(lista_100))