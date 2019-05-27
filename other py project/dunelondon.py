from requests_html import HTMLSession
from multiprocessing import Pool 
import urllib.request
import os


filename = 'dune.csv'
downloadfolder = 'dunelondon'
folder = 'C:/Users/minhcq/Desktop/download/'+downloadfolder



def getImage(item_link):
	item = dict()
	session = HTMLSession()
	item_session = session.get(item_link)
	item_session.html.render(timeout=20,sleep=3,wait=2)
	SKU = item_session.html.find('.mb1-5,f-13')[0].text
	SKU = SKU[16:]
	i = 0
	images = item_session.html.find('.amp-visible')
	for image in images:
		image_link = image.find('img')[0].attrs['src']
		image_link = image_link[:image_link.find('?')]
		item['image'+str(i)] = image_link
		i += 1
		imgdownload = folder + '/' + SKU + '/' + str(image_link.split('/')[-1]) + '.jpg'
		try:
			makemydir(folder+'/'+SKU)
			print('SKU: '+ SKU + ' ---- IMAGE: '+ image_link + ' ------- Downloading: '+ imgdownload)
			urllib.request.urlretrieve(image_link,imgdownload)
		except:
			print('Error: ' + image_link+ '----' + imgdownload)
			pass
	session.close()
	item['SKU']=SKU
	item['url'] = item_link
	return item

def makemydir(whatever):
	try:
		os.makedirs(whatever)
	except OSError:
		pass
  # let exception propagate if we just can't
  # cd into the specified directory
	os.chdir(whatever)

urls = ['https://www.dunelondon.com/alesandra-kitten-heel-point-toe-court-shoe-0085503940206039/?cswatch=1',
'https://www.dunelondon.com/alesandra-kitten-heel-point-toe-court-shoe-0085503940206483/?cswatch=1',
'https://www.dunelondon.com/alexxa-point-toe-stiletto-court-shoe-0163508750008050/',
'https://www.dunelondon.com/alexxa-point-toe-stiletto-court-shoe-0163508750008014/?cswatch=1',
'https://www.dunelondon.com/alexxa-point-toe-stiletto-court-shoe-0163508750008012/?cswatch=1',
'https://www.dunelondon.com/alixxe-stacked-wedge-heel-court-shoe-0085503940045625/',
'https://www.dunelondon.com/alixxe-stacked-wedge-heel-court-shoe-0085503940045149/?cswatch=1',
'https://www.dunelondon.com/ambre-ombre-mid-heel-court-shoe-0085503940159309/',
'https://www.dunelondon.com/andersonn-sweetheart-vamp-court-shoe-0085503940054628/',
'https://www.dunelondon.com/andersonn-sweetheart-vamp-court-shoe-0085503940054095/?cswatch=1',
'https://www.dunelondon.com/andersonn-v-cut-studded-court-shoe-0085503940054715/?cswatch=1',
'https://www.dunelondon.com/andersonn-sweetheart-vamp-court-shoe-0085503940054649/?cswatch=1',
'https://www.dunelondon.com/andersonn-v-cut-studded-court-shoe-0085503940054725/?cswatch=1',
'https://www.dunelondon.com/animal-bow-detail-pointed-toe-court-shoe-0085503940106114/',
'https://www.dunelondon.com/apricot-square-toe-flat-shoe-0100503940029059/?cswatch=1',
'https://www.dunelondon.com/apricot-square-toe-flat-shoe-0100503940029095/',
'https://www.dunelondon.com/ashe-wavy-top-line-high-heel-court-0085503940125516/',
'https://www.dunelondon.com/ashe-wavy-top-line-high-heel-court-0085503940125034/?cswatch=1',
'https://www.dunelondon.com/aspiration-twist-heel-stiletto-court-shoe-0085503940060515/',
'https://www.dunelondon.com/aspiration-twist-heel-stiletto-court-shoe-0085503940060633/?cswatch=1',
'https://www.dunelondon.com/aspire-point-toe-kitten-heel-shoe-0085503940046515/',
'https://www.dunelondon.com/aspire-point-toe-kitten-heel-shoe-0085503940046670/?cswatch=1',
'https://www.dunelondon.com/aurrora-mid-heel-court-shoe-0085503940172061/',
'https://www.dunelondon.com/aurrora-mid-heel-court-shoe-0085503940172034/?cswatch=1',
'https://www.dunelondon.com/aurrora-mid-heel-court-shoe-0085503940172095/?cswatch=1',
'https://www.dunelondon.com/bache-wingtip-brogue-shoe-0272509520017585/',
'https://www.dunelondon.com/bache-wingtip-brogue-shoe-0272509520017359/?cswatch=1',
'https://www.dunelondon.com/bache-wingtip-brogue-shoe-0272509520017177/?cswatch=1',
'https://www.dunelondon.com/bae-true-love-embellished-pointed-court-shoe-0084500620013723/',
'https://www.dunelondon.com/bafari-ponyhair-soft-clutch-bag-0007500110008024/',
'https://www.dunelondon.com/bali-woven-hardware-detail-shoe-0274508050012306/',
'https://www.dunelondon.com/bali-woven-hardware-detail-shoe/?cswatch=1',
'https://www.dunelondon.com/balloon-contrast-sole-loafer-shoe-0478509520002177/',
'https://www.dunelondon.com/balloon-contrast-sole-loafer-shoe-0478509520002511/?cswatch=1',
'https://www.dunelondon.com/balloon-contrast-sole-loafer-shoe-0478509520002722/?cswatch=1',
'https://www.dunelondon.com/balotelli-knitted-brogue-wedge-shoe-0272509520015298/',
'https://www.dunelondon.com/balotelli-knitted-brogue-wedge-shoe-0272509520015165/?cswatch=1',
'https://www.dunelondon.com/barca-suede-tassel-loafer-0274508050014350/',
'https://www.dunelondon.com/barmouth-bay-woven-saddle-loafer-0274510470002177/',
'https://www.dunelondon.com/barthez-suede-tassel-loafer-0274510090003164/',
'https://www.dunelondon.com/barthez-suede-tassel-loafer-0274510090003350/?cswatch=1',
'https://www.dunelondon.com/beaula-embellished-kitten-heel-court-shoe-0084503940082011/',
'https://www.dunelondon.com/beaula-embellished-kitten-heel-court-shoe-0084503940082382/?cswatch=1',
'https://www.dunelondon.com/beaumonte-diamante-floral-trim-kitten-heel-court-shoe-0084503940042638/',
'https://www.dunelondon.com/bellowes-jewelled-slither-heel-court-shoe-0084503940194516/?cswatch=1',
'https://www.dunelondon.com/bellowes-jewelled-slither-heel-court-shoe-0084503940194215/',
'https://www.dunelondon.com/bergamos-punch-detail-lace-up-shoe-0272508050016511/',
'https://www.dunelondon.com/bergamos-punch-detail-lace-up-shoe-0272508050016506/?cswatch=1',
'https://www.dunelondon.com/besee-pointed-bow-mid-heel-court-shoe-0084503940119485/',
'https://www.dunelondon.com/besee-pointed-bow-mid-heel-court-shoe-0084503940119484/?cswatch=1',
'https://www.dunelondon.com/bestte-wavy-topline-ankle-strap-court-shoe-0084508750022164/?cswatch=1',
'https://www.dunelondon.com/bestte-wavy-topline-ankle-strap-court-shoe-0084508750022204/',
'https://www.dunelondon.com/biijou-foldover-clutch-bag-0007500670126638/',
'https://www.dunelondon.com/bonie-fold-over-clutch-0007500670073011/?cswatch=1',
'https://www.dunelondon.com/bonie-fold-over-clutch-0007500670073629/',
'https://www.dunelondon.com/boyde-woven-embossed-driver-shoe-0478508050001177/',
'https://www.dunelondon.com/bradshawe-pointed-toe-block-heel-shoe-1137508750008011/',
'https://www.dunelondon.com/brightest-diamante-striped-clutch-0007500670157568/',
'https://www.dunelondon.com/britania-scalloped-pointed-toe-court-shoe-0084508750017011/?cswatch=1',
'https://www.dunelondon.com/britania-scalloped-pointed-toe-court-shoe-0084508750017219/',
'https://www.dunelondon.com/brylee-wavy-topline-mesh-insert-court-heel-0084508750020011/',
'https://www.dunelondon.com/brylee-wavy-topline-mesh-insert-court-heel-0084508750020040/?cswatch=1',
'https://www.dunelondon.com/buddy-lace-up-brogue-shoe-0272503730007177/',
'https://www.dunelondon.com/buddy-lace-up-brogue-shoe-0272503730007509/?cswatch=1',
'https://www.dunelondon.com/carding-woven-peep-toe-mid-heel-shoe-0094504510001487/',
'https://www.dunelondon.com/cas-u-cut-slingback-court-0094503940074625/',
'https://www.dunelondon.com/cas-u-cut-slingback-court-0094503940074302/?cswatch=1',
'https://www.dunelondon.com/casandra-kitten-heel-slingback-court-shoe-0094503940027275/?cswatch=1',
'https://www.dunelondon.com/cassius-u-cut-slingback-flat-shoe-1138503940011484/',
'https://www.dunelondon.com/casterly-studded-strap-kitten-heel-shoe-0094503940059630/',
'https://www.dunelondon.com/catelyn-open-back-studded-tbar-court-shoe-0094503940062484/',
'https://www.dunelondon.com/caydence-peep-toe-wedge-sandal-0094500620001059/',
'https://www.dunelondon.com/caydence-peep-toe-wedge-sandal-0094500620001164/?cswatch=1',
'https://www.dunelondon.com/charllotte-pointed-toe-flat-shoe-0094503940087690/',
'https://www.dunelondon.com/cherubb-contrasting-kitten-heel-slingback-court-shoe-0094503940064039/',
'https://www.dunelondon.com/cherubb-contrasting-kitten-heel-slingback-court-shoe-0094503940064061/?cswatch=1',
'https://www.dunelondon.com/christyne-pointed-two-part-court-shoe-0094503940060171/',
'https://www.dunelondon.com/clareece-cross-over-strap-pointed-toe-court-shoe-0095503940101011/',
'https://www.dunelondon.com/clemmiee-bow-trim-sling-back-kitten-heel-court-shoe-0094503940099627/',
'https://www.dunelondon.com/clemmiee-bow-trim-sling-back-kitten-heel-court-shoe-0094503940099484/?cswatch=1',
'https://www.dunelondon.com/countess-ankle-strap-pointed-toe-court-shoe-0094503940061103/',
'https://www.dunelondon.com/courtnee-cross-strap-kitten-heel-court-shoe-0094503940067616/?cswatch=1',
'https://www.dunelondon.com/courtnee-cross-strap-kitten-heel-court-shoe-0094503940067171/?cswatch=1',
]

if __name__ == '__main__':
	pool = Pool(processes=8)
	outputs = pool.map(getImage,urls)
	pool.close()
	pool.join()
	f = open(filename, "w", encoding="utf-8")
	f.write("")
	for items in outputs:
		f.write(items['url'])
		f.write('*')
		f.write( items['SKU'] )
		for i in range(0,len(items)-1):
			try:
				f.write('*'+items['image'+str(i)])
			except:
				pass
		f.write('\n')
	print('DONE')