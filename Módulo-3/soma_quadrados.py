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

#OU

"""
import quadrado^2

def soma_quadrados(n:int) -> int:
    soma=0
    for i in range(1,n+1):
        q= quadrado.quadrado^2(i)
        soma=soma + q 
    return soma

assert soma_quadrados(3)==14,"Valor devolvido devia ser 14" #assert = testar a função e ve se funciona
assert soma_quadrados(5)==55,"Valor devolvido devia ser 55"
print("A função passou nos testes")

"""