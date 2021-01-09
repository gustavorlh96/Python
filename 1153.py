num = int(input())
fat = 1

while num >= 1:
  fat = fat * num
  num -= 1

print('%d' % (fat))
