"""
Programa para validar um expressão matemática quanto aos ()
"""
#Pedir a expressão ao utilizador
expressao = input("Introduza uma função matemática: ")
#fazer a validação com uma função
def Validar(expressao):
    """
    Função que recebe uma expressão matemática para validar os ()
    A função devolve False se a expressão tiver erros de outra forma devolve True
    """
    for l in expressao:
        if l == "(":
            contar=contar+1
        if l == ")":
            contar=contar-1
        if contar <0:
            return False
    if contar == 0:
        return True
    else:
        return False
#Chamar a função
resultado= Validar(expressao)

#indicar ao utilizador se a expressão é ou não válida
if resultado== False:
    print("A expressão não é válida")
else:
    print("A expressão válida")
















#Minha forma de resolver
"""def Função():
    texto=input("Introduza a expressão: ")
    contar_1=0
    contar_2=0
    contar_3=0
    contar_4=0
    for i in texto:
        if i == "(":
            contar_1=contar_1+1
        
        if i == ")":
            contar_2=contar_2+1
            if contar_1==0:
                break
    

    if contar_1 == contar_2:
        print(True)
    else:
        print(False)

"Função()"




def Função2():
    texto=input("Introduza a expressão: ")
    contar=0
    for i in texto:
        if i =="(":
            contar=contar+1
        if i ==")":
            contar=contar-1
        if contar < 0:
            break

    if contar !=0:
        print(False)
    else:
        print(True)

    
    
Função2()
"""
