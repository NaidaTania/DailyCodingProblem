#Given
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


#Can be used both ways
def innerCar(a,b):
    return a

def innerCdr(a,b):
    return b

#how to call normal closure
# uwu = cons2(2,3)
# print(uwu())

#Directly 
uwu = cons(2,3)
print("the other way around car:",uwu(innerCar))
print("the other way around car:",uwu(innerCdr))


def car(pair):
    return pair(innerCar)

def cdr(pair):
    return pair(innerCdr)

#Indirectly according to problem statement
assert car(cons(3, 4)) == 3
assert cdr(cons(3, 4)) == 4