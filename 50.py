#Exercicio 50
#Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

h = 1
n = 2
h_lista = []
n_lista = []
print("H = 1 +", end = "")
while n <= 10 -1:
    print(" ",h, "/", n, " + ", end="")
    h_lista.append(h)
    n_lista.append(n)
    n += 1

print(h, "/", n, " => ", sum(h_lista), "/", sum(n_lista), " => ", round(sum(h_lista) / sum(n_lista)), 2)