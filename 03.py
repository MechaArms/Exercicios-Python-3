#Exercício 3
'''
Faça um programa que leia e valide as seguintes informações:
    a. Nome: maior que 3 caracteres;
    b. Idade: entre 0 e 150;
    c. Salário: maior que zero;
    d. Sexo: 'f' ou 'm';
    e. Estado Civil: 's', 'c', 'v', 'd';
'''

Nome = str(input('Digite o Nome: '))
lista = []
for casa in str(Nome):
    lista.append(casa)
    while len(lista) < 4:
        print('O Nome precisa ser maior que 3 caracteres')
        Nome = str(input('Digite o Nome: '))
        lista = []
        for casa in str(Nome):
            lista.append(casa)
    print(f'O Nome está correto: {Nome}')

Idade = int(input('\nDigite a Idade: '))
while Idade < 0 or Idade > 150:
    print('A Idade precisa ser entre 0 e 150 anos')
    Idade = int(input('Digite a Idade: '))
print(f'A Idade está correta: {Idade}')

Salario = int(input('\nDigite o Salário: '))
while Salario < 0:
    print('O Salario precisa ser maior que zero')
    Salario = int(input('Digite o Salário: '))
print(f'O Salario está correto: {Salario}')

Sexo = str(input('\nDigite a Sexo: ').lower())
while 'f' != Sexo != 'm':
    print('O Sexo precisa ser "f" ou "m"')
    Sexo = str(input('Digite a Sexo: ').lower())
print(f'O Sexo está correto: {Sexo}')

Estado_Civil = str(input('\nDigite o Estado Civil: ').lower())
while 's' != Estado_Civil != 'c'and 'v' != Estado_Civil != 'd':
    print('O Estado Civil precisa ser "s", "c", "v" ou "d"')
    Estado_Civil = str(input('Digite a Estado Civil: ').lower())
print(f'O Estado Civil está correto: {Estado_Civil}')