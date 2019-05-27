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
debug = 1

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

url = ['7584701501-1*https://anmy.com.vn/products/ozium-air-sanitizer-spray-3-5-oz-99g-original-ozm-1',
 '7584701501-2*https://anmy.com.vn/products/ozium-air-sanitizer-spray-3-5-oz-99g-original-ozm-1',
 '7584701501-4*https://anmy.com.vn/products/ozium-air-sanitizer-spray-3-5-oz-99g-original-ozm-1',
 '7584701522-1*https://anmy.com.vn/products/ozium-air-sanitizer-spray-3-5-oz-99g-new-car-ozm-22',
 '7584701522-2*https://anmy.com.vn/products/ozium-air-sanitizer-spray-3-5-oz-99g-new-car-ozm-22',
 '7584701522-4*https://anmy.com.vn/products/ozium-air-sanitizer-spray-3-5-oz-99g-new-car-ozm-22',
 '1991203528-1*https://anmy.com.vn/products/ozium-air-sanitizer-spray-3-5-oz-99g-country-fresh-ozm-15',
 '1991203528-2*https://anmy.com.vn/products/ozium-air-sanitizer-spray-3-5-oz-99g-country-fresh-ozm-15',
 '1991203528-4*https://anmy.com.vn/products/ozium-air-sanitizer-spray-3-5-oz-99g-country-fresh-ozm-15',
 '7584701523-1*https://anmy.com.vn/products/ozium-air-sanitizer-spray-3-5-oz-99g-vanilla-ozm-23',
 '7584701523-2*https://anmy.com.vn/products/ozium-air-sanitizer-spray-3-5-oz-99g-vanilla-ozm-23',
 '7584701523-4*https://anmy.com.vn/products/ozium-air-sanitizer-spray-3-5-oz-99g-vanilla-ozm-23',
 '7584701531-1*https://anmy.com.vn/products/ozium-air-sanitizer-spray-3-5-oz-99g-outdoor-essence-ozm-31',
 '7584701531-2*https://anmy.com.vn/products/ozium-air-sanitizer-spray-3-5-oz-99g-outdoor-essence-ozm-31',
 '7584701531-4*https://anmy.com.vn/products/ozium-air-sanitizer-spray-3-5-oz-99g-outdoor-essence-ozm-31',
 '7584751001-1*https://anmy.com.vn/products/ozium-air-sanitizer-spray-0-8-oz-22-6g-original-oz-1',
 '7584751001-2*https://anmy.com.vn/products/ozium-air-sanitizer-spray-0-8-oz-22-6g-original-oz-1',
 '7584751001-4*https://anmy.com.vn/products/ozium-air-sanitizer-spray-0-8-oz-22-6g-original-oz-1',
 '7584751001-6*https://anmy.com.vn/products/ozium-air-sanitizer-spray-0-8-oz-22-6g-original-oz-1',
 '7584751015-1*https://anmy.com.vn/products/ozium-air-sanitizer-spray-0-8-oz-22-6g-country-fresh-oz-15',
 '7584751015-2*https://anmy.com.vn/products/ozium-air-sanitizer-spray-0-8-oz-22-6g-country-fresh-oz-15',
 '7584751015-4*https://anmy.com.vn/products/ozium-air-sanitizer-spray-0-8-oz-22-6g-country-fresh-oz-15',
 '7584751015-6*https://anmy.com.vn/products/ozium-air-sanitizer-spray-0-8-oz-22-6g-country-fresh-oz-15',
 '7584751022-1*https://anmy.com.vn/products/ozium-air-sanitizer-spray-0-8-oz-22-6g-new-car-oz-22',
 '7584751022-2*https://anmy.com.vn/products/ozium-air-sanitizer-spray-0-8-oz-22-6g-new-car-oz-22',
 '7584751022-4*https://anmy.com.vn/products/ozium-air-sanitizer-spray-0-8-oz-22-6g-new-car-oz-22',
 '7584751022-6*https://anmy.com.vn/products/ozium-air-sanitizer-spray-0-8-oz-22-6g-new-car-oz-22',
 '7584751023-1*https://anmy.com.vn/products/ozium-air-sanitizer-spray-0-8-oz-22-6g-vanilla-oz-23',
 '7584751023-2*https://anmy.com.vn/products/ozium-air-sanitizer-spray-0-8-oz-22-6g-vanilla-oz-23',
 '7584751023-4*https://anmy.com.vn/products/ozium-air-sanitizer-spray-0-8-oz-22-6g-vanilla-oz-23',
 '7584751023-6*https://anmy.com.vn/products/ozium-air-sanitizer-spray-0-8-oz-22-6g-vanilla-oz-23',
 '7584751031-1*https://anmy.com.vn/products/ozium-air-sanitizer-spray-0-8-oz-22-6g-outdoor-essence-oz-31',
 '7584751031-2*https://anmy.com.vn/products/ozium-air-sanitizer-spray-0-8-oz-22-6g-outdoor-essence-oz-31',
 '7584751031-4*https://anmy.com.vn/products/ozium-air-sanitizer-spray-0-8-oz-22-6g-outdoor-essence-oz-31',
 '7584751031-6*https://anmy.com.vn/products/ozium-air-sanitizer-spray-0-8-oz-22-6g-outdoor-essence-oz-31',
 '7584751062-1*https://anmy.com.vn/products/ozium-air-sanitizer-spray-0-8-oz-22-6g-citrus-oz-62',
 '7584751062-2*https://anmy.com.vn/products/ozium-air-sanitizer-spray-0-8-oz-22-6g-citrus-oz-62',
 '7584751062-4*https://anmy.com.vn/products/ozium-air-sanitizer-spray-0-8-oz-22-6g-citrus-oz-62',
 '7584751062-6*https://anmy.com.vn/products/ozium-air-sanitizer-spray-0-8-oz-22-6g-citrus-oz-62',
 '1991202034-1*https://anmy.com.vn/products/nhan-ban-cua-ozium-air-sanitizer-gel-4-5-oz-127g',
 '1991202034-2*https://anmy.com.vn/products/nhan-ban-cua-ozium-air-sanitizer-gel-4-5-oz-127g',
 '1991202034-4*https://anmy.com.vn/products/nhan-ban-cua-ozium-air-sanitizer-gel-4-5-oz-127g',
 '1991202035-1*https://anmy.com.vn/products/ozium-air-sanitizer-gel-4-5-oz-127g-outdoor-essence',
 '1991202035-2*https://anmy.com.vn/products/ozium-air-sanitizer-gel-4-5-oz-127g-outdoor-essence',
 '1991202035-4*https://anmy.com.vn/products/ozium-air-sanitizer-gel-4-5-oz-127g-outdoor-essence',
 '1991203930-1*https://anmy.com.vn/products/ozium-air-sanitizer-gel-4-5-oz-127g-citrus',
 '1991203930-2*https://anmy.com.vn/products/ozium-air-sanitizer-gel-4-5-oz-127g-citrus',
 '1991203930-4*https://anmy.com.vn/products/ozium-air-sanitizer-gel-4-5-oz-127g-citrus',
 '1991203876-1*https://anmy.com.vn/products/scents-luxe-vent-rose-gold-806332',
 '1991203876-2*https://anmy.com.vn/products/scents-luxe-vent-rose-gold-806332',
 '1991203876-4*https://anmy.com.vn/products/scents-luxe-vent-rose-gold-806332',
 '1991203876-6*https://anmy.com.vn/products/scents-luxe-vent-rose-gold-806332',
 '1991204255-1*https://anmy.com.vn/products/scents-luxe-vent-brushed-silver-806711',
 '1991204255-2*https://anmy.com.vn/products/scents-luxe-vent-brushed-silver-806711',
 '1991204255-4*https://anmy.com.vn/products/scents-luxe-vent-brushed-silver-806711',
 '1991204255-6*https://anmy.com.vn/products/scents-luxe-vent-brushed-silver-806711',
 '1991204253-1*https://anmy.com.vn/products/scents-luxe-vent-carbon-fiber-806709',
 '1991204253-2*https://anmy.com.vn/products/scents-luxe-vent-carbon-fiber-806709',
 '1991204253-4*https://anmy.com.vn/products/scents-luxe-vent-carbon-fiber-806709',
 '1991204253-6*https://anmy.com.vn/products/scents-luxe-vent-carbon-fiber-806709',
 '1991204254-1*https://anmy.com.vn/products/scents-luxe-vent-burlwood-806710',
 '1991204254-2*https://anmy.com.vn/products/scents-luxe-vent-burlwood-806710',
 '1991204254-4*https://anmy.com.vn/products/scents-luxe-vent-burlwood-806710',
 '1991204254-6*https://anmy.com.vn/products/scents-luxe-vent-burlwood-806710',
 '7584711300-1*https://anmy.com.vn/products/scents-vent-oil-newcar-vntfr-22',
 '7584711300-2*https://anmy.com.vn/products/scents-vent-oil-newcar-vntfr-22',
 '7584711300-4*https://anmy.com.vn/products/scents-vent-oil-newcar-vntfr-22',
 '7584711301-1*https://anmy.com.vn/products/scents-vent-oil-outdoor-breeze-vntfr-28',
 '7584711301-2*https://anmy.com.vn/products/scents-vent-oil-outdoor-breeze-vntfr-28',
 '7584711301-4*https://anmy.com.vn/products/scents-vent-oil-outdoor-breeze-vntfr-28',
 '7584711548-1*https://anmy.com.vn/products/scents-vent-oil-vanilla-vntfr-33',
 '7584711548-2*https://anmy.com.vn/products/scents-vent-oil-vanilla-vntfr-33',
 '7584711548-4*https://anmy.com.vn/products/scents-vent-oil-vanilla-vntfr-33',
 '7584711550-1*https://anmy.com.vn/products/gai-cua-gio-scents-vent-oil-island-colada-vntfr-44',
 '7584711550-2*https://anmy.com.vn/products/gai-cua-gio-scents-vent-oil-island-colada-vntfr-44',
 '7584711550-4*https://anmy.com.vn/products/gai-cua-gio-scents-vent-oil-island-colada-vntfr-44',
 '1991200228-1*https://anmy.com.vn/products/scents-vent-oil-after-midnight-800001641',
 '1991200228-2*https://anmy.com.vn/products/scents-vent-oil-after-midnight-800001641',
 '1991200228-4*https://anmy.com.vn/products/scents-vent-oil-after-midnight-800001641',
 '1991202076-1*https://anmy.com.vn/products/scents-vent-oil-lavender-vanilla-804323',
 '1991202076-2*https://anmy.com.vn/products/scents-vent-oil-lavender-vanilla-804323',
 '1991202076-4*https://anmy.com.vn/products/scents-vent-oil-lavender-vanilla-804323',
 '1991202078-1*https://anmy.com.vn/products/scents-vent-oil-strawberry-kiwi-804325',
 '1991202078-2*https://anmy.com.vn/products/scents-vent-oil-strawberry-kiwi-804325',
 '1991202078-4*https://anmy.com.vn/products/scents-vent-oil-strawberry-kiwi-804325',
 'ORG-001-1*https://anmy.com.vn/products/sap-thom-paradise-air-fresh-42g-cherry-org-001',
 'ORG-001-2*https://anmy.com.vn/products/sap-thom-paradise-air-fresh-42g-cherry-org-001',
 'ORG-001-4*https://anmy.com.vn/products/sap-thom-paradise-air-fresh-42g-cherry-org-001',
 'ORG-002-1*https://anmy.com.vn/products/paradise-air-fresh-42g-strawberry-org-002',
 'ORG-002-2*https://anmy.com.vn/products/paradise-air-fresh-42g-strawberry-org-002',
 'ORG-002-4*https://anmy.com.vn/products/paradise-air-fresh-42g-strawberry-org-002',
 'ORG-003-1*https://anmy.com.vn/products/paradise-air-fresh-42g-black-org-003',
 'ORG-003-2*https://anmy.com.vn/products/paradise-air-fresh-42g-black-org-003',
 'ORG-003-4*https://anmy.com.vn/products/paradise-air-fresh-42g-black-org-003',
 'ORG-004-1*https://anmy.com.vn/products/paradise-air-fresh-42g-vanilla-org-004',
 'ORG-004-2*https://anmy.com.vn/products/paradise-air-fresh-42g-vanilla-org-004',
 'ORG-004-4*https://anmy.com.vn/products/paradise-air-fresh-42g-vanilla-org-004',
 'ORG-007-1*https://anmy.com.vn/products/paradise-air-fresh-42g-new-car-org-007',
 'ORG-007-2*https://anmy.com.vn/products/paradise-air-fresh-42g-new-car-org-007',
 'ORG-007-4*https://anmy.com.vn/products/paradise-air-fresh-42g-new-car-org-007',
 'ORG-010-1*https://anmy.com.vn/products/paradise-air-fresh-42g-gold-org-010',
 'ORG-010-2*https://anmy.com.vn/products/paradise-air-fresh-42g-gold-org-010',
 'ORG-010-4*https://anmy.com.vn/products/paradise-air-fresh-42g-gold-org-010']
downloadfolder = 'anmy'
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

