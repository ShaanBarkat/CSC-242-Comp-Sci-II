#hw1
#Shaan Barkat, Collab with Anthony Marsilio and Marcus Lofton

class BankAccount:

    def __init__(self, c=0):
        self.bala = c
    def __repr__(self):
        return "BankAccount({})".format(self.bala)
    def set(self,setbala):
        self.bala=setbala
    def withdraw(self,amount):
        self.bala -= amount
    def deposit(self,amount):
        self.bala += amount
    def balance(self):
        return self.bala

def processAccount(x):
    file = open(x,"r")
    lineinfile = file.readlines()
    file.close()
    B = BankAccount()
    for line in lineinfile:
        line.strip()
        if 'w' in line.lower():
            z = line.split()
            B.withdraw(eval(z[1]))
        elif 'd' in line.lower():
            z = line.split()
            B.deposit(eval(z[1]))
        else:
            B.set(eval(line))
    return B



if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw1TEST.py'))

    

    
