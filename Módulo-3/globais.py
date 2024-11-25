#variaveis globais
g_resultado= 0 

def Soma(x,y):
    global g_resultado
    g_resultado=x+y #está a criar uma variável local

Soma(10,5)
print(g_resultado)