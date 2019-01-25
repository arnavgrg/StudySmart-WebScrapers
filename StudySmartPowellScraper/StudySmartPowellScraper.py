import json
from bs4 import BeautifulSoup as bs
import requests
import sys

if __name__ == '__main__':
    url = "http://calendar.library.ucla.edu/spaces?lid=4394&gid=7748"
    r = requests.get(url)
    #Check if request returns 200
    if r.ok:
        soup = bs(r.text, "html.parser")
    else:
        sys.stderr.write("Link returns bad signal\n")
