#Exercicio 45
'''
Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, 
o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com 
o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). 
Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. 
Após todos os alunos terem respondido informar:
    a. Maior e Menor Acerto;
    b. Total de Alunos que utilizaram o sistema;
    c. A Média das Notas da Turma.
    Gabarito da Prova:

        01 - A
        02 - B
        03 - C
        04 - D
        05 - E
        06 - E
        07 - D
        08 - C
        09 - B
        10 - A
Após concluir isto você poderia incrementar o programa permitindo que 
o professor digite o gabarito da prova antes dos alunos usarem o programa.
'''
#----sem input professor----

gabarito = ['A','B','C','D','E','E','D','C','B','A']
turma = []
teste = True
aluno = 1

while teste !=0:

    exame = []
    questao = 1
    
    print(aluno,'º Aluno\n')
    for i in range (10):
        print('Questão nº', questao)
        teste = str(input('Digite a sua resposta: ')).upper()
        if teste not in gabarito:
            while teste not in gabarito:
                print('resposta invalida, digite apenas: [A, B, C, D, E]')
                teste = str(input('Digite a sua resposta: ')).upper()
        exame.append(teste)
        questao += 1

    print('')
    contador = 0
    pontos = 0

    for i in range (10):
        print("questão ", contador + 1, end=" : ")
        if exame[contador] == gabarito[contador]:
            print(exame[contador],'- resposta correta!')
            pontos += 1
            contador +=1
        else:
            print(exame[contador],'- resposta errada! A correta é: ',gabarito[contador])
            contador +=1
    turma.append(pontos)
    print('Total de pontos: ',pontos)

    retorno = str(input('\nOutro aluno vai utilizar o sistema?\nDigite [s] Sim ou [n] Não: ')).lower()
    if retorno == 's':
        aluno += 1
    else:
        print('\nPrograma concluido\nVerificando notas\n')
        break
 
print('O maior Acerto:', max(turma))
print('O menor Acerto:', min(turma))
print('O total de alunos:', len(turma))
print('A Média das Notas da Turma:', sum(turma) / len(turma))

#----com input professor----

gabarito = ['A','B','C','D','E','E','D','C','B','A']
letras = ['A','B','C','D','E']
turma = []
exame = []
teste = True
aluno = 1

print('\n[Acesso Professor]')
confirmacao = str(input('\nDeseja mudar o gabarito da prova?\nDigite [s] Sim ou [n] Não: ')).lower()
if confirmacao == 's':
    gabarito.clear()
    while teste !=0:
        
        print('\n' * 2)
                
        for i in range (10):
            print('Questão nº', i + 1)
            avaliacao = str(input('Digite a sua resposta: ')).upper()
            while avaliacao not in letras:
                print('resposta invalida, digite apenas: [A, B, C, D, E]')
                avaliacao = str(input('Digite a sua resposta: ')).upper()
            gabarito.append(avaliacao)
                    
        print(gabarito)
        confirmacao_2 = str(input('\nDeseja mudar o gabarito da prova?\nDigite [s] Sim ou [n] Não: ')).lower()
        if confirmacao_2 == 's':
            continue
        else:
            print('Gabarito confirmado!\n')
            break

print('\n[Acesso Aluno]')
while teste !=0:

    print('\n' * 2)
    exame.clear()
        
    print(aluno,'º Aluno\n')
    for i in range (10):
        print('Questão nº', i + 1)
        teste = str(input('Digite a sua resposta: ')).upper()
        while teste not in letras:
            print('resposta invalida, digite apenas: [A, B, C, D, E]')
            teste = str(input('Digite a sua resposta: ')).upper()
        exame.append(teste)

    print('')
    contador = 0
    pontos = 0

    for i in range (10):
        print("questão ", contador + 1, end=" : ")
        if exame[contador] == gabarito[contador]:
            print(exame[contador],'- resposta correta!')
            pontos += 1
            contador +=1
        else:
            print(exame[contador],'- resposta errada! A correta é: ',gabarito[contador])
            contador +=1
    turma.append(pontos)
    print('Total de pontos: ',pontos)

    retorno = str(input('\nOutro aluno vai utilizar o sistema?\nDigite [s] Sim ou [n] Não: ')).lower()
    if retorno == 's':
        aluno += 1
    else:
        print('\nPrograma concluido\nVerificando notas\n')
        break
 
print('O maior Acerto:', max(turma))
print('O menor Acerto:', min(turma))
print('O total de alunos:', len(turma))
print('A Média das Notas da Turma:', sum(turma) / len(turma))
print('As Notas da Turma foram:', turma)