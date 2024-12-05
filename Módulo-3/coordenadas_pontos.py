import utils
def coordenadas():
    """Esta Função mostra onde se localiza um certo ponto"""
    x=utils.ler_numero_inteiro("Introduza o valor de x: ")
    y=utils.ler_numero_inteiro("Introduza o valor de y: ")
    if x ==0 or y ==0:
        print("Está no ponto zero")
    elif (x==0 and y>1) or (y==0 and x>1):
        print("Está no eixo")
    elif x>=1 and y>=1:
        print("Está no 1º quadrante")
    elif x<1 and y>=1:
        print("Está no 2º quadrante")
    elif x<1 and y<1:
        print("Está no 3º quadrante")
    elif x>=1 and y<1:
        print("Está no 4º quadrante")

coordenadas()
    
    
    