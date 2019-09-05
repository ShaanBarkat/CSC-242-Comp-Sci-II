#HW4
#Shaan Barkat
#Collabed with Anthony Marsilio and Marcus Lofton
from tkinter import *
def mask(s,exc):
    s = s.upper()
    exc = exc.upper()
    word = ''
    for i in s:
        if i not in exc:
            word += '?'
        else:
            word += i
    return word
 

class hangman(Frame):
    def __init__(self,s,parent=None):
        self.rkeys = ''
        self.wkeys = ''
        Frame.__init__(self,parent)
        self.word = s.upper()
        self.ans = Entry(self)
        self.ans.grid(row=0,column=2,columnspan=4)
        maskedstring = mask(self.word,'')
        self.ans.insert(END,mask(self.word,''))
        Label(self,text='Word:').grid(row=0,column=0,columnspan=2)
        self.right = Entry(self)
        self.right.grid(row=1,column=2,columnspan=4)
        Label(self,text='Right:').grid(row=1,column=0,columnspan=2)
        self.wrong = Entry(self)
        self.wrong.grid(row=2,column=2,columnspan=4)
        Label(self,text='Wrong:').grid(row=2,column=0,columnspan=2)
        labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(len(labels)):
            def cmd(key=labels[i]):
                self.click(key)
            b = Button(self,command=cmd,text=labels[i],width=5,height=3)
            b.grid(row=i//6+3,column=i%6)

    def click(self,key):
            if key in self.word:
                if key in self.rkeys:
                    pass
                else:
                    self.rkeys += key
                    self.right.insert(END,key)
                    self.ans.delete(0,END)
                    self.ans.insert(END,mask(self.word,self.rkeys))
            if key not in self.word:
                if key in self.wkeys:
                    pass
                else:
                    self.wkeys += key
                    self.wrong.insert(END,key)
            if self.ans.get() == self.word:
                messagebox.showinfo('Hangman','You Win!')
            if len(self.wrong.get()) == 6:
                messagebox.showinfo('Hangman','You Lose!')
if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw4TEST.py' ))

