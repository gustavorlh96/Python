i = 1
par = 0

while i <= 5:
  num = int(input())
  if num % 2 == 0:
    par += 1
  i += 1

print('%d valores pares' % (par))
