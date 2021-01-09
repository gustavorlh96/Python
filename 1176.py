fibonacci = [0,1]

limite = int(input())
fibo0 = 0
fibo1 = 1

for i in range(60):
  SOMA = fibo0 + fibo1
  fibonacci.append(SOMA)
  fibo0 = fibo1
  fibo1 = SOMA

for i in range(1, limite + 1):
  Num = int(input())
  print('Fib(%d) = %d' % (Num, fibonacci[Num]))
