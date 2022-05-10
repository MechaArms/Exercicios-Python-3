#Exercício 5
'''
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
Valide a entrada e permita repetir a operação
'''

def retorno(a, b, ano, tx_a, tx_b):
    while a < b:
        ano += 1
        a = a + (a/100) * tx_a
        b = b + (b/100) * tx_b
    print(f'\nTotal de anos = {ano} \nPaís A = {round(a)} \nPaís B = {round(b)}')
    pergunta = str(input('Gostaria de repetir a operação? ["s" ou "n"]: ').lower())
    while 's' != pergunta != 'n':
        print('O Resposta precisa ser "Sim" ou "Não" ["s" ou "n"]')
        pergunta = str(input('Gostaria de repetir a operação? ["s" ou "n"]: ').lower())
    if pergunta == 's':
        entrada()
    else:
        print('Programa Concluido!')

def entrada():
    ano = 0
    print('')
    a = int(input('Informe o numero populacional do pais A: '))
    b = int(input('Informe o numero populacional do pais B: '))
    tx_a = float(input('Informe a taxa de crescimento do pais A: '))
    tx_b = float(input('Informe a taxa de crescimento do pais B: '))
    while a <= 0 or b <= 0 or tx_a <= 0 or tx_b <= 0 or tx_a < tx_b:
        print('\nNenhum dos valores pode ser menor que 1. \nE tambem a taxa de crecimento do país B não pode ser maior que a do país A. \nPor favor digite novamente\n')
        entrada()
    retorno(a, b, ano, tx_a, tx_b)

entrada()