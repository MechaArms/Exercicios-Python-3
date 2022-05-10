#Exercicio 14
#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

lista_par = []
lista_impar = []
qtd_par = 0
qtd_impar = 0

for x in range(10):
    numero = int(input("Digite o Numero: "))
    if numero % 2 != 0:
        lista_impar.append(numero)
        qtd_impar += 1
    else:
        lista_par.append(numero)
        qtd_par += 1

print(lista_par)
print(f'foram {qtd_par} numeros pares')
print(lista_impar)
print(f'foram {qtd_impar} numeros impares')