#Exercicio 11
#Altere o programa anterior para mostrar no final a soma dos números.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

for i in range(n1 + 1, n2):
        print(i)

for j in range(n2 + 1, n1):
        print(j)

print("Soma dos números: ", i + j)