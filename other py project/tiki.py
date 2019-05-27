from requests_html import HTMLSession
from multiprocessing import Pool 
import urllib.request
import os


filename = 'image.csv'
downloadfolder = 'tiki'
folder = 'C:/Users/minhcq/Desktop/download/'+downloadfolder

def gettiki(item_link):
    item = dict()
    item['SKU']=item_link.split('*')[0]
    item_link = item_link.split('*')[1]
    if item_link.find('jpg')<0 and item_link.find('tiki') >0:
        session = HTMLSession()
        item_session = session.get(item_link)
        item_session.html.render(timeout=20,sleep=3,wait=2)
        if item['SKU'] == '':
            SKU = item_session.html.find('.item-sku')[0].text
            item['SKU'] = SKU[SKU.find('\n')+1:]
        images = item_session.html.find('.flx')
        i = 0
        for image in images:
            image_link = image.find('img')[0].attrs['src']
            image_link = image_link.replace('75x75','w1200')
            item['image'+str(i)] = image_link
            i+=1
        print(item_link+'          '+ item['SKU'] + '   Image Count: '+str(i))  
        for i in range(0,len(item)-1):
            try:
                #print('SKU: '+ SKU)
                if len(item)-1 >= 3:
                    makemydir(folder+'/3 anh/'+item['SKU'])
                    imgdownload = folder+'/3 anh/'+'/'+item['SKU']+'/'+item['image'+str(i)].split('/')[-1]
                    #print('SKU: '+ item['SKU'] +'------ Image: '+item['image'+str(i)] + '------ Downloading: '+ imgdownload)
                    urllib.request.urlretrieve(item['image'+str(i)],imgdownload)
                else:
                    makemydir(folder+'/it hon 3 anh/'+item['SKU'])
                    imgdownload = folder+'/it hon 3 anh/'+'/'+item['SKU']+'/'+item['image'+str(i)].split('/')[-1]
                    #print('SKU: '+ item['SKU'] +'------ Image: '+item['image'+str(i)] + '------ Downloading: '+ imgdownload)
                    urllib.request.urlretrieve(item['image'+str(i)],imgdownload)
            except:
                print('Error - '+ SKU)
                pass
        session.close()
    else:
        makemydir(folder+'/it hon 3 anh/'+item['SKU'])
        imgdownload = folder+'/it hon 3 anh/'+'/'+item['SKU']+'/'+item_link.split('/')[-1]
        try:
            urllib.request.urlretrieve(item_link,imgdownload)
        except:
            print('Cant download '+ item_link)
            pass
    return item

def makemydir(whatever):
    try:
        os.makedirs(whatever)
    except OSError:
        pass
  # let exception propagate if we just can't
  # cd into the specified directory
    os.chdir(whatever)

urls = ['3337872420603_PYE*https://tiki.vn/sua-rua-mat-va-tam-cho-da-kho-da-nhay-cam-man-ngua-la-roche-posay-lipikar-syndet-ap-cream-200ml-p470544.html',
'6955818216768*https://mint07.com/wp-content/uploads/2018/01/Kem-Nhuom-Toc-LOreal-Paris-Excellence-Fashion-6.13-review.png',
'6902395475637*https://cf.shopee.vn/file/9e08cfd9cd196015be7649589b152586',
'41554259247*https://cochiskin.com/wp-content/uploads/2018/06/B%C3%BAt-che-khuy%E1%BA%BFt-%C4%91i%E1%BB%83m-Maybelline-Instant-Age-Rewind-110-Fair.jpg',
'6902395472452*https://alcazo.com/wp-content/uploads/2018/06/6902395472452_s_02.u2409.d20170630.t102302.821265-600x600.jpg',
'6902395472469*https://images.summitmedia-digital.com/spotph/images/2017/02/13/powdermatte-barelyther.JPG',
'6902395472483*https://images.summitmedia-digital.com/spotph/images/2017/02/13/powdermatte-touchofnude.JPG',
'6902395472520*https://www.maybelline.com.my/~/media/mny/ms_my/lips/lipstick/color%20sensational%20powder%20mattes/cspowdermatte_textureshot_mor09avenuec.jpg?thn=0&w=380&hash=91F7705FD8AD6621B152C4A353634351BA850245',
'6902395472582*https://images.summitmedia-digital.com/spotph/images/2017/02/13/powdermatte-uptodate.JPG',
'6902395472612*https://images.summitmedia-digital.com/spotph/images/2017/02/13/maybelline-powder-matte-lipstick-4-2g-red-dy-red.jpg',
'6902395472629*https://images.summitmedia-digital.com/spotph/images/2017/02/13/powdermatte-getreddy.JPG',
'6902395472636*https://images.summitmedia-digital.com/spotph/images/2017/02/13/powdermatte-cherrychic.JPG',
'6902395472643*https://images.summitmedia-digital.com/spotph/images/2017/02/13/powdermatte-plumperfection.JPG',
'6902395472605*https://images.summitmedia-digital.com/spotph/images/2017/02/13/powdermatte-noirred.JPG',
'6902395510154*https://media.hasaki.vn/catalog/product/s/o/son-li-maybelline-chilli-nude-3-9g_img_800x800_eb97c5_fit_center.jpg',
'6902395510208*https://media.hasaki.vn/catalog/product/s/o/son-li-maybelline-pretty-please-3-9g_img_800x800_eb97c5_fit_center.jpg',
'6902395620976*https://media.hasaki.vn/catalog/product/s/o/son-li-maybelline-toast-brown-3-9g-1_img_800x800_eb97c5_fit_center.jpg',
'6902395621003*https://media.hasaki.vn/catalog/product/s/o/son-li-maybelline-almond-pink-3-9g_img_800x800_eb97c5_fit_center.jpg',
'6902395482321*https://media.hasaki.vn/catalog/product/s/o/son-li-mem-moi-mau-do-tim-05-chocoholic-4-2g05_1__img_800x800_eb97c5_fit_center.jpg',
'6902395482345*https://media.hasaki.vn/catalog/product/s/o/son-li-mem-moi-mau-do-07-dynamite-red-4-2g07_1__img_800x800_eb97c5_fit_center.jpg',
'6902395482352*https://media.hasaki.vn/catalog/product/s/o/son-li-mem-moi-mau-cam-08-sunny-coral-4-2g_1__img_800x800_eb97c5_fit_center.jpg',
'6902395482369*https://media.hasaki.vn/catalog/product/s/o/son-li-mem-moi-mau-hong-do-09-midnight-date-4-2g09_1__img_800x800_eb97c5_fit_center.jpg',
'6902395482376*https://media.hasaki.vn/catalog/product/s/o/son-li-mem-moi-mau-do-10-smoking-red-4-2g10_1__img_800x800_eb97c5_fit_center.jpg',
'6902395482383*https://media.hasaki.vn/catalog/product/s/o/son-li-mem-moi-mau-hong-11-raspberry-rendezvous-4-2g11_1__img_800x800_eb97c5_fit_center.jpg',
'6902395482406*https://media.hasaki.vn/catalog/product/s/o/son-li-mem-moi-mau-hong-13-fuchsia-4-2g13_1__img_800x800_eb97c5_fit_center.jpg',
'6902395482420*https://media.hasaki.vn/catalog/product/s/o/son-li-mem-moi-mau-do-ruou-15-berry-bossy-4-2g15_1__img_800x800_eb97c5_fit_center.jpg',
'rnw_py01*http://cdn.nhanh.vn/cdn/store1/32962/ps/20181226/royal_honey_propolis_mask3_1000x1000.jpg',
'catalina geo_py01*https://tiki.vn/mascara-lam-dai-day-mi-catalina-lash-power-volumizing-mascara-geo-7g-p5472705.html',
'geo_py02*https://tiki.vn/kem-duong-da-tri-mun-sempre-h-p-flowater-clear-cream-geo_py02-50g-p5208699.html?src=search&2hi=1&keyword=Kem+d%C6%B0%E1%BB%A1ng+da+tr%E1%BB%8B+m%E1%BB%A5n+Geo+Sempre+H%26amp%3BP+Flowater+Clear+Cream+50g',
'geo_py03*https://tiki.vn/sua-rua-mat-keo-ong-lam-trang-da-sorite-clarity-washable-cleansing-foam-geo_py03-200ml-p5208733.html?src=search&2hi=1&keyword=geo_py03',
'geo_py04*https://tiki.vn/phan-phu-sempre-happy-please-pact-01-geo_py04-p5208765.html?src=search&2hi=1&keyword=geo_py04',
'catalina geo_py02*https://tiki.vn/mascara-lam-dai-mi-catalina-long-deep-mascara-6-black-catalina-geo_py02-p5208805.html?src=search&2hi=1&keyword=catalina+geo_py02',
'catalina geo_py03*https://tiki.vn/kem-nen-trang-diem-lafine-catalina-fisso-foundation-10-rose-pink-catalina-geo_py03-40ml-p5208843.html?src=search&2hi=1&keyword=catalina+geo_py03',
'geo_py05*https://tiki.vn/phan-phu-catalina-pact-01-natural-beige-catalina-geo_py05-22g-p5209481.html?src=search&2hi=1&keyword=geo_py05',
'geo_py07*https://tiki.vn/kem-duong-trang-da-sempre-happy-please-flowater-whitening-cream-geo_py07-50g-p5208989.html?src=search&2hi=1&keyword=geo_py07',
'geo_py08*https://tiki.vn/phan-nen-sempre-c-water-two-way-23-geo_py08-p5209025.html?src=search&2hi=1&keyword=geo_py08',
'geo_py09*https://tiki.vn/son-trang-diem-duong-moi-sempre-happy-please-lipstick-24-dahlia-geo_py09-8g-p5209027.html?src=search&2hi=1&keyword=geo_py09',
'geo_py10*https://tiki.vn/nuoc-hoa-hong-lam-trang-da-sempre-happy-please-flowater-whitening-skin-geo_py10-145ml-p5209183.html?src=search&2hi=1&keyword=geo_py10',
'geo_py11*https://tiki.vn/kem-dac-tri-nhan-va-quang-tham-vung-mat-catalina-intensive-anti-wrinkle-eye-cream-geo_py11-35ml-p5209187.html?src=search&2hi=1&keyword=geo_py11',
'catalina geo_py17*https://tiki.vn/kem-duong-da-chong-lao-hoa-catalina-intensive-anti-wrinkle-cream-sortie-geo_py17-30g-p5209221.html?src=search&2hi=1&keyword=geo_py17',
'geo_py15*https://tiki.vn/sua-tam-trang-da-huong-hoa-hong-perfume-body-cleanser-rose-spa-geo_py15-600ml-p5209329.html?src=search&2hi=1&keyword=geo_py15',
'geo_py16*https://tiki.vn/son-trang-diem-duong-moi-sempre-happy-please-lipstick-27-gladiolus-geo_py16-8g-p5209407.html?src=search&2hi=1&keyword=geo_py16',
'geo_py17*https://tiki.vn/sua-rua-mat-hoa-qua-tri-mun-duong-trang-vegetable-foam-cleansing-geo_py17-200ml-p5209441.html?src=search&2hi=1&keyword=geo_py17',
'geo_py18*https://tiki.vn/son-trang-diem-duong-moi-sempre-happy-please-lipstick-25-sweet-pea-geo_py18-8g-p5209443.html?src=search&2hi=0&keyword=geo_py18',
'catalina geo_py05*https://tiki.vn/phan-phu-catalina-pact-01-natural-beige-catalina-geo_py05-22g-p5209481.html?src=search&2hi=1&keyword=catalina+geo_py05',
'geo_py19*https://tiki.vn/mascara-lam-dai-mi-sempre-happy-please-volume-mascara-geo_py19-7g-p5209541.html?src=search&2hi=1&keyword=geo_py19',
'geo_py20*https://tiki.vn/son-trang-diem-duong-moi-sempre-happy-please-lipstick-34-milkweed-geo_py20-8g-p5209549.html?src=search&2hi=1&keyword=geo_py20',
'geo_py21*https://tiki.vn/sua-duong-da-tri-dau-va-mun-sempre-happy-please-flowater-clear-emulsion-geo_py21-145ml-p5209557.html?src=search&2hi=1&keyword=geo_py21',
'geo_py22*https://tiki.vn/bot-rua-mat-chanh-lemon-juice-foam-cleansing-geo_py22-200ml-p5209567.html?src=search&2hi=1&keyword=geo_py22',
'geo_py23*https://tiki.vn/kem-chong-nang-3-trong-1-sempre-happy-please-cover-up-sunblock-3-in-1-spf50-pa-100g-geo_py23-100g-p5209609.html?src=search&2hi=1&keyword=geo_py23',
'geo_py24*https://tiki.vn/sua-tam-trang-da-thao-duoc-perfume-body-cleanser-herb-spa-geo_py24-600ml-p5209617.html?src=search&2hi=1&keyword=geo_py24',
'geo_py25*https://tiki.vn/sua-rua-mat-trang-da-vitamin-c-foam-cleansing-geo_py25-200g-p5209619.html?src=search&2hi=1&keyword=geo_py25',
'geo_py26*https://tiki.vn/phan-ma-4-mau-soft-color-face-touch-02-geo_py26-22g-p5209657.html?src=search-beta&keyword=geo_py26&2hi=0',
'geo_py28*https://tiki.vn/son-trang-diem-duong-moi-sempre-happy-please-lipstick-32-lychee-geo_py28-8g-p5209693.html?src=search&2hi=1&keyword=geo_py28',
'geo_py29*https://tiki.vn/chi-ke-may-catalina-auto-eye-brow-pencil-g1-grey-brown-geo_py29-0-2g-p5209695.html?src=search&2hi=1&keyword=geo_py29',
'geo_py30*https://tiki.vn/son-trang-diem-duong-moi-sempre-happy-please-lipstick-22-magnolia-geo_py30-8g-p5209729.html?src=search&2hi=1&keyword=geo_py30',
'geo_py31*https://tiki.vn/kem-nen-sempre-happy-please-liquid-foundation-21-natural-beige-geo_py31-p5209731.html?src=search&2hi=1&keyword=geo_py31',
'catalina geo_py06*https://tiki.vn/kem-nen-trang-diem-lafine-catalina-fisso-foundation-21-light-beige-catalina-geo_py06-p5209733.html?src=search&2hi=1&keyword=catalina+geo_py06',
'geo_py32*https://tiki.vn/phan-nen-sempre-c-water-two-way-21-light-beige-geo_py32-10-5g-p5209765.html?src=search&2hi=1&keyword=geo_py32',
'geo_py34*https://tiki.vn/son-trang-diem-duong-moi-sempre-happy-please-lipstick-1-poppy-geo_py34-8g-p5209803.html?src=search&2hi=1&keyword=geo_py34',
'catalina geo_py07*https://tiki.vn/phan-phu-catalina-pact-2-catalina-geo_py07-22g-p5209805.html?src=search&2hi=1&keyword=catalina+geo_py07',
'catalina geo_py08*https://tiki.vn/kem-nen-trang-diem-da-chuc-nang-catalina-multi-recovery-blemish-balm-catalina-geo_py08-50g-p5209845.html?src=search&2hi=1&keyword=catalina+geo_py08',
'catalina geo_py09*https://tiki.vn/kem-duong-tri-nhan-chong-lao-hoa-catalina-intensive-anti-wrinkle-cream-catalina-geo_py09-60g-p5209881.html?src=search&2hi=0&keyword=catalina+geo_py09',
'geo_py36*https://tiki.vn/phan-bot-sempre-happy-please-powder-2-geo_py36-p5209883.html?src=search&2hi=1&keyword=geo_py36',
'geo_py37*https://tiki.vn/son-trang-diem-duong-moi-sempre-happy-please-lipstick-26-chelone-geo_py37-8g-p5209917.html?src=search&2hi=1&keyword=geo_py37',
'catalina geo_py10*https://tiki.vn/kem-trang-diem-da-chuc-nang-catalina-intensive-anti-wrinkle-whitening-bb-cream-sps-35pa-catalina-geo_py10-50ml-p5209919.html?src=search&2hi=1&keyword=catalina+geo_py10',
'catalina geo_py11*https://tiki.vn/sua-rua-mat-cai-thien-nep-nhan-cataline-intensive-cleansing-foam-catalina-geo_py11-200ml-p5209955.html?src=search&2hi=1&keyword=catalina+geo_py11',
'geo_py38*https://tiki.vn/phan-nen-kiem-dau-essence-two-way-cake-matt-21-geo_py38-p5209957.html?src=search&2hi=1&keyword=geo_py38',
'lafine_py02*https://tiki.vn/kem-massage-lafine-vegetable-deep-massage-cream-lafine-lafine_py02-350g-p5209959.html?src=search&2hi=1&keyword=lafine_py02',
'geo_py39*https://tiki.vn/gel-tay-te-bao-chet-lemon-juice-peeling-gel-geo_py39-160ml-p5209995.html?src=search&2hi=1&keyword=geo_py39',
'geo_py40*https://tiki.vn/son-trang-diem-duong-moi-sempre-happy-please-lipstick-31-peach-blossom-geo_py40-8g-p5210033.html?src=search&2hi=1&keyword=geo_py40',
'geo_py41*https://tiki.vn/phan-bot-sempre-happy-please-powder-1-geo_py41-25g-p5210037.html?src=search&2hi=1&keyword=geo_py41',
'geo_py42*https://tiki.vn/phan-ma-4-mau-geo-soft-color-face-touch-geo_py42-p5832257.html?src=search&2hi=1&keyword=geo_py42',
'geo_py43*https://tiki.vn/son-trang-diem-duong-moi-sempre-happy-please-lipstick-23-bouvardia-geo_py43-8g-p5210141.html?src=search&2hi=1&keyword=geo_py43',
'catalina geo_py13*https://tiki.vn/ke-mat-nuoc-catalina-eye-liner-mau-den-6g-catalina-geo_py13-6g-p5210145.html?src=search&2hi=1&keyword=catalina+geo_py13',
'catalina geo_py14*https://tiki.vn/chi-ke-long-may-catalina-auto-brow-pencil-b1-black-brown-catalina-geo_py14-0-2g-p5210217.html?src=search&2hi=1&keyword=catalina+geo_py14',
'geo_py45*https://tiki.vn/sua-duong-the-trang-da-huong-hoa-hong-perfume-body-lotion-rose-spa-geo_py45-300ml-p5210219.html?src=search&2hi=1&keyword=geo_py45',
'geo_py47*https://tiki.vn/kem-lot-trang-diem-sempre-happy-please-makeup-base-spf20-2-geo_py47-p5210331.html?src=search&2hi=1&keyword=geo_py47',
'geo_py48*https://tiki.vn/sua-duong-da-sempre-happy-please-flowater-whitening-emulsion-geo_py48-145ml-p5210333.html?src=search&2hi=1&keyword=geo_py48',
'geo_py49*https://tiki.vn/son-trang-diem-duong-moi-sempre-happy-please-lipstick-21-peony-geo-p5472819.html?spid=5472821&utm_source=google&utm_medium=cpc&utm_campaign=SEA_NBR_GGL_SMA_DAP_ALL_VN_ALL_UNK_UNK_C.ALL_X.1649792293_Y.61335112537_V.5472821_W.c_A.&gclid=Cj0KCQiA7briBRD7ARIsABhX8aDQqXgPC8NMMdGFWwBfAAxvUMCSvoqj5PHhwXorwIFRiY-ZMjyLOcYaAuSlEALw_wcB',
'geo_py51*https://tiki.vn/nuoc-duong-tri-mun-lam-sach-da-sempre-happy-please-flowater-clear-skin-geo_py51-145ml-p5210437.html?src=search&2hi=1&keyword=geo_py51',
'catalina geo_py16*https://tiki.vn/nuoc-can-bang-tri-nhan-da-catalina-intensive-anti-wrinkle-skin-catalina-geo_py16-150ml-p5210439.html?src=search&2hi=1&keyword=%27catalina+geo_py16%2A%27%2C',
'geo_py52*https://tiki.vn/bot-rua-mat-chanh-lemon-juice-foam-cleansing-geo_py52-100g-p5210441.html?src=search&2hi=1&keyword=geo_py52',
'geo_py53*https://tiki.vn/ke-mat-nuoc-sat-net-clarity-finish-eyeliner-geo_py53-6g-p5210513.html?src=search&2hi=1&keyword=geo_py53',
'geo_py54*https://tiki.vn/phan-trang-diem-am-min-da-essence-two-way-moist-21-geo_py54-p5210523.html?src=search&2hi=1&keyword=geo_py54',
'geo_py55*http://cdn.nhanh.vn/cdn/store1/32962/ps/20181013/_1__ruby_red_762x1100.jpg',
'geo_py56*https://cf.shopee.vn/file/de7ad96c7dca6ad22dc95902f63028d4',
'geo_py57*http://cdn.nhanh.vn/cdn/store1/32962/ps/20181013/_3__enchanting_pink_762x1100.jpg',
'geo_py58*http://cdn.nhanh.vn/cdn/store1/32962/ps/20181013/_4__sweet_pink_762x1100.jpg',
'geo_py59*http://cdn.nhanh.vn/cdn/store1/32962/ps/20181013/_5__pure_orange_762x1100.jpg',
'renoma_py20*https://tiki.vn/bo-son-moi-va-son-bong-duong-lareine-signature-lipstick-p3-lafine-renoma_py20-p5208731.html?src=search&2hi=1&keyword=renoma_py20',
'renoma_py09*https://tiki.vn/phan-mat-4-mau-lareine-eye-shadow-14-renoma_py09-8g-p5209767.html?src=search&2hi=1&keyword=renoma_py09',
'renoma_py02*https://tiki.vn/phan-mat-4-mau-lareine-eyeshadow-19-renoma_py02-p5208949.html?src=search&2hi=1&keyword=renoma_py02',
'renoma_py13*https://tiki.vn/phan-mat-4-mau-lareine-eye-shadow-17-renoma_py13-8g-p5210035.html?src=search&2hi=1&keyword=renoma_py13',
'renoma_py07*https://tiki.vn/phan-mat-4-mau-lareine-eye-shadow-18-renoma_py07-8g-p5209405.html?src=search&2hi=0&keyword=renoma_py07',
'renoma_py01*https://tiki.vn/phan-phu-lareine-extreme-twin-pact-21-renoma_py01-p5208807.html?src=search&2hi=1&keyword=renoma_py01',
'renoma_py04*https://tiki.vn/phan-mat-4-mau-lareine-eye-shadow-13-renoma_py04-8g-p5209065.html?src=search&2hi=1&keyword=renoma_py04',
'renoma_py05*https://tiki.vn/phan-mat-4-mau-lareine-eye-shadow-15-renoma_py05-8g-p5209365.html?src=search&2hi=1&keyword=renoma_py05',
'renoma_py08*https://tiki.vn/phan-ma-lareine-marble-blusher-1-renoma_py08-12g-p5209493.html?src=search&2hi=1&keyword=renoma_py08',
'renoma_py12*https://tiki.vn/phan-ma-lareine-marble-blusher-2-renoma_py12-12g-p5210027.html?src=search&2hi=0&keyword=%27renoma_py12%2A%27%2C',
'renoma_py11*https://tiki.vn/phan-phu-lareine-extreme-twin-pact-23-renoma_py11-p5209993.html?src=search&2hi=1&keyword=renoma_py11',
'renoma_py14*https://tiki.vn/phan-mat-4-mau-lareine-eye-shadow-12-renoma_py14-p5210143.html?src=search&2hi=1&keyword=renoma_py14',
'renoma_py16*https://tiki.vn/phan-mat-4-mau-lareine-eye-shadow-11-renoma_py16-8g-p5210253.html?src=search&2hi=1&keyword=renoma_py16',
'renoma_py17*https://tiki.vn/bo-son-moi-va-son-bong-duong-lareine-signature-lipstick-p5-renoma_py17-p5210289.html?src=search&2hi=1&keyword=renoma_py17',
'renoma_py19*https://tiki.vn/phan-mat-4-mau-lareine-eye-shadow-16-renoma_py19-8g-p5210515.html?src=search&2hi=1&keyword=renoma_py19',
'renoma_py03*https://tiki.vn/bo-son-moi-va-son-bong-duong-lareine-signature-lipstick-p6-renoma_py03-p5209023.html?src=search&2hi=1&keyword=renoma_py03',
'sortie_py01*https://tiki.vn/kem-tay-trang-va-te-bao-chet-keo-ong-clarity-deep-cleansing-cream-sortie_py01-300ml-p5208697.html?src=search&2hi=1&keyword=sortie_py01',
'sortie_py02*https://tiki.vn/kem-duong-da-nobline-neutro-cream-sortie_py02-55ml-p5208663.html?src=search&2hi=1&keyword=%27sortie_py02%2A%27%2C',
'sortie_py03*https://tiki.vn/kem-massage-lam-san-chac-da-clarity-firming-massage-cream-sortie_py03-300ml-p5208767.html?src=search&2hi=1&keyword=%27sortie_py03%2A%27%2C',
'sortie_py05*https://tiki.vn/phan-phu-caviar-deluxe-pact-spf25-pa-21-sortie_py05-p5208841.html?src=search&2hi=1&keyword=%27sortie_py05%2A%27%2C',
'sortie_py06*https://tiki.vn/dung-dich-tay-trang-mat-va-moi-clarity-lip-eye-remover-sortie_py06-150ml-p5209029.html?src=search&2hi=1&keyword=%27sortie_py06%2A%27%2C',
'sortie_py08*https://tiki.vn/bo-duong-da-nobline-intensial-eye-filler-cream-set-sortie_py08-p5209331.html?src=search&2hi=1&keyword=%27sortie_py08%2A%27%2C',
'sortie_py09*https://tiki.vn/kem-duong-da-nobline-aqua-cream-sortie_py09-55ml-p5209501.html?src=search&2hi=1&keyword=%27sortie_py09%2A%27%2C',
'sortie_py10*https://tiki.vn/bo-cham-soc-da-toan-than-herb-therapy-clarity-body-set-2-sortie_py10-p5209621.html?src=search&2hi=1&keyword=%27sortie_py10%2A%27%2C',
'sortie_py11*https://tiki.vn/mascara-dai-mi-nobline-power-up-mascara-sortie_py11-10g-p5209655.html?src=search&2hi=1&keyword=%27sortie_py11%2A%27%2C',
'sortie_py12*https://tiki.vn/kem-duong-da-va-mong-tay-clarity-hand-nail-cream-sortie_py12-100g-p5209843.html?src=search&2hi=1&keyword=%27sortie_py12%2A%27%2C',
'sortie_py14*https://tiki.vn/phan-phu-caviar-deluxe-pact-23-sortie_py14-p5210369.html?src=search-beta&keyword=%27sortie_py14*%27,&2hi=0',
'sortie_py16*https://tiki.vn/bo-cham-soc-da-toan-than-flora-spa-clarity-body-set-2-sortie_py16-p5210481.html?src=search&2hi=1&keyword=%27sortie_py16%2A%27%2C',
]

if __name__ == '__main__':
    pool = Pool(processes=4)
    outputs = pool.map(getImage,urls)
    pool.close()
    pool.join()
    f = open(filename, "w", encoding="utf-8")
    f.write("")
    for item in outputs:
        #print('SKU: '+ item['SKU'])
        f.write(item['SKU'])
        for i in range(0,len(item)-1):
            f.write('*'+item['image'+str(i)])
            #print(' Image: '+item['image'+str(i)])
        f.write('\n')
    print('DONE')