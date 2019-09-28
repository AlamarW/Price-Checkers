from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from datetime import datetime

# Creating a file to put csv data
file_name = 'Compilers Book Price.csv'
f = open(file_name, "a+")

# setting up client, pulling raw html
page_url = "https://www.amazon.com/dp/9332518661/"
user_client = urlopen(page_url)
raw_html = user_client.read()

# soup-ing the raw_html
parser = 'html.parser'
s = soup(raw_html, parser)

# Grabbing title and price from soup, and adding a time marker
price = s.find('span', {'class' : 'a-size-medium a-color-price header-price'})
price = price.text.strip()
print('Price: '+ price)


title = s.find('span',{'class' : 'a-size-extra-large'})
title = title.text
print('Title: ' + title)

time = datetime.now()
time = time.strftime("%m/%d/%Y %H:%M:%S")
print('Time: ' + time)

f.write(title + '\t' + price + '\t' + time + '\n')
f.close()
