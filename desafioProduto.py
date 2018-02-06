produto_1 = int(input('Primeiro produto A: '))
produto_2 = int(input('Segundo produto B: '))
produto_3 = int(input('Terceiro produto C: '))

valor_do_produto = min(produto_1, produto_2, produto_3)

print('O produto mais barato é, R$ ' + '%.2f' % float(valor_do_produto) )

