import undetected_chromedriver
from bs4 import BeautifulSoup
import time
import urllib
from random import randint
import re


if __name__ == '__main__':
    import pymysql.cursors
    with open('links.txt', 'r') as f:
        links = f.readlines()
        f.close()
    for link in links:
    # Подключиться к базе данных.
        con = pymysql.connect(host="31.31.196.77",
                              user='u1679896_test',
                              password='17vanya01',
                              db='u1679896_db',
                              charset='utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor)
        print("connect successful!!")
        #link = "https://www.dns-shop.ru/catalog/17a89aab16404e77/videokarty/?stock=now-today-tomorrow-later&f[mv]=ldmod&f[mz]=2fj"
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
        for el in a:
            names.append(el.find('span').string)
        for el in b:
            prices.append(int(re.sub(r'[^0-9]', '', el.text)))
        if not names:
            names.append(c.string)
        if not prices:
            print("no")
            continue
        ind_min = prices.index(min(prices))
        print(prices, names[ind_min])

        if 'Жесткий' in names[ind_min]:
            with con:
                cur = con.cursor()
                cur.execute('SELECT * FROM `hdd`')
                rows = cur.fetchall()
                cur = con.cursor()
                sql = f'INSERT INTO `hdd`(`link`, `price`) VALUES ("{link}",{prices[ind_min]})'
                for row in rows:
                    print(row)
                    row = row.items()
                    if ('link', link) in row:
                        sql = f'UPDATE `hdd` SET `price`={prices[ind_min]} WHERE `link`="{link}"'
                        break
                    else:
                        sql = f'INSERT INTO `hdd`(`link`, `price`) VALUES ("{link}",{prices[ind_min]})'
                cur.execute(sql)
                con.commit()
        elif 'Видеок' in names[ind_min]:
            print(1)
            with con:
                cur = con.cursor()
                cur.execute('SELECT * FROM `graphic_cards`')
                rows = cur.fetchall()
                cur = con.cursor()
                for row in rows:
                    row = row.items()
                    if ('link', link) in row:
                        sql = f'UPDATE `graphic_cards` SET `price`={prices[ind_min]} WHERE `link`="{link}"'
                        break
                    else:
                        sql = f'INSERT INTO `graphic_cards`(`link`, `price`) VALUES ("{link}",{prices[ind_min]})'
                cur.execute(sql)
                con.commit()
        elif 'SSD' in names[ind_min]:
            with con:
                cur = con.cursor()
                cur.execute('SELECT * FROM `ssd`')
                rows = cur.fetchall()
                cur = con.cursor()
                sql = f'INSERT INTO `ssd`(`link`, `price`) VALUES ("{link}",{prices[ind_min]})'
                for row in rows:
                    row = row.items()
                    if ('link', link) in row:
                        sql = f'UPDATE `ssd` SET `price`={prices[ind_min]} WHERE `link`="{link}"'
                        break
                    else:
                        sql = f'INSERT INTO `ssd`(`link`, `price`) VALUES ("{link}",{prices[ind_min]})'
                cur.execute(sql)
                con.commit()
        elif 'Кулер' in names[ind_min]:
            with con:
                cur = con.cursor()
                cur.execute('SELECT * FROM `coolers`')
                rows = cur.fetchall()
                cur = con.cursor()
                sql = f'INSERT INTO `coolers`(`link`, `price`) VALUES ("{link}",{prices[ind_min]})'
                for row in rows:
                    row = row.items()
                    if ('link', link) in row:
                        sql = f'UPDATE `coolers` SET `price`={prices[ind_min]} WHERE `link`="{link}"'
                        break
                    else:
                        sql = f'INSERT INTO `coolers`(`link`, `price`) VALUES ("{link}",{prices[ind_min]})'
                cur.execute(sql)
                con.commit()
        elif 'Система охлаждения' in names[ind_min]:
            with con:
                cur = con.cursor()
                cur.execute('SELECT * FROM `coolers`')
                rows = cur.fetchall()
                cur = con.cursor()
                sql = f'INSERT INTO `coolers`(`link`, `price`) VALUES ("{link}",{prices[ind_min]})'
                for row in rows:
                    row = row.items()
                    if ('link', link) in row:
                        sql = f'UPDATE `coolers` SET `price`={prices[ind_min]} WHERE `link`="{link}"'
                        break
                    else:
                        sql = f'INSERT INTO `coolers`(`link`, `price`) VALUES ("{link}",{prices[ind_min]})'
                cur.execute(sql)
                con.commit()
        if 'Корпус' in names[ind_min]:
            with con:
                cur = con.cursor()
                cur.execute('SELECT * FROM `case`')
                rows = cur.fetchall()
                cur = con.cursor()
                sql = f'INSERT INTO `case`(`link`, `price`) VALUES ("{link}",{prices[ind_min]})'
                for row in rows:
                    row = row.items()
                    if ('link', link) in row:
                        sql = f'UPDATE `case` SET `price`={prices[ind_min]} WHERE `link`="{link}"'
                        break
                    else:
                        sql = f'INSERT INTO `case`(`link`, `price`) VALUES ("{link}",{prices[ind_min]})'
                cur.execute(sql)
                con.commit()
        if 'Блок' in names[ind_min]:
            with con:
                cur = con.cursor()
                cur.execute('SELECT * FROM `bp`')
                rows = cur.fetchall()
                cur = con.cursor()
                sql = f'INSERT INTO `bp`(`link`, `price`) VALUES ("{link}",{prices[ind_min]})'
                for row in rows:
                    row = row.items()
                    if ('link', link) in row:
                        sql = f'UPDATE `bp` SET `price`={prices[ind_min]} WHERE `link`="{link}"'
                        break
                    else:
                        sql = f'INSERT INTO `bp`(`link`, `price`) VALUES ("{link}",{prices[ind_min]})'
                cur.execute(sql)
                con.commit()
        if 'Процессор' in names[ind_min]:
            with con:
                cur = con.cursor()
                cur.execute('SELECT * FROM `cpus`')
                rows = cur.fetchall()
                cur = con.cursor()
                sql = f'INSERT INTO `cpus`(`link`, `price`) VALUES ("{link}",{prices[ind_min]})'
                for row in rows:
                    row = row.items()
                    if ('link', link) in row:
                        sql = f'UPDATE `cpus` SET `price`={prices[ind_min]} WHERE `link`="{link}"'
                        break
                    else:
                        sql = f'INSERT INTO `cpus`(`link`, `price`) VALUES ("{link}",{prices[ind_min]})'
                cur.execute(sql)
                con.commit()