#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
get_ipython().run_line_magic('matplotlib', 'inline')

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.hubertiming.com/results/2017GPTR10K"

html = urlopen(url)

soup = BeautifulSoup(html, "html.parser")
type(soup)
#bs4.BeautifulSoup

text = soup.get_text()
#print(soup.text)

#all_links = soup.find_all('a')
#for link in all_links:
#    print(link.get("href"))

rows = soup.find_all('tr')
#print(rows[:10])
for row in rows:
    row_td = row.find_all('td')
#print(row_td)
#str_cells = str(row_td)
#cleantext=BeautifulSoup(str_cells, "html.parser").get_text()
#print(cleantext)
#type(row_td)

#Regular Expression Test 

list_rows = []
for row in rows:
    cells = row.find_all('td')
    str_cells = str(cells)
    clean = re.compile('<.*?>')
    clean2 =(re.sub(clean, '',str_cells))
    list_rows.append(clean2)
type(clean2)

df = pd.DataFrame(list_rows)
#df.head(10)
df1 = df[0].str.split(',',expand=True)
#df1[0] = df1[0].str.split('[')
df1.head(10)


# In[ ]:




