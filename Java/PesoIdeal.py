# coding: iso-8859-1 -*-
altura = float(input("Informe a altura"))
sexo = (input("Informe o seu sexo m/f: "))

if sexo.lower() == 'm':
    PesoIdeal = (72.7 * altura) - 58
elif sexo.lower() == 'f':
    PesoIdeal = (62.1 * altura) - 44.7
else:
    PesoIdeal = 0 
    print("sexo nao reconhecido")
print("seu peso ideal é {0:.2f}".format(PesoIdeal))
