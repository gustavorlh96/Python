def gasto_Combust():
  formula = (horas * velocidade) / 12
  return formula

horas = float(input())
velocidade = float(input())

res = gasto_Combust()
print('%.3f' % (res))
