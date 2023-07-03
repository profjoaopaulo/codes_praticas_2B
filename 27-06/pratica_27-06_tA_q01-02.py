#Prova prática dia 27/06 tipo A (Questões 01 e 02)
#Definição da função - questão 02
def modificaTexto(texto):
    texto = list(texto) #transformando a string em lista - assim permite modificar cada elemento
    for i in range(len(texto)):
        if i % 2 == 1:
            texto[i] = texto[i].upper()

        if texto[i].isnumeric():
            texto[i] = '%'

    return "".join(texto) #transforma a lista de volta em string

#Main
s = input("Digite o texto alfanumérico: ")
print( modificaTexto(s) )
