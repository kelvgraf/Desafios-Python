user = input('Nome do usuario? ')
password = input('Senha do usuario? ')
data_nascimentos = input('Sua data de nascimento? ')
bicho_extimacao = input('Qual nome do seu bicho de estimação? ')

caracter_qtde = len(password)

if user == password or user == data_nascimentos or user == bicho_extimacao:
	print(' Seu usuario não foi aceito, Tente novamente.' )

elif  caracter_qtde < 8 :
	print(' Seu usuario não foi aceito. Tente uma senha maior que 8 caracteres.' )

else:
	print('Usuario aceito')

	