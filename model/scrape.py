from bs4 import BeautifulSoup
import requests
import re
import html2text
import io
f = io.open("essays.txt", "a", encoding="utf-8")

h = html2text.HTML2Text()
h.ignore_links = True
h.ignore_images = True

#get page html in string
url = "http://www.paulgraham.com/articles.html"
response = requests.get(url)
data = response.text

soup = BeautifulSoup(data, 'html.parser')

tags = set(soup.find_all('a'))

links = []
for tag in tags:
    links.append(tag.get("href"))

links = set(links)

links.remove("rss.html")
links.remove('https://sep.yimg.com/ty/cdn/paulgraham/acl1.txt?t=1577624393&')
links.remove('https://sep.yimg.com/ty/cdn/paulgraham/acl2.txt?t=1577624393&')

# for i in range(len(links)-1):
#     links.pop()

for link in links:
    url = "http://www.paulgraham.com/"+link
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')
    
    # soup.table.decompose()

    fontsTags = soup.findAll('font', {"size" : 2, "face":"verdana"})
    for fontsTag in fontsTags:
        tableTags = fontsTag.find_all('table')
        for tableTag in tableTags:
            tableTag.decompose()
    
    # print(fontsTags)
    # string = str(fontsTags[0])
    # print(string)

        
    for fontsTag in fontsTags:
        
        print(link)
        try:
            string = str(fontsTag)
            cleaned = h.handle(string)
            f.write(cleaned)
        except(AttributeError):
            pass
        # string = re.sub("<br/?>", '<br/>\n', string)
        # soup = BeautifulSoup(string, 'html.parser')
        # cleaned = soup.get_text()
        
        
        # print(cleaned)
        

        # print(cleaned)

    # print(re.sub(">((.|\n|\r)*)?20((.|\n|\r)*)?<br/?>", '>', string, count=1))
    # x = re.sub(">.*?<br/?>", '>', str(fontsTags[0]), count=1)
    # print(x)
    # for fontTag in fontsTags:
    #     print(fontTag)
