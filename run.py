import requests
import csv

#This for input key
# key = input('Masukan key : ')

#Write data from key to csv
# write = csv.writer(open('hasil/{}.csv'.format(key), 'w', newline=''))
# column = []

'''
This is domain bukalapak, in categories fullbike bicycle.
For get url, open inspect element in browser open network and click headers
For get query string scroll down find query string parameter
'''

page = input("Page : ")
key = input("Keyword : ")

#This for create file.csv
write = csv.writer(open('data-csv/{}.csv'.format(key), 'w', newline=''))
header = ['Nama', 'Harga', 'Stok', 'kota']
write.writerow(header)

count = 0
url = 'https://api.bukalapak.com/multistrategy-products?prambanan_override=true&category_id=242&sort=bestselling&limit=50&offset=0&page=1&facet=true&access_token=UqeubsgkJfWGwu4oFrM948AnYiEq8wClpTFcb4otWvmW3g'
parameter = {
    'prambanan_override': True,
    'category_id': 242,
    'sort': 'bestselling',
    'limit': 50,
    'offset': 0,
    'page': page,
    'facet': True,
    'access_token': 'Please login'
}

#This for request to url
r = requests.get(url, params=parameter).json()

#This is take data from json
products = r['data']

for p in products:
    nama = p['name']
    harga = p['price']
    stok = p['stock']
    kota = p['store']['address']['city']
    count += 1
    print('count: ', count, 'nama : ', nama, 'harga : ', harga, 'stok : ', stok, 'store: ', kota)

    #This for add product to file csv
    write = csv.writer(open('data-csv/{}.csv'.format(key), 'a', newline=''))
    data = [nama, harga, stok, kota]
    write.writerow(data)
