#1. class defination
class A():
    #1. property/variable
    n1=10
    #2. constructor/esp.function
    #3. function/method
    pass
class B(A):
    #1. property/variable
    n2=10
    #2. constructor/esp.function
    #3. function/method
    pass

#2. create class external object
b1=B()
print(b1.n1 + b1.n2)
