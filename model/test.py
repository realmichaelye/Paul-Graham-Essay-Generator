import re
from bs4 import BeautifulSoup
str = "<font face='verdana' size='2'><p>April 2000<br/>The best wa"

#Check if the string starts with 'hello':

x = re.sub(">((.|\n|\r)*)?20((.|\n|\r)*)?<br/?>", '>', str, count=1)
print(x)

soup = BeautifulSoup(x,  'html.parser')
text = soup.get_text()
print(text)

# if (x):
#   print("Yes, the string starts with 'hello'")
# else:
#   print("No match")
