"""Uma função que recebe uma palavra e devolve a mesma palavra convertida na lingua dos P
Alguns exemplos:
    Casa  -> Capasapa
    Bola  -> Bopolapa
    Olá   -> Opolápá
    Muito -> Muipuitopo
"""


def E_Vogal(letra):
    """Função que devolve true/false se letra é vogal/consoante"""
    vogais="aeiouáàãéèêíùóòôõúù"
    if letra.lower() in vogais:
        return True
    return False


def ConverteSilaba(silaba):
    """Função que recebe uma silaba e junta a mesma siliba na lingua dos P
    P.E.: Ca-> Capa
          Mui-> Muipui
          O -> Opo
    """
    if E_Vogal(silaba[0]):
        silaba= silaba + "p" + silaba.lower()
    else:
        temp= "p"
        for i in range(1,len(silaba)):
            temp=temp+silaba[i]
        silaba = silaba + temp
        return silaba


def Converte(palavra:str) -> str:
    """Função que converte uma palavra na lingua dos P"""
