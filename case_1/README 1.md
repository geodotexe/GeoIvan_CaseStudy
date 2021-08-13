# GeoIvan_CaseStudy
Case study 1 for scraping Rajasusu.com

Asumsi:

1. Tidak memiliki pengalaman dalam web scraping.
2. Sulit dan pastinya akan ribet dan akan susah.
3. Apakah request response website akan diterima atau tidak.
4. Gagal scraping atau tidak memuaskan hasil data scrapingnya.

Pembelajaran:
Selama 3 hari pengerjaan, saya dapat:

1. Memahami penggunaan library python untuk web scraping yaitu, BeautifulSoup, requests, dan csv
2. Memahami bagaimana cara untuk mendapatkan request response 200, sehingga mendapatkan access ke website yang diinginkan.
3. Memahami dalam memparsing data menggunakan library BeautifulSoup
4. Memahami struktur website yang digunakan, yaitu HTML dari situs Rajasusu.com
5. Teliti dalam memeriksa struktur HTML, untuk mana yang Nama SKU, Harga, Kesediaan barang, situs URL.
6. Cukup memahami untuk bagaimana menampilkan data yang tidak ditampilkan oleh website.
7. Memahami dengan cukup baik untuk logika pada web scraping yang diminta dari soal case study 1.
8. Memahami untuk merapikan data yang telah diparsing.
9. Memahami bagaimana scraping bisa dilakukan dengan memasukan dari beberapa keywords dan juga dari halaman awal hingga halaman yang diinginkan.
10. Memahami seluruh logika dan bagimana codingan itu bekerja dari awal hingga akhir
11. Meneliti dan diperiksa untuk data yang sudah diparsing dan dimasukkan ke dalam csv. Apakah data csv yang dihasilkan dari parsing itu sudah sesuai dengan website apa tidak (kecocokan).

Tantangan:
Dalam pengerjaan case study 1, sempat mengalami:

1. Data ketersediaan stok dihidden dari website, dan saat saya parsing dengan classnya, sempat tidak muncul dan kosong nilainya. Sehingga, saya memiliki asumsi jika barang itu bisa dimasukan ke dalam keranjang, bisa terjadi kemungkinan bahwa stok barang tersebut itu ada (avaialable)
2. Sedikit kebingungan untuk mengambil dan menampilkan data untuk URL produk khusus pada brand tertentu, dan juga hasil yang ditampilkan ke dalam tabel kolom URL terdapat tiga bagian untuk menampilkan URL untuk produk khusus yang diminta. Jadi, saya menscraping dengan keywords merk/brand product yang diminta dari URL tersebut agar URL tersebut dapat muncul pada saat keywords brand tersebut discrape


