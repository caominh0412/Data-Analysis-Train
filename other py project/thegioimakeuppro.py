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
from colorama import Fore
from colorama import Style
import colorama
colorama.init()
urls = ['NFB99*https://thegioimakeuppro.com/tay-trang-mat-moi-nyx-professional-makeup-eye-lip-makeup-remover-elmur',
]


filename = 'image.csv'
downloadfolder = 'makeup'
folder = 'C:/Users/minhcq/Desktop/download/'+downloadfolder


def getImage(item_link):
	itemfolder=item_link.split('*')[0]
	item_link = item_link.split('*')[1]
	item = dict()
	session = HTMLSession()
	item_session = session.get(item_link)
	item_session.html.render(timeout=20,sleep=3,wait=2)
	SKUs =  item_session.html.find('.swatch-hai')
	if len(SKUs) > 0:
		i = 0
		for SKU in SKUs:
			item['swatch'+str(i)] = SKU.attrs['value']
			if item['swatch'+str(i)].find(itemfolder) != -1:
				item['image'+str(i)] = 'https:'+ SKU.attrs['data-large-img'].split('?')[0]		
				makemydir(folder+'/'+itemfolder)
				imgdownload = folder+'/'+itemfolder+'/'+'image.jpg'
				#print('SKU: '+ item['swatch'+str(i)] +'------ Image: '+item['image'+str(i)] + '------ Downloading: '+ imgdownload)
				try:
					urllib.request.urlretrieve(item['image'+str(i)],imgdownload)           
				except:
					print(f'{Fore.red}Error downloading- '+ item['swatch'+str(i)]+f'{Style.RESET_ALL}')
					pass
				i+=1
	else:
		try:
			name = item_session.html.find('h1[class="product-name"]')[0].text
			image ='https:' + item_session.html.find('.cloud-zoom,checkurl')[0].attrs['href'].split('?')[0]
			item['swatch'] = name
			item['image'] = image
			try:
				makemydir(folder+'/'+itemfolder)
				imgdownload = folder+'/'+itemfolder+'/'+'image.jpg'
				#print('SKU: '+ item['swatch']+ ' ---- Image: '+item['image'] + ' ---- Downloading: '+imgdownload)
				urllib.request.urlretrieve(item['image'],imgdownload)
			except:
				print(f'{Fore.GREEN}Error - '+ item['swatch']+f'{Style.RESET_ALL}')
				pass
		except:
			print(f'{Fore.RED}Error geting info - ' + itemfolder+f'{Style.RESET_ALL}')		
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


if __name__ == '__main__':
    pool = Pool(processes=4)
    outputs = pool.map(getImage,urls)
    pool.close()
    pool.join()
    print('DONE')

