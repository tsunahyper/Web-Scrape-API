import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://en.wikipedia.org/wiki/Spider-Man'

response = requests.get(url)

content = BeautifulSoup(response.content, 'html.parser')

_table = content.find_all('table', {'class': 'wikitable'})
_columnname = _table[0].find_all('th')
_title = []
for title in _columnname:
    _title.append(title.text.strip())

## df act as a naming convention for data frameßs
df = pd.DataFrame(columns=_title)

_columndata = _table[0].find_all('tr')
for data in _columndata[1:]:
    _row = data.find_all('td')
    _one_row = [x.text.strip() for x in _row]
    length = len(df)
    df.loc[length] = _one_row

df.to_csv('spiderman.csv',index=False)