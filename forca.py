print('*********************************')
print('***Bem vindo ao jogo da Forca!***')
print('*********************************')

palavra_secreta = 'banana'
palavra =['_','_','_','_','_','_']

acertou = False
enforcou = False
erro = 0
print(palavra)
while(not acertou and not enforcou):
    chute = input('Qual letra? ')
    if(chute in palavra_secreta):
        posicao = 0
        for letra in palavra_secreta:
            if (chute.lower() == letra.lower()):
                palavra[posicao] = letra
            posicao = posicao + 1
    else:
        erro +=1
    enforcou = erro == 6
    acertou = '_' not in palavra
    print(palavra)