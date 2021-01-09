A,B,C = input().split()
A = float(A)
B = float(B)
C = float(C)

if A + B > C and B + C > A and A + C > B:
  perimetro = A + B + C
  print('Perimetro = %.1f' % (perimetro))
else:
  area = 0.5 * (A + B) * C
  print('Area = %.1f' % (area))
