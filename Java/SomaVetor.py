# coding: iso-8859-1 -*-
vetor = []
soma = 0
for n in range(0, 20):
    num = int(input("Infome {0}/20 valor para o vetor: ".format(n+1)))
    vetor.append(num)
    soma = soma + num
print("A soma do vetor é {0}".format(soma))
