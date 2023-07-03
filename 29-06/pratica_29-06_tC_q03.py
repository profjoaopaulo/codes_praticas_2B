#Prova prática dia 29/06 tipo C (Questão 03)
def menorImpar(listaNumeros):
    menor = 1000000
    for i in listaNumeros:
        if i % 2 == 1 and i < menor:
            menor = i
    
    if menor == 1000000:
        return -1
    
    return menor

#Main
q = int(input("Qts? "))
numeros = []
for i in range(q):
    numeros.append(int(input("Number: ")))

print(menorImpar(numeros))
