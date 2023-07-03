#Prova prática dia 27/06 tipo B (Questões 01 e 02)
#Definição da função - questão 02
def modificaTexto(texto):
    texto = list(texto) #transformando a string em lista - assim permite modificar cada elemento
    for i in range(len(texto)):
        if texto[i] == 'a' or texto[i] == 'e' or texto[i] == 'i' or texto[i] == 'o' or texto[i] == 'u':
            texto[i] = texto[i].upper()
        elif texto[i].isnumeric():
            texto[i] = ""

    return "".join(texto) #transforma a lista de volta em string

#Main
s = input("Digite o texto: ")
print( modificaTexto(s) )
