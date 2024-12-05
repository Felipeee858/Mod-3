"""Para cada letra do alfabeto portugues, indique o número de vezes que aparece na frase.
Todos os caracteres que não pertencerem ao alfabeto portugues não devem ser contabilizados"""

"""print(ord("a"))
print(chr(97))"""

def ContarLetra(letra,frase):
    """Função para contar quantas vezes a letra aparece na frase"""
    contar=0
    for l in frase:
        if letra ==l:
            contar=contar+1
    return contar

def ContarFrequencia(frase):
    """Função que mostra o nº de vezes que cada letra do alfabeto aparece na frase"""
    #percorrer o alfabeto
    for i in range(97,123):# 97=a e 122=z
        #chamar função ContarLetra
        contar=ContarLetra(chr(i),frase)
        #mostrar o que a função devolveu
        print(f"{chr(i)} - {contar}")

frase=input("Introduza uma frase: ")
ContarFrequencia(frase)
