A,B,C = input().split()
A = float(A)
B = float(B)
C = float(C)

if A == 0:
  print('Impossivel calcular')
else:
  D = (B ** 2) - (4 * A * C)

  if D < 0:
   print('Impossivel calcular')
  else:
   D = D ** (1/2)
   E = 2 * A

   R1 = (- B + D) / E
   R2 = (- B - D) / E
   
   print('R1 = %.5f\nR2 = %.5f' % (R1, R2))
