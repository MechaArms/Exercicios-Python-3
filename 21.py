#Exercicio 21
#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
#Um número primo é aquele que é divisível somente por ele mesmo e por 1.

n = int(input("Verificar numeros primos ate: "))
mult=0

for count in range(2,n):
    if (n % count == 0):
        print("Múltiplo de",count)
        mult += 1

if(mult==0):
    print("É primo")
else:
    print("Tem",mult," múltiplos acima de 2 e abaixo de",n)