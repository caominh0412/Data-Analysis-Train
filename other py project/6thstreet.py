from requests_html import HTMLSession
from multiprocessing import Pool 
import urllib.request
import os


filename = 'image.csv'
downloadfolder = 'dunelondon'
folder = 'C:/Users/minhcq/Desktop/download/'+downloadfolder


def getImage(item_link):
	item = dict()
	session = HTMLSession()
	item_session = session.get(item_link)
	item_session.html.render(timeout=20,sleep=3,wait=2)
	SKU = item_session.html.find('.mb1-5,f-13')[0].text
	SKU = SKU[16:]
	images = item_session.html.find('.amp-slide,amp-seen,amp-visible,amp-selected')
	for image in images:
		image_link = image.find('img')[0].attrs['src']
		image_link = image_link[:image_link.find('?')]
		imgdownload = folder + '/' + SKU + '/' + str(image_link.split('/')[-1]) + '.jpg'
		try:
			makemydir(folder+'/'+SKU)
			print('SKU: '+ SKU + '---- IMAGE: '+ image_link + '------- Downloading: '+ imgdownload)
			urllib.request.urlretrieve(image_link,imgdownload)
		except:
			print('Error: ' + image_link+ '----' + imgdownload)
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