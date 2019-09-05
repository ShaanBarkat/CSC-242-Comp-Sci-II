# Shaan Barkat
# Collab with Anthony Marsilio and Marcus Lofton
# hw3
class Stat:
    def __init__(self,lst=[]):
        self.x = list(lst)
        
    def __repr__(self):
        return "Stat({})".format(self.x)
    
    def add(self,z):
        self.x.append(z)
        
    def __len__(self):
        return len(self.x)
    
    def min(self):
        if len(self.x) != 0:
            return min(self.x)
        else:
            raise EmptyStatError("empty Stat does not have a min")
        
    def max(self):
        if len(self.x) != 0:
            return max(self.x)
        else:
            raise EmptyStatError("empty Stat does not have a max")
        
    def sum(self):
        if len(self.x) != 0:
            return sum(self.x)
        else:
            return 0
        
    def mean(self):
        if len(self.x) != 0:
            return sum(self.x) / len(self.x)
        else:
            raise EmptyStatError("empty Stat does not have a mean")
        
    def clear(self):
        self.x = []

        
class intlist(list):
    def __init__(self,lst):
        self.extend(list)
        
    def append(self,num):
        self.insert(len(self),num)
    def extend(self,num):
        for a in num:
            self.append(a)
            
    def insert(self,index,num):
        if type(num) == int:
            list.insert(self,index,num)
        else:
            raise NotIntError("{} not an int".format(num))
            
    def __repr__(self):
        return "intlist({})".format(list.__repr__(self))
    
    def __setitem__(self,index,c):
        if type(c)==int:
            list.__setitem__(self,index,c)
        else:
            raise NotIntError("{} not an int".format(c))
        
    def __getitem__(self,k):
        return list.__getitem__(self,k)
    
    def odds(self):
        oddlist = intlist([])
        for i in self:
            if i%2 == 1:
                oddlist.append(i)
        return oddlist
    
    def evens(self):
        evenlist = intlist([])
        for i in self:
            if type(i) == int:
                if i%2 == 0:
                    evenlist.append(i)
        return evenlist
    def __init__(self,num = []):
        self.extend(num)

        
class NotIntError(Exception):
    pass
class EmptyStatError(Exception):
    pass
    
if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw3TEST.py' ))

