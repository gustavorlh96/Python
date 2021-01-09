limite = int(input())
i = 1

while i <= limite:
  nome = str(input())
  GRAU = float(input())
  SOMA = 0
  SOMA = float(SOMA)
  M = -1
  M = float(M)
  N = 11
  N = float(N)
  Nota_Final = 0
  Nota_Final = float(Nota_Final)
  NOTAS = input().split()
  nota1, nota2, nota3, nota4, nota5, nota6, nota7, = NOTAS
  nota1 = float(nota1)
  nota2 = float(nota2)
  nota3 = float(nota3)
  nota4 = float(nota4)
  nota5 = float(nota5)
  nota6 = float(nota6)
  nota7 = float(nota7)

  if (nota1 > M):
    M = nota1
  if (nota2 > M):
    M = nota2
  if (nota3 > M):
    M = nota3
  if (nota4 > M):
    M = nota4
  if (nota5 > M):
    M = nota5
  if (nota6 > M):
    M = nota6
  if (nota7 > M):
    M = nota7
  if (nota1 < N):
    N = nota1
  if (nota2 < N):
    N = nota2
  if (nota3 < N):
    N = nota3
  if (nota4 < N):
    N = nota4
  if (nota5 < N):
    N = nota5
  if (nota6 < N):
    N = nota6
  if (nota7 < N):
    N = nota7

  SOMA = nota1 + nota2 + nota3 + nota4 + nota5 + nota6 + nota7 - M - N
  Nota_Final = SOMA * GRAU

  i += 1

  print('%s %.2f' % (nome, Nota_Final))
