from requests_html import HTMLSession
from multiprocessing import Pool 
import urllib.request
import os


filename = 'image.csv'
downloadfolder = 'tinviet_2'
folder = 'C:/Users/minhcq/Desktop/download/'+downloadfolder


def getImage(item_link):
	SKU=item_link[:item_link.find('*')]
	item_link = item_link[item_link.find('*')+1:]
	session = HTMLSession()
	item_session = session.get(item_link)
	item_session.html.render(timeout=20,sleep=3,wait=2)
	images = item_session.html.find('.mTSThumbContainer')
	for image in images:
		image_link = 'http:'+image.find('a')[0].attrs['data-image']
		imgdownload = folder + '/' + SKU + '/' + str(image_link.split('/')[-1])
		try:
			makemydir(folder+'/'+SKU)
			#print('SKU: '+ SKU + '---- IMAGE: '+ image_link + '------- Downloading: '+ imgdownload)
			urllib.request.urlretrieve(image_link,imgdownload)
		except:
			print('Error: ' + image_link+ ' ---- ' + imgdownload)
			pass
	images_contents = item_session.html.find('#description')[0].find('img')
	for images_content in images_contents:
		image_link = 'http:' + images_content.attrs['src']
		imgdownload = folder + '/' + SKU + '/' + str(image_link.split('/')[-1])
		try:
			makemydir(folder+'/'+SKU)
			#print('SKU: '+ SKU + '---- IMAGE: '+ image_link + '------- Downloading: '+ imgdownload)
			urllib.request.urlretrieve(image_link,imgdownload)
		except:
			print('Error: ' + image_link+ ' ---- ' + imgdownload)
			pass
	session.close()

def makemydir(whatever):
	try:
		os.makedirs(whatever)
	except OSError:
		pass
	# let exception propagate if we just can't
	# cd into the specified directory
	os.chdir(whatever)

urls = ['GE0201-01*http://silkygirl.com.vn/collections/mat/products/but-ke-mat-silkygirl-long-wearing-eyeliner',
'GE0201-02*http://silkygirl.com.vn/collections/mat/products/but-ke-mat-silkygirl-long-wearing-eyeliner',
'GE0211-01*http://www.silkygirl.com.vn/products/silkygirl-natural-eyeliner',
'GE0226-01*http://www.silkygirl.com.vn/products/ke-mat-silkygirl-perfect-stay-20hr-eyeliner',
'GE0226-02*http://www.silkygirl.com.vn/products/ke-mat-silkygirl-perfect-stay-20hr-eyeliner',
'GE0235-01*http://www.silkygirl.com.vn/products/ke-mat-nuoc-li-silkygirl-perfect-matte',
'GE0238-01*http://www.silkygirl.com.vn/products/ke-mat-nuoc-silkygirl-perfect-sharp-matte',
'GE0221-01*http://www.silkygirl.com.vn/products/mascara-silkygirl-big-eye-collagen-waterproof',
'GE0236-01*http://www.silkygirl.com.vn/products/mascara-silkygirl-eye-opener-waterproof',
'GE0230-01*http://www.silkygirl.com.vn/products/mascara-silkygirl-lash-prism-waterproof',
'GE0202-01*http://www.silkygirl.com.vn/products/but-ke-mat-silkygirl-natural-brow-pencil',
'GE0202-02*http://www.silkygirl.com.vn/products/but-ke-mat-silkygirl-natural-brow-pencil',
'GE0215-01*http://www.silkygirl.com.vn/products/chi-may-silkygirl-hi-definition-brow-liner',
'GE0215-02*http://www.silkygirl.com.vn/products/chi-may-silkygirl-hi-definition-brow-liner',
'GE0239-01*http://www.silkygirl.com.vn/products/chi-dinh-hinh-may-2-dau-silkygirl-perfect-brow-liner-powder',
'GE0239-02*http://www.silkygirl.com.vn/products/chi-dinh-hinh-may-2-dau-silkygirl-perfect-brow-liner-powder',
'GF0142-01*http://www.silkygirl.com.vn/products/tao-khoi-2-dau-silkygirl-photosharp-contour-highlighter',
'GF0142-02*http://www.silkygirl.com.vn/products/tao-khoi-2-dau-silkygirl-photosharp-contour-highlighter',
'GE0224-01*http://www.silkygirl.com.vn/products/phan-mat-2-o-silkygirl-double-intense',
'GE0224-03*http://www.silkygirl.com.vn/products/phan-mat-2-o-silkygirl-double-intense',
'GE0224-06*http://www.silkygirl.com.vn/products/phan-mat-2-o-silkygirl-double-intense',
'GE0237-01*http://www.silkygirl.com.vn/products/bang-phan-mat-6-mau-silkygirl-truly-nude',
'GE0237-02*http://www.silkygirl.com.vn/products/bang-phan-mat-6-mau-silkygirl-truly-nude',
'GF0107-01*http://www.silkygirl.com.vn/products/phan-phu-dang-bot-shine-free-loose-powder',
'GF0107-02*http://www.silkygirl.com.vn/products/phan-phu-dang-bot-shine-free-loose-powder',
'GF0119-01*http://www.silkygirl.com.vn/products/phan-phu-pure-smooth-pressed-powder-spf-20',
'GF0119-02*http://www.silkygirl.com.vn/products/phan-phu-pure-smooth-pressed-powder-spf-20',
'GF0132-01*http://www.silkygirl.com.vn/products/phan-phu-magic-bb-oil-control-spf-45-pa-mini-size',
'GF0132-02*http://www.silkygirl.com.vn/products/phan-phu-magic-bb-oil-control-spf-45-pa-mini-size',
'GF0135-01*http://www.silkygirl.com.vn/products/magic-bb-all-in-one-powder-foundation-spf-35-pa',
'GF0135-02*http://www.silkygirl.com.vn/products/magic-bb-all-in-one-powder-foundation-spf-35-pa',
'GF0136-01*http://www.silkygirl.com.vn/products/phan-nen-bb-white-chiffon',
'GF0136-02*http://www.silkygirl.com.vn/products/phan-nen-bb-white-chiffon',
'GF0141-01*http://www.silkygirl.com.vn/products/phan-nuoc-silkygirl-magic-bb-cushion-spf50-pa',
'GF0141-02*http://www.silkygirl.com.vn/products/phan-nuoc-silkygirl-magic-bb-cushion-spf50-pa',
'GF0143-01*http://www.silkygirl.com.vn/products/phan-phu-magic-bb-oil-control-spf-45-pa-mini-size',
'GF0143-02*http://www.silkygirl.com.vn/products/phan-phu-magic-bb-oil-control-spf-45-pa-mini-size',
'GF0144-01*http://www.silkygirl.com.vn/products/loi-bb-cushion-refill',
'GF0144-02*http://www.silkygirl.com.vn/products/loi-bb-cushion-refill',
'GF0109-01*http://www.silkygirl.com.vn/products/kem-nen-silkygirl-skin-perfect-liquid-foundation-spf-30-pa',
'GF0109-02*http://www.silkygirl.com.vn/products/kem-nen-silkygirl-skin-perfect-liquid-foundation-spf-30-pa',
'GF0146*http://www.silkygirl.com.vn/products/phan-phu-khoang-silkygirl-no-sebum-mineral-powder',
'GF0110-01*http://www.silkygirl.com.vn/products/phan-ma-hong-silkygirl-shimmer-duo',
'GF0110-02*http://www.silkygirl.com.vn/products/phan-ma-hong-silkygirl-shimmer-duo',
'GF0110-03*http://www.silkygirl.com.vn/products/phan-ma-hong-silkygirl-shimmer-duo',
'GF0145-01*http://www.silkygirl.com.vn/products/but-che-khuyet-diem-quick-fix-care-concealer',
'GF0145-02*http://www.silkygirl.com.vn/products/but-che-khuyet-diem-quick-fix-care-concealer',
'GL0004-01*http://www.silkygirl.com.vn/products/chi-vien-moi-silkygirl-long-wearing-lipliner',
'GL0004-02*http://www.silkygirl.com.vn/products/chi-vien-moi-silkygirl-long-wearing-lipliner',
'GL0004-03*http://www.silkygirl.com.vn/products/chi-vien-moi-silkygirl-long-wearing-lipliner',
'GL0004-05*http://www.silkygirl.com.vn/products/chi-vien-moi-silkygirl-long-wearing-lipliner',
'GL0010-03*http://www.silkygirl.com.vn/products/son-duong-co-mau-silkygirl-moisture-smooth-lipcolor',
'GL0010-07*http://www.silkygirl.com.vn/products/son-duong-co-mau-silkygirl-moisture-smooth-lipcolor',
'GL0010-09*http://www.silkygirl.com.vn/products/son-duong-co-mau-silkygirl-moisture-smooth-lipcolor',
'GL0010-12*http://www.silkygirl.com.vn/products/son-duong-co-mau-silkygirl-moisture-smooth-lipcolor',
'GL0010-13*http://www.silkygirl.com.vn/products/son-duong-co-mau-silkygirl-moisture-smooth-lipcolor',
'GL0010-14*http://www.silkygirl.com.vn/products/son-duong-co-mau-silkygirl-moisture-smooth-lipcolor',
'GL0010-15*http://www.silkygirl.com.vn/products/son-duong-co-mau-silkygirl-moisture-smooth-lipcolor',
'GL0025-03*http://www.silkygirl.com.vn/products/son-duong-co-mau-silkygirl-moisture-rich-lipcolor',
'GL0025-04*http://www.silkygirl.com.vn/products/son-duong-co-mau-silkygirl-moisture-rich-lipcolor',
'GL0025-05*http://www.silkygirl.com.vn/products/son-duong-co-mau-silkygirl-moisture-rich-lipcolor',
'GL0025-06*http://www.silkygirl.com.vn/products/son-duong-co-mau-silkygirl-moisture-rich-lipcolor',
'GL0025-07*http://www.silkygirl.com.vn/products/son-duong-co-mau-silkygirl-moisture-rich-lipcolor',
'GL0025-08*http://www.silkygirl.com.vn/products/son-duong-co-mau-silkygirl-moisture-rich-lipcolor',
'GL0025-11*http://www.silkygirl.com.vn/products/son-duong-co-mau-silkygirl-moisture-rich-lipcolor',
'GL0025-12*http://www.silkygirl.com.vn/products/son-duong-co-mau-silkygirl-moisture-rich-lipcolor',
'GL0025-13*http://www.silkygirl.com.vn/products/son-duong-co-mau-silkygirl-moisture-rich-lipcolor',
'GL0025-18*http://www.silkygirl.com.vn/products/son-duong-co-mau-silkygirl-moisture-rich-lipcolor',
'GL0025-25*http://www.silkygirl.com.vn/products/son-duong-co-mau-silkygirl-moisture-rich-lipcolor',
'GL0026-01*http://www.silkygirl.com.vn/products/son-duong-2-loi-silkygirl-moisture-balm',
'GL0026-02*http://www.silkygirl.com.vn/products/son-duong-2-loi-silkygirl-moisture-balm',
'GL0026-03*http://www.silkygirl.com.vn/products/son-duong-2-loi-silkygirl-moisture-balm',
'GL0026-04*http://www.silkygirl.com.vn/products/son-duong-2-loi-silkygirl-moisture-balm',
'GL0026-05*http://www.silkygirl.com.vn/products/son-duong-2-loi-silkygirl-moisture-balm',
'GL0026-06*http://www.silkygirl.com.vn/products/son-duong-2-loi-silkygirl-moisture-balm',
'GL0026-07*http://www.silkygirl.com.vn/products/son-duong-2-loi-silkygirl-moisture-balm',
'GL0026-08*http://www.silkygirl.com.vn/products/son-duong-2-loi-silkygirl-moisture-balm',
'GL0023-01*http://www.silkygirl.com.vn/products/son-kem-silkygirl-matte-junkie-lip-cream-12-enigma',
'GL0023-02*http://www.silkygirl.com.vn/products/son-kem-silkygirl-matte-junkie-lip-cream-12-enigma',
'GL0023-04*http://www.silkygirl.com.vn/products/son-kem-silkygirl-matte-junkie-lip-cream-12-enigma',
'GL0023-05*http://www.silkygirl.com.vn/products/son-kem-silkygirl-matte-junkie-lip-cream-12-enigma',
'GL0023-06*http://www.silkygirl.com.vn/products/son-kem-silkygirl-matte-junkie-lip-cream-12-enigma',
'GL0023-07*http://www.silkygirl.com.vn/products/son-kem-silkygirl-matte-junkie-lip-cream-12-enigma',
'GL0023-08*http://www.silkygirl.com.vn/products/son-kem-silkygirl-matte-junkie-lip-cream-12-enigma',
'GL0023-09*http://www.silkygirl.com.vn/products/son-kem-silkygirl-matte-junkie-lip-cream-12-enigma',
'GL0023-10*http://www.silkygirl.com.vn/products/son-kem-silkygirl-matte-junkie-lip-cream-12-enigma',
'GL0023-11*http://www.silkygirl.com.vn/products/son-kem-silkygirl-matte-junkie-lip-cream-12-enigma',
'GL0023-12*http://www.silkygirl.com.vn/products/son-kem-silkygirl-matte-junkie-lip-cream-12-enigma',
'GL0027-01*http://www.silkygirl.com.vn/products/son-li-sieu-min-silkygirl-omg-powder-matte-10-mauve',
'GL0027-02*http://www.silkygirl.com.vn/products/son-li-sieu-min-silkygirl-omg-powder-matte-10-mauve',
'GL0027-03*http://www.silkygirl.com.vn/products/son-li-sieu-min-silkygirl-omg-powder-matte-10-mauve',
'GL0027-04*http://www.silkygirl.com.vn/products/son-li-sieu-min-silkygirl-omg-powder-matte-10-mauve',
'GL0027-05*http://www.silkygirl.com.vn/products/son-li-sieu-min-silkygirl-omg-powder-matte-10-mauve',
'GL0027-06*http://www.silkygirl.com.vn/products/son-li-sieu-min-silkygirl-omg-powder-matte-10-mauve',
'GL0027-07*http://www.silkygirl.com.vn/products/son-li-sieu-min-silkygirl-omg-powder-matte-10-mauve',
'GL0027-08*http://www.silkygirl.com.vn/products/son-li-sieu-min-silkygirl-omg-powder-matte-10-mauve',
'GL0027-09*http://www.silkygirl.com.vn/products/son-li-sieu-min-silkygirl-omg-powder-matte-10-mauve',
'GL0027-10*http://www.silkygirl.com.vn/products/son-li-sieu-min-silkygirl-omg-powder-matte-10-mauve',
'GL0028-01*http://www.silkygirl.com.vn/products/son-duong-sieu-mau-silkygirl-lacquer',
'GL0028-02*http://www.silkygirl.com.vn/products/son-duong-sieu-mau-silkygirl-lacquer',
'GL0028-03 *http://www.silkygirl.com.vn/products/son-duong-sieu-mau-silkygirl-lacquer',
'GL0028-04*http://www.silkygirl.com.vn/products/son-duong-sieu-mau-silkygirl-lacquer',
'GL0028-05*http://www.silkygirl.com.vn/products/son-duong-sieu-mau-silkygirl-lacquer',
'GQ0403*http://www.silkygirl.com.vn/products/tay-trang-mat-va-moi-silkygirl-gentle-eye-lip-makeup-remover',
'GQ0402*http://www.silkygirl.com.vn/products/tay-trang-mat-va-moi-silkygirl-gentle-eye-lip-makeup-remover',
'GQ0408*http://www.silkygirl.com.vn/products/tay-trang-silkygirl-pure-fresh-gel-makeup-remover',
'GQ0410*http://www.silkygirl.com.vn/products/tay-trang-micellar-pure-fresh-all-in-one',
'GF0134-01*http://www.silkygirl.com.vn/products/che-khuyet-diem-thoi-mini-photo-perfect-concealer',
'GF0134-02*http://www.silkygirl.com.vn/products/che-khuyet-diem-thoi-mini-photo-perfect-concealer',
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