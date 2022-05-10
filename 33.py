#Exercicio 33
#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas,
# e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

print('Departamento Estadual de Meteorologia')

confirm = 's'
cont = 1
lista_temp = []

while confirm != 'n':
    print('\nTemperatura n° ', cont)
    temp = int(input('\nDigite a temperatura em C°: '))
    confirm = str(input('Deseja digitar uma nova temperatura?\nDigite [s] Sim ou [n] Não: ')).lower()
    lista_temp.append(temp)
    cont += 1
    
print("\n" * 2)
print(f'As temperaturas são:\n{lista_temp}')
print(f'O maior das temperaturas é: {max(lista_temp)}')
print(f'O menor das temperaturas é: {min(lista_temp)}')
print(f'A soma das temperaturas é: {sum(lista_temp)}')
print(f'A media das temperaturas é: %.2f'% (sum(lista_temp) / len(lista_temp)))