#Exercicio 20
#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

fatorial = int

def calculo_fatorial(fatorial):
    fatorial=int(input("Digite o numero: "))

    while fatorial <= 0 or fatorial > 16:
        print('Por favor digite apenas números entre 1 e 16')
        fatorial=int(input("Digite o numero: "))

    valor = fatorial
    multi = 1

    for count in range(fatorial):
        multi *= fatorial
        fatorial -= 1
    print(f'{valor}! = {multi}')
    repeticao_fatorial(fatorial)

def repeticao_fatorial(fatorial):
    pergunta = str(input('Gostaria de calcular novamente? ["s" ou "n"]: ').lower())
    if pergunta == 's':
        calculo_fatorial(fatorial)
    else:
        print('programa concluido')

calculo_fatorial(fatorial)