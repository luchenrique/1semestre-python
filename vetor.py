"""
vet = []
for i in range(5):
    vet.append(int(input('Informe um valor: ')))

print('\nVetor')
for i in range(5):
    print(vet[i])

print('\nVetor')
print(vet)
"""

#====================================================================================================================
#====================================================================================================================

"""
vet = []
N = int(input('Entre com uma quantidade: '))
for i in range (N):
    vet.append(int(input('Entre com um número: ')))
print('\nVetor')
for i in range(N):
    print(vet[i])
print('\nVetor')
print(vet)
"""

#====================================================================================================================
#====================================================================================================================

"""
soma = 0
vet = []
x = int(input('Entre com uma quantidade: '))
for i in range (x):
    vet.append(int(input('Entre com um número: '))) 
    soma += vet[i] 
print('A soma dos vetores', vet,'é igual a', soma)
"""

#====================================================================================================================
#====================================================================================================================

# Considere um programa que calcule a média aritmética geral de uma classe de alunos e imprima a quantidade de 
# notas que estão acima da média calculada. O usuário deve entrar com a quantidade de alunos.

"""
soma = 0
vet = []
med = 0
cont = 0
x = int(input('Entre com a quantidade de alunos : '))
for i in range (x):
    vet.append(int(input('Entre com as notas dos alunos: '))) 
    soma += vet[i] 
    med = soma/x
    if vet[i] > med:
        cont += 1
print('A média da turma é de', med)
print('O total de notas acima da média é de: ', cont)
"""

#====================================================================================================================
#====================================================================================================================

# Fazer um programa que leia um vetor de 20 números inteiros e determine qual o maior e o menor número do vetor 
# e imprima os dois valores.

vet = []
maior = 0
menor = 0
aux = 0
for i in range(4):
    vet.append(int(input('Informe um valor: ')))
    if vet[i]>maior:
        vet[i] == maior
        print(maior)
    else:
        print(menor)



#====================================================================================================================
#====================================================================================================================

# Crie um programa que leia um vetor de 20 números inteiros e em seguida divida estes números em outros 2 novos 
# vetores, separando os números pares dos números ímpares.