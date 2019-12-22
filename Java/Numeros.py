# coding: iso-8859-1 -*-
maior = 0
n = int(input("Informe um numero: "))
while n != 0:  
     if n > maior:
        maior = n
     n = int(input("Informe um numero: "))
print("O numero maior é {0}".format(maior))
