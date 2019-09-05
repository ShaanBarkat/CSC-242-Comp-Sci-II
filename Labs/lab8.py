#Shaan Barkat
#Collab with Anthony Marsilio and Marcus Lofton


from html.parser import HTMLParser
from urllib.request import urlopen


class HeadingParser(HTMLParser):
    
    def __init__(self):
        HTMLParser.__init__(self)
        self.lst = []
        self.val = False

    def handle_starttag(self, tag, attrs):
        if tag in ['h1','h2','h3','h4','h5','h6']:
            self.val = True

    def handle_endtag(self, tag):
        if tag in ['h1','h2','h3','h4','h5','h6']:
            self.val = False

    def hanlde_data(self, data):
        if self.val:
            data = data.strip()
            if data != '':
                self.lst.append(data)
                
    def getheadings(self):
        return self.lst

def testHP(url):
    hp = HeadingParser()
    hp.feed( urlopen(url).read().decode() )
    return hp.getheadings()

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab8TEST.py' ))


    
                   
