#Shaan Barkat
#Collab with Anthony Marsilio and Marcus Lofton
#hw2
class Pizza():
    def __init__(self,size = 'M',t2 = {}):
        self.size = size
        self.t2 = set(t2)
    def __repr__(self):
        return "Pizza('{}',{})".format(self.size,self.t2)
    def setSize(self,sizes):
        self.size = sizes
    def getSize(self):
        return self.size
    def addTopping(self,t1):
        if t1 not in self.t2:
            self.t2.add(t1)
    def removeTopping(self,t1):
        if t1 in self.t2:
            self.t2.remove(t1)
    def price(self):
        price = 0
        a = (len(self.t2))
        if self.size == 'S':
            price = 6.25
            price += .70*a
        elif self.size == 'M':
            price = 9.95
            price += 1.45*a
        elif self.size == 'L':
            price = 12.95
            price += 1.85*a
        return price
    def __eq__(self,other):
        return self.t2 == other.t2 and self.size == other.size
def orderPizza():
    K = Pizza()
    A = 0
    print('Welcome to Python Pizza!')
    K.setSize(input('What size pizza would you like (S,M,L): '))
    while A == 0:
        X = input('Type topping to add (or Enter to quit): ')
        if X != '':
            K.addTopping(X)
        else:
            A += 1
    print('Thanks for ordering!')
    print('Your pizza costs ${}'.format(K.price()))
    return K

if __name__=='__main__':
    import doctest
    print( doctest.testfile('hw2TEST.py') )

    
            
            
    
