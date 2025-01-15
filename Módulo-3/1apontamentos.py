
def Soma():
    """Função para ler e Somar dois números"""
    n1=int(input("Introduza o Número: "))
    n2=int(input("Introduza o Número: "))
    Soma=n1+n2
    return Soma
    """Quando utilizado o return ao invez de um print temo q guarda o valor em uma variável"""
#x=Soma()
#print(Soma)
#print(Soma())<-"Funciona pois ele avalia oq está dentro do print primeiro"


def Soma2(n1,n2):
    """Função para receber e Somar 2 nºs"""
    Soma=n1+n2
    print(Soma)


#Soma2(1,2) #ao invez de receber o argumento direto "1,2" poderia tambem com um input


"""Exercício 2: Escreva uma função chamada `e_par` que receba um número como parâmetro e
 retorne True se o número for par, e False caso contrário."""

def e_par(n):
    if n % 2 ==0:
        return True
    else:
        return False

"""print(e_par(0))"""




