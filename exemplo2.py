nome = input('Nome: ') 
idade = int(input('Idade: ')) #int inteiro
nota = float(input('Digite sua nota: ')) #float real

print('%s possui %d anos e nota %.2f' %(nome, idade, nota))

print(nome,'possui', idade, 'anos e nota', nota)

print('{0} possui {1} anos e nota {2:.2f}'. format(nome, idade, nota))
print('{} possui {} anos e nota {:.2f}'. format(nome, idade, nota))

print(f'{nome} possui {idade} anos e nota {nota:.2f}')