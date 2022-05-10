#Exercicio 30
'''
O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. 
Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
    Preço do pão: R$ 0.18
    Panificadora Pão de Ontem - Tabela de preços
    1 - R$ 0.18
    2 - R$ 0.36
    ...
    50 - R$ 9.00
'''

preco_pao = float(input('Digite o preço do pão: R$ '))
cont = 1

print(f'Preço do pão: R$ {preco_pao}')
print('Panificadora Pão de Ontem - Tabela de preços')

for x in range(50):
    total = preco_pao * cont
    print(f'{cont} - R$ {total}')
    cont += 1