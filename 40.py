#Exercicio 40
'''
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
    a.Código da cidade;
    b.Número de veículos de passeio (em 1999);
    c.Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
    d.Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
    e.Qual a média de veículos nas cinco cidades juntas;
    f.Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
'''
# for loop 5 cidades // maior e menor acidentes // media veiculos // media acidentes < 2000 veiculos

cod_cidade = []
num_veiculo = []
num_acidente = []
num_veiculo2000 =[]

for x in range(5):
    print("\nCidade n° ", x + 1)
    codigo = int(input("Digite o código: "))
    veiculo = int(input("Digite o número de veículos de passeio: "))
    acidente = int(input("Digite o número de acidentes de trânsito com vítimas: "))
    cod_cidade.append(codigo)
    num_veiculo.append(veiculo)
    num_acidente.append(acidente)
        
cod_maior_acidente = num_acidente.index(max(num_acidente))
cod_menor_acidente = num_acidente.index(min(num_acidente))

print("\n" * 2)
print("O maior índice de acidentes é", max(num_acidente), "e seu codigo é", cod_cidade[cod_maior_acidente])
print("O menor índice de acidentes é", min(num_acidente), "e seu codigo é", cod_cidade[cod_menor_acidente])
print("Média média de veículos nas cinco cidades juntas:", sum(num_veiculo) / len(num_veiculo))
print("Média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio:", sum(num_veiculo2000) / len(num_veiculo2000))