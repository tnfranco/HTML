maior = 0

n = int(input("Informe um numero: "))
while n != 0:
    if n > maior:
        maior = n
        n = int(input("Informe um numero: "))
    print("O maior numero é {0}".format(maior))
