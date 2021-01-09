def roda_bateria(T):
  menor = 999
  for _ in range(T):
    tempo = float(input())
    if tempo < menor:
      menor = tempo
  return menor

def main():
  while True:
    try:
      T = int(input())
      menor = roda_bateria(T)
      print(menor)
    except EOFError:
      break


main()
