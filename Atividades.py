# == igual
# != diferente
# and conjunção
# or disjunção


#Escreva um algoritmo que leia um
#número e imprima se o número é
#positivo, negativo ou zero.

"""
nmr1=int(input('Entre com um número: '))
if nmr1 > 0:
    print('Positivo')
elif nmr1 < 0:
    print('Negativo')
else:
    print('Zero')
"""

"""-------------------------------------------------------------------------------------------------------------------"""

#Fazer um algoritmo que leia um número e
#imprima se o número é par ou ímpar.

""""
nmr1 = int(input('Escreva um número'))
if nmr1 %2 == 0:
    print('O número é par: ')
else:
    print('O número é impar: ')
"""

"""-------------------------------------------------------------------------------------------------------------------"""

#Escreva um algoritmo que leia dois
#valores inteiros e diferentes, e mostre-os
#em ordem decrescente.

"""
nmr1 = int(input('Digite o primeiro valor: '))
nmr2 = int(input('Digite um valor diferente do primeiro: '))

if nmr1 > nmr2:
    print(nmr1, nmr2)
elif nmr1 < nmr2:
    print(nmr2, nmr1)
else :
    print('Os números são iguais, favor digitar números diferentes')
"""



"""-------------------------------------------------------------------------------------------------------------------"""

#Fazer um algoritmo que leia 3 valores inteiros
#e verifique se eles podem formar um
#triângulo. Se for possível formar um triângulo,
#escreva uma mensagem informando se é um
#triângulo equilátero, isósceles ou escaleno.

#Observações:
#O comprimento de um lado do triângulo é
#sempre menor do que a soma dos outros dois.
#Equilátero: todos lados iguais
#Isósceles: dois lados iguais
#Escaleno: todos os lados diferentes

"""
nmr1 = int(input('Digite o primeiro valor: '))
nmr2 = int(input('Digite o segundo valor: '))
nmr3 = int(input('Digite o terceiro valor: '))

if nmr1 + nmr2 < nmr3 or nmr1 + nmr3 < nmr2 or nmr2 + nmr3 < nmr1:
    print('Isso não é um tr iângulo')

else:
    if nmr1 == nmr2 == nmr3:
        print('Triangulo Equilátero')
    elif nmr1 == nmr2 != nmr3:
        print('Triangulo Isósceles')
    elif nmr1 != nmr2 == nmr3:
        print('Triangulo Isósceles')
    elif nmr1 == nmr3 != nmr2:
        print('Triangulo Isósceles')
    else: 
        print('Triangulo Escaleno') 
"""
    

"""-------------------------------------------------------------------------------------------------------------------"""





