def tradutor(entr_codigo):

  morse = {'=.===' : 'a', '===.=.=.=' : 'b', '===.=.===.=' : 'c', '===.=.=' : 'd', '=' : 'e', '=.=.===.=' : 'f', '===.===.=' : 'g', '=.=.=.=' : 'h', '=.=' : 'i', '=.===.===.===' : 'j', '===.=.===' : 'k', '=.===.=.=' : 'l', '===.===' : 'm', '===.=' : 'n', '===.===.===' : 'o', '=.===.===.=' : 'p', '===.===.=.===' : 'q', '=.===.=' : 'r', '=.=.=' : 's', '===' : 't', '=.=.===' : 'u',  '=.=.=.===' : 'v', '=.===.===' : 'w', '===.=.=.===' : 'x', '===.=.===.===' : 'y', '===.===.=.=' : 'z'}

  for entrada in range(len(entr_codigo)):
    translate = entr_codigo[entrada]
    translate = translate.split('...')

    for i in range(len(translate)):
      print(morse[translate[i]], end = '')
  
    if entrada != len(entr_codigo) - 1:
      print(end = ' ')

  print()

def main():
  limite = int(input())
  
  for _ in range(limite):
   entr_codigo = input()
   entr_codigo = entr_codigo.split('.......')
   tradutor(entr_codigo)

main()
