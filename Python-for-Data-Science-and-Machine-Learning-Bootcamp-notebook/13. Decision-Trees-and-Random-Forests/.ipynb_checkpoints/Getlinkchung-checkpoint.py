from requests_html import HTMLSession
from multiprocessing import Pool 
import urllib.request
import os
import flickrapi
import flickr_download
import pandas as pd
flickr=flickrapi.FlickrAPI('11b99b3dea83234ce76bcd877a334c74', 'b12284268485a0c1', cache=True)

import urllib.request
class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.69 Safari/537.36"
urllib._urlopener = AppURLopener()


#--------------------------------CONFIG-----------------------------
debug = 2

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

url = ['89346140150252*https://nhanvan.vn/images/detailed/34/S%E1%BB%AFa_%C4%90%E1%BA%ADu_N%C3%A0nh_Fami_Nguy%C3%AAn_Ch%E1%BA%A5t_H%E1%BB%99p_200ml_cx21-e5.jpg;https://s1.marquis.vn/assets/2017/2017-11/73ce8fa41e9dab53ab6211ce17683a83.jpg;https://cdn.tgdd.vn/Products/Images/2943/80495/bhx/sua-dau-nanh-fami-hop-200ml-loc-3-org.jpg',
 '89346140217439*http://data.chonghanggia.vn/wp-content/uploads/image-99.jpeg;https://s1.marquis.vn/assets/2017/2017-10/6c64db81cacad8565f7a0175c43dfb7e.jpg;https://cdn.tgdd.vn/Products/Images/2943/86166/sdn-fami-canxi-hop-200ml-thung-4.jpg',
 '89346140300422*https://media-ak.static-adayroi.com/820_820/80/had/h59/9523697254430.jpg;https://media-ak.static-adayroi.com/820_820/80/h35/hfd/9523920699422.jpg;https://cdn02.static-adayroi.com/0/2017/01/10/1484045988084_3731437.jpg',
 '89346140216752*https://www.adayroi.com/sua-dau-nanh-fami-kid-huong-so-co-la-vinasoy-loc-6-hop-x-200ml-p-PRI145484?offer=PRI145484_CHK&search=H%E1%BB%99p%20Fami%20Kid%20Socola%20200ml',
 '89346140216822*https://www.adayroi.com/sua-dau-nanh-vi-so-co-la-fami-kid-vinasoy-loc-4-hop-x-125ml-p-PRI11722',
 '89346140301892*https://www.adayroi.com/sua-dau-nanh-fami-go-vi-dau-do-nep-cam-3-hop-x-200ml-p-2057166?offer=2057166_CHK&refSearch=search_offer&refKeyword=h%E1%BB%99p+fami%20go%20%C4%91%E1%BA%ADu%20%C4%91%E1%BB%8F%20n%E1%BA%BFp%20c%E1%BA%A9m%20200ml&refPage=Product',
 '89346140302262*https://www.adayroi.com/sua-dau-nanh-fami-go-vi-me-den-nep-cam-3-hop-x-200ml-p-2057170?offer=2057170_CHK&search=H%E1%BB%99p%20Fami%20Go%20m%C3%A8%20%C4%91en%20n%E1%BA%BFp%20c%E1%BA%A9m%20200ml',
 '89346140216512*https://www.adayroi.com/sua-dau-nanh-nguyen-chat-vinasoy-loc-6-hop-x-200ml-p-PRI145425?offer=PRI145425_CHK&search=H%E1%BB%99p%20Vinasoy%20nguy%C3%AAn%20ch%E1%BA%A5t%20200ml']
downloadfolder = 'nhua cho lon 3'
filename= downloadfolder + '.csv'
folder = 'C:/Users/minhcq/Desktop/download/'+downloadfolder

def passthing(excel):
	df = pd.read_excel(excel)
	df.dropna(axis=1,inplace=True,how='all')
	print(df.head())
	row = input('Columns :')
	df.columns=df.iloc[int(row)]
	for i in range(0,int(row)+1):
		df.drop(i,axis=0,inplace=True)
	print(df.head())
	for i in df.columns:
		try:
			a = df[i].iloc[1]
			#print(a)
			if (a.find('https') >= 0):
				link = i
		except:
			continue
	return df,link

def getImg_frompandas(df,sku,link):
	item =[] 
	#return params = str(SKU) + "*" + str(link)
	for i in df.index:
		item.append("{}*{}".format(df[sku].loc[i],df[link].loc[i]))
	return item

#def
def getImage(params,folder):
	if params.find('*') >0:
		item_link = params.split('*')[1]
		saveas = params.split('*')[0]
	else:
		item_link = params
		saveas = ''
	print('PROCESSING: '+ item_link)
	item = dict()
	if item_link.find('flickr.com') >=0:
		item['SKU'] =saveas
		photo_id = item_link.split('/')[5]
		a =	flickr.photos.getSizes(photo_id=photo_id)[0].find('./size/[@label="Original"]').attrib['source']
		item['image0'] = a
	elif (item_link.find(';') >=0 ):
		item['SKU'] = saveas
		link_split = item_link.split(';')
		for i,k in enumerate(link_split):
			item['image'+str(i)] = k
	else:
		session = HTMLSession()	
		item['SKU'] = saveas
		if item_link.find('adayroi.com') >=0:
			item_session = session.get(item_link)
			item_session.html.render(timeout=20,sleep=3,wait=2)
			if saveas != '':
				item_SKU = item_session.html.find('.panel-serial-number')[0].text
				SKU = item_SKU[8:item_SKU.find(' - ')]
			#barcode = item_SKU[item_SKU.find('Mã SKU: ')+8:item_SKU.find(')')-1]
			#item['barcode'] = barcode
			item['SKU'] = SKU
			images = item_session.html.find('.theatre-image__list-item')
			#item['short_des'] = item_session.html.find('.short-des__content')[0].text
			#item['long_des'] = item_session.html.find('.product-detail__description')[0].text
			i = 0
			#print(SKU)
			if len(images) != 0:
				for image in images:
					image_link=image.find('img')[0].attrs['src']
					#image_link = image[image.find('data-zoom-image')+17:image.find("'>")]
					image_link = image_link.replace('348_502','762_1100')
					item['image'+str(i)] = image_link
					i+=1
				#print(item_link+'          '+ item['SKU'] + '   Image Count: '+str(i))    
			if len(images) == 0:	
				images = item_session.html.find('.gallery-thumbnail__item-image')
				for image in images:
					image_link = image.attrs['data-zoom-image']
					item['image'+str(i)] = image_link
					i+=1
			#print(item_link+'          '+ item['SKU'] + '   Image Count: '+str(i))
		elif item_link.find('tiki') >= 0:
			item_session = session.get(item_link,verify = False)
			item_session.html.render()		
			if saveas != '':
				SKU = item_session.html.find('.item-sku')[0].text
				item['SKU'] = SKU[SKU.find('\n')+1:]
			images = item_session.html.find('.flx')
			i = 0
			for image in images:
				image_link = image.find('img')[0].attrs['src']
				image_link = image_link.replace('75x75','w1200')
				item['image'+str(i)] = image_link
				i+=1
		elif item_link.find('elmich.vn') >= 0:
			item_session = session.get(item_link)
			item_session.html.render(timeout=20,sleep=3,wait=2)
			images = item_session.html.find('.lSGallery')[0].find('img')
			i = 0
			for image in images:
				image_link = image.find('img')[0].attrs['src']
				item['image'+str(i)] = 'https://elmich.vn'+ image_link
				i+=1
		elif item_link.find('lazada.vn') >=0:
			item_session = session.get(item_link)
			item_session.html.render(timeout=20,sleep=3,wait=2)
			images = item_session.html.find('.item-gallery__thumbnail-image')
			i = 0
			for image in images:
				image_link = image.attrs['src']
				item['image'+str(i)] = 'https:'+image_link[:image_link.find('.jpg')+4]
				i+=1
		elif item_link.find('shopee.vn') >=0:
			item_session = session.get(item_link)
			item_session.html.render(timeout=20,sleep=3,wait=2)
			images = item_session.html.find('._3XaILN')
			i = 0
			for image in images:
				a = image.attrs['style']
				item_link = a[a.find('url')+5:a.find(');')-1]
				item['image'+str(i)] = item_link[:-3]
				i+=1							
		elif item_link.find('noithathoanmy.com.vn') >=0:
			item_session = session.get(item_link)
			item_session.html.render(timeout=20,sleep=3,wait=2)
			images = item_session.html.find('.flickity-lazyloaded')
			i = 0
			for image in images:
				a = image.attrs['src']
				item_link = a.replace('155755884cefe51827e3bd79057a4762','10f519365b01716ddb90abc57de5a837')
				item['image'+str(i)] = item_link
				i+=1	
		elif item_link.find('sapakitchen.vn') >=0:
			item_session = session.get(item_link)
			item_session.html.render(timeout=20,sleep=3,wait=2)
			images = item_session.html.find('.slick-slide')
			i = 0
			for image in images:
				a = image.find('img')[0].attrs['src']
				item_link = a.replace('thumbs-428-428-0--1/','')
				item['image'+str(i)] = item_link
				i+=1
		elif item_link.find('nhuacholon') >= 0:
			item_session = session.get(item_link)
			item_session.html.render()
			images = item_session.html.find('.item_pic_thumb')
			if images != '':
				i = 0
				for image in images:
					item['image'+str(i)] = 'http://nhuacholon.com.vn'+image.find('img')[0].attrs['src'].replace('thumbs/53_','')				
					print(item['image'+str(i)])
					i+=1
			else:
				item['image1'] = 'http://nhuacholon.com.vn' + item_session.html.find('.ad-image')[0].find('a')[0].attrs['href']
				print(item['image1'])
			#print(str(SKU)+' - '+item_link)
		elif item_link.find('handskid') >0:
			item_session = session.get(item_link)
			images = item_session.html.find('.product-block')
			i = 0
			for image in images:
				item_link = image.find('img')[0].attrs['src']
				if item_link.find('275')<0:
					item['image'+str(i)] = item_link.replace('483x483','700x700')
				i+=1
			if len(item)==1:
				item_session.html.render()
				x = item_session.html.find('.zoomWindowContainer')
				a = str(x[0].find('div')[1])
				item['image0'] = a[a.find('url')+5:a.find('");')]
		elif item_link.find('anmy') >0:
			item_session = session.get(item_link,verify=False)
			images = item_session.html.find('.thumbnail-item')
			i = 0
			for image in images:
				item_link = image.find('img')[0].attrs['src']
				item['image'+str(i)] ='https:' + item_link
				i+=1	
		else:
			print("ERROR - Cant get link " + item_link )
		session.close()
	if len(item)>1:				
		for i in range(0,len(item)-1):
			try:
				if saveas == '':
					saveas = item['SKU']
				#print('SKU: '+ SKU)
				imgdownload = folder+'/'+saveas+'/'+item['image'+str(i)].split('/')[-1]
				#imgdownload = folder+'/'+barcode+'/'+SKU+'_'+str(i+1)+'.jpg'
				if os.path.exists(imgdownload) == False:
					try:
						makemydir(folder+'/'+saveas)
					except:
						pass
					print('SKU: '+ item['SKU'] +'------ Image: '+item['image'+str(i)] + '------ Downloading: '+ imgdownload)
					urllib._urlopener.retrieve(item['image'+str(i)],imgdownload)           
			except Exception as e:
				print('Error '+ str(e) + ' - '+ item['image'+str(i)] + ' -- ' + imgdownload + ' -- ')
				pass	
	return item

def makemydir(whatever):
	try:
		if os.path.exists(whatever):
			pass
		else:
			os.makedirs(whatever)
	except:
		pass
  # let exception propagate if we just can't
  # cd into the specified directory
		os.chdir(whatever)

