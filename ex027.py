nome = str(input('Digite o seu nome completo: ')).strip()  ##elimina os espaços antes e depois
print('Seu nome me maiúsulo é {} '.format(nome.upper()))
print('Seu nome em minúsculo é {} '.format(nome.lower()))
print('Seu nome ao todo tem :  '.format(len(nome) - nome.count(' '))) ## conta os espaços
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa =  nome.split() ## faz uma lista com os nomes
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))