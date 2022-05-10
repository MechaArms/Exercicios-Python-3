#Exercicio 27
#Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos

turma = int(input('Quantas turmas? '))
lista = []
soma = 0
cont = 1 

for i in range(turma):
    alunos= int(input('Quantos alunos na turma? '))
    
    while alunos <= 0 or alunos > 40:
        print('Valor invalido! As turmas não podem ter mais de 40 alunos ou menos que zero')
        alunos= int(input('Responda novamente. Quantos alunos na turma? '))

    print(f'Você adicionou {alunos} na turma {cont}')
    lista.append(alunos)
    soma = soma + alunos
    cont += 1

print("A quantidade de alunos nas turmas são: \n",lista)
media = soma / turma

print('A Media de alunos é: ', media)