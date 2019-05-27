from requests_html import HTMLSession
from multiprocessing import Pool 
import urllib.request
import os


filename = 'benew.csv'
downloadfolder = 'benew'
folder = 'C:/Users/minhcq/Desktop/download/'+downloadfolder

def getImage(item):
	SKU = item[:item.find('*')]
	item_link = item[item.find('*')+1:]
	item = dict()
	session = HTMLSession()
	item_session = session.get(item_link)
	item_session.html.render(timeout=20,sleep=3,wait=2)
	item['SKU'] = str(SKU)
	images = item_session.html.find('.img-thumb-detail')
	i = 0
	for image in images:
		image_link ='http://www.benew.vn' + image.attrs['src']  
		item['image'+str(i)] = image_link
		i+=1
	print(item_link+'          '+ item['SKU'] + '   Image Count: '+str(i))
	for i in range(0,len(item)-1):
		try:
			#print('SKU: '+ SKU)
			makemydir(folder+'/'+SKU)
			imgdownload = folder+'/'+SKU+'/'+item['image'+str(i)].split('/')[-1]
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

urls = ['8809511190734*http://www.benew.vn/san-pham/sua-tam-nuoc-hoa-trang-da-benew-perfume-moisture-rich-body-cleanser-white-milk-500ml.html',
'8809563060962*http://www.benew.vn/san-pham/mascara-chuot-mi-cao-cap-han-quoc-benew-collagen-perfect-volume.html',
'8809511190727*http://www.benew.vn/san-pham/phan-phu-ngu-coc-han-quoc-benew-cereal-perfect-brightening-two-way-cake-13.html',
'8809511190024*http://www.benew.vn/san-pham/kem-lot-nen-trang-diem-bb-cao-cap-benew-special-snail.html',
'8809511190574*http://www.benew.vn/san-pham/kem-trang-diem-cao-cap-benew-special-c-c-cream.html',
'8809511190666*http://www.benew.vn/san-pham/kem-trang-diem-ma-thuat-bb-benew-magic-snow-white.html',
'8809511190536_03*http://www.benew.vn/san-pham/son-duong-moi-chong-tham-co-mau-benew-natural-herb-lip-balm-lb03.html',
'8809511190536_02*http://www.benew.vn/san-pham/son-duong-co-mau-chong-tham-moi-benew-natural-herb-lip-balm-lb02.html',
'8809511190536_01*http://www.benew.vn/san-pham/son-duong-co-mau-chong-tham-moi-benew-natural-herb-lip-balm-lb01.html',
'8809233803011_1*http://www.benew.vn/san-pham/son-li-sieu-mem-muot-benew-perfect-kissing-lipstick-01-pop-pink.html',
'8809233803011_2*http://www.benew.vn/san-pham/son-li-sieu-mem-muot-benew-perfect-kissing-lipstick-02-real-red.html',
'8809233803011_3*http://www.benew.vn/san-pham/son-li-sieu-mem-muot-benew-perfect-kissing-lipstick-03-kissing-red.html',
'8809233803011_4*http://www.benew.vn/san-pham/son-li-sieu-mem-muot-benew-perfect-kissing-lipstick-04-baby-orange.html',
'8809233803011_5*http://www.benew.vn/san-pham/son-li-sieu-mem-muot-benew-perfect-kissing-lipstick-05-cute-orange.html',
'8809233803011_6*http://www.benew.vn/san-pham/son-li-sieu-mem-muot-benew-perfect-kissing-lipstick-06-baby-pink.html',
'8809511190673*http://www.benew.vn/san-pham/nuoc-tay-trang-duong-am-benew-make-up-remover.html',
'8809511190789*http://www.benew.vn/san-pham/mieng-tay-trang-cao-cap-tra-xanh-benew-make-up-remover-pads.html',
'8809511190703*http://www.benew.vn/san-pham/sua-duong-the-trang-da-benew-whitening-body-lotion.html',
'8809511190581*http://www.benew.vn/san-pham/bo-10-mieng-dap-mat-na-benew-natural-herb-mask-pack-aloe.html',
'8809511190598*http://www.benew.vn/san-pham/bo-10-mieng-dap-mat-na-benew-natural-herb-mask-pack-green-tea.html',
]

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