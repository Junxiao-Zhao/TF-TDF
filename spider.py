from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.cbc.ca/news/canada/ottawa/tara-hills-ottawa-mom-changes-anti-vaccination-stand-before-7-kids-get-sick-1.3025592?cmp=rss").read()
soup = BeautifulSoup(html, "html.parser")

print(soup.find('h1', 'detailHeadline').string)

story_tag = soup.find('div', 'story')
for tags in story_tag.findAll('p'):
    s = tags.string
    if s != None:
        print(s)

for tags in story_tag.findAll('li'):
    s = tags.string
    if s != None:
        print(s)