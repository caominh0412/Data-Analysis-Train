'''
Use this to copy
from requests_html import HTMLSession
from multiprocessing import Pool 
import urllib.request
import os
session = HTMLSession()
item_session = session.get(item_link)
item_session.html.render()

'''
from requests_html import HTMLSession
from multiprocessing import Pool 
import urllib.request
import os


def getImage(item_link):
	item = dict()
	session = HTMLSession()
	item_session = session.get(item_link)
	item_session.html.render(timeout=20,sleep=3,wait=2)
	SKU =  item_session.html.find('.fixw')[1].text
	item['SKU'] = SKU[SKU.find(':')+2:]
	images = item_session.html.find('img[id="img_giaykim"]')
	i = 0
	for image in images:
		image_link = image.attrs['src']
		image_link = image_link.replace('_thumbs/I','i')
		item['image'+str(i)] = image_link
		i+=1
	print(item_link+'          '+ item['SKU'] + '   Image Count: '+str(i))  
	for i in range(0,len(item)-1):
		try:
			#print('SKU: '+ SKU)
			makemydir(folder+'/'+item['SKU'])
			imgdownload = folder+'/'+item['SKU']+'/'+item['image'+str(i)].split('/')[-1]
			print('SKU: '+ SKU +'------ Image: '+item['image'+str(i)] + '------ Downloading: '+ imgdownload)
			urllib.request.urlretrieve(item['image'+str(i)],imgdownload)           
		except:
			print('Error - '+ SKU)
			pass
	session.close()
	return item

def makemydir(whatever):
	try:
		os.makedirs(whatever)
	except OSError:
		pass
  # let exception propagate if we just can't
  # cd into the specified directory
	os.chdir(whatever)

urls = ['http://babycolor.com.vn/san-pham/sach-vai-the-gioi-ky-dieu.html',
'http://babycolor.com.vn/san-pham/sach-vai-safari-mix-match.html',
'http://babycolor.com.vn/san-pham/sach-vai-be-thay-gi-nao.html',
'http://babycolor.com.vn/san-pham/xuc-xac-vui-nhon-pipovietnam.html',
'http://babycolor.com.vn/san-pham/sach-vai-dong-vat-an-thit.html',
'http://babycolor.com.vn/san-pham/sach-vai-canh-bao-bong.html',
'http://babycolor.com.vn/san-pham/sach-vai-canh-bao-nga.html',
'http://babycolor.com.vn/san-pham/sach-vai-canh-bao-nguy-hiem.html',
'http://babycolor.com.vn/san-pham/sach-vai-con-trung.html',
'http://babycolor.com.vn/san-pham/sach-vai-vong-quanh-the-gioi.html',
'http://babycolor.com.vn/san-pham/sach-kem-gam-nuou-chu-de-thoi-tiet.html',
'http://babycolor.com.vn/san-pham/sach-kem-gam-nuou-chu-de-dong-vat-nuoi.html',
'http://babycolor.com.vn/san-pham/sach-kem-gam-nuou-chu-de-hinh-khoi.html',
'http://babycolor.com.vn/san-pham/sach-kem-gam-nuou-chu-de-hoa-qua.html',
'http://babycolor.com.vn/san-pham/sach-kem-gam-nuou-chu-de-sinh-vat-bien.html'

]


filename = 'image.csv'
downloadfolder = '1-6'
folder = 'C:/Users/minhcq/Desktop/download/'+downloadfolder

if __name__ == '__main__':
    pool = Pool(processes=4)
    outputs = pool.map(getImage,urls)
    pool.close()
    pool.join()
    f = open(filename, "w", encoding="utf-8")
    f.write("")
    for item in outputs:
        print('SKU: '+ item['SKU'])
        f.write(item['SKU'])
        for i in range(0,len(item)-1):
            f.write('*'+item['image'+str(i)])
            print(' Image: '+item['image'+str(i)])
        f.write('\n')
    print('DONE')