def Validar(expressao):
    """"""
    abriu=""
    for l in expressao:
        if l == "(" or l == "[":
            abriu= abriu + l
        if l == ")" or l =="]":
            if abriu== "":
                return False
            ultimo = abriu[len(abriu)-1]
            if (ultimo == "("and l ==")") or (ultimo=="["and l =="]"):
                temp=abriu
                #limpar a string para copiar todos os carateres menos o último 
                abriu=""
                for i in range(len(temp)-1):
                    abriu = abriu + temp[i]
            else:
                return False
    if abriu=="":
        return True
    return False
Validar()