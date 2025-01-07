def Primo(n) -> bool:
    """esta função indica se o numero é primo
    true = primo
    false = não é primo"""
    primo = True

    for n in range(2,n):
        if n % n == 0:
            primo = False
            break
    
    if primo == True:
        return(primo)
    else:
        return(primo)
    
n=int(input("Introduza"))
print(Primo(n))


"""
def Primo(n) - >bool:
    primo =True
    if n %
"""