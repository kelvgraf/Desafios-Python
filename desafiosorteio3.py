import random
numero = random.randint(1,30)

tentativas = 0

while tentativas < 3:
	digite = int(input("Digite um número:"))
	tentativas = tentativas +1

if digite == numero :
	print( 'Parábens!,' + str(tentativa) + 'vezes.')

else:
	print('Tente novamente. O número foi:' + str(numero))