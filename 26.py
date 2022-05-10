#Exercicio 26
#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
#Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

def votacao(candidato_1, candidato_2, candidato_3, voto_nulo):
    
    n = int(input("Digite número total de eleitores: "))

    while n <= 0:
        print("Valor invalido! Por favor digite no minimo 1 (Hum) eleitor")
        n = int(input("Digite número total de eleitores: "))

    print('O numero correspondente aos caditatos são: \n + [1]para candidato 1 \n + [2]para candidato 2 \n + [3]para candidato 3 ')

    for casa in range(n):
        voto = int(input('\nDigite o numero do candidato: '))

        if voto == 1:
            candidato_1 += 1
            print('Você votou no candidato 1')
        elif voto == 2:
            candidato_2 += 1
            print('Você votou no candidato 2')
        elif voto == 3:
            candidato_3 += 1
            print('Você votou no candidato 3')
        else:
            print('Você digitou um numero invalido! Seu voto será anulado!')
            voto_nulo += 1

    urna.update({
        'candidato 1': candidato_1, 
        'candidato 2': candidato_2, 
        'candidato 3': candidato_3, 
        'votos nulos': voto_nulo
    })
    decisao(candidato_1, candidato_2, candidato_3, voto_nulo)


def decisao(candidato_1, candidato_2, candidato_3, voto_nulo):
    #vitoria majoritaria
    if candidato_1 > candidato_2 and candidato_1 > candidato_3 and candidato_1 > voto_nulo:
        print('\nO candidato 1 ganhou!\n')
        vencedor(urna)
    elif candidato_2 > candidato_1 and candidato_2 > candidato_3 and candidato_2 > voto_nulo:
        print('\nO candidato 2 ganhou!\n')
        vencedor(urna)
    elif candidato_3 > candidato_1 and candidato_3 > candidato_1 and candidato_3 > voto_nulo:
        print('\nO candidato 3 ganhou!\n')
        vencedor(urna)
    elif voto_nulo > candidato_1 and voto_nulo > candidato_2 and voto_nulo > candidato_3:
        print('\nO voto nulo ganhou! Não houve candidatos vencedores.\n')
        vencedor(urna)
    else:
        #empate
        print('\nEmpate! Não houve candidatos vencedores\n')
        vencedor(urna)


def vencedor(urna):
    for i in sorted(urna, key = urna.get, reverse=True):
        print(i, 'tiveram', urna[i], 'votos')


urna = {'candidato 1': 0, 'candidato 2': 0, 'candidato 3': 0, 'votos nulos': 0}
candidato_1 = 0
candidato_2 = 0
candidato_3 = 0
voto_nulo = 0

votacao(candidato_1, candidato_2, candidato_3, voto_nulo)