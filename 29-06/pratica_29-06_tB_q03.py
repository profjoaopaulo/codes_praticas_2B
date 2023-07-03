#Prova prática dia 29/06 tipo B (Questão 03)
def somaMenores10(listaNumeros):
    soma = 0
    for i in listaNumeros:
        if i < 10:
            soma += i

    return soma

#Main
q = int(input("Qts? "))
numeros = []
for i in range(q):
    numeros.append(int(input("Number: ")))

print(somaMenores10(numeros))
