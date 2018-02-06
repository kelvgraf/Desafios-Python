turno = input('Qual turno você estuda? Digite  M-matutino ou V-Vespertino ou N- Noturno:  ')

resposta = turno


if resposta == 'M':
	print(' Bom dia!' )

elif  resposta == 'V' :
	print(' Boa tarde!' )

elif  resposta == 'N' :
	print(' Boa noite!' )

else:
	print('Valor invalido!')