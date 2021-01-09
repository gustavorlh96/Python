def f_r():
  r = ((3 * x) ** 2) + y ** 2
  return r

limite = int(input())

for i in range(limite):
  def f_b():
   b = (2 * (x ** 2)) + (5 * y) ** 2
   return b

  def f_c():
   c = (-100 * x) + (y ** 3)
   return c

  x, y = map(int, input().split())

  final_r = f_r()
  final_b = f_b()
  final_c = f_c()

  if (final_r > final_b) and (final_r > final_c):
   print('Rafael ganhou')
  elif (final_b > final_r) and (final_b > final_c):
   print('Beto ganhou')
  else:
   print('Carlos ganhou')

  i += 1
