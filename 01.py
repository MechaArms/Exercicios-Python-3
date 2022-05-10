#Exercício 1
'''
Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
'''

nota = int(input('Digite o valor da nota entre [0 a 10]: '))

while nota > 10 or nota < 0:
    print(f'O valor {nota} é invalido')
    nota = int(input('Digite o valor da nota entre [0 a 10]: '))

print(f'O valor {nota} é valido')