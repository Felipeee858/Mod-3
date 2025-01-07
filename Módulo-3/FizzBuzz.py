
def fizzBuzz(upTo):
    for i in range(1,upTo+1):
        if i % 3 ==0 and i % 5 == 0:
            print("fizzBuzzz",end=" ")
        
        elif i % 3 ==0:
            print("Fizz",end=" ")
    
        elif i % 5 ==0:
            print("Buzz",end=" ")
        else:
            print(i,end=" ")
        

def fizzBuzz_v2(upTo):
    for i in range(1,upTo+1):
        if i % 15 ==0:
            print("fizzBuzzz",end=" ")
        
        elif i % 3 ==0:
            print("Fizz",end=" ")
    
        elif i % 5 ==0:
            print("Buzz",end=" ")
        else:
            print(i,end=" ")

def fizzBuzz_v3(upTo):
    for n in range(1,upTo+1):
        print("FizzBuzz" if n % 15==0 else "Fizz" if n%3==0 else "Buzz" if n%5==0 else str(n),end=" ")

        



nº=int(input("Introduza o nº: "))
fizzBuzz(nº)
fizzBuzz_v2(nº)
fizzBuzz_v3(nº)
