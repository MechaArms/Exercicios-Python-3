#Exercicio 9
#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

lista = []
impar = 0

for casa in range(50):
    impar = impar + 1
    if impar % 2 != 0:
        lista.append(impar)
    else:
        continue

print(lista)