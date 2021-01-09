def dist_Pontos():
  Distancia = (((x2 - x1) ** 2) + (y2 - y1) ** 2) ** (1/2)
  return Distancia

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

res = dist_Pontos()
print('%.4f' % (res))
