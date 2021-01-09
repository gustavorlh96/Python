quant = int(input())
i = 1
coelhos = 0
ratos = 0
sapos = 0

while i <= quant:
  cobaia = input().split()
  num, anim, = cobaia
  if anim == 'C':
    coelhos = coelhos + int(num)
  if anim == 'R':
    ratos = ratos + int(num)
  if anim == 'S':
    sapos = sapos + int(num)
  i += 1 

total = coelhos + ratos + sapos
pc_coelhos = (coelhos / total) * 100
pc_ratos = (ratos / total) * 100
pc_sapos = (sapos / total) * 100

print('Total: %d cobaias' % (total))
print('Total de coelhos: %d' % (coelhos))
print('Total de ratos: %d' % (ratos))
print('Total de sapos: %d' % (sapos))
print('Percentual de coelhos: %.2f %%' % (pc_coelhos))
print('Percentual de ratos: %.2f %%' % (pc_ratos))
print('Percentual de sapos: %.2f %%' % (pc_sapos))
# tentei printar na mesma linha, mas sempre acontecia algum bug de sintaxe
