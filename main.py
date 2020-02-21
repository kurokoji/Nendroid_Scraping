from urllib import request
from urllib import parse
from bs4 import BeautifulSoup
from tqdm import tqdm
import uuid
import time


def get_nendroid():
    url = 'https://www.goodsmile.info/ja/nendoroid'
    for i in range(11):
        l, r = i * 100 + 1, 100 + i * 100
        if i == 0:
            l = 0

        time.sleep(2)
        st = '{:03}-{:03}'.format(l, r)
        res = request.urlopen(url + st)
        soup = BeautifulSoup(res, features='html.parser')
        res.close()

        print(url + st, soup.title.text)
        for link in tqdm(soup.find_all('a')):
            h = link.get('href')
            if h is None:
                continue

            if 'product' in h and not 'products' in h:
                res2 = request.urlopen(h)
                soup2 = BeautifulSoup(res2, features='html.parser')
                res2.close()
                # print(soup2)

                for idx, im in enumerate(soup2.find_all('img', attrs={'class', 'itemImg'})):
                    img_src = im.get('src')
                    if img_src is None:
                        continue
                    try:
                        web_file = request.urlopen('https:' + img_src)
                        data = web_file.read()
                        with open('./images/' + '{}_{}.jpg'.format(soup2.title.text.replace('/', '-').replace('ねんどろいど ', ''), idx) , mode='wb') as f:
                            f.write(data)
                    except Exception as e:
                        print(e)


def get_scale_fig():
    url = 'https://www.goodsmile.info/ja/products/category/scale/released/'
    for i in range(2006, 2022):
        res = request.urlopen(url + str(i))
        soup = BeautifulSoup(res, features='html.parser')
        res.close()
        print(url + str(i), soup.title.text)
        for link in tqdm(soup.find_all('a')):
            h = link.get('href')
            if h is None:
                continue

            if 'product' in h and not 'products' in h:
                # print(parse.unquote(h))
                res2 = request.urlopen(h)
                soup2 = BeautifulSoup(res2, features='html.parser')
                res2.close()
                # print(soup2)

                for idx, im in enumerate(soup2.find_all('img', attrs={'class', 'itemImg'})):
                    img_src = im.get('src')
                    if img_src is None:
                        continue
                    try:
                        web_file = request.urlopen('https:' + img_src)
                        data = web_file.read()
                        with open('./scale_images/' + '{}_{}.jpg'.format(soup2.title.text.replace('/', '-'), idx), mode='wb') as f:
                            f.write(data)
                    except Exception as e:
                        print(e)

def main():
    get_nendroid()
    # get_scale_fig()


if __name__ == '__main__':
    main()
