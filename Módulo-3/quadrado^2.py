"""
Elabora um programa que determine o quadrado de um número inteiro n. O número n deve ser pedido
ao utilizador e,através de uma função,devolver o seu quadrado"""


def quadrado(n):
    resultado=n**2
    return resultado

def main():
    n=int(input("Introduza o nº desejado: "))
    q= quadrado(n) #variavel para executar a função
    print(q)
    #ou
    #print(quadrado(n))


if __name__=="__main__":
    main()


