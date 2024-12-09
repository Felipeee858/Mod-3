frase=input("Introduza a frase: ")
alfabeto="abcdefghijklmnopqrstuvwxyz"
for i in alfabeto:
    contar=0
    for l in frase:
        if i ==l:
            contar=contar+1