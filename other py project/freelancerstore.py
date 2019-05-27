from requests_html import HTMLSession
from multiprocessing import Pool 
import urllib.request
import os

session = HTMLSession()
filename = 'image.csv'
downloadfolder = 'freelancer'
folder = 'C:/Users/minhcq/Desktop/download/'+downloadfolder

def getImage(item_link):
    item = dict()
    item_session = session.get(item_link,verify=False)
    SKU = item_session.html.find('.detail-sku')[0].text
    SKU = SKU[13:]
    item['SKU'] = SKU
    item['Link'] = item_link
    images = item_session.html.find('.xzoom-gallery')
    i = 0
    for image in images:
        image_link=image.attrs['src']
        #image_link = image[image.find('data-zoom-image')+17:image.find("'>")]
        item['image'+str(i)] = image_link
        i+=1
        #print(' Image : ' + image_link)
    #print(SKU)
    return item

def makemydir(whatever):
  try:
    os.makedirs(whatever)
  except OSError:
    pass
  # let exception propagate if we just can't
  # cd into the specified directory
  os.chdir(whatever)

def getlink(url):
    links = []
    url_session = session.get(url,verify=False)
    items = url_session.html.find('.produc')
    for item in items:
        try:
            item_link = item.find('.title')[1].find('a')[0].attrs['href']
        except IndexError:
            item_link = item.find('.title')[2].find('a')[0].attrs['href']
        links.append(item_link)
        print(item_link)
    return links


url =  'https://freelancerstores.vn/collections/john-henry'
f = open(filename, "w", encoding="utf-8")
f.write("")
if __name__ == '__main__':
    items =[]
    for i in range(2,30):
        print('Page '+str(i-1))
        urlpage = url +'?page='+str(i-1)
        print(urlpage)
        items = items + getlink(urlpage)
    pool = Pool(processes=4)
    outputs = pool.map(getImage,items)
    pool.close()
    pool.join()
    pool.close()
    for item in outputs:
        print('SKU: '+ item['SKU'])
        f.write(item['SKU'])
        f.write('*'+ item['Link'])
#		#print(imgdownload)
#        makemydir(folder+'/'+item['SKU'])
#        for i in range(0,len(item)-1):
#            f.write('*'+item['image'+str(i)])
#            print(' Image: '+item['image'+str(i)])
#            try:
#                imgdownload = folder+'/'+item['SKU']+'/'+item['image'+str(i)].split('/')[-1]
#                urllib.request.urlretrieve(item['image'+str(i)],imgdownload)
#            except:
#                pass
        f.write('\n')
    print('DONE')