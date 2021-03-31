import os
import requests
from tqdm import tqdm
import img2pdf

url = "https://www.rfbr.ru/rffi/djvu_page?objectId=2079222&width=1000&page=0"
url_prefix = "&cache=cache.png"


for page in tqdm(range(0,220)):
    r = requests.get(f"{url}{page}{url_prefix}")
    open(f"/home/pi/tmp/book/{page}.png", 'wb').write(r.content)

list_book = [i for i in os.listdir("/home/pi/tmp/book") if i.endswith(".png")]
list_book.sort(key=lambda f: int(os.path.splitext(f)[0]))
list_book = [os.path.join("/home/pi/tmp/book", i) for i in list_book]

with open("/home/pi/tmp/book/book.pdf", 'wb') as book:
    book.write(
        img2pdf.convert(
            list_book
        )
    )
