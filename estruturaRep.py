"""
print('Exemplo 1')
for numero in range (0, 10, 1):
    print (numero)

print('Exemplo 2')
for numero in range (10, 0, -2):
    print (numero)

print('Exemplo 3')
for numero in range (10) :
    print (numero)
"""

#====================================================================================================================
#====================================================================================================================

"""
nomes = ['Pedro', 'Ana', 'Maria']
for n in nomes:
    print(n)
"""

#====================================================================================================================
#====================================================================================================================


"""
lista = [1,2,3,4,5,7,8]
for num in lista:
    if num > 6 :
        print(num)
"""

#====================================================================================================================
#====================================================================================================================

"""
i = 0
while(i<10):
    print(i)
    i = i + 1
"""

#====================================================================================================================
#====================================================================================================================

"""
conta = 0
x = 2
while(conta <= 5):
    print(x)
    conta += 1
else:"""
   # print('Valor de varíavel conta é %d' %conta)


#====================================================================================================================
#====================================================================================================================

# Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem decrescente. 
# Utilize para tal uma seleção encadeada.
"""
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

if n1 == n2 == n3 or n1 == n2 != n3 or n1 != n2 == n3 or n1 != n3 == n2:
    print('Os valores são iguais, valor digiar números diferentes')

else:
    if n1 < n2 < n3:
        print(n3, n2, n1)
    elif n3 < n2 < n1:
        print(n1, n2, n3)
    elif n2 < n1 < n3:
        print(n3, n1, n2) 
    elif n1 < n2 > n3:
        print(n2, n1, n3)
    elif n1 > n2 < n3:
        print(n1, n3, n2)
"""
#====================================================================================================================
#====================================================================================================================

#Faça um programa que efetue a soma de todos os números ímpares que são múltiplos de 3 e que 
# se encontram no conjunto dos números de 1 até 500.
"""
soma = 0
for num in range(1, 500, 2):
    if num % 3 == 0:
        soma += num
print('A soma é %d\n' %soma)
"""

#====================================================================================================================
#====================================================================================================================

#Construa um programa que calcule a média aritmética de um conjunto de números pares fornecidos pelo usuário. 
# O usuário irá fornecer um total de 10 números. Observe que nada impede que o usuário forneça quantos números 
# ímpares quiser, com a ressalva de que eles não poderão ser acumulados.

"""media = 0
cnt = 0
soma = 0

for num in range(1, 11): 
    n1 = int(input('Informe 10 valores: '))
    if n1 % 2 == 0:
        soma += n1
        cnt += 1
    else:
        soma = soma + 0
    media = soma / cnt
print('A média aritimética desses valores é de ', media)"""

# ==================================== CORREÇÃO ====================================

"""
cont = soma = 0
for 1 in range(10):
    n = int(input('Digite um número: '))
    if n%2 == 0:
        soma += n
        cont += 1
if cont > 0:
    media = soma/cont
    print('A média é de %.1f' %media)
else:
    print('Nenhum número par foi digitado!')
"""

#====================================================================================================================
#====================================================================================================================

#Construa um programa que calcule a média aritmética de um conjunto de números pares que forem fornecidos pelo usuário.
# O valor de finalização será a entrada do número 0 (zero). Observe que nada impede que o usuário forneça quantos 
# números ímpares quiser, com a ressalva de que eles não poderão ser acumulados.

"""
media = 0
cnt = 0
soma = 0
n2 = int(input('Digite qualquer valor diferente de 0 para iniciar: '))

while n2 != 0:
    n1 = int(input('Informe os valores: '))
    if n1 % 2 == 0:
        soma += n1
        cnt += 1
    else:
        soma = soma + 0
    media = soma / cnt
print('A média aritimética desses valores é de ', media)
"""

# ==================================== CORREÇÃO ====================================

"""
cont = soma = 0

n = int(input('Digite um número: '))
while(n != 0):
    if n%2 == 0:
        soma += n
        cont += 1
    n = int(input('Digite um número: '))
if(cont == 0):
    print('Não houveram números pares para calcular a média.')
else:
    media = soma/cont
    print('A média é: {}'. format(media))
"""

#====================================================================================================================
#====================================================================================================================

#Fazer um programa que simule uma contagem regressiva de 10 minutos, ou seja, mostre: 10:00, 9:59, 
# 9:58, 9:57, ..., 8:59, 8:58, até 0:00.

"""
seg = 59
min = 9
print('10:00')
for min in range (9, -1, -1):
    for seg in range (59, -1, -1):
        print('%02d:%02d' %(min, seg))
"""

#====================================================================================================================
#====================================================================================================================









