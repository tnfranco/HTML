# coding: iso-8859-1 -*-
vetor = []
MaiorQue50 = False
total = 0
for n in range (0, 10):
    num = int(input("Informe {0} valor para o vetor ".format(n+1)))
    vetor.append(num)
for n in vetor:
    if n > 50:
        total = total + num
        print("O numero {0} esta na posicao {1} do vetor".format(n, vetor.index(n)))
        MaiorQue50 = True
if MaiorQue50 == False:
    print("Não existem valores maiores que 50")
