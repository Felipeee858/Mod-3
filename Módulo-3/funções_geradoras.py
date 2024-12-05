"""for i in range(10):
    print(i)
    i=0"""



"""def FunçaoA():
    x=0
    while x<10:
        x=x+1
        return x

print(FunçaoA())"""

def FunçaoB():
    x=0
    while x<10:
        x=x+1
        yield x #devolve o valor e mantém o estado
for i in FunçaoB():
    print(i)


