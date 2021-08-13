# GeoIvan_CaseStudy
Case study 2 for scraping from Shopee.co.id

Asumsi:
1. Tidak memiliki pengalaman dalam web scraping.
2. Sulit dan pastinya akan ribet dan akan susah daripada case study 1.
3. Apakah request response website akan diterima atau tidak.
4. Gagal scraping atau tidak memuaskan hasil data scrapingnya.

Pembelajaran:
Selama 3 hari pengerjaan, saya dapat:

1. Memahami penggunaan library python untuk web scraping yaitu, requests, math, dan csv
2. Memahami bagaimana cara untuk mendapatkan request response 200, sehingga mendapatkan access ke website yang diinginkan.
3. Memahami dalam memparsing data dengan menggunakan metode yang berbeda dari case study yang pertama, dikarenakan menscraping dengan API dari Shopee
4. Memahami struktur website yang digunakan, yaitu .JSON dari situs Shopee.co.id
5. Teliti dalam memeriksa struktur .JSON, untuk menemukan Nama SKU, Harga, total penjualan, dan halaman produk.
6. Memahami dengan cukup baik untuk logika pada web scraping yang diminta dari soal case study kedua.
7. Memahami untuk merapikan data yang telah diparsing.
8. Memahami bagaimana scraping bisa dilakukan dengan memasukan dari beberapa keywords dan juga dari halaman awal hingga halaman yang diinginkan.
9. Memahami seluruh logika dan bagimana codingan itu bekerja dari awal hingga akhir
10. Meneliti dan diperiksa untuk data yang sudah diparsing dan dimasukkan ke dalam csv. Apakah data csv yang dihasilkan dari parsing itu sudah sesuai dengan website apa tidak (kecocokan) dan apakah sudah dapat mencetak halaman dimana produk barang di keywords brand tersebut ditampilkan.

Tantangan:
Dalam pengerjaan case study 1, sempat mengalami:

1. Berbeda dengan case study yang pertama dengan menggunakan HTML, sedangkan untuk case study yang kedua menggunakan format .JSON saat dipreview di inspeksi elemen di halaman situs Shopee.co.id
2. Kemudian untuk requests agar mendapatkan response 200 dari situs shopee, cara yang digunakan juga berbeda dari sebelumnya, pada case study kedua menggunakan query string parameter untuk menghasilkan response 200.
3. Sedikit kebingungan untuk mengambil dan menampilkan data untuk nama product, harga, dan histori penjualan yang dimana data tersebut di dalam sub bab dari format .JSON tersebut.
4. Bagaimana caranya menampilkan halaman yang sesuai dengan produknya pada saat di scraping.
5. Pada soal diminta produk konichiwa discrape hingga 10 kali, kemudian hasil output menghasilkan data yang berulang dikarenakan pada keywords brand konichiwa hanya terdapat 3 halaman saja di situs Shopee, sehingga pada saat discrape dan proses scraping berjalan dari halaman 1 kemudian selesai di halaman 3, maka scraping akan melooping terus hingga 10 halaman dan terdapat barang yang sama di dalam tabel tersebut. Bagaimana caranya menghentikan looping scraping saat halaman yang dibutuhkan tidak sesuai dengan halaman yang ada pada website itu sendiri.
6. Menghadapi masalah pada scraping keywords produk konichiwa saat scraping hanya sampai halaman perama muncul error dengan pengkodean yang terjadi saat saya mencoba mencetaknya, membaca / menulis atau membukanya. Dengan, menambahkan .encoding = "utf-8" akan membantu error pada terminal jika saya ingin mencetaknya hingga 10 kali.




