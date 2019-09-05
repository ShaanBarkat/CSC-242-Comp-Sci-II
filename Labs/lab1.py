# lab 1
# Shaan Barkat Collab with Anthony Marsilio and Marcus Lofton

def printTwoLargest():
    a =1
    maxi = 0
    secondmaxi = 0
    while float(a)>0:
        a = eval(input("Please enter a number: "))
        if a > maxi:
            maxi = a
        if a > secondmaxi and a< maxi:
            secondmaxi = a
    if secondmaxi != 0:
        print("The largest is", maxi)
        print("The second largest is", secondmaxi)
    elif maxi != 0 and secondmaxi == 0:
        print("The largest is", maxi)
    elif maxi == 0 and secondmaxi == 0:
        print ("No positive numbers were entered")

def printWordsLines(filename):
    numlines = 0
    infile = open(filename, 'r')
    s = infile.read()
    a = s.split()
    numwords = len(a)
    for lines in s:
        if '\n' in lines:
            numlines += 1
    print("The file", filename, "contains", numwords, "words and", numlines, "lines.")
    infile.close()

def reverseDict(Dict):
    Empty = {}
    for Keys in Dict:
        Empty[Dict[Keys]]=Keys
    return(Empty)

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab1TEST.py' ))


    
    
