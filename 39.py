#Exercicio 39
'''
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. 
Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
'''

cod_aluno = []
altura_aluno = []
n_aluno = 1

for x in range(10):
    print("\nAluno n° ", n_aluno)
    codigo = int(input("Digite o código: "))
    altura = float(input("Digite a altura: "))
    cod_aluno.append(codigo)
    altura_aluno.append(altura)
    n_aluno += 1

cod_alto = altura_aluno.index(max(altura_aluno))
cod_baixo = altura_aluno.index(min(altura_aluno))

print("\nCódigo do mais alto é", cod_aluno[cod_alto], "e sua altura é", max(altura_aluno))
print("Código do mais baixo é", cod_aluno[cod_baixo], "e sua altura é", min(altura_aluno))