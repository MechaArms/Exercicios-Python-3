#Exercício 2
'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''

login = str(input('Digite o login: '))
senha = str(input('Digite a senha: '))

while login == senha:
    print('A senha não pode ser igual ao login')
    login = str(input('Digite o login: '))
    senha = str(input('Digite a senha: '))

print('Login e Senha estão OK')