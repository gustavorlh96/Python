quant = int(input())
i = 1

while i <= quant:
  SOMA = 0
  aux = 1
  num = 0
  num = int(input())

  while aux < num:
    if (num % aux) == 0:
      SOMA += aux 
    aux += 1
  
  if SOMA == num:
    print('%d eh perfeito' % (num))
    i += 1
  else:
    i += 1
    print('%d nao eh perfeito' % (num))
