# Shaan Barkat
# Collab with Marcus Lofton and Anthony Marsilio
# Lab3

class Stack(object):

   def __init__(self, lst = []):
      self.items = list(lst)

   def __repr__(self):
      return 'Stack({})'.format(self.items)

   def push(self, item):
      self.items.append(item)

   def pop(self):
       return self.items.pop()

   def isEmpty(self):
       return len(self.items) == 0

   def __len__(self):
      return len(self.items)

   def __getitem__(self, index):
      return self.items[index]


def parenthesesMatch(s1):
   S = Stack()
   a,b = "([(",")])"
   for x in s1:
      if x in S:
         S.push(s1)
      elif x in b:
         if lenS.isEmpty():
            return False
         else:
            stacktop = S.pop()
            j = stacktop + x
            if j not in a,b
               return False
            else:
               continue
      return Stack.isEmpty()


   
      
if __name__=='__main__':
    import doctest
    print( doctest.testfile('lab3TEST.py') )
        

       
    
