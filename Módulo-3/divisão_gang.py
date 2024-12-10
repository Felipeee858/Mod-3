import math


def Valor_total():
    valor_total=float(input("Introduza quanto rendeu o Assalto: "))
    return valor_total
def Conta_Líder(valor_total):
    Líder=valor_total*50/100
    print(f"O Líder recebe {round(Líder,2)}€")
    return Líder
def Conta_Musculado(valor_total):
    Musculado=valor_total*20/100
    print(f"O Musculado recebe {round(Musculado,2)}€")
    return Musculado
def Conta_Motorista(valor_total):
    Motorista=valor_total*10/100
    print(f"O Motorista recebe {round(Motorista,2)}€")
    return Motorista
    
    
def Gasto_seguro_Líder(Líder):
        Líder_gasto=Líder*0.05
        if Líder_gasto >= 1000:
             Líder_gasto=1000
        meses=Líder/Líder_gasto
        meses=math.ceil(meses)
        print(f"O Líder pode gastar {round(Líder_gasto,2)}€")
        print(f"Os {Líder}€ sáo gasto em {meses} meses, gastando {Líder_gasto}€")
def Gasto_seguro_Musculado(Musculado):
        Musculado_gasto=Musculado*0.05
        if Musculado_gasto >= 1000:
             Musculado_gasto=1000
        meses=Musculado/Musculado_gasto
        meses=math.ceil(meses)
        print(f"O Musculado pode gastar {round(Musculado_gasto,2)}€")
        print(f"Os {Musculado}€ sáo gasto em {meses} meses, gastando {Musculado_gasto}€")
def Gasto_seguro_Motorista(Motorista):
        Motorista_gasto=Motorista*0.05
        if Motorista_gasto >= 1000:
            Motorista_gasto=1000
        meses=Motorista/Motorista_gasto
        meses=math.ceil(meses)
        print(f"O Motorista pode gastar {round(Motorista_gasto,2)}€")
        print(f"Os {Motorista}€ sáo gasto em {meses} meses, gastando {Motorista_gasto}€")
        

def main():
    valor_total=Valor_total()
    Líder=Conta_Líder(valor_total)
    Musculado=Conta_Musculado(valor_total)
    Motorista=Conta_Motorista(valor_total)
    Gasto_seguro_Líder(Líder)
    Gasto_seguro_Musculado(Musculado)
    Gasto_seguro_Motorista(Motorista)

    

if __name__=="__main__":
    main()

    