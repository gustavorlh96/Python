def media():
  if (0 <= a <= 10) and (0 <= b <= 10):
   MEDIA = ((a * 3.5) + (b * 7.5)) / 11
   return MEDIA

a = float(input())
b = float(input())

res = media()
print('MEDIA = %.5f' % (res))
