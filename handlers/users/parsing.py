from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.epravda.com.ua/")
soup = BeautifulSoup(r.content,'html.parser')

headers = soup.select('.article__title')
list_h = []
for h in headers[:4]:
    header = h.text
    list_h.append(header)


list_links = []
links = soup.select('.article__title > a')
for l in links[:4]:
    link = l.get('href')
    list_links.append(link)
new_links = [el if el[0:5] == "https" else 'https://www.epravda.com.ua' + el for el in list_links]
for i in new_links:
    print(i)


articles=[]
for i in new_links:
    n=requests.get(i)
    new_soup=BeautifulSoup(n.content,"html.parser")
    text=new_soup.select(".post__text > p")
    article_body=[]
    for u in text:
        t=u.text
        article_body.append(f"{t}\n")
    a="".join(article_body)
    articles.append(a)

r2 = requests.get("https://www.pravda.com.ua/")
soup = BeautifulSoup(r2.content,'html.parser')

headers = soup.select('.article_header')
list_h2 = []
for h in headers[:4]:
    header = h.text
    list_h2.append(header)


list_links2 = []
links2 = soup.select('.article_header > a')
for l in links2[:4]:
    link = l.get('href')
    list_links2.append(link)

new_links2 = [el if el[0:5] == "https" else 'https://www.pravda.com.ua' + el for el in list_links2]
for i in new_links2:
    print(i)

articles2 = []
for l in new_links2:
    n_r = requests.get(l)
    new_soup = BeautifulSoup(n_r.content,'html.parser')
    text = new_soup.select('.post_text > p')
    article_body = []
    for i in text:
        text_article = i.text
        article_body.append(f"{text_article}\n")
    article_text = ''.join(article_body)
    articles2.append(article_text)