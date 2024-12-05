x=int(input("Introduza a coordenada x do ponto: "))
y= int(input("Introduza a coordenada y do ponto: "))
#testar se o ponto está em cima de algum eixo
def quadrantes(x,y):
    if x==0 or y==0:
        print("O ponto está sobre os eixos")
    else:
        if x>0:
            if y>0:
                return "1º Quadrante"
            else:
                return ("4º Quadrante")
        else:
                if y>0:
                    return ("2º Quadrante")
                else: 
                    return("3º Quadrante")

assert quadrantes(5,5)== "1º Quadrante","Erro: a função não deu 1º Quadrante" #testa a função ter que dar 1º Quadrante caso não escreve "Erro: a função não deu 1º Quadrante"
assert quadrantes(5,5)== "2º Quadrante","Erro: a função não deu 2º Quadrante"
assert quadrantes(5,5)== "3º Quadrante","Erro: a função não deu 3º Quadrante"
assert quadrantes(5,5)== "4º Quadrante","Erro: a função não deu 4º Quadrante"

print("pass")