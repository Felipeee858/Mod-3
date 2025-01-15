"""Programa para fazer uma calculadora com as 4 operações"""
import time
def menu():
    op=1
    while op!=0:
        print("1.Soma \n2.Subtraçao \n3.Multiplicação \n4.Divisão \n5 Tudo \n6.Terminar ")
        op=int(input("Introduza a sua opção: "))
        if op==6:
            break
        n1=int(input("Introduza o número: "))
        n2=int(input("Introduza o número: "))
        if op==1:
            print("Resultado: ",Soma(n1,n2))
            time.sleep(3)
        elif op ==2:
            print("Resultado: ",Subtração(n1,n2))
            time.sleep(3)
        elif op ==3:
            print("Resultado: ",Multiplicação(n1,n2))
            time.sleep(3)
        elif op==4:
            print("Resultado: ",Divisão(n1,n2))
            time.sleep(3)
        elif op ==5:
            Tudo(n1,n2)
            time.sleep(3)
    print("Fim do Programa")
    
    

def Soma(n1,n2):
    Soma=n1+n2
    return Soma
def Subtração(n1,n2):
    Subtração=n1-n2
    return Subtração
def Multiplicação(n1,n2):
    Multiplicação=n1*n2
    return Multiplicação
def Divisão(n1,n2):
    Divisão=n1/n2
    return Divisão
def Tudo(n1,n2):
    Soma=n1+n2
    Subtração=n1-n2
    Multiplicação=n1*n2
    Divisão=n1/n2
    Total=Soma+Subtração+Multiplicação+Divisão
    print("Resultado Soma: ",Soma,"\nResultado Subtração: ",Subtração,"\nResultado Multiplicação: ",Multiplicação,"\nResultado Divisão: ",Divisão,"\nResultado Soma Total: ",Total)
    


menu()