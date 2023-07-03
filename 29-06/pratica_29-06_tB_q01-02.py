#Prova prática dia 29/06 tipo B (Questões 01 e 02)
#Definição da função - questão 02
def qtVogais(texto):
    qt = 0
    for i in texto:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            qt += 1 #contando as vogais

    return qt

#Main
s = input("Texto: ")
print( qtVogais(s) )
