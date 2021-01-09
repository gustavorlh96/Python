limite = int(input())

for i in range(0, limite):
  palavra = input()
  desloc = int(input())
  descod = ''

  for j in palavra:
    pos = ord(j) - desloc

    if pos < 65:
      descod += chr(91 - (65 - pos))

    else:
      descod += chr(ord(j) - desloc)

  print('%s' % (descod))
