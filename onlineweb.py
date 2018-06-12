#!/usr/bin/python3
import  nltk
from nltk.corpus import  stopwords
import urllib.request
from bs4 import BeautifulSoup
web_data=urllib.request.urlopen('https://php.net')
# complete html based code 
html=web_data.read()
#print(html)

soup=BeautifulSoup(html,"html5lib")
text=soup.get_text()
print(text)

#print(text)
# tokenize string -- means seperate into words 
token=[i for i  in text.split()]
#print(token)

# frequency count 
freq_data=nltk.FreqDist(token)
#print(freq_data.items())
'''
for key,value in freq_data.items():
    print(str(key) +': '+str(value))
'''
#  here this is number of count of words as a parameter
freq_data.plot(20)
#freq_data.plot(5,cumulative=False)

# removing  stop words 
'''
clean_freq_data=token[:]
for  i  in  freq_data:
    if  i in stopwords.words('english'):
        clean_freq_data.remove(i)

print(clean_freq_data)



'''
