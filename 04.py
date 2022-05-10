#Exercício 4
'''
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
'''

#A = 80.000 com 3% ao ano
#B = 200.000 com 1,5% ao ano

ano = 0
a = 80000
b = 200000

while a < b:
    ano += 1
    a = a + (a/100)*3
    b = b + (b/100)*1.5
print(f'Total de anos = {ano}')
print(f'País A = {round(a)}\nPaís B = {round(b)}')