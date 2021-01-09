def volume_Esfera():
  formula = (4.0/3) * 3.14159 * (raio ** 3)
  return formula

raio = float(input())

res = volume_Esfera()
print('VOLUME = %.3f' % (res))
