'''Crie um prograama que receba a idade e o nome de uma pessoal e verifique se ela pode votar.

entrada:
input

saida:
nome tem idade e pode votar.
'''



nome= input("Seu nome? " )
idade= int(input("Sua idade? " ))

if idade > 18:
	print(nome + ' tem' + str(idade) + ' anos e pode votar' )

elif idade >= 16:
	print(nome + ' tem' + str(idade) + ' anos é opcional votar' )

else:
	print(nome  + ' tem ' + str(idade) + ' anos e não pode votar')