"""Dois números primos gémeos são dois nº primos que distam em 
2 unidades um do outro

p.ex:
3 e 5
5 e 7
Fazer um programa que lê dois nº inteiros positivos do
utilizador e diz se são primos e primos gémeos"""

import utils
import primo

#ler dois nº inteiros positivos
n1=utils.ler_numero_inteiro("Introduza um valor inteiro:")
n2=utils.ler_numero_inteiro("Introduza um valor inteiro:")

#testar se são primos
if primo.Primo(n1) and primo.Primo(n2):
    #calcular a diferença
    diferenca = n1 - n2
    if abs(diferenca) == 2:
        print(f"Os valores {n1} e {n2} são primos gémeos")
    else:
        print(f"Os valores {n1} e {n2} são primos gémeos")
else:
    if primo.Primo(n2):
        print(f"O valor {n2} é primo")
    elif primo.Primo(n2):
        print(f"O valor {n2} é primo")
    else:
        print("Nenhum dos valores é primo")

    
