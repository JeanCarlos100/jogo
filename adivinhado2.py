numero = 42
tentativa = 4
rodada = 1
x = 3
print('******************************')
print('*    Jogo da adivinhação     *')
print('******************************')
for rodada in range(1, tentativa):
	print("Tentativa que você uso {} por tentativa por usa {}".format(rodada,x))
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

	x-=1
print ("Fim do jogo!")