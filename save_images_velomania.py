import urllib.request
import requests
from bs4 import BeautifulSoup
import re
from tqdm import tqdm


def get_html(url: str):
    resp = urllib.request.urlopen(url)
    return resp.read()


def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    hrefs = soup.find_all('a', attrs={'href': re.compile('^https://forum.velomania.ru/attachment.php')})
    images = {}
    for link in tqdm(hrefs):
        images[f"{link.text}"] = link['href']
    return images



if __name__ == '__main__':
    url = 'https://forum.velomania.ru/showthread.php?t=428791&page='

    for page in tqdm(range(368+31+2+6, 413)):
        html = get_html(f"{url}{page}")
        images = parse(html)
        for key in images.items():
            # r = requests.get(key[1])
            # open(, 'wb').write(r.content)
            try:
                urllib.request.urlretrieve(key[1], f'/home/pi/tmp/velomania/{key[0]}')
            except:
                print(f"Error on {key}")
