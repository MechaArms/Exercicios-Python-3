#Exercicio 49
'''
Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
Imprima no final a soma da série.
'''

n1 = 1
n2 = 1
n1_lista = []
n2_lista = []
print("S = ", end = "")
while n1 <= 10 -1:
    print(n1, "/", n2, " + ", end="")
    n1_lista.append(n1)
    n2_lista.append(n2)
    n1 += 1
    n2 += 2

print(n1, "/", n2, " = ", sum(n1_lista), "/", sum(n2_lista))