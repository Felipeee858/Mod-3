from termcolor import colored
def Função_cor():
    pergunta=input("Introduza a Frase que deseja passar a cor verde,azul e vermelho")
    print(colored(pergunta,"red"))
    print(colored(pergunta,"green"))
    print(colored(pergunta,"blue"))

Função_cor()