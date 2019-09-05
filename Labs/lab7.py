#lab7
#Shaan Barkat
#Collab with Anthony Marsilio

def printPattern(x, y=0):
    if x > 0:
        printPattern(x//2, y)
        print(' '*y+'*'*x)
        printPattern(x//2, y + x//2)

def gcd(x, y):
    if x==0:
        return y
    elif y==0:
        return x
    elif x>=y:
        return gcd(x-y,y)
    elif y>=x:
        return gcd(x,y-x)

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab7TEST.py' ))

    
