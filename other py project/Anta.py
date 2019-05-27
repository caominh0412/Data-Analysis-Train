import requests
#from bs4 import BeautifulSoup as soup
import bs4

#url = 'https://moolez.vn/san-pham/bop-nam-4'
#headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
#page = requests.get(url,headers = headers)
#soup = soup(page.text, 'html.parser')
#print(soup)
#sku = soup.findAll('span',{'class':'variant-sku'})[0].text
#images = soup.findAll('a',{'class':'thumb-link'})
#print(sku)
#for image in images:
#    link = 'https://moolez.vn/'+ image.get('data-zoom-image')
 #   print(link)

#for i in range (1,15):

filename = 'aonu.doc'
f = open(filename, "w", encoding="utf-8")
#headers = "Name,link\n"
f.write("")
for i in range(1,5):
    url = 'http://antavn.com/collections/ao-nu-1?page='+str(i)
    print(url)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    page = requests.get(url,headers = headers)
    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    items = soup.findAll('a',{'class':'product-name'})
    for item in items:
        item_name = item.text.strip()
        link = 'http://antavn.com' + item.get('href')
        print(item_name)
        f.write(item_name + "+" +link + "+")
        #print(item_page)
        page2 = requests.get(link,headers = headers)
        soup2 = bs4.BeautifulSoup(page2.content, 'html.parser')
        #print(soup2)
        skus = soup2.findAll('li',{'class':'product-thumb'})
        #print(sku)
        for sku in skus:
            sku_image = sku.a.get('data-zoom-image')
            imagelink = 'https:' + sku_image
            #print(imagelink)
            f.write(imagelink+"+")
        #images = soup2.findAll('a',{'class':'thumb-link'})
        #print(sku)
        #for image in images:
        #    link = 'https://moolez.vn/'+ image.get('data-zoom-image')
        #    print(link)
        f.write("\n")
    url=""
    page=""
    soup=""
    item_name=""
    link=""
    page2=""
    soup2=""
f.close()