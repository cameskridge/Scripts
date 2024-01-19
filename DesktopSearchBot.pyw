#Search bot adjusted for timer; 5 seconds per search, 15 minutes per 4 searches

import webbrowser
import time
import os

edge_path = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'
webbrowser.register('microsoft-edge', None, webbrowser.BackgroundBrowser(edge_path))
browser = 'microsoft-edge'


urls = ['https://www.bing.com/search?q=slauson+boy+2&form=ANSPH1&refig=1236518b784d466bae73381ccd0ea0ea&pc=U531','https://www.bing.com/search?q=stock+market+today&qs=LS&pq=stock+m&sc=10-7&cvid=29F87A7E1BEC45D588202DD143618363&FORM=QBLH&sp=1&ghc=1&lq=0','https://www.bing.com/search?q=cost+of+living+austin+tx&form=ANSPH1&refig=B888142C39284CE78E7F07D57AA78D3B&pc=U531&sp=1&lq=0&qs=AS&pq=cost+of+living+austin&sc=10-21&cvid=b888142c39284ce78e7f07d57aa78d3b', 'https://www.bing.com/search?q=bulking+and+cutting&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=bulking+and+cutting&sc=11-19&sk=&cvid=7E8DDD1FADD84B8FA8127D40DE29DD74&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=nfl+mvp+race&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=nfl+mvp+race&sc=11-12&sk=&cvid=B7E623DABA4C431089B501059BC5351F&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=texans+next+game&form=QBLH&sp=-1&ghc=1&lq=0&pq=texans+next+game&sc=9-16&qs=n&sk=&cvid=2CFE78ECFF5144589E813D1131A62831&ghsh=0&ghacc=0&ghpl=', 
'https://www.bing.com/search?q=ev+charging+stations+near+me&qs=LS&pq=ev+charging+statio&sk=LS1&sc=10-18&cvid=0944B6D7DFC14C5C9D11152ABE294123&FORM=QBRE&sp=2&ghc=1&lq=0',
'https://www.bing.com/search?q=rockets+roster&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=rockets+roster&sc=11-14&sk=&cvid=111391EC1CDC498BB05A965764DE589F&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=software+engineering+no+experience&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=software+engineering+no+experience&sc=11-34&sk=&cvid=3EE6264CD947454EAA53A892C12BF7C8&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=tired+of+upper+lower+split&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=tired+of+upper+lower+split&sc=11-26&sk=&cvid=0DBB3E113902459AA26D15FCEC50695C&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=4+day+high+frequency+split&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=4+day+high+frequency+split&sc=11-26&sk=&cvid=C1DA6E7A4790437DA7559873C35733C1&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=steam+most+played&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=steam+most+played&sc=11-17&sk=&cvid=804BA229F2DA4078B86C546777AD6D62&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=xbox+most+played&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=xbox+most+played&sc=11-16&sk=&cvid=0C30D3A1C46C46CC8CEA58D674D24F9B&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=playstation+most+played&qs=n&form=QBRE&sp=-1&lq=0&pq=playstation+most+played&sc=8-23&sk=&cvid=46F669C460E44341B1C99E4BD02C5518&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=volta+fast+charging&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=volta+fast+charging&sc=10-19&sk=&cvid=475CFE65724D4E659D62E67BFE7BEDDE&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=german+shepherd+average+life+span&qs=MT&pq=german+shepherd+averag&sk=AS1&sc=10-22&cvid=4F022D871BFA446FB84A81442902F507&FORM=QBRE&sp=2&ghc=1&lq=0',
'https://www.bing.com/search?q=Logitech+POP+Keys+Mechanical+Wireless+Keyboard+With+Customizable+Emoji+%2c+Durable+Compact+Design%2c+Bluetooth+Or+USB+Connectivity%2c+Multi-Device%2c+OS+Comp&FORM=HDRSC1',
'https://www.bing.com/search?q=logitech+pop+mechanical+keyboard+review&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=logitech+pop+mechanical+keyboard+review&sc=11-39&sk=&cvid=4361A1A2CD4D407FB4442D0C93FFA702&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=options+settle+time&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=options+settle+time&sc=11-19&sk=&cvid=ABEDA9E7CF4E486FA22473BDAA01DA2F&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=how+many+skill+magazines+are+in+starfield&qs=UT&pq=how+many+skill+ma&sc=10-17&cvid=87A8FA6FEFFA428E9E34794D4C837923&FORM=QBRE&sp=1&ghc=1&lq=0',
'https://www.bing.com/search?q=nfl+playoff+picture&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=nfl+playoff+picture&sc=11-19&sk=&cvid=87B46F59605B41608B7D4357282D3D74&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=wolf+dog&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=wolf+dog&sc=11-8&sk=&cvid=DE45291A316F4E4AA8DFA4017CB8579F&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=top+selling+albums+of+the+year&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=top+selling+albums+of+the+year&sc=11-30&sk=&cvid=F45E3A9B96E54BACACFED9C42809E620&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=top+selling+rap+album&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=top+selling+rap+album&sc=11-21&sk=&cvid=205DB1F6C0554123A02223D83805AABF&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=current+presidential+polls&qs=LS&pq=current+preside&sc=10-15&cvid=1676B455580E4252831FD55772553C0B&FORM=QBRE&sp=1&ghc=1&lq=0',
'https://www.bing.com/search?q=metacritic&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=metacritic&sc=11-10&sk=&cvid=10E4294AC52F40309EB05EBC867C8CF7&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=slickdeals&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=slickdeals&sc=11-10&sk=&cvid=2BEFD3BCF9B145C8B0A97A16CD785E2A&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=youtube&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=youtube&sc=11-7&sk=&cvid=0838B916048744B2A029B62FEB087F49&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=this+week%27s+weather&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=this+week%27s+weather&sc=11-19&sk=&cvid=EF4DEA65DA2D464B882DD23544C9EE8B&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=year+of+the+backup+quarterback&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=year+of+the+backup+quarterbac&sc=2-29&sk=&cvid=974ED0C87D9A4D9998D25E94544A48DA&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=foobar2000&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=foobar2000&sc=11-10&sk=&cvid=2073D5AA9D1F4FCFA213BFE3C8DF72EB&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=average+life+expectancy&qs=LS&pq=average+life&sc=10-12&cvid=3688528C6D98493AA29E306A55503310&FORM=QBRE&sp=1&ghc=1&lq=0',
'https://www.bing.com/search?q=best+bootcamps+for+coding&qs=AS&pq=best+bootcam&sk=LS1&sc=10-12&cvid=1A050826E68245E9BAB4C575FC2BD3A0&FORM=QBRE&sp=2&ghc=1&lq=0',
'https://www.bing.com/search?q=ai+stock+trading&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=ai+stock+trading&sc=11-16&sk=&cvid=C0C6F14E442D4714B2EB108CB615A0B8&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=+4+or+5+day+splits&form=QBLH&sp=-1&ghc=1&lq=0&pq=+4+or+5+day+splits&sc=11-18&qs=n&sk=&cvid=33CBB1B16B8747D2946938C6245913BE&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=tired+eyes&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=tired+eyes&sc=11-10&sk=&cvid=3BE52F9B71204C5AA9584589768F3EE3&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=baggy+eyes&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=baggy+eyes&sc=11-10&sk=&cvid=1D246CB984324091B3B4E4C5EE580940&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=1&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=1&sc=10-1&sk=&cvid=C3BBB445BAC84148AA4CEDA545D55BC0&ghsh=0&ghacc=0&ghpl=', 
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
'https://www.bing.com/search?q=gjhj&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=gjhj&sc=10-4&sk=&cvid=072BA35486F44C1AB395665B441D4D07&ghsh=0&ghacc=0&ghpl='
]

for i in range(len(urls)):
    webbrowser.get(browser).open(urls[i], new=0)
    if (i+1)%4==0:
        time.sleep(901) # 15 minutes
    else:
        time.sleep(6)
#os.system("shutdown /s /t 1") 
