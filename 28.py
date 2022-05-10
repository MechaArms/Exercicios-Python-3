#Exercicio 28
#Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. 
#O usuário deverá informar a quantidade de CDs e o valor para em cada um.


Total_CD = int(input('Quantos CDs no total fora comprados? '))
lista = []
soma = 0
cont = 1

for i in range(Total_CD):
    Valor_CD = float(input('Qual o valor do CD? '))    
    
    while Valor_CD <= 0:
        print('Valor invalido! O valor não pode ser menor que zero')
        Valor_CD = float(input('Responda novamente. Qual o valor do CD? '))

    print(f'Foi adicionado o valor de {Valor_CD} no CD {cont}')
    
    lista.append(Valor_CD)
    soma = soma + Valor_CD
    cont += 1
    
media = soma / Total_CD

print("Os valores de cada CD são: \n",lista)
print('O valor médio gasto em cada CD é: ', media)
print('O valor total gasto em cada CD é: ', soma)