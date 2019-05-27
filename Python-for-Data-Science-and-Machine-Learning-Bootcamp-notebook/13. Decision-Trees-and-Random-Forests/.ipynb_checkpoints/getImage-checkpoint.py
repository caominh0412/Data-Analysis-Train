from requests_html import HTMLSession
from multiprocessing import Pool 
import urllib.request
import os


urls = ['https://www.adayroi.com/bo-4-hop-muoi-ngam-chan-khu-mui-hoi-giam-dau-nhuc-bao-nhien-350g-p-924025?offer=924025_R4T',
'https://www.adayroi.com/cao-che-vang-loi-sua-giam-can-bao-nhien-75g-p-PRI1222299?offer=PRI1222299_R4T',
'https://www.adayroi.com/binh-xit-xua-duoi-con-trung-fly-way-bao-nhien-100ml-p-PRI1222018?offer=PRI1222018_R4T',
]



filename = 'MAC.csv'
downloadfolder = 'adayroi'
folder = 'C:/Users/minhcq/Desktop/download/'+downloadfolder

def getImage(item_link):
    item = dict()
    session = HTMLSession()
    item_session = session.get(item_link)
    item_session.html.render(timeout=20,sleep=3,wait=2)
    item_SKU = item_session.html.find('.panel-serial-number')[0].text
    SKU = item_SKU[8:item_SKU.find(' - ')]
    barcode = item_SKU[item_SKU.find('Mã SKU: ')+8:item_SKU.find(')')-1]
    item['barcode'] = barcode
    item['SKU'] = SKU
    images = item_session.html.find('.theatre-image__list-item')
    item['short_des'] = item_session.html.find('.short-des__content')[0].text
    item['long_des'] = item_session.html.find('.product-detail__description')[0].text
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
    i = 0
    for i in range(0,len(item)-1):
        try:
            #print('SKU: '+ SKU)
            imgdownload = folder+'/'+barcode+'/'+item['image'+str(i)].split('/')[-1]
            #imgdownload = folder+'/'+barcode+'/'+SKU+'_'+str(i+1)+'.jpg'
            if os.path.exists(imgdownload) == False:
                makemydir(folder+'/'+barcode)
                #print('SKU: '+ SKU +'------ Image: '+item['image'+str(i)] + '------ Downloading: '+ imgdownload)
                urllib.request.urlretrieve(item['image'+str(i)],imgdownload)           
        except Exception as e:
            print('Error '+ str(e) + ' - '+ image_link + ' -- ' + imgdownload + ' -- ')
            pass
    session.close()
    return item

def getPrice(item_link):
    session = HTMLSession()
    item = dict()
    item_session = session.get(item_link)
    item_session.html.render()
    SKU = item_session.html.find('.panel-serial-number')[0].text
    SKU = SKU[8:SKU.find(' - ')]
    item['SKU'] = SKU
    item['price'] = item_session.html.find('.price-info__original')[0].text
    print('SKU: ' + item['SKU'] + '- Price:' + item['price'])
    return item

def makemydir(whatever):
  try:
    os.makedirs(whatever)
  except OSError:
    pass
  # let exception propagate if we just can't
  # cd into the specified directory
  os.chdir(whatever)


def gettotalpage(url):
    session = HTMLSession()
    url_session = session.get(url)
    totalpage = url_session.html.find('a[aria-label="Next"]')[0].attrs['href']
    totalpage = int(totalpage[-len(totalpage)+totalpage.find('page=')+5:])+1
    print('Total page= ' + str(totalpage))
    return totalpage

def getlink(url):
    session = HTMLSession()
    links = []
    url_session = session.get(url)
    items = url_session.html.find('.product-item__container')
    for item in items:
        item_name = item.find('.product-item__info-title')[0].text
        item_link = 'https://adayroi.com'+item.find('.product-item__info-title')[0].attrs['href']
        #item_price = item.find('.product-item__info-price-original')[0].text
        print(item_name)
        #print(item_price)
        links.append(item_link)
    return links
    




if __name__ == '__main__':
    for url in urls:
        getImage(url)

    print('DONE')