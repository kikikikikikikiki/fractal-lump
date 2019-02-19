def cons(a,b):
    def pair(f):
        return f(a,b)
    return pair

def car(a,b):
    return a

def cad(a,b):
    return b
print(cons(3,4)(cad))
