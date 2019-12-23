# coding: iso-8859-1 -*-
maior = -999
menor = 999
soma = 0
for n in range (1, 5):
     valor = int(input("Digite um numero"))
     if valor > 0:
        if valor > maior:
             maior = valor
        if valor < menor:
             menor = valor
        soma = soma + valor
     else:
        valor = int(input("Digite um numero: "))
media = soma/10
print("Maior é {0}".format(maior))
print("Menor é {0}".format(menor))
print("Média é {0}".format(media))
