from getImage import getImage,getlink,getPrice,gettotalpage,makemydir
from multiprocessing import Pool
import urllib.request

filename = 'thienanh.csv'
url =  'https://www.adayroi.com/m-a-c-br12841'
f = open(filename, "w", encoding="utf-8")
f.write("")
if __name__ == '__main__':
	totalpage = int(gettotalpage(url))
	items =[]
	for i in range(1,int(totalpage)+1):
		print('Page '+str(i-1))
		urlpage = url +'?page='+str(i-1)
		print(urlpage)
		items = items + getlink(urlpage)
	pool = Pool(processes=4)
	outputs = pool.map(getImage,items)
	pool.close()
	pool.close()
	pool.join()
	f = open(filename, "w", encoding="utf-8")
	f.write("")
	for item in outputs:
		print('SKU: '+ item['SKU'])
		f.write(item['barcode'])
		for i in range(0,len(item)-1):
			f.write('*'+item['image'+str(i)])
			#print(' Image: '+item['image'+str(i)])
		f.write('*'+item['short_des'])
		f.write('*'+item['long_des'])
		f.write('\n')
	print('DONE')
