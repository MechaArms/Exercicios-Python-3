#Exercicio 38
'''
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
    a. Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
    b. Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
    c. A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 
        Faça um programa que determine o salário atual desse funcionário. 
        Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
'''

import datetime

salario = float(input("Dgite o salario inicial do funcionario: "))
aumento = 1.5
ano = 1995
ano_atual = datetime.datetime.now().year
salario_atual = salario

for i in range(ano, ano_atual):
    print("Salario em ", i, " = R$ %.2f"% salario_atual)
    aumento = aumento * 2
    salario_atual = salario + (salario * (aumento / 100))