#Shaan Barkat
#HW5
#Collabed with Anthony Marsilio

def pascalLine(x):
    if x == 0:
        return [1]
    else:
        prev = pascalLine(x-1)
        lst = [1]
        for i in range(len(prev)-1):
            lst.append(prev[i] + prev[i+1])
        lst.append(1)
    return lst

def levy(x):
    if x == 0:
        return "F"
    else:
        turns = levy(x-1)
        return turns.replace("F", "LFRRFL")

def base(x,z):
    if x < z:
        return str(x)
    else:
        return base(x//z,z)+ str(x%z)

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw5TEST.py' ))
