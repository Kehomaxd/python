
def Decorators(f):  #function 

    def Sum(*args, **kwargs):  # (a, b)
        r = f(*args, **kwargs)  # (a, b)
        r += 2
        return r
    return Sum

@Decorators
def multiply(a,b): 
    return a*b

def multiply2(a,b): 
    return a*b

# print(multiply2(1,2))
print(multiply(1,3)) 