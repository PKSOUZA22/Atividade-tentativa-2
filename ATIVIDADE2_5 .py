num = int(input("Digite um nÃºmero inteiro: "))

for i in range(num):
    potencia = 2 ** i
    if potencia > num:
        break
    print(potencia)