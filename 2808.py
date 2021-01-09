def desenv(lin, col):
  if (col == 1 and lin == 2) or (col == 2 and lin == 1):
    result = 'VALIDO'
    return result
  else:
    result = 'INVALIDO'
    return result

def principal():
  i, j = input().split()

  lin = abs(ord(i[0]) - ord(j[0]))
  col = abs(int(i[1]) - int(j[1]))

  res = desenv(lin, col)

  print('%s' % (res))

principal()
