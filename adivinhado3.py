from random import*
numero = (randint(1,100))
rodada = 1
print('******************************')
print('*    Jogo da adivinhação     *')
print('******************************')
print('números aleatorio de 1 a 100\n')

print("1 para o nível A com 40 tentativa")
print("2 para o nível B com 35 tentativa")
print("3 para o nível C com 30 tentativa")
print("4 para o nível D com 25 tentativa")
print("5 para o nível E com 20 tentativa")
print("6 para o nível F com 15 tentativa")
print("7 para o nível G com 10 tentativa")
print("8 para o nível H com 5 tentativa")
print("9 para o nível I com 3 tentativa")
print("10 para o nível J com 1 tentativa")


escola = int(input("Escola o nivel do jogo: \n"))
while (escola <1) or (escola > 10): 
	escola = int(input("Valor invalido, digite novamente: \n"))

if (escola == 1):
	tentativa = 40
elif (escola == 2):
	tentativa =35
elif (escola == 3):
	tentativa = 30
elif (escola == 4):
	tentativa =25
elif (escola == 5):
	tentativa = 20
elif (escola == 6):
	tentativa =15
elif (escola == 7):
	tentativa = 10
elif (escola == 8):
	tentativa =5
elif (escola == 9):
	tentativa = 3
elif (escola == 10):
	tentativa =1

while (tentativa > 0):
	print("Tentativa que você uso {} por tentativa por usa {}".format(rodada,tentativa))
	chute = int(input("digite um número: \n"))
	print("\n")

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

if (acertou == False):
	print("O número foi o ",numero)