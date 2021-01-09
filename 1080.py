i = 1
maior = 0
pos = 0

while i <= 100:
  num = int(input())
  if num > maior:
    maior = num
    pos = i
  i += 1

print('%d\n%d' % (maior, pos))
