# Shaan Barkat
# lab6
# Collab with Anthony Marsilio and Marcus Lofton
def silly(n):
    if n>0:
        print('*', end='')
        silly(n-1)
        print('!', end='')


def stars(n):
    if n>0:
        stars(n-1)
        print('*'*n)
        stars(n-1)
        

def pattern(n):
    if n>0:
        pattern(int(n/2))
        pattern(int(n/2))
        print(n, end='')


if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab6TEST.py' ))

     
        
    
        
        
        
