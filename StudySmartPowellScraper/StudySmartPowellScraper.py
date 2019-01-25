import json
from bs4 import BeautifulSoup as bs
import requests
import sys

<<<<<<< HEAD

=======
if __name__ == '__main__':
    url = "http://calendar.library.ucla.edu/spaces?lid=4394&gid=7748"
    r = requests.get(url)
    #Check if request returns 200
    if r.ok:
        soup = bs(r.text, "html.parser")
        #print(soup.prettify())
        #for item in soup.body.a.findall(attrs={'class': 'fc-timeline-event'}):
         #   print(item['title'])
        #for item in soup.findall(attrs={'class' : 'fc-timeline-event'}):
         #   print(item.a['title'])
    else:
        sys.stderr.write("Link returns bad signal\n")
>>>>>>> 83e3c01ab603fa5d7589b0b5ca6303526e3aca7f
