#Prova prática dia 29/06 tipo A (Questões 01 e 02)
#Definição da função - questão 02
def somaIndicesVogais(texto):
    soma = 0
    for i in range(len(texto)):
        if texto[i] == 'a' or texto[i] == 'e' or texto[i] == 'i' or texto[i] == 'o' or texto[i] == 'u':
            soma += i #somando o índice da vogal

    return soma

#Main
s = input("Texto: ")
print( somaIndicesVogais(s) ) #chamada da função
