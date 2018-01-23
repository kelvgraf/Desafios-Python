precodog = int(input('Preço do Hotdog? \n'))

nameclient = input('Nome do cliente? \n')

quantidade = int(input('Quantos Hotdog'))

Valorpago = precodog * quantidade

print('O valor do seu lanche é R$' + str('%.2f' % Valorpago))