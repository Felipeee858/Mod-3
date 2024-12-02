def ler_numero_inteiro()->int:
    """Função que lè do utilizador de um nºinteiro.Afunção garante que o valor inserindo é um valor válido"""
    while True:
        dados = input("Introduza um valor inteiro: ")
        #verificar se existe um - no inicio da str(valor )
        if dados[0]=="-":
            testar = dados.replace("-","")
        else:
            testar=dados
        if testar.isdigit():
            return int(dados)
        print("Erro: o valor inserio não é válido.")

