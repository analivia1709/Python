nome = (input('Digite o seu nome: '))
print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um segundo numeror: '))
print('A soma vale {}'.format(n1+n2))

n3 = int(input('Entre com um valor: '))
n4 = int(input('Entre com um outro valor: '))
s = n3 + n4
m = n3 * n4
sub = n3 - n4
d = n3 / n4
di= n3 // n4
e = n3 ** n4
print('A soma entre os valor é {}'.format(n3 + n4))
print('A mutiplicação between os values é {}'.format(n3 * n4))
print('A subtração between values é {} '.format(n3 - n4))
print('A divisão between values é {:.3f}'.format(n3 / n4))
print('A divisão inteira between values é {}'.format(n3 // n4))
print('The value da exponenciação é {}'.format(n3 ** n4))