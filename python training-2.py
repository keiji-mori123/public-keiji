from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

url = 'https://.com/python_list/'
r = requests.get(url)
time.sleep(3)

print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
contents = soup.find(class_="entry-content")

get_a = contents.find_all("a")
len(get_a)

title_links = []
for i in range(len(get_a)):
    try:
        link_ = get_a[i].get("href")
        title_links.append(link_)
    except:
        pass
    
print(title_links)

youtube_titles = []
youtube_links = []

for i in range(len(title_links)):
    title_link = title_links[i]
    
    r = requests.get(title_link)
    time.sleep(3)
    soup = BeautifulSoup(r.text, 'html.parser')
       
    youtube_title = soup.find(class_="entry-title").text
    if youtube_title == '404 NOT FOUND':
        continue
    else:
        youtube_titles.append(youtube_title)
    
    youtube_link = soup.find('iframe')['src'].replace("embed/","watch?v=")
    youtube_links.append(youtube_link)
    
    result ={
        'youtube_title': youtube_titles,
        'youtube_link': youtube_links
    }
    
    df = pd.DataFrame(result)
    
    df.to_csv('result.csv', index=False, encoding='utf-8')
    print(df)