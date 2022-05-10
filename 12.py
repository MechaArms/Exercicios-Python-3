#Exercicio 12

#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
#Tabuada de 5:
#   5 X 1 = 5
#   5 X 2 = 10
#   ...
#   5 X 10 = 50


num = int(input('Digite o Numero: '))
mult = 1

print(f'\nTabuada de {num}')

for casa in range(10):
    tabuada = num * mult
    print(f'{num} X {mult} = {tabuada}')
    mult += 1