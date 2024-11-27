"""
Função que,recebe como parâmetros de entrada as medidas dos dois catetos de um
triângulo retângulo, e devolva a medida da hipotenusa com 3 casa decimais
"""

import math 

def hip(c1,c2):
    hipotenusa=math.sqrt(c1**2+c2**2) #math.sqrt(x)) #raiz quadrada
    return(hipotenusa)



def main():
    c1=int(input("Introduza o valor do cateto: "))
    c2=int(input("Introduza o valor do cateto: "))
    hip(2,2)
    print(hip(2,2))
    
    pass

if __name__=="__main__":
    main()