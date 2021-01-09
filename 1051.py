salario = float(input())

if salario > 0 and salario < 2000:
  print('Isento')
elif salario >= 2000.01 and salario <= 3000.00:
  sal_imp = salario - 2000
  imposto = sal_imp * 0.08
  imposto = float(imposto)
  print('R$ %.2f' % (imposto))
elif salario >= 3000.01 and salario <= 4500.00:
  sal_imp = salario - 3000
  imposto = sal_imp * 0.18 + 1000 * 0.08
  imposto = float(imposto)
  print('R$ %.2f' % (imposto))
else:
  sal_imp = salario - 4500
  imposto = sal_imp * 0.28 + 1000 * 0.08 + 1500 * 0.18
  imposto = float(imposto)
  print('R$ %.2f' % (imposto))
