numero_1 = int(input('Primeiro numero A: '))
numero_2 = int(input('Segundo numero B: '))
numero_3 = int(input('Terceiro numero C: '))

decrescente = sorted((numero_1, numero_2, numero_3), key = int,  reverse = True)

print('A ordem decrescente é, ' + str(decrescente))
