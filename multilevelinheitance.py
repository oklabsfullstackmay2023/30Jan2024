#1. class defination
class A():
    #1. property/variable
    n1=10
    #2. constructor/esp.function
    #3. function/method
    pass
class B(A):
    #1. property/variable
    n2=20
    #2. constructor/esp.function
    #3. function/method
    pass
class C(B):
    #1. property/variable
    n3=30
    #2. constructor/esp.function
    #3. function/method
    pass

#2. create class external object
ceo1=C()
print(ceo1.n1 + ceo1.n2 + ceo1.n3)

