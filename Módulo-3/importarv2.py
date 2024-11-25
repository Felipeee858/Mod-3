#Programa ler as notas de 3 alunos e calcular a média
from funções import media_D
nota1=int(input("Introduza uma nota: "))
nota2=int(input("Introduza uma nota: "))
nota3=int(input("Introduza uma nota: "))

media = media_D(nota1,nota2,nota3)

print(media)