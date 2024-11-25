def media_A():
    n1=int(input("Introduza o número: "))
    n2=int(input("Introduza o número: "))
    n3=int(input("Introduza o número: "))
    média=(n1+n2+n3)/3
    print(média)


def media_B(n4,n5,n6):
    média=(n4+n5+n6)/3
    print(média)



def media_C():
    n7=int(input("Introduza o número: "))
    n8=int(input("Introduza o número: "))
    n9=int(input("Introduza o número: "))
    média=(n7+n8+n9)/3
    return média

def media_D(n10,n11,n12):
    média=(n10+n11+n12)/3
    return média

media_D(10,34,5)
    
def main():
    #media_A()
    #media_B(5,5,5)
    #print(media_C())#chama a função e mostra o valor devolvido
    print(media_D(5,5,5)) #chama a função com os argumentos e mostra o valor devolvido
if __name__=="__main__":
    main()
    