def NPerfeito(n):
    Soma=0
    for i in range(1,n):
        if n % i == 0:
            Soma=Soma+i
    if Soma==n:
        return True
    return False
    
def Main():
    n=int(input("Introduza o número:"))
    if NPerfeito(n)==True:
        print("Número perfeito")

    else:
        print("Número não perfeito")



if __name__=="__main__":
    Main()