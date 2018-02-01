hrganha = int(input())
hrtrabalhada = int(input())


salariofull = hrganha * hrtrabalhada


ir = salariofull * 0.11
inss = salariofull * 0.08
sindicato = salariofull * 0.05
liquido = salariofull -(ir + inss + sindicato)


print('R$%.2f' % salariofull + 'Salario bruto')
print('R$%.2f' % ir + 'DEsconto IR')
print('R$%.2f' % inss + 'Desconto INSS')
print('R$%.2f' % sindicato + 'Sindicato')
print('R$%.2f' % liquido + ' Salario liquido')





