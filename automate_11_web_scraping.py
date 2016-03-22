
# coding: utf-8

# https://automatetheboringstuff.com/

# In[ ]:

# test save


# In[ ]:

import numpy as np
import pandas as pd


# In[ ]:

get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt


# In[ ]:

print np.arange(10)


# In[ ]:

#!pwd


# In[ ]:

#!ls


# In[ ]:

#!cat automate_1.py


# In[ ]:

pd.DataFrame({"A":np.arange(10), "B":np.arange(10)*10}).plot()
plt.show()


# #### Description
# 
# This plot is rendered

# https://automatetheboringstuff.com/chapter11/

# In[ ]:

import webbrowser


# In[ ]:

#webbrowser.open('http://inventwithpython.com/')


# In[ ]:

import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)


# In[ ]:

res


# In[ ]:

res.status_code == requests.codes.ok


# In[ ]:

len(res.text)


# In[ ]:

#res.text
print res.text[:250]


# In[ ]:

#res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
#res.raise_for_status()
# HTTPError: 404 Client Error: Not Found for url: http://inventwithpython.com/page_that_does_not_exist


# In[ ]:

res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))


# In[ ]:




# In[ ]:

# Saving Downloaded Files to the Hard Drive


# In[ ]:

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)


# In[ ]:

get_ipython().system(u'ls -la')


# In[ ]:

get_ipython().system(u'cat RomeoAndJuliet.txt | head -10')


# In[ ]:

import bs4
res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
type(noStarchSoup)


# In[ ]:

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile)
type(exampleSoup)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



