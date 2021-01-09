lista = []

for i in range(0, 100):
  num = float(input())
  lista.append(num)

  if num <= 10:
   print('A[%d] = %.1f' % (i, num))
