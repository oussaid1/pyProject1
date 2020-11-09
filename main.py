

def fist():
    n = int(input())
    for x in range(1, n):
        if x % 2 != 0:
            if x % 3 == 0 and x % 5 == 0:
                print('SoloLearn')
            elif x % 3 == 0:
                print('solo')
            elif x % 5 == 0:
                print('Learn')
            else:
                print(x)


class Juice:

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __add__(self, other):
        return Juice(str(self.name +' & '+ other.name),( self.capacity + other.capacity))

    def __str__(self):
        return (''+self.name +' ('+ str(self.capacity ) +'L)')

def makeJuice(fruit1,Qn1,fruit2,Qn2):
    a = Juice(fruit1, Qn1)
    b = Juice(fruit2,Qn2) 
    res=a+b
    print(res)
    return res

#makeJuice('Banana',1,'Avocado',1)
class Needs:
    def __init__(self, name, percentage,budget,left,consumed,items):
        self.name = name
        self.percentage=percentage
        self.budget=budget
        self.left=left
        self.consumed=consumed
        self.items=items
class Budget:
    def __init__(self, budget,date):
        self.budget=budget
        self.date=date


x=1200

def getBudget(item,perc):
    y=(x*perc)/100
    print(str(item )+ ': '+str(y))
  
getBudget('Shop',50)
print('Hello Python Am comming')

