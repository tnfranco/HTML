# coding: iso-8859-1 -*-

indice = float(input("Informe o indice de poluiçao: "))

if indice >= 0.3 and indice < 0.4:
    print("Atenção: Industrias do grupo1 devem suspender as atividades")
elif indice >= 0.4 and indice <0.5:
    print("Atenção: Industrias do grupo1 e grupo2 devem suspender as atividades")
elif indice > 0.5:
    print("Atenção: Todos os grupos devem suspender as atividades")
