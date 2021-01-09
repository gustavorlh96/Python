quant = int(input())
i = 1

while i <= quant:
  SOMA = 0
  aux = 1
  num = 0
  num = int(input())

  while aux <= num:
    if (num % aux) == 0:
      SOMA += 1
    aux += 1
  
  if SOMA > 2:
    print('%d nao eh primo' % (num))
    i += 1
  else:
    i += 1
    print('%d eh primo' % (num))
