# coding: iso-8859-1 -*-

ValorHora = 10.00
ValorHE = 20.00
e = 0

c = int(input("Informe o codigo: "))
n = float(input("Informe o numero de horas trabalhadas: "))

if n > 50:
   e = (n - 50) * ValorHE #20.00
   salario = (50 * ValorHora) + e #10.00
   print("Salario total R$ {0:.2f}".format(salario))
   print("Salario excedente R$ {0:.2f}1".format(e))
else:
    salario = (n * ValorHora) #10.00
    print("Salario total R$ {0:.2f}".format(salario))
    print("Salario excedente R$ {0:.2f}".format(e))
   
