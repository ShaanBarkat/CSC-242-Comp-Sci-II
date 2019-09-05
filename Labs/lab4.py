# Shaan Barkat

# lab4

class Mapping(dict):
    def __init__(self, d={}):
        for k in d:
            self[k]=d[k]
        

    def __setitem__(self,k,value):
        if k in self:
            self.pop(k)
        if value in self:
            self.pop(value)
        dict.__setitem__(self,k,value)
        dict.__setitem__(self,value,k)

    def __repr__(self):
        return "Mapping({})".format(dict.__repr__(self))
    

    def pop(self,k):
        val = self[k]
        if k == val:
            dict.pop(self,k)
        else:
            dict.pop(self,k)
            dict.pop(self,val)

if __name__=='__main__':
    import doctest
    print( doctest.testfile('lab4TEST.py') )

