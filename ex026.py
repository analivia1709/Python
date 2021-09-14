##frase[9::3] pula 3 em 3 letras
##len[frase] qual o cumprimento da frase
##frase.count('o') conta quanto o minusculos tem
##frase.find('deo') mostra onde começa a primeira opção
##frase.find('androind')devolve o valor -1
##'curso' in frase = o in serve pra ver se tem a palavra curso ou não
##frase.replace('python', 'androind')
##frase.upper()coloca tudo em maiuscula
##frase.lower() deixa tudo minusculo
##frase.capitalize (deixa so a primeira em maiuscula)
##frase.title()analisa quaantas palavras tem
##frase.strip = remove os  espaços
##frase.rstrip() trata pela direita
##frase.lsttrip() trata pela esquerda
##frase.split() divir a string em umsa lista
##'-'.join(frase)junta a frase com o hifen
## para textos longos basta colocar 3 ""


frase= 'Curso em video python'
print(frase[3])

frase2= 'Curso em video python'
print(frase2[3:13])

frase3 = 'Curso em video python'
print(frase3[:13])

frase4 = 'Curso em video python'
print (frase4[1:15:2]) ##do 1 ao 15 pulando de 2 em  2

frase5 = 'Curso em video python'
print(frase5[1::2]) ## vai ate o final

frase6 = 'Curso em video python'
print(frase6[::2])

frase10 = 'Curso em video python'
dividido = frase10.split()
print(dividido[0])

frase8 = 'Curso em video python'
print(len(frase8))

frase9 = 'Curso em video python'
print(frase9.split())

frase7 = 'Curso em video python'
print(frase7.count('o'))


