# coding: iso-8859-1 -*-

idade = int(input("Digite sua idade: "))

if idade >= 5 and idade <= 7:
    print("Infantil A")
elif idade >= 8 and idade <= 11:
    print("Infantil B")
elif idade >= 12 and idade <= 13:
    print("Juvenil")
elif idade > 14 and idade <=17:
    print("Adolescente")
elif idade > 18:
    print ("Adulto")
