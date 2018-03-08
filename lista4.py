palavra = input('Digite sua palavra:\n' )

numberletter = len(palavra)

final = numberletter - 4

if numberletter > 0:
	final = palavra[2:numberletter]
	print(final + 'gato')


else:
	print('Digite uma palavra maior.')
	

#INCOMPLETO