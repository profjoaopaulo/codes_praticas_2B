#Prova prática dia 29/06 tipo D (Questão 03)
def maiorPar(listaNumeros):
    maior = -1
    for i in listaNumeros:
        if i % 2 == 0 and i > maior:
            maior = i
        
    return maior

#Main
q = int(input("Qts? "))
numeros = []
for i in range(q):
    numeros.append(int(input("Number: ")))

print(maiorPar(numeros))
