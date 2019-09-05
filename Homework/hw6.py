#Shaan Barkat
#HW 6
#Collab with Anthony Marsilio

from web import LinkCollector
from web import Crawler  
from html.parser import HTMLParser
from urllib.request import urlopen
from urllib.parse import urljoin
from urllib.error import URLError

class ImageCollector(HTMLParser):
    def __init__(self,url):
        HTMLParser.__init__(self)
        self.url = url
        self.Images = set()

    def handle_starttag(self,tag,attrs):
        if tag=='img':
            for attr,val in attrs:
                if attr=='src':
                    self.Images.add(urljoin(self.url, val) )
                    
    def getImages(self):
        return self.Images
    
class ImageCrawler(Crawler):
    def __init__(self):
        Crawler.__init__(self)
        self.Imagesc = set()
        self.Imagesd = set()

    def crawl(self,url,depth=0,relativeOnly=True):
        ic = ImageCollector(url)
        try:
            ic.feed( urlopen(url).read().decode()  )
        except (UnicodeDecodeError, URLError):
            self.dead.add( url )
        for i in ic.Images:
            self.Imagesc.add(i)
        Crawler.crawl(self,url,depth,relativeOnly)

    def getImages(self):
        return self.Imagesc
    
def scrapeImages(url,filename,depth,relativeOnly):
    ic = ImageCrawler()
    ic.crawl(url,depth,relativeOnly)
    f = open(filename,'w')
    f.write('<html><body>')
    for image in ic.getImages():
        f.write('<img src={}>'.format(image))
    f.write('<html><body>')
    f.close()
'''
if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw6TEST.py' ))
'''    
