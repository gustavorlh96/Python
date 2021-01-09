def formula():
  DIFERENCA = (A * B - C * D)
  return DIFERENCA

# A, B, C, D = map(int, input().split()) // Se fosse aceito pelo exercício.
A = int(input())
B = int(input())
C = int(input())
D = int(input())

res = formula()
print('DIFERENCA = %d' % (res))
