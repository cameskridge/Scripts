'''This program is designed to farm bing search query points that can be exchanged for gift cards and other items.
This allows you to get 170 points with no effort by searching from the desktop view through the Microsoft Edge browswer.'''

import webbrowser
import time

edge_path = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'
webbrowser.register('microsoft-edge', None, webbrowser.BackgroundBrowser(edge_path))
browser = 'microsoft-edge'


urls = ['https://www.bing.com/search?q=1&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=1&sc=10-1&sk=&cvid=C3BBB445BAC84148AA4CEDA545D55BC0&ghsh=0&ghacc=0&ghpl=', 
'https://www.bing.com/search?q=h&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=h&sc=10-1&sk=&cvid=F958E779C58F4D22AE99461FFD47077A&ghsh=0&ghacc=0&ghpl=', 
'https://www.bing.com/search?q=hjhkjh&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=hjhkjh&sc=3-6&sk=&cvid=37839DBFC3194898938199BB274C2EFE&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=2&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=2&sc=10-1&sk=&cvid=0EF1B21813134A9C87A1D3F22171DD8D&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=23&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=23&sc=10-2&sk=&cvid=346ABD8D2C9549159C3DF8F2318FEF76&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=24&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=24&sc=10-2&sk=&cvid=18D97D0DFE584D72A4D67D86B3B5AF04&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=247&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=247&sc=10-3&sk=&cvid=F263D47A5B6A4F869C15FBFB7D2543C7&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=2479&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=2479&sc=10-4&sk=&cvid=DACBF7DF308D40B0ABF8D96FB5C9BC99&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=247910&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=247910&sc=10-6&sk=&cvid=DD56DE4BE76C45DD9E2D5206F1953447&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=hggdddd&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=hggdddd&sc=10-7&sk=&cvid=9CF7D838339047988588493BA5B8B260&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=hggddddf&qs=n&form=QBRE&sp=-1&lq=0&pq=hggddddf&sc=10-8&sk=&cvid=0A45974EE87F4303B3D2ACFFEDF6846F&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=ffdgd&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=ffdgd&sc=10-5&sk=&cvid=4A7685EBD1E545CCAEC51CF51BEBD694&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=fgrrrrr&qs=n&form=QBRE&sp=-1&ghc=2&lq=0&pq=fgrrrrr&sc=10-7&sk=&cvid=81B20C12E5064B038D78A7C0098A55E6&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=fgrrrrrsass&qs=n&form=QBRE&sp=-1&lq=0&pq=fgrrrrrsass&sc=0-11&sk=&cvid=ECBC0994222A4C37A63DDE4E7C50EBE6&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=fgrrrrrsasscxxc&qs=n&form=QBRE&sp=-1&lq=0&pq=fgrrrrrsasscxxc&sc=0-15&sk=&cvid=0E069912817241FBB2D4375F1C322805&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=fgrrrrrsasscxx&qs=n&form=QBRE&sp=-1&lq=0&pq=fgrrrrrsasscxx&sc=0-14&sk=&cvid=CEF37E6E422F4A9E8E35CB40F9241457&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=fgrrrrrsassc&qs=n&form=QBRE&sp=-1&lq=0&pq=fgrrrrrsassc&sc=0-12&sk=&cvid=1329A924B55B4084B5F46ECD08B05939&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=fgrrrrrsasscqq&qs=n&form=QBRE&sp=-1&lq=0&pq=fgrrrrrsasscqq&sc=0-14&sk=&cvid=86276CD1DE6845F48DFF5FF2A1DB4CDB&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=fgrrrrrsasscqqj&qs=n&form=QBRE&sp=-1&lq=0&pq=fgrrrrrsasscqqj&sc=0-15&sk=&cvid=841347014C294760A4574E43505CCF5A&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=fgrrrrrsasscqqjh&qs=n&form=QBRE&sp=-1&lq=0&pq=fgrrrrrsasscqqjh&sc=0-16&sk=&cvid=CB1EF430C29A43F4B8A3A5BF4EE01A2F&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=fgrrrrrsasscqqjhg&qs=n&form=QBRE&sp=-1&lq=0&pq=fgrrrrrsasscqqjhg&sc=0-17&sk=&cvid=80767B9C092E424DB629845C5637BCEB&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=fgrrrrrsasscqqjhgg&qs=n&form=QBRE&sp=-1&lq=0&pq=fgrrrrrsasscqqjhgg&sc=0-18&sk=&cvid=D6BDF7A76B93413AA16DBD46EAD775F6&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=fgrrrrrsasscqqjhggf&qs=n&form=QBRE&sp=-1&lq=0&pq=fgrrrrrsasscqqjhggf&sc=0-19&sk=&cvid=45D448C1A0534245A872DCD91D8D26CF&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?pglt=2081&q=gj&cvid=c265ac266ed444a18d939b02ed8ac23a&aqs=edge.0.0l9.2031j0j1&FORM=ANNTA1&PC=U531',
'https://www.bing.com/search?q=gjh&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=gjh&sc=10-3&sk=&cvid=39CA4037FC9A4D309852F205268E6A16&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=gjhj&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=gjhj&sc=10-4&sk=&cvid=072BA35486F44C1AB395665B441D4D07&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=gjhjg&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=gjhjg&sc=6-5&sk=&cvid=12CCDDD02C994BE3AEED05338D17965F&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=gjhjgf&qs=n&form=QBRE&sp=-1&lq=0&pq=gjhjgf&sc=10-6&sk=&cvid=27F8ACDBF9BC407E80D5A9751AF2E9D5&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=gjhjgff&qs=n&form=QBRE&sp=-1&lq=0&pq=gjhjgff&sc=10-7&sk=&cvid=25F4F97E6C5F4B1CBA76C2B0FC175D6E&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=gjhjgffg&qs=n&form=QBRE&sp=-1&lq=0&pq=gjhjgffg&sc=7-8&sk=&cvid=E5EBF15767D9488AA1413F20FE47704C&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=gjhjgffgf&qs=n&form=QBRE&sp=-1&lq=0&pq=gjhjgffgf&sc=6-9&sk=&cvid=13420ADEB37E481F86D112495D268808&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=gjhjgffgffd&qs=n&form=QBRE&sp=-1&lq=0&pq=gjhjgffgffd&sc=0-11&sk=&cvid=F6F6E32E15B24180841BB631CC6B968C&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=gjhjgffgffdhh&qs=n&form=QBRE&sp=-1&lq=0&pq=gjhjgffgffdhh&sc=0-13&sk=&cvid=9C3FEB2386414B97A7574BC141C45A37&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=lg&form=ANNTH1&refig=e20d1da1b10e4dd893638ba33f3c143f'
]

for url in urls:
    webbrowser.get(browser).open(url, new=0)
    time.sleep(2)