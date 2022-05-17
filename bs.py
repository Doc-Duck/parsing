from bs4 import BeautifulSoup
from sql import cur, base
html = open('page.html', 'r', encoding="utf-8")
soup = BeautifulSoup(html, 'html.parser')

names = []
prices =[]
a = soup.find_all('a', class_="catalog-product__name")
b = soup.find_all('div', class_="product-buy__price")
for el in a:
    names.append(el.find('span').string)
for el in b:
    prices.append(int(el.string.replace('₽','').replace(' ', '')))
ind_min = prices.index(min(prices))
cur.execute('INSERT INTO Matherboards  VALUES(?, ?)', (f'{names[ind_min]}',f'{prices[ind_min]}'))
base.commit()
print(prices[ind_min], names[ind_min])
