#1. class defination
class P1():
    #1. property/variable
    n1=10
    #2. constructor/esp.function
    #3. function/method
    pass
class P2():
    #1. property/variable
    n2=20
    #2. constructor/esp.function
    #3. function/method
    pass
class B(P1,P2):
    pass

#2. create class external object
c1=B()
print(c1.n1 + c1.n2)
