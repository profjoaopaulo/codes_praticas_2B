#Prova prática dia 29/06 tipo D (Questões 01 e 02)
#Definição da função - questão 02
def firstLastUpper( texto ):
    return (texto[0] + texto[len(texto)-1]).upper()

#Main
s = input("Texto: ")
print(firstLastUpper(s))
