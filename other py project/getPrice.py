from getImage import getImage,getlink,getPrice,gettotalpage,makemydir
from multiprocessing import Pool
import urllib.request

filename = 'image.csv'
downloadfolder = 'test'
folder = 'C:/Users/minhcq/Desktop/download/'+downloadfolder
url =  'https://www.adayroi.com/SUPOR-HN-mc2420?q=:relevance:category:862'
#f = open(filename, "w", encoding="utf-8")
#f.write("")
if __name__ == '__main__':
    totalpage = int(gettotalpage(url))
    items =[]
    for i in range(1,int(totalpage)+1):
        print('Page '+str(i-1))
        urlpage = url +'?page='+str(i-1)
        print(urlpage)
        items = url_session.html.find('.product-item__container')
        for item in items:
            item_name = item.find('.product-item__info-title')[0].text
            item_link = 'https://adayroi.com'+item.find('.product-item__info-title')[0].attrs['href']
            item_price = item.find('.product-item__info-price-original')[0].text
            print(item_name)
            print(item_price)
            print(item_link)

            "1. Y:\2.SXMOI\TTKD Thời Trang\me & be\Chụp hình\Năm 2018\00_ Mẹ bé Sau Quy Hoạch\M5D_Anh Duong\180912_M5D_Anh Duong_8sku
2. Y:\2.SXMOI\TTKD Thời Trang\me & be\Chụp hình\Năm 2018\00_ Mẹ bé Sau Quy Hoạch\161371_BGroup\180913_161371_BGroup_18sku
3. Y:\2.SXMOI\TTKD Thời Trang\me & be\Chụp hình\Năm 2018\00_ Mẹ bé Sau Quy Hoạch\174016_The Gioi Ti Hon\180913_174016_The Gioi Ti Hon_9sku"
