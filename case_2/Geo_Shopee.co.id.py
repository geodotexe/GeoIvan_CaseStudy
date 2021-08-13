import requests
#from bs4 import BeautifulSoup
import csv
import math

key = input('Search : ') #keywords
y = input('\nScrape from page 1 - ')
z = int(y)+1
writer = csv.writer(open('MAGPIE/{}_Shopee.csv'.format(key),'w', newline=''))
head = ['NO', 'NAMA SKU', 'HARGA', 'JUMLAH PENJUALAN', 'HALAMAN']
writer.writerow(head)

url_site ='https://shopee.co.id/api/v4/search/search_items'

count=0 #numbering the scraped products
count_page=0
for page in range(1, int(z)):
   parameter = {
      'by': 'relevancy',
      'keyword': key,
      'limit': 60,
      'newest': 60,
      'order': 'desc',
      'page_type': page,
      'scenario': 'PAGE_GLOBAL_SEARCH',
      'version': 2
   }

   r = requests.get(url_site, params=parameter).json()
   prods = r['items']
   for p in prods:
      nama = p['item_basic']['name']
      #nama = p['ads_keyword']['item_basic']['name']
      harga = p['item_basic']['price']/100000
      hargaConvert = math.trunc(harga)
      sumSold = p['item_basic']['historical_sold']
      count+=1
      print('NO:', count, '\n*Nama SKU :', nama, '\n*Harga :', hargaConvert, '\n*Jumlah Penjualan:', sumSold,'\n*Muncul di Halaman :', page)
      writer = csv.writer(open('MAGPIE/{}_Shopee.csv'.format(key),'a',encoding="utf-8", newline=''))
      table_title = [count, nama, hargaConvert, sumSold, page]
      writer.writerow(table_title)


