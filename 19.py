#Exercicio 19
#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

lista = []
soma = 0
cont = int(input('Favor informe quantos numeros serão avaliados: '))

for casa in range(cont):
    num = int(input('Digite o Numero: '))
    while num < 0 or num > 1000: 
        print('Por favor digite apenas números entre 0 e 1000')
        num = int(input('Digite o Numero: '))
    lista.append(num)
    soma = soma + num
lista.sort(reverse = True)

print(lista)
print(f'O maior é {lista[0]}')
print(f'O menor é {lista[-1]}')
print(f'A Soma é: {soma}')