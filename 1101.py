M = 0
M = int(M)
N = 0
N = int(N)
i = 0
boolean = True

while boolean:
  numeros = input().split() # Não sei como converter para int aqui dentro!
  num1, num2, = numeros
  num1 = int(num1)
  num2 = int(num2)
  if (num1 <= 0 or num2 <= 0):
    break
  if num1 > num2:
    M = num1
  if num2 > num1:
    M = num2
  if num2 < num1:
    N = num2
  if num1 < num2:
    N = num1
  
  if M > N:
    i = M
    M = N
    N = i

  SOMA = 0 # Aqui reseta a soma anterior
  
  while M <= N:
    #print('%d ', end = '' % (M))
    print(M, end = ' ')
    SOMA += M
    M += 1
  
  print('Sum=%d' % (SOMA))
