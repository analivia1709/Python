nome = str(input('Digite uma frase: ')).lower().strip()
print('Tem {} letras A'.format(nome.count('a')))
print('A primeira letra "a" esta {} posição'.format(nome.find('a')))
print('A ultima letra "a" esta na posição {}'.format(nome.rfind('a')))