import undetected_chromedriver
import time
from bs4 import BeautifulSoup

if __name__ == '__main__':
    link = 'https://www.dns-shop.ru/catalog/17a89c2216404e77/bloki-pitaniya/?stock=now-today-tomorrow-later&brand=1stplayer-asus-bequiet-coolermaster-corsair-cougar-crown-deepcool-enermax-evga-fractaldesign-fsp-gigabyte-inwin-msi-nzxt-qdion-seasonic-silverstone-superflower-thermaltake-xpgadata&fr[wts5]=750-1600&f[w6]=9cm-9cn-9cq-9co-7grf-9cr'
    option = undetected_chromedriver.ChromeOptions()
    option.add_argument('--headless')
    try:
        driver = undetected_chromedriver.Chrome(options=option)
        option.headless = True
        driver.get(link)
        time.sleep(5)
    except Exception as ex:
        print(ex)
    finally:
        f = driver.page_source
        driver.close()
        driver.quit()
        soup = BeautifulSoup(f, 'html.parser')
    names = []
    prices = []
    a = soup.find_all('a', class_="catalog-product__name")
    b = soup.find_all('div', class_="product-buy__price")
    c = soup.find('h1', class_="product-card-top__title")
    for it in b:
        print(type(it.text))
    print(b)