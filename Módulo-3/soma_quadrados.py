"""Uma função com o nome soma_quadrados que recebe um nº inteiro positivo,n,e
devolve a soma dos quadrados de todos os nºs inteiros positivos até n"""


def soma_quadrados(nºinteiro):
    valor=0
    for i in range(1,nºinteiro+1):
        valor= valor + i**2
    return valor


def main():
    nºinteiro=int(input("Introduza o nº: "))
    soma_quadrados(nºinteiro)
    print(soma_quadrados(nºinteiro))
if __name__=="__main__":
    main()