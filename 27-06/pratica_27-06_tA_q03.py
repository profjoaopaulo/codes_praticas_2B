#Prova prática dia 27/06 tipo A (Questão 03)
def somaPares(listaNumeros):
    soma = 0
    for i in listaNumeros:
        if i % 2 == 0:
            soma += i

    return soma

#Main
t = int(input("Qts números? "))
numeros = []
for i in range(t):
    numeros.append( int(input("Número: ")) )

print( somaPares(numeros) )
