i = 1
media = 0
quantpos = 0
valpos = 0

while i <= 6:
  valdig = float(input())
  if (valdig > 0):
    valpos = valpos + valdig
    quantpos += 1
  i += 1

media = valpos / quantpos

print('%d valores positivos\n%.1f' % (quantpos, media))
