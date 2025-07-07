import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_Indian_IT_companies'
responce = requests.get(url)

soup = BeautifulSoup(responce.text, 'html.parser')

table = soup.find_all('table', class_='wikitable')[2]
titles_column = table.find_all('tr')[0].find_all('th')

titles_list = [title.text.strip() for title in titles_column]

df = pd.DataFrame(columns=titles_list)

table_rows = table.find_all('tr')[1:]
for row_data in table_rows:
    rows = row_data.find_all('td')
    values = [row.text.strip() for row in rows]
    df.loc[len(df)] = values

footer = soup.find('li', id='footer-info-lastmod')
last_updated = footer.text if footer else "Last updated info not found."

print(df)
print("\nPage " + last_updated)

df.to_excel(r"C:\\Users\\LENOVO\\Desktop\\Indian_IT_companies.xlsx", index=False)