'''
arquivo.write('jean carlos')
arquivo.close()
testte = open('jean.txt', 'w')
testte.write('Jean carlos\n ')'''
#arquivo = open('aquivos.txt', 'a')
#arquivo.read()
#arquivo.write('ivr d dnre9reuinejd vks.akbnrieaurnv')

teste = open('palavras.txt', 'w')
teste.write('banana\n')
teste.write('melancia\n')
teste.write('morango\n')
teste.write('manga\n')
teste.write('Abacate\n')
teste.write('Abacaxi\n')
teste.write('Mangaba\n')
teste.write('Acerola\n')
teste.write('Amora\n')
teste.write('Araticum\n')
teste.write('Bacaba\n')
teste.write('Pequi\n')
teste.write('Cacau\n')
teste.write('Pera\n')
teste.write('Caqui\n')
teste.write('Carambola\n')
teste.write('Cereja\n')
teste.write('Cidra\n')
teste.write('Coco\n')
teste.write('Pitanga\n')
teste.write('Figo\n')
teste.write('Framboesa\n')
teste.write('Goiaba\n')
teste.write('Groselha\n')
teste.write('Jabuticaba\n')
teste.write('Jaca\n')
teste.write('Jambo\n')
teste.write('Jenipapo\n')
teste.write('Kiwi\n')
teste.write('Laranja\n')
teste.close()
teste = open('palavras.txt', 'r')
palavras = []
for linha in teste:
    linha = linha.strip()
    palavras.append(linha)
from random import randrange

x = randrange(0,len(palavras))

print(palavras[x])
