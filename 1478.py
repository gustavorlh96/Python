def imprime_matriz(N):
  for lin in range(1, N + 1):
    for col in range(1, N + 1):
      v = col - lin + 1
      if v <= 0:
        v -= 2
        v = abs(v)
      if col > 1 and col <= N:
        print(' ', end = '')
      print('%3d' % v, end = '')
    print('')

  print('')

while True:
  N = int(input())
  if N == 0:
   break
  imprime_matriz(N)
