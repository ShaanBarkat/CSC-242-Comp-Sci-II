#Shaan Barkat
#Lab9

def maximum(lst):
    a = []
    if type(lst) != list:
        return lst
    else:
        for i in lst:
            a.append(maximum(i))
        return max(a)




def printstack(n, a=0):
    if n==1:
        print(' '*(a)+'U '*(n))
    else:
        printstack(n-1, a+1)
        print(' '*(a)+'U '*(n))

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab9TEST.py' ))

        
    
