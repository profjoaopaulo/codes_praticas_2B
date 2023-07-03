#Prova prática dia 29/06 tipo C (Questões 01 e 02)
#Definição da função - questão 02
def qtEspeciais(texto):
    qt = 0
    for i in texto:
        if not i.isalnum():
            qt += 1
        
    return qt

#Main
s = input("Texto: ")
print(qtEspeciais(s))
