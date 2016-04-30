# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 13:14:22 2016

@author: bikeshkawan
"""

import requests
from bs4 import BeautifulSoup

g = requests.get("https://google.com")
print(g.text)

soup = BeautifulSoup(g.text)

for item in soup.find_all('a'):
    print('######'*12, item)

for item in soup.find_all('a'):
    if 'तस्बिर' in item:
        print('--'*12, item)