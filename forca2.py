print('*********************************')
print('***Bem vindo ao jogo da Forca!***')
print('*********************************')
palavra_secreta = 'banana'
letras_acertadas = ['_', '_', '_', '_', '_', '_']
enforcou = False
acertou = False
erros = 0
print(letras_acertadas)
while(not enforcou and not acertou):
    chute = input("Qual letra? ")
    if(chute in palavra_secreta):
        posicao = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[posicao] = letra
            posicao = posicao + 1
    else:
        erros += 1
    enforcou = erros == 6
    acertou = '_' not in letras_acertadas
    print(letras_acertadas)