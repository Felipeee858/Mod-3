def Soma(x,y):
    t = x + y
    return t
x = Soma(10,5)
print(x)
print(Soma(5,10))
x=0 # este valor não será mudado
y=0 # este valor não será mudado
x=int(input(""))
y=int(input(""))
z=int(input(""))
t=Soma(x,Soma(y,z))
