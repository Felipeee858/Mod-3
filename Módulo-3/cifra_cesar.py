"""
Implemente um programa que codifica ou descodifica uma mensagem com base nos alfabetos
fornecidos.
"""

original="abcdefghijklmnopqrstuvwxyz"
codigo="bcdefghijklmnopqrstuvwxyza"

def menu():
    """
    Função para ler a opção do utilizador e executar a função adequada: codificar ou
    descodificar"""
    
    pergunta=input("Deseja (C)odificar ou (D)escodificar")
    if pergunta == "C":
        codifica()
    elif pergunta=="D":
        descodifica()
    else:
        print("Erro")

        

def codifica(mensagem:str)->str:
    """
    Função que recebe uma mensagem e devolve a mesma codificada de acordo com os alfabetos
    fornecidos"""

    global original
    global codigo
    texto=""
    mensagem = mensagem.lower()
    for l in mensagem:
        if l not in original:
            #caso n encontre a letra no alfabeto deve manter a letra original
            texto=texto + l
        else:
            for p in range(len(original)):
                if l == original[p]:
                    texto=texto+codigo[p]
        
    return texto
   
def descodifica(mensagem_codificada:str)->str:
    """
    Função que recebe uma mensagem codificada e devolve a mesma descodificada de acordo com os
    alfabetos fornecidos"""

    global original
    global codigo
    texto=""
    mensagem = mensagem.lower()
    for l in mensagem:
        if l not in codigo:
            #caso n encontre a letra no alfabeto deve manter a letra original
            texto=texto + l
        else:
            for p in range(len(codigo)):
                if l == codigo[p]:
                    texto=texto+original[p]
    pass
def main():
    menu()

if __name__=="__main__":
    main()
    