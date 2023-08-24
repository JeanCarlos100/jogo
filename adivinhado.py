numero = 42
tentativa = 3
rodada = 1
print('******************************')
print('*    Jogo da adivinhação     *')
print('******************************')
while (tentativa > 0):
	print("Tentativa que você uso {} por tentativa por usa {}".format(rodada,tentativa))
	chute = int(input("digite um número: \n"))

	acertou = chute == numero
	maior = chute > numero
	menor = chute < numero

	if(acertou):
		print('Você acertou!\n')
		break
	elif(maior):
		print('Você errou! O seu chute foi maior que o número secreto\n')
	elif(menor):
		print('Você errou! O seu chute foi menor que o número secreto\n')

	tentativa -=1
	rodada +=1
print ("Fim do jogo!")