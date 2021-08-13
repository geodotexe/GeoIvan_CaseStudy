import requests
from bs4 import BeautifulSoup
import csv

key = input('Search Product/Brand : ')
y = input('\nScrape from page 1 - ')
z = int(y)+1
url='https://rajasusu.com/catalogsearch/result/index/?q={}&p='.format(key)
web_url = 'https://rajasusu.com'

headers={
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 OPR/77.0.4054.277'
}

datas = []
count_page=0
for page in range(1, int(z)):
   count_page+=1
   print('Scraping the data from page - ', count_page)
   req = requests.get(url+str(page), headers=headers)
   soup = BeautifulSoup(req.text, 'html.parser')
   items = soup.findAll('div','product-item pcard-item')
   for it in items:
      name = it.find('div','pcard-name').text
      price = ''.join(it.find('span','price').text.strip().split('\n'))
      try : stock = it.find('span').text
      except : stock=''
      if 'Add to Cart' in stock: stock='In stock'.format(stock)
      try : web = it.find('a',{'title':'Pediasure Madu 200Gr'})['href']
      except : web =''
      try : web1 = it.find('a',{'title':'Pediasure Vanila 850 Gr'})['href']
      except : web1=''
      try : web2 = it.find('a',{'title':'Nutrilon Royal 3 Madu 800 Gr'})['href']
      except : web2=''
      datas.append([name, price, stock, web_url, (web, web1, web2)])

head = ['NAMA SKU', 'HARGA SKU', 'KETERSEDIAAN BARANG', 'URL', 'Products_URL']
writer = csv.writer(open('MAGPIE/{}_RajaSusu.csv'.format(key),'w', newline=''))
writer.writerow(head)
for d in datas: writer.writerow(d)