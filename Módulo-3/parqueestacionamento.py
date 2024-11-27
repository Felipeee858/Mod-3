"""
Um parque de estacionamento cobra aos clientes em blocos de 15 minutos.
Pretendemos um programa,que utiliza funções, para ler o custo de cada 15 minutos e a hora e
minutos de entrada do veiculo do cliente. O programa deve ler a hora e os minutos do computador para 
calcular qual o valor a pagar.
"""
import datetime

def Duração(hora:int,minutos:int)->int:
    """
    Função que calcula a duração do estacionamento em minutos com base nos valores do parâmetros e a hora atual
    """
    
    hora_Atuais=datetime.datetime.now().hour
    minutos_Atuais=datetime.datetime.now().minute
    nºhoras=hora_Atuais - hora
    nºminutos=minutos_Atuais-minutos
    if nºminutos<0:
        nºhoras=nºhoras-1
        nºminutos= 60 - minutos + minutos_Atuais
    duração_total_minutos= nºhoras * 60 + nºminutos
    return duração_total_minutos
    

def BlocosMinuto(minutos:int)->int:
    """
    Função que recebe a duração em minutos e devolve quantos blocos de 15 minutos existem
    """
    blocos=minutos//15
    if minutos%15 !=0:
        blocos+1
    return blocos



def Custo(blocos:int,preço_bloco:float)->float:
    """
    Função que calcula o custo do estacionamento com base na duração em blocos de 15 minutos e o preço
    de cada bloco
    """
    return blocos * preço_bloco




def main():
    #ler dados
    preço=int(input("Introduza o preço por cada 15 minutos: "))
    hora=int(input("Introduza as horas: "))
    minutos=int(input("Introduza os minutos: "))
    #calcular a duração em minutos
    duraçao_minutos=Duração(hora,minutos)
    blocos=BlocosMinuto(duraçao_minutos)
    #calcular o custo
    custo=Custo(blocos,preço)
    #mostrar resultado
    print("Estacionamento com duração de",duraçao_minutos," que corresponde a ",blocos,"de 15 minutos com o custo de",custo,"€")


if __name__=="__main__":
    main()

