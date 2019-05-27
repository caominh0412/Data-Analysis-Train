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
debug = 0

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}



downloadfolder = 'glass'
filename= downloadfolder + '.csv'
folder = 'C:/Users/minhcq/Desktop/download/'+downloadfolder

url = ['190665133097*https://vn-live-02.slatic.net/p/4fe2f22615f30d9e744dee1bf3ca6c05.jpg;https://vn-live-02.slatic.net/p/6f09ca6410890bb70d384449a60fefea.jpg;https://vn-live-02.slatic.net/p/a9f08f94f96818e2439e68190d980558.jpg;https://vn-live-02.slatic.net/p/a86fa8d27c809a33ad84852214e8b0dc.jpg;https://vn-live-02.slatic.net/p/648f2f55a55e50f4bde34747b3d6bb25.jpg;;',
'190665130225*https://vn-live-02.slatic.net/p/2c5c751ca1a0277a1b347e6436c8c020.jpg;https://vn-live-02.slatic.net/p/54b44b75c8ac03a0f1474362f827d2d8.jpg;https://vn-live-02.slatic.net/p/c25317a0220dd5c296b2dd677717d446.jpg;https://vn-live-02.slatic.net/p/ef536ba553e4b4ab348f7894f76f0d83.jpg;https://vn-live-02.slatic.net/p/f04a9128a671f439e935f0a6f542b3a4.jpg;;',
'190665105087*https://vn-live-02.slatic.net/p/19fff1777361fc881d26ff06ce44218b.jpg;https://vn-live-02.slatic.net/p/53b0c30048a6ad6f087f13824b93422e.jpg;https://vn-live-02.slatic.net/p/a0c7ec735484cd6925745ecf2837988e.jpg;https://vn-live-02.slatic.net/p/e96984f5d983c91e5ee9805875bc01a3.jpg;https://vn-live-02.slatic.net/p/df4916a45e90fb500fe2d80f8b598833.jpg;https://vn-live-02.slatic.net/p/a7ac50bb0c78c26f4d2ec1b098300c66.jpg;https://vn-live-02.slatic.net/p/a5dc37fb49ec5965235790d86a535a24.jpg',
'800090824087*https://vn-live-02.slatic.net/p/541afa7db6b62e2643fa02004e97fafe.jpg;https://vn-live-02.slatic.net/p/a5932aec299c2a43357f0342bc914195.jpg;https://vn-live-02.slatic.net/p/38699d9ddc231d671dec6f543f47d964.jpg;https://vn-live-02.slatic.net/p/bb665529be2fe5a662d7b0925416cf24.jpg;https://vn-live-02.slatic.net/p/14b259c274f349faf0f6deebd91ee3c6.jpg;https://vn-live-02.slatic.net/p/3debc3f8822bc80f24ce5399721fe3b2.jpg;https://vn-live-02.slatic.net/p/60b36a4dd28c3598c150d283023c665b.jpg',
'883985879775*https://vn-live-02.slatic.net/p/711da3e18001c528910e4ade5547c0c4.jpg;https://vn-live-02.slatic.net/p/b78f19db1926a332e112426c5edcd17a.jpg;https://vn-live-02.slatic.net/p/1733d02157400a63eafb3f2967f25e4e.jpg;https://vn-live-02.slatic.net/p/ebce5c528d14e8c16ca1c070f7e732a2.jpg;https://vn-live-02.slatic.net/p/da36f0781f86d98e92a112dec0623489.jpg;;',
'190665117479*https://vn-live-02.slatic.net/p/2d55e4d94651cb64b708117b609212d7.jpg;https://vn-live-02.slatic.net/p/175963cff9ff97d96362ed3d3c908f09.jpg;https://vn-live-02.slatic.net/p/0c6101ba5017e6159d912fda998ebc9c.jpg;https://vn-live-02.slatic.net/p/932de1cc3d10fbf8eae7d4c7ed47486d.jpg;https://vn-live-02.slatic.net/p/0c8e37294a0a46dba4adb96cb21ece87.jpg;;',
'883985906280*https://vn-live-02.slatic.net/p/e6f1279256c67316007ea8f3e66f746d.jpg;https://vn-live-02.slatic.net/p/29d6fe75791b9ba2452523875b86208f.jpg;https://vn-live-02.slatic.net/p/77aac4a1fccbfc4b696580220f8b22fc.jpg;https://vn-live-02.slatic.net/p/13dc2ff977520c7f0a7bd04c887d8e83.jpg;https://vn-live-02.slatic.net/p/12fdceb17839f83528cde5a316670ff1.jpg;https://vn-live-02.slatic.net/p/9502648a3eea8235233f96cd9bca5c9f.jpg;https://vn-live-02.slatic.net/p/f903835da7397a095ba3804d1597830f.jpg',
'190665131581*https://vn-live-02.slatic.net/p/f7c48683070612f9029fd78421d9a272.jpg;https://vn-live-02.slatic.net/p/209d29b4a89d120d86747e5eee194fbe.jpg;https://vn-live-02.slatic.net/p/23d0e3cc4a305e5ea00ea2f5b885f797.jpg;https://vn-live-02.slatic.net/p/fd9c1c75fc13952120da13ec6d4f1e0d.jpg;https://vn-live-02.slatic.net/p/e13c6958cc67cf2d7d8cb92716ff6b7d.jpg;;',
'190665115529*https://vn-live-02.slatic.net/p/12c33230de949693e1bc6f137a38af71.jpg;https://vn-live-02.slatic.net/p/aa7b41a8625e2ca6146036b0f78828ad.jpg;https://vn-live-02.slatic.net/p/a7dac27740be1e03ab1da40cae041471.jpg;https://vn-live-02.slatic.net/p/d73abbcffc2575ff88e3f48a3b0fe269.jpg;https://vn-live-02.slatic.net/p/4eeda71cd21b4944785356af4d0eea37.jpg;;',
'190665131741*https://vn-live-02.slatic.net/p/711386e9688e656328095d540ccc7370.jpg;https://vn-live-02.slatic.net/p/c4ab88b96c5f3ed59b14072828babfcb.jpg;https://vn-live-02.slatic.net/p/e6e413b343dce2b13825ce2f833c073f.jpg;https://vn-live-02.slatic.net/p/61ebaaebd87556d2f0ea59a082ae740c.jpg;https://vn-live-02.slatic.net/p/3df06e90784aa575f240fb176d0e27ad.jpg;;',
'190665106152*https://vn-live-02.slatic.net/p/e43bc333ed0ead7b941768984cf6c8b0.jpg;https://vn-live-02.slatic.net/p/4d7d27481fab2b14ff4f46364f68fad4.jpg;https://vn-live-02.slatic.net/p/8fc99efa6a26a660073f70b7ba4ba343.jpg;;;;',
'190665007671*https://vn-live-02.slatic.net/p/9dc3ea3d50b0cf3763feb949eab776b7.jpg;https://vn-live-02.slatic.net/p/a9f39410a04c5ebf26eca19ba0125e80.jpg;https://vn-live-02.slatic.net/p/b697186d0bf8a829b88efa7914e37122.jpg;https://vn-live-02.slatic.net/p/b58ad3373f4e9ab03433d92ee429f176.jpg;https://vn-live-02.slatic.net/p/0454a5f8fdb347eb0fe95996281c030c.jpg;https://vn-live-02.slatic.net/p/abc13668dd097d4d8d67697145f8d91e.jpg;https://vn-live-02.slatic.net/p/e4b19961c02efa2e8dfbbfc9612f7074.jpg',
'190665107661*https://vn-live-02.slatic.net/p/d8eff35a235abd620cb3d0590adff6a0.jpg;https://vn-live-02.slatic.net/p/52b2244e2d1126e6ae798edaf27c14fd.jpg;https://vn-live-02.slatic.net/p/44e4335c54f1208aef64bee7e2d20e5e.jpg;https://vn-live-02.slatic.net/p/473f753c4c231bccb8b8cef93e9fa099.jpg;https://vn-live-02.slatic.net/p/d72012368b6142b17d6c8f38b96355e8.jpg;;',
'190665106411*https://vn-live-02.slatic.net/p/5ab3ed4ee8c90d7feac51ada51a8ce90.jpg;https://vn-live-02.slatic.net/p/90b741f74354c70fb06f1efb27a85b06.jpg;https://vn-live-02.slatic.net/p/ddf672e4dcc67b498bc65ae94e112ce3.jpg;https://vn-live-02.slatic.net/p/5c791819faf2fbdbba451b207753116e.jpg;https://vn-live-02.slatic.net/p/bfadb00795f318d463bf14ccf2f0a248.jpg;;',
'190665116854*https://vn-live-02.slatic.net/p/6426a97de6f67e3631beb7e99253bb28.jpg;https://vn-live-02.slatic.net/p/8fe6df1ed347e31fa71a1614e494e59d.jpg;https://vn-live-02.slatic.net/p/d77db48678081f2d360ffab113ae35c5.jpg;https://vn-live-02.slatic.net/p/ff6bcba0371e1a4e0c1240497ab645fc.jpg;https://vn-live-02.slatic.net/p/70972d970126503218023c6b7f6aef93.jpg;https://vn-live-02.slatic.net/p/b2e97baa6172f729407adbb23c5b4e5f.jpg;',
'190665143942*https://vn-live-02.slatic.net/p/5f9fe985bfe6d78a500aedf1c75b8818.jpg;https://vn-live-02.slatic.net/p/39458ae0b410d67a8b103e8e4d1a06dc.jpg;https://vn-live-02.slatic.net/p/5cd084f64dbdfaca071e3f4b16c9ef40.jpg;https://vn-live-02.slatic.net/p/dfc02c8375999c04d50bd66cd02e74c3.jpg;https://vn-live-02.slatic.net/p/6f0a06c1cc6b2086f28b7f52d54bbf5b.jpg;;',
'190665116953*https://vn-live-02.slatic.net/p/4e5a98599d443db8520ec40ab7dfc3d6.jpg;https://vn-live-02.slatic.net/p/0707dab59f5d4b5099905c6c9cb6e0e5.jpg;https://vn-live-02.slatic.net/p/482b3339e5b5ba4c664a089116bbcccb.jpg;https://vn-live-02.slatic.net/p/9ae19910ca3a3adfa0d287b7072518f2.jpg;https://vn-live-02.slatic.net/p/7272e29ed1c478808a94178e9879a055.jpg;https://vn-live-02.slatic.net/p/a5aafea48961de055db804788b037c4a.jpg;https://vn-live-02.slatic.net/p/25153637326880f78a9837d4f7413401.jpg',
'190665123098*https://vn-live-02.slatic.net/p/c67f8644e0a94940d2c748e1ad7a4675.jpg;https://vn-live-02.slatic.net/p/8f0fe759eb1fc59499f8ba54d2ec7a16.jpg;https://vn-live-02.slatic.net/p/957fa83095560c8612e1669399e42e8a.jpg;https://vn-live-02.slatic.net/p/3e0d0a5a34b2c8ef0e478d3d4682b541.jpg;https://vn-live-02.slatic.net/p/c59404c43911a52314d4088b8748e5d0.jpg;;',
'190665106527*https://vn-live-02.slatic.net/p/c25aa18e50c9c5ba62458f6eecb0ea9c.jpg;https://vn-live-02.slatic.net/p/921d8199084ade7a23080586787c8699.jpg;https://vn-live-02.slatic.net/p/f56ebd9dcbf59e86deaaac28fd64b16e.jpg;https://vn-live-02.slatic.net/p/450b7f3e7e991f13044663f4b28c6191.jpg;https://vn-live-02.slatic.net/p/f8933e142d240928d1dcd977f3940792.jpg;;',
'190665114720*https://vn-live-02.slatic.net/p/fa6c967df1cf04135ec15fcd4a64068c.jpg;https://vn-live-02.slatic.net/p/452caf88956409c62420d9a3f2473058.jpg;https://vn-live-02.slatic.net/p/5e8da242539ebd41afa1faf9aeb32023.jpg;https://vn-live-02.slatic.net/p/a4b8d07ca90ec4e8526d3ac4fa50fa40.jpg;https://vn-live-02.slatic.net/p/06a48705da266a2bfbb620c76b914aaf.jpg;;',
'190665133509*https://vn-live-02.slatic.net/p/2eb1c28209850e5971b1d29060cfb1ed.jpg;https://vn-live-02.slatic.net/p/577dc71c184df23c35142abbd46ad53b.jpg;https://vn-live-02.slatic.net/p/609f3640a8b4f2357d22e05b1ac6f4af.jpg;https://vn-live-02.slatic.net/p/fb01cd909f69280c650a28fbe2a54dbb.jpg;https://vn-live-02.slatic.net/p/7e24e5042c08236ae94cbd14aaa449f1.jpg;;',
'190665011975*https://vn-live-02.slatic.net/p/dbde2b0f2e283484c07511997b869e37.jpg;https://vn-live-02.slatic.net/p/f7d380680fc65389e98cfb4e4c8a5e82.jpg;https://vn-live-02.slatic.net/p/dd1b00d70239b2e3c8d59b88efb3248d.jpg;https://vn-live-02.slatic.net/p/eb3dd8d96d835fddbf63a4c502d476bf.jpg;https://vn-live-02.slatic.net/p/7a276c54650a42ee25e97616829002dc.jpg;https://vn-live-02.slatic.net/p/3b4c5535b625d53d90c92f74e34ea212.jpg;https://vn-live-02.slatic.net/p/481de955e396d1a2c0ea178f14bfda7d.jpg',
'190665063264*https://vn-live-02.slatic.net/p/e34e3836b1d59dc08a13d4d125b7809e.jpg;https://vn-live-02.slatic.net/p/0ea686ae1fdfe130025d818f62cd9b5e.jpg;https://vn-live-02.slatic.net/p/9cc642c0f80d04bfe8f67653c1e711b7.jpg;https://vn-live-02.slatic.net/p/081cc7d3202f58f0b9563320dde5d03e.jpg;https://vn-live-02.slatic.net/p/36d1a9a70cf74e1ba7a78a4594d8bf59.jpg;https://vn-live-02.slatic.net/p/114d4d7b43fc4da1cc9f3da4c5b63649.jpg;https://vn-live-02.slatic.net/p/1bd94ef4120d4415319118552fc6b337.jpg',
'190665128451*https://vn-live-02.slatic.net/p/7661e79b94eeee03a0126d9a727e9fe4.jpg;https://vn-live-02.slatic.net/p/374de2b5bfc7c030cd65760db0cbddf7.jpg;https://vn-live-02.slatic.net/p/b0b7923df1e17637e7747c2b88377213.jpg;https://vn-live-02.slatic.net/p/9c397680c825a072ed055f72e22f6812.jpg;https://vn-live-02.slatic.net/p/8c38e2a7ea6bdd3d8425fcf266342322.jpg;https://vn-live-02.slatic.net/p/54a79576ae68373fa1a77903c5e76d80.jpg;https://vn-live-02.slatic.net/p/83ce8d8605a62ec594b4645a754a5b30.jpg',
'190665097030*https://vn-live-02.slatic.net/p/40910d2cb87b89924c951f369cff7d91.jpg;https://vn-live-02.slatic.net/p/cde233d37e77f29e974bac6dfdf503d4.jpg;https://vn-live-02.slatic.net/p/07384537fce6fc346cc045bc8e0643a9.jpg;https://vn-live-02.slatic.net/p/eac4bb17ca04823e4eb6f9a57ae81a09.jpg;;;',
'883985044692*https://vn-live-02.slatic.net/p/25edf1e428dfa8a90c0cc435f4358037.jpg;https://vn-live-02.slatic.net/p/35ddfe8f9946e28db95b44908faa7fd5.jpg;https://vn-live-02.slatic.net/p/1949791522d8c36d1b2018ff181f472e.jpg;https://vn-live-02.slatic.net/p/a075df4613f00f0afb9b6c1f4b902867.jpg;https://vn-live-02.slatic.net/p/c7bc4fd124cdc36d25502bea228cf040.jpg;https://vn-live-02.slatic.net/p/fbae6fe8e2e8262717d6182ed3deaace.jpg;https://vn-live-02.slatic.net/p/088a0b5bcf8c0bd235c46c6f645f0076.jpg',
'190665143768*https://vn-live-02.slatic.net/p/7a154e1a6ce7fee0106faf81ef0444d4.jpg;https://vn-live-02.slatic.net/p/aa50c72deef57d4071a1c723375358c8.jpg;https://vn-live-02.slatic.net/p/9d88ee8866d793b191f00e55d72f0424.jpg;https://vn-live-02.slatic.net/p/06dac2c9b1ed46009a5cad0b007f1189.jpg;https://vn-live-02.slatic.net/p/749308137eb33345ff2446461fc1441c.jpg;;',
'2327300195*https://vn-live-02.slatic.net/p/5b46dc6e3aac689f2b00a5797d583cae.jpg;https://vn-live-02.slatic.net/p/a7f34e799d2883557755eb0f6d0682f4.jpg;https://vn-live-02.slatic.net/p/6849e7f9f19ba0f54158814149708bdb.jpg;https://vn-live-02.slatic.net/p/bcfb260b5e1bde6a71f9bcf5719046bb.jpg;https://vn-live-02.slatic.net/p/2929cd99252c0ff390b08038ee8bd6d5.jpg;;',
'190665118360*https://vn-live-02.slatic.net/p/e760b913d56149d09bb2cf28730a3b4c.jpg;https://vn-live-02.slatic.net/p/93c81f2dfb0312bff4610c014254b27e.jpg;https://vn-live-02.slatic.net/p/226a2422291850802b1673ea9cb14869.jpg;https://vn-live-02.slatic.net/p/22a94cd4fbf9a9ee6a82494385d889c6.jpg;https://vn-live-02.slatic.net/p/6f70f5fe1fd9625426b7e75a1ab1eebb.jpg;;',
'883985986756*https://vn-live-02.slatic.net/p/dddbb6cccf982062c8befca517ce6a1d.jpg;https://vn-live-02.slatic.net/p/724b5ee456ad0d2b051379946f9cf9a4.jpg;https://vn-live-02.slatic.net/p/fc268195f4f88647ed14f7f5a5cd66a1.jpg;https://vn-live-02.slatic.net/p/b1ce0dd895d9e512fd76a389c63c02e5.jpg;https://vn-live-02.slatic.net/p/c3aed919aa90c689158cc8d260d506e0.jpg;https://vn-live-02.slatic.net/p/44b7c271318313896c6fd12d82dfc79b.jpg;https://vn-live-02.slatic.net/p/240b6a8da1b2bff969c3283001ff70ab.jpg',
'190665133202*https://vn-live-02.slatic.net/p/4eaf07f1351ce1cdb4f12434d58d9b23.jpg;https://vn-live-02.slatic.net/p/7790d88c79fdbe6d4ec28b3c007bbf7b.jpg;https://vn-live-02.slatic.net/p/1f5f08050b5845752443c48b150da955.jpg;https://vn-live-02.slatic.net/p/cedf6497ff0a2aa50cbe5020b79bcc09.jpg;https://vn-live-02.slatic.net/p/8a0b2ea12bf83ed5159fabac936049a0.jpg;;',
'190665133301*https://vn-live-02.slatic.net/p/db21c9dc9fa44998cb01c1ea7d599c6d.jpg;https://vn-live-02.slatic.net/p/d549866f9c018174b9e5be4f9488013a.jpg;https://vn-live-02.slatic.net/p/c35f009ba51822d914c78bef10b55992.jpg;https://vn-live-02.slatic.net/p/24bf6c2da885eb807dcd07e7395aaabb.jpg;https://vn-live-02.slatic.net/p/1118c0f0824b2da70f01f3f58061e70a.jpg;;',
'190665144079*https://vn-live-02.slatic.net/p/d239e636f62f92f0a7b9116d3839bff6.jpg;https://vn-live-02.slatic.net/p/fc240e6ed225276dd90a14742744775d.jpg;https://vn-live-02.slatic.net/p/2f937d15bed68af19789e45052c79c92.jpg;https://vn-live-02.slatic.net/p/8064736eb37735b3ab651af43689b353.jpg;https://vn-live-02.slatic.net/p/415dc4f1d5f5033bda71d663870ab4c2.jpg;;',
'190665097122*https://vn-live-02.slatic.net/p/be2ad560a75a07eadbfa1dec888b68ab.jpg;https://vn-live-02.slatic.net/p/947faeff4bdbd61b2f4170cd83b80548.jpg;https://vn-live-02.slatic.net/p/93cee79bb5a46add5c147cc9af5702f3.jpg;https://vn-live-02.slatic.net/p/43151dbdc4808faef09d77116db9a8ce.jpg;https://vn-live-02.slatic.net/p/6c4e8eb6c25d1e33afdec371e4fb231a.jpg;;',
'190665143812*https://vn-live-02.slatic.net/p/a81755e971b649783615085c3370b597.jpg;https://vn-live-02.slatic.net/p/2f508933b5c04ede2ff75d1be176dfd7.jpg;https://vn-live-02.slatic.net/p/7c47a92703e43a991bd9ec81f7246c07.jpg;https://vn-live-02.slatic.net/p/770310593808b508cfeb0c1cd6c5bae1.jpg;;;',
'190665144000*https://vn-live-02.slatic.net/p/eec015c667485fb09b975f70bf3c777a.jpg;https://vn-live-02.slatic.net/p/b81dac97c8f4782ca5e296ad908b72f7.jpg;https://vn-live-02.slatic.net/p/57c54bc3c1a1198f4fc91cc2b5a8b0ee.jpg;https://vn-live-02.slatic.net/p/13dd3a4a5c349e686e0d3ec8ffacc413.jpg;;;',
'883985890763*https://vn-live-02.slatic.net/p/4b33bb9565ea224ddd76d94941286bdd.jpg;https://vn-live-02.slatic.net/p/c64ce1996bc83c3e7d3912f2fa70681a.jpg;https://vn-live-02.slatic.net/p/484ae247d509816a1fd112963d38e85f.jpg;https://vn-live-02.slatic.net/p/e59a77eb6622f3f1cd343a0889f76ab7.jpg;https://vn-live-02.slatic.net/p/a5ca67df97628674c90b34da404f8493.jpg;https://vn-live-02.slatic.net/p/d684c83a431ede15ae0d3d367559ed23.jpg;https://vn-live-02.slatic.net/p/dcbebb670d9103964822c05238c558e9.jpg',
'800090797008*https://vn-live-02.slatic.net/p/c159d4e7396123aae1c8bb572fb45990.jpg;https://vn-live-02.slatic.net/p/cc591571a113a36d88c6fb3d515fc7f3.jpg;https://vn-live-02.slatic.net/p/b92e149b3a0195c431d776e6f9d90d50.jpg;https://vn-live-02.slatic.net/p/d83e89efd69916a989d1b032c4092f59.jpg;https://vn-live-02.slatic.net/p/f833b730ce72b41663d61c12f24c49f7.jpg;https://vn-live-02.slatic.net/p/66b7b712ff58a5d6dd7990d8c34657f0.jpg;https://vn-live-02.slatic.net/p/7101b3ffc482d6f25521b6146cfed590.jpg',
'883985220652*https://vn-live-02.slatic.net/p/903109a3450bcd113e8ecdd67e1bfc4f.jpg;https://vn-live-02.slatic.net/p/22f070f699a29400658ff1eafad1229a.jpg;https://vn-live-02.slatic.net/p/c29c46e3c458698c538ca0747d61083e.jpg;https://vn-live-02.slatic.net/p/eeee718ce45698b7edd2acb203f94919.jpg;https://vn-live-02.slatic.net/p/b3c306a660fcc40b134aa29d68deec3f.jpg;https://vn-live-02.slatic.net/p/873cabec0857456d85622f503c6efea3.jpg;https://vn-live-02.slatic.net/p/15a5e0226691fb710e78c64a23f8e6f9.jpg',
'190665143898*https://vn-live-02.slatic.net/p/e66a509d2edcc1812ed9eeb199f899ae.jpg;https://vn-live-02.slatic.net/p/3d6c54505781c5c5a9a7a697370e2ad8.jpg;https://vn-live-02.slatic.net/p/78b440233c7785ac168212f76dbdbaf8.jpg;https://vn-live-02.slatic.net/p/2754d7bf46a5f61ecbe876fbfe72c4e8.jpg;https://vn-live-02.slatic.net/p/311ba4158acad89a4d034576ace7c215.jpg;;',
'190665008357*https://vn-live-02.slatic.net/p/ff8d62044ccb02ffeab920aca7a47665.jpg;https://vn-live-02.slatic.net/p/dd69cc246fe5e86f2e694586b382389f.jpg;https://vn-live-02.slatic.net/p/d9b8064ef577d828e4f7cc11ab5e8603.jpg;https://vn-live-02.slatic.net/p/0f815e0f20322c71e4daa318831cc650.jpg;https://vn-live-02.slatic.net/p/1749f8c93d43e75e979897268c3b30fb.jpg;https://vn-live-02.slatic.net/p/df71f3691f8728e16fe38b4b172f3bcb.jpg;https://vn-live-02.slatic.net/p/71325d2f8e5ac309c16372f64fb5989c.jpg',
'883985959125*https://vn-live-02.slatic.net/p/2c717c73f8e701973324b71532630d89.jpg;https://vn-live-02.slatic.net/p/c9a11a26981dfbbaab13e77387d99560.jpg;https://vn-live-02.slatic.net/p/6d215d3c71b4b65f8a73409ba6f82786.jpg;https://vn-live-02.slatic.net/p/574dc64d857c1ee908fb09904fb4d6dc.jpg;https://vn-live-02.slatic.net/p/e1750f750e53604a4572f87bf1ae8aa5.jpg;https://vn-live-02.slatic.net/p/5cd06e8945322eb27d21fc9c3ee96fba.jpg;https://vn-live-02.slatic.net/p/13691b7ba9b48631af42a48526737f6d.jpg',
'883985886995*https://vn-live-02.slatic.net/p/111417b1a3f264f59656af49df0312d0.jpg;https://vn-live-02.slatic.net/p/f0206ae414df04d73555e8e55c869d9c.jpg;https://vn-live-02.slatic.net/p/58e7aef8c7515199d021af09fb13a6ee.jpg;https://vn-live-02.slatic.net/p/ac0822b8b37a52d942c54cc3c03b22c8.jpg;https://vn-live-02.slatic.net/p/71459c883403b5b0422f05d3b2c37f3a.jpg;https://vn-live-02.slatic.net/p/0b57336814261af1c3488c0ffdfac782.jpg;https://vn-live-02.slatic.net/p/8df908d7f76d3058bab205e49ebf0f39.jpg',
'190665107791*https://vn-live-02.slatic.net/p/3311f7ab30c1ff26c565f9d8f8e76fc5.jpg;https://vn-live-02.slatic.net/p/5247b2b52118fc67d39a1882648c3345.jpg;https://vn-live-02.slatic.net/p/9f2fecf944dca651ab76fb5c4b130741.jpg;https://vn-live-02.slatic.net/p/3371e12bef46ed4754952093242132af.jpg;https://vn-live-02.slatic.net/p/32a4edac38477ee9fb01409a95cdeea4.jpg;;',
'713472098290*https://vn-live-02.slatic.net/p/6373d5df17ee5ec48cd9132676842a01.jpg;https://vn-live-02.slatic.net/p/4d7d27481fab2b14ff4f46364f68fad4.jpg;https://vn-live-02.slatic.net/p/8fc99efa6a26a660073f70b7ba4ba343.jpg;;;;',
'190665109900*https://vn-live-02.slatic.net/p/151f58926afd82cd8810da906599e963.jpg;https://vn-live-02.slatic.net/p/08f4b39da4b13487bfd42929a4651868.jpg;https://vn-live-02.slatic.net/p/8d0a282ba7f2007866b0198ef1976618.jpg;https://vn-live-02.slatic.net/p/ae52f05ff62e2dabddde06c769bbe731.jpg;https://vn-live-02.slatic.net/p/ded64b10c7234cff31b819aa29bf4f01.jpg;;',
'883985983373*https://vn-live-02.slatic.net/p/e50490866f74d96a103c0c0c7114be0d.jpg;https://vn-live-02.slatic.net/p/58fe95179e8648b201907bb4d402e422.jpg;https://vn-live-02.slatic.net/p/ae76f1d36088f2ba330e0710018e3afb.jpg;https://vn-live-02.slatic.net/p/7ec363848ecb3e65862850726ef4f19a.jpg;https://vn-live-02.slatic.net/p/156b2707f57e21f4d258d3fcbdb5744e.jpg;https://vn-live-02.slatic.net/p/1f8a2a094424922ae2a44cc4b44ac940.jpg;https://vn-live-02.slatic.net/p/08c4b95b8718d46e40064a1154579cd3.jpg',
'883985417540*https://vn-live-02.slatic.net/p/490c8eafd329df014b319e04c09aee8e.jpg;https://vn-live-02.slatic.net/p/073fff2207062d99ba50691d939cf6a0.jpg;https://vn-live-02.slatic.net/p/854487f0b715a83f90403d905e0c6c4e.jpg;https://vn-live-02.slatic.net/p/7a337ce934adf843442d90cf50cb689b.jpg;https://vn-live-02.slatic.net/p/4f0ee61f9b674e23683815be290574a5.jpg;https://vn-live-02.slatic.net/p/4dc0b55431429f2e43d530b3c7972b0a.jpg;https://vn-live-02.slatic.net/p/fec046ab3bcb4defaea1f27fea4884e9.jpg',
'883985973480*https://vn-live-02.slatic.net/p/5a694095300db76c4d465f09b8003e9b.jpg;https://vn-live-02.slatic.net/p/f163e16bcc515d8007670ca9771e0d24.jpg;https://vn-live-02.slatic.net/p/e40b704f0bb105637a3c0aed227e1365.jpg;https://vn-live-02.slatic.net/p/d3b37bb5322f11fadd93fdce4bc96e27.jpg;https://vn-live-02.slatic.net/p/fead5f6957eb3c23e26db763d7e32ea9.jpg;https://vn-live-02.slatic.net/p/a2045a7808c96973d28f8f3f9701a618.jpg;https://vn-live-02.slatic.net/p/5f3143172a77979056223fbc666bf238.jpg',
'190665007541*https://vn-live-02.slatic.net/p/71301d048064190180cff90fa313ad3c.jpg;https://vn-live-02.slatic.net/p/93f1ebc2be885616438b7ca421ec20fe.jpg;https://vn-live-02.slatic.net/p/b2ed4f8097670750b5d45c6af4424d02.jpg;https://vn-live-02.slatic.net/p/5db7e89484b5a7b93fd4ffae29331a8a.jpg;https://vn-live-02.slatic.net/p/8520a8c28c72b35539389e12dedf76ee.jpg;https://vn-live-02.slatic.net/p/b59ba518fa72bd80833e2d2fbeb98dfe.jpg;https://vn-live-02.slatic.net/p/97bba033381e77e87172a8e8f1c013da.jpg',
'883985866669*https://vn-live-02.slatic.net/p/2a92a7d851fa59cb84c03c67ebf21e90.jpg;https://vn-live-02.slatic.net/p/2b7b46a6de0fd13dcf30d01b108474c3.jpg;https://vn-live-02.slatic.net/p/3fd62ec259fd5907fc3eb1caa29a9059.jpg;https://vn-live-02.slatic.net/p/e813280d1eca7d879c56a6b495b8fb80.jpg;https://vn-live-02.slatic.net/p/db929dc04b9eac8869c80e9d4962d86a.jpg;https://vn-live-02.slatic.net/p/17a40f05c26b3497fa9fe0f736ce3f6a.jpg;https://vn-live-02.slatic.net/p/f3e1397335fa4c499df20149709c473a.jpg',
'883985758872*https://vn-live-02.slatic.net/p/3ed8d6bb3366028a659fc0ebc330051e.jpg;https://vn-live-02.slatic.net/p/4d7d27481fab2b14ff4f46364f68fad4.jpg;https://vn-live-02.slatic.net/p/8fc99efa6a26a660073f70b7ba4ba343.jpg;;;;',
'800090851281*https://vn-live-02.slatic.net/p/4199c6ced6bcf7a5f1455979cf99cfb3.jpg;https://vn-live-02.slatic.net/p/622d76e440abbd448397dce0c5500b0a.jpg;https://vn-live-02.slatic.net/p/70f8b78dad68f8d6c2d394fbd873cec5.jpg;https://vn-live-02.slatic.net/p/6e1f86cc596d52c3561ce7b5cdbf73e6.jpg;https://vn-live-02.slatic.net/p/565e161fd2d18f36577e2e45f06f83f8.jpg;;',
'800090797480*https://vn-live-02.slatic.net/p/018c6a17fa994f7c5fd8b5205f32449e.jpg;https://vn-live-02.slatic.net/p/8253e0f1ce9fa997d86c430ed1a114ec.jpg;https://vn-live-02.slatic.net/p/3752bffe7a1d96e53004704406a61138.jpg;https://vn-live-02.slatic.net/p/73fbecdda86c48bd32776142d3914dd7.jpg;https://vn-live-02.slatic.net/p/6d127cabf13ab24ee6c3d93faeae43ff.jpg;https://vn-live-02.slatic.net/p/cf0c5250f958e1104a74e551c8c8db7e.jpg;https://vn-live-02.slatic.net/p/f705c3da25f4b7f241dd8c411caa6468.jpg',
'190665120851*https://vn-live-02.slatic.net/p/5c004c56321b57ef9f14a77e177533e9.jpg;https://vn-live-02.slatic.net/p/4d7d27481fab2b14ff4f46364f68fad4.jpg;https://vn-live-02.slatic.net/p/8fc99efa6a26a660073f70b7ba4ba343.jpg;;;;',
'645435336012*https://vn-live-02.slatic.net/p/2db0677b2a0347791f4a09ab1c59690e.jpg;https://vn-live-02.slatic.net/p/4d7d27481fab2b14ff4f46364f68fad4.jpg;https://vn-live-02.slatic.net/p/8fc99efa6a26a660073f70b7ba4ba343.jpg;;;;',
'883985719910*https://vn-live-02.slatic.net/p/9955ffba3c35b13b26217e3a0db6f928.jpg;https://vn-live-02.slatic.net/p/815290a6755c9a9fa1ad3a23302a4af2.jpg;https://vn-live-02.slatic.net/p/cf316b879fda82371048b856be2be248.jpg;https://vn-live-02.slatic.net/p/c4c0267e8253158012e96d150367a355.jpg;https://vn-live-02.slatic.net/p/bfe6b8e5a9152a7f3eccc92dae342f59.jpg;https://vn-live-02.slatic.net/p/674231075787b79f95c0b33ffebfd93c.jpg;https://vn-live-02.slatic.net/p/2aca43c3e71adec4f33b007b5ce63268.jpg',
'800090796650*https://vn-live-02.slatic.net/p/33d781c9641b81bbdcd1c6dabddfba86.jpg;https://vn-live-02.slatic.net/p/38a33d5e87eaaeb1878cc84eabda2b37.jpg;https://vn-live-02.slatic.net/p/c73e7a5aee7ce51b65b36d715a023d04.jpg;https://vn-live-02.slatic.net/p/d593995ad1160e083325a52f2f434d65.jpg;https://vn-live-02.slatic.net/p/2b502c3eb7ff5960d0225c5414d267e1.jpg;https://vn-live-02.slatic.net/p/8987c01f4d5a400243b51c3b40e634b2.jpg;https://vn-live-02.slatic.net/p/3d9a9fd3f2ed0f78c8dc53a7ad03edbe.jpg',
'883985758759*https://vn-live-02.slatic.net/p/4519adc161bb3212874559ca9604cde2.jpg;https://vn-live-02.slatic.net/p/4d7d27481fab2b14ff4f46364f68fad4.jpg;https://vn-live-02.slatic.net/p/8fc99efa6a26a660073f70b7ba4ba343.jpg;;;;',
'883985885103*https://vn-live-02.slatic.net/p/51904d4a7c6a87645418a9b6b327af18.jpg;https://vn-live-02.slatic.net/p/85b3aa861a7b67cb8380a2d3e9696570.jpg;https://vn-live-02.slatic.net/p/7fd43768ede5eb9ee93b9e6e50c7bf3c.jpg;https://vn-live-02.slatic.net/p/7fac7a2f2f13c31f3795c0085db9286c.jpg;https://vn-live-02.slatic.net/p/ef28f6949d1aff36f0f8cff0b61738dd.jpg;https://vn-live-02.slatic.net/p/e40520d18c8b5ba08c26150598b831b0.jpg;https://vn-live-02.slatic.net/p/dbc79aed87e14f0098477d80db03795d.jpg',
'883985890855*https://vn-live-02.slatic.net/p/3a1b300cd603f0a89511e695185f4910.jpg;https://vn-live-02.slatic.net/p/9f1aa2006976154e15bfe780ab2cb9a5.jpg;https://vn-live-02.slatic.net/p/d4664f14d57bf6b4ba76fcea55a67374.jpg;https://vn-live-02.slatic.net/p/ee89b641fffcb073102ec0b1a5e6c585.jpg;https://vn-live-02.slatic.net/p/033cb1427d1d2c504c55f219eb5f0cb1.jpg;https://vn-live-02.slatic.net/p/481fbcd27b3fb375ce63db161bb7071a.jpg;https://vn-live-02.slatic.net/p/2541e5ee0071805c62e337979a19f81f.jpg',
'883985396425*https://vn-live-02.slatic.net/p/7d25243e921d565e2007dcb2301c1f9b.jpg;https://vn-live-02.slatic.net/p/7193ac691103ea728cd0440856b690ea.jpg;https://vn-live-02.slatic.net/p/7a66019cf4db4beb6ed9faab9e972917.jpg;https://vn-live-02.slatic.net/p/4c665f4278dca4f47b0060257a885c2d.jpg;https://vn-live-02.slatic.net/p/5e1c936696aa554d9a5ebef2b79632aa.jpg;https://vn-live-02.slatic.net/p/3e97b9addfedda48f28cda81ba026515.jpg;https://vn-live-02.slatic.net/p/1a13a4979925f15b0f589f153e01231e.jpg',
'883985830608*https://vn-live-02.slatic.net/p/fe0d28f10326cb640b78cd16f2b83e73.jpg;https://vn-live-02.slatic.net/p/5465ef6faabafe50d1d70a4793714fa6.jpg;https://vn-live-02.slatic.net/p/82a89c6293af1180f0dc51f39db9cf6b.jpg;https://vn-live-02.slatic.net/p/7ad4802d2b4f9b7d8f61b795cd2529a9.jpg;https://vn-live-02.slatic.net/p/1856c5dd771b8f61f937b4c209a2289b.jpg;https://vn-live-02.slatic.net/p/ddeca2bed078afad416b46a9bb9fa7c1.jpg;https://vn-live-02.slatic.net/p/67583fc7d160dacf9dca85468df9c4be.jpg',
'768396001567*https://vn-live-02.slatic.net/p/fa006ced2ffa9e2fc0685b2222cbda8d.jpg;https://vn-live-02.slatic.net/p/f644bb1461ef929d249bb01ea5d634e7.jpg;https://vn-live-02.slatic.net/p/33eabba0c2728f1a9018aa6e35060d83.jpg;https://vn-live-02.slatic.net/p/dbf46077937632be246c6a454a69f41f.jpg;https://vn-live-02.slatic.net/p/cfb900de7b20a01e43c661a8299bb219.jpg;https://vn-live-02.slatic.net/p/6b6eb4e97d932187fc13ddb9d8f40584.jpg;https://vn-live-02.slatic.net/p/f7a390d98630d78ba11a6fbcedcb08e2.jpg',
'713472098405*https://vn-live-02.slatic.net/p/bca70ab39682631c68d96b3f661a3ef0.jpg;https://vn-live-02.slatic.net/p/4d7d27481fab2b14ff4f46364f68fad4.jpg;https://vn-live-02.slatic.net/p/8fc99efa6a26a660073f70b7ba4ba343.jpg;;;;',
'883985886735*https://vn-live-02.slatic.net/p/c9dff5debff45496ffde65e797aed251.jpg;https://vn-live-02.slatic.net/p/d3e90b5366b68216cedec362223c5acb.jpg;https://vn-live-02.slatic.net/p/9cbef288837bc80860a2f3fd804bdfcc.jpg;https://vn-live-02.slatic.net/p/f65dcf3e7f46c2bb004d6fd6cdc71488.jpg;https://vn-live-02.slatic.net/p/414f0671f0775a078e9dfd89edb47112.jpg;https://vn-live-02.slatic.net/p/c5dbe808fb0178de9e7135d2dcbd3e55.jpg;https://vn-live-02.slatic.net/p/5d00b49c023ebc3149672f2541274cf3.jpg',
'768396024214*https://vn-live-02.slatic.net/p/b8eac2c8a89ebcab0e89de9e2a43cb3f.jpg;https://vn-live-02.slatic.net/p/0a08c3ea1b3fd235b3b991882a8a0eed.jpg;https://vn-live-02.slatic.net/p/7936647b47ea7475744fef817b91fa11.jpg;https://vn-live-02.slatic.net/p/c4646c65a5932e7c06ff55344e88406c.jpg;https://vn-live-02.slatic.net/p/50129a8fc6789d8564bdb1c5f6bdbf76.jpg;https://vn-live-02.slatic.net/p/5250de6f16ebe6a239aade6e9826fd71.jpg;',
]


def passthing(excel):
	df = pd.read_excel(excel)
	df.dropna(axis=1,inplace=True,how='all')
	print(df.head())
	row = input('Columns :')
	df.columns=df.iloc[int(row)]
	for i in range(0,int(row)+1):
		df.drop(i,axis=0,inplace=True)
	print(df.columns)
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
def getImage(params):
	if params.find('*') >0:
		item_link = params.split('*')[1]
		saveas = params.split('*')[0]
	else:
		item_link = params
		saveas = ''
	#print('PROCESSING: '+ item_link)
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
			try:
				if saveas != '':
					item_SKU = item_session.html.find('.panel-serial-number')[0].text
					SKU = item_SKU[8:item_SKU.find(' - ')]
					item['SKU'] = SKU
			except:
				item['SKU'] = saveas
				print('Loi ne ?' + saveas)
			#barcode = item_SKU[item_SKU.find('Mã SKU: ')+8:item_SKU.find(')')-1]
			#item['barcode'] = barcode
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
				item['image'+str(i)] ='https:' + item_link.replace('small','master')
				i+=1
		elif item_link.find('aokang') >0:
			item_session = session.get(item_link,verify=False)
			images = item_session.html.find('.slide')
			i = 0
			for image in images:
				item_link = image.attrs['data-thumb']
				item['image'+str(i)] ='https:' + item_link.replace('small','master')
				i+=1
		elif item_link.find('sprox') >0:
			item_session = session.get(item_link,verify=False)
			item_session.html.render()
			images = item_session.html.find('.thumb_item')
			if images == []:
				print('Cant get this link ' + item_link)
			i = 0
			for image in images:
				item_link = image.find('a')[0].attrs['data-zoom-image']
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
					#print('SKU: '+ item['SKU'] +'------ Image: '+item['image'+str(i)] + '------ Downloading: '+ imgdownload)
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

if debug == 0:
	if __name__ == '__main__':
		pool = Pool(processes=4)
		outputs = pool.map(getImage,url)
		pool.close()
		pool.join()
		#f = open(filename, "w", encoding="utf-8")
		#f.write("")
		#for item in outputs:
			#print('SKU: '+ item['SKU'])
		#	f.write(item['SKU'])
		#	for i in range(0,len(item)-1):
		#		f.write('*'+item['image'+str(i)])
				#print(' Image: '+item['image'+str(i)])
		#	f.write('\n')
		print('DONE')
elif debug == 1:
	for i in url:
		getImage(i)

else:
	excel = input('Excel: ')
	df,linkCol = passthing(excel)
	skuCol = input('Cot SKU: ')  
	#linkCol = input('Cot link: ')
	item = getImg_frompandas(df,skuCol,linkCol)
	for i in item:
		getImage(i)
	print('DONE')
