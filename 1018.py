num = int(input())

print('%d' % (num))

num100 = num // 100
num = num - num100 * 100
num50 = num // 50
num = num - num50 * 50
num20 = num // 20
num = num - num20 * 20
num10 = num // 10
num = num - num10 * 10
num5 = num // 5
num = num - num5 * 5
num2 = num // 2
num = num - num2 * 2
num1 = num // 1
num = num - num1 * 1

print('%d nota(s) de R$ 100,00\n%d nota(s) de R$ 50,00\n%d nota(s) de R$ 20,00\n%d nota(s) de R$ 10,00\n%d nota(s) de R$ 5,00\n%d nota(s) de R$ 2,00\n%d nota(s) de R$ 1,00' % (num100, num50, num20, num10, num5, num2, num1))
