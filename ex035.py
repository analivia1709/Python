import random
from time import sleep
##o random.randint gera numeros inteiros
pc = random.randint(1,6)
usuario = int(input('Descubra o numero numero escolido pelo computador: '))
print('PROCESSANDO...')
sleep(3)
if pc == usuario:
    print('Parabens voce acertou')
else:
    print('Infelizmente voce nao acertou, o computador pensou no numero {} e voce pensou no numero {} '.format(pc, usuario))