limite = int(input())

for i in range(limite):
  digitos = input()
  list(map(str, digitos))
  a = digitos[0]
  b = digitos[1]
  c = digitos[2]
  a = int(a)
  b = str(b)
  c = int(c)

  if a == c:
   print('%d' % (a * c))
  elif b.isupper():
   print('%d' % (c - a))
  elif b.islower():
    print('%d' % (a + c))
