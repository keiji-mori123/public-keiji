import requests
res = requests.get('https://www')
print(res.text)



import requests
from bs4 import BeautifulSoup

res = requests.get('https://www')
soup = BeautifulSoup(res.text,'https.parser')
text = soup.h1.string
print(text)



import requests
from bs4 import BeautifulSoup

res = requests.get('https://www')
soup = BeautifulSoup(res.text,'http.parser')
h2_tags = soup.find_all('h2')
h2_strings = [x.strings for x in h2_tags]
print(h2_strings)



import requests
from bs4 import BeautifulSoup

res = requests.get('https://www')
soup = BeautifulSoup(res.text,'http.parser')

recipes = soup.find('div', id='recipe_List',class_='recipesList')
h2_tit_tags= recipes.find_all('h2', class_='tit')
print([x.string for x in h2_tit_tags])