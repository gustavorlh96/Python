dias = int(input(''))

anos = int(dias / 365)
dias = dias % 365
mes = int(dias / 30)
dias = dias % 30

print('%d ano(s)' % (anos))
print('%d mes(es)' % (mes))
print('%d dia(s)' % (dias))
