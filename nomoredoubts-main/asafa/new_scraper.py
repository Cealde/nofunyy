
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

page = requests.get(url)


soup=bs(page.text,'html.parser')

dwarves_table = soup.findall('table',{"class":"wikitable sortable"})

total_table = len(dwarves_table)

temp_list = []

# Webdriver
browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

new_dwarves_data = []

table_rows = dwarves_table[1].findall('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in]
    temp_list.append(row)



    Star_names = []
    Distance.append = []
    Mass.append= []
    Radius.append= []

    print(temp_list)
for i in range(1,len(temp_list)):
    
    Star_names.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])

# Convert to CSV
headers = ['Star_name','Distance','Mass','Radius']  
df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,)),columns=['Star_name','Distance','Mass','Radius'])
print(df2)

df2.to_csv('dwarf_stars.csv', index=True, index_label="id")