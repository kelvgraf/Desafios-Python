number_1 = int(input('Primeiro número '))
number_2 = int(input('Segundo número '))
number_3 = int(input('Terceiro número '))

def maior():
	if number_1 > number_2 and number_1 > number_3:
		print(str(number_1) + ' e maior')

	elif number_2 > number_1 and number_2 > number_3:
		print(str(number_2) + ' e maior')

	elif number_3 > number_1 and number_3 > number_2 :
		print(str(number_3) + ' e maior')
	else:
		print('Todos maiores são iguais')


def menor():
	if number_1 < number_2 and number_3:
		print(str(number_1) + ' e maior')

	elif number_2 < number_1 and number_3:
		print(str(number_2) + ' e maior')

	elif number_3 < number_1 and number_2:
		print(str(number_3) + ' e maior')
	else:
		print('Todos menores são iguais')

maior()
menor()