import requests
from bs4 import BeautifulSoup

url = 'https://www.w3schools.com/html/default.asp'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

items = soup.find_all('div', attrs={'id':'leftmenuinnerinner'})
print(len(items))

if len(items) == 0:
    print('Not Found')
else:
    titles = items[0].find_all('a')
    
    
for item in titles:
    print(item.getText())
    