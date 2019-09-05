# lab 2
# Shaan Barkat, collab with Anthony and Marcus


class Animal:

    def __init__(self, species = 'default',lang= 'default',age= 0):
        self.species=species
        self.lang = lang
        self.age = age

    def __repr__(self):
        return "Animal('{}','{}',{})".format(str(self.species),str(self.lang),int(self.age))

    def setSpecies(self,species):
        self.species =species

    def setLanguage(self,lang):
        self.lang=lang

    def setAge(self,age):
        self.age=age
        

    def speak(self):
        print( "I am a",self.age,"year-old",self.species,"and I",self.lang + '.')


def processAnimals(file):
    b = open(file, 'r')
    fileread = b.readlines()
    b.close
    lst = []

    for line in fileread:
        a = line.split(',')
        p = Animal()
        p.setSpecies(a[0])
        p.setLanguage(a[1])
        p.setAge(a[2].strip())
        lst.append(p)
        p.speak()
    return lst
        
        
        
                                
if __name__=='__main__':
    import doctest
    print( doctest.testfile('lab2TEST.py') )
                        
                                        
                    
        

