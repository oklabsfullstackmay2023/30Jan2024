#1. class deifnation
class Vehicle():
    #1. property/variable
    speed=""
    color=''
    noofwheels=''
    #2. constructor/esp.function
    #3. function/method
    pass
 
class Motorcycle(Vehicle):
    #1. property/variable
    #2.constructor/esp.function
    def __init__(self,s,c,n):
        self.speed=s
        self.color=c
        self.noofwheels=n
     #3. function/method   



class Car(Vehicle):
    #1. property/variable
    #2.  constructor/esp.function
    def __init__(self,s,c,n):
        self.speed=s
        self.color=c
        self.noofwheels=n
     #3. function/method
    

#2. create class etxernal object
ninjah2r=Motorcycle(440,'green',2)
print(f'The bike  speed is {ninjah2r.speed} kmph')
print(f'The bike color is {ninjah2r.color}')
print(f'The no of wheels of the bike is  {ninjah2r.noofwheels}')

porsche911turbo=Car(205,'red',4)
print(f'The Porsche 911 Turbo speed is {porsche911turbo.speed} kmph')
print(f'The Porsche 911 Turbo color is {porsche911turbo.color} ')
print(f'The Porsche 911 Turbo no of wheels are  {porsche911turbo.noofwheels} ')


