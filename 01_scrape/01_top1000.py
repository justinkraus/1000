from bs4 import BeautifulSoup, SoupStrainer
import requests

#url = "https://embed.spotify.com/?uri=spotify:playlist:"
url ="https://www.gutenberg.org/browse/scores/top1000"

page = requests.get(url)    
data = page.text
soup = BeautifulSoup(data, features="html.parser")

for link in soup.find_all('a'):
    print(link.get('href'))