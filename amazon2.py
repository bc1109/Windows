import bs4
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36', }

res = requests.get(
    'https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994', headers=headers)
res.raise_for_status()


soup = bs4.BeautifulSoup(res.text, 'html.parser')
soup2 = '(soup.prettify())'
