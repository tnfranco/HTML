vetor1 = []
vetor2 =[]
soma = []
for n in range(0, 10):
    num1 = int(input("Digite o Valor para o primeiro Vetor: "))
    vetor1.append(num1)
    num2 = int(input("Digite o valor para o segundo Vetor: "))
    vetor2.append(num2)
    soma.append(num1 + num2)
for n in soma:
    print(n)
