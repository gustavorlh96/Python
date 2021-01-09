def cachorro(quantidade):
  final = quantidade * 4.00
  print('Total: R$ %.2f' % (final))


def xissalada(quantidade):
  final = quantidade * 4.50
  print('Total: R$ %.2f' % (final))

def xisbacon(quantidade):
  final = quantidade * 5.00
  print('Total: R$ %.2f' % (final))

def torrada(quantidade):
  final = quantidade * 2.00
  print('Total: R$ %.2f' % (final))

def refri(quantidade):
  final = quantidade * 1.50
  print('Total: R$ %.2f' % (final))

def main():
  escolha, quantidade = map(int, input().split())

  if escolha == 1:
    cachorro(quantidade)
  if escolha == 2:
    xissalada(quantidade)
  if escolha == 3:
    xisbacon(quantidade)
  if escolha == 4:
    torrada(quantidade)
  if escolha == 5:
    refri(quantidade)

main()
