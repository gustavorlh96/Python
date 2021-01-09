i = 0
alcool = 0
gasosa = 0
diesel = 0

while i != 4:
  i = int(input())
  if i == 1:
    alcool += 1
  if i == 2:
    gasosa += 1
  if i == 3:
    diesel += 1

print('MUITO OBRIGADO\nAlcool: %d\nGasolina: %d\nDiesel: %d' % (alcool, gasosa, diesel))
