limite = int(input())

for i in range(limite):
  PA, PB, G1, G2, = map(float, input().split())

  PA = int(PA)
  PB = int(PB)
  ano = 0

  while PA <= PB:
    PA = int(PA * (1 + G1 / 100)) # Converter na mesma linha facilita o arrendondamento
    PB = int(PB * (1 + G2 / 100))

    ano += 1

    if ano > 100:
     print('Mais de 1 seculo.')
     break
  
  if ano <= 100:
    print('%d anos.' % (ano))
