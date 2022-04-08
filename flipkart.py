from bdb import set_trace
from email.mime import image
from itertools import count
from weakref import proxy
from pip import main
import requests
from bs4 import BeautifulSoup
from lxml import html
from lxml import etree
import random as rd
import time


def get_proxy():
    proxies = [
    
    {
    'http': 'http://youparcel:Proxy2022!@us-ca.proxymesh.com:31280',
    'http': 'https://youparcel:Proxy2022!@us-ca.proxymesh.com:31280',
     },
     {
    'http': 'http://youparcel:Proxy2022!@us-ny.proxymesh.com:31280',
    'http': 'https://youparcel:Proxy2022!@us-ny.proxymesh.com:31280',
    },
    {
    'http': 'http://youparcel:Proxy2022!@us-fl.proxymesh.com:31280',
    'http': 'https://youparcel:Proxy2022!@us-fl.proxymesh.com:31280',
    },
    {
    'http': 'http://youparcel:Proxy2022!@us.proxymesh.com:31280',
    'http': 'https://youparcel:Proxy2022!@us.proxymesh.com:31280',
    },
    {
    'http': 'http://youparcel:Proxy2022!@open.proxymesh.com:31280',
    'http': 'https://youparcel:Proxy2022!@open.proxymesh.com:31280',
    }
    ]
    return rd.choice(proxies)


links = [
'https://www.flipkart.com/computers/laptops/pr?sid=6bo,b5g&otracker=categorytree',"https://www.flipkart.com/laptop-accessories/replacement-screens/pr?sid=6bo,ai3,ac1&otracker=categorytree",
"https://www.flipkart.com/laptop-accessories/memory-card-reader/pr?sid=6bo,ai3,ban&otracker=categorytree","https://www.flipkart.com/laptop-accessories/power-banks/pr?sid=6bo,ai3,7m7&otracker=categorytree"
"https://www.flipkart.com/laptop-accessories/keyboard-replacement-keys/pr?sid=6bo,ai3,b2u&otracker=categorytree","https://www.flipkart.com/laptop-accessories/mouse/pr?sid=6bo,ai3,2ay&otracker=categorytree",
"https://www.flipkart.com/laptop-accessories/number-pads/pr?sid=6bo,ai3,pvy&otracker=categorytree","https://www.flipkart.com/laptop-accessories/printer-covers/pr?sid=6bo,ai3,bjm&otracker=categorytree",
"https://www.flipkart.com/laptop-accessories/ups/pr?sid=6bo,ai3,pi1&otracker=categorytree","https://www.flipkart.com/laptop-accessories/keyboard-replacement-keys/pr?sid=6bo,ai3,adl&otracker=categorytree",
"https://www.flipkart.com/laptop-accessories/monitor-tv-covers/pr?sid=6bo,ai3,7h1&otracker=categorytree","https://www.flipkart.com/laptop-accessories/spike-busters-surge-protectors/pr?sid=6bo,ai3,mt9&otracker=categorytree",
"https://www.flipkart.com/laptop-accessories/heat-sinks/pr?sid=6bo,ai3,nap&otracker=categorytree","https://www.flipkart.com/laptop-accessories/laptop-bag-covers/pr?sid=6bo,ai3,nye&otracker=categorytree",
"https://www.flipkart.com/laptop-accessories/stands/pr?sid=6bo,ai3,0rp&otracker=categorytree","https://www.flipkart.com/laptop-accessories/hinges/pr?sid=6bo,ai3,63y&otracker=categorytree",
"https://www.flipkart.com/laptop-accessories/projector-screens/pr?sid=6bo,ai3,1vp&otracker=categorytree","https://www.flipkart.com/laptop-accessories/laptop-skins-decals/pr?sid=6bo,ai3,zvm&otracker=categorytree",
"https://www.flipkart.com/laptop-accessories/laptop-adapters/pr?sid=6bo,ai3,8p1&otracker=categorytree","https://www.flipkart.com/laptop-accessories/batteries/pr?sid=6bo,ai3,w65&otracker=categorytree",
"https://www.flipkart.com/laptop-accessories/cooling-padscooling-stands/pr?sid=6bo,ai3,59n&otracker=categorytree","https://www.flipkart.com/laptop-accessories/laptop-bags/pr?sid=6bo,ai3,qq9&otracker=categorytree",
"https://www.flipkart.com/laptop-accessories/keyboards/pr?sid=6bo,ai3,3oe&otracker=categorytree","https://www.flipkart.com/laptop-accessories/hard-drive-enclosures/pr?sid=6bo,ai3,f23&otracker=categorytree",
"https://www.flipkart.com/laptop-accessories/presentation-remotes/pr?sid=6bo,ai3,4hy&otracker=categorytree","https://www.flipkart.com/laptop-accessories/screen-guards/pr?sid=6bo,ai3,csg&otracker=categorytree",
"https://www.flipkart.com/laptop-accessories/usb-gadgets/pr?sid=6bo,ai3,0xm&otracker=categorytree","https://www.flipkart.com/laptop-accessories/hard-disk-cases/pr?sid=6bo,ai3,68d&otracker=categorytree",
"https://www.flipkart.com/laptop-accessories/laser-pointers/pr?sid=6bo,ai3,cn2&otracker=categorytree","https://www.flipkart.com/laptop-accessories/touchpads/pr?sid=6bo,ai3,p1m&otracker=categorytree",
"https://www.flipkart.com/laptop-accessories/keyboard-skins/pr?sid=6bo,ai3,qh2&otracker=categorytree","https://www.flipkart.com/laptop-accessories/webcams/pr?sid=6bo,ai3,r3e&otracker=categorytree",
"https://www.flipkart.com/laptop-accessories/mouse-pads/pr?sid=6bo,ai3,siy&otracker=categorytree","https://www.flipkart.com/laptop-accessories/blank-media/pr?sid=6bo,ai3,x3f&otracker=categorytree",
"https://www.flipkart.com/laptop-accessories/security-locks/pr?sid=6bo,ai3,xk1&otracker=categorytree","https://www.flipkart.com/laptop-accessories/cleaning-kits/pr?sid=6bo,ai3,zy6&otracker=categorytree",
"https://www.flipkart.com/laptop-accessories/wrist-rests/pr?sid=6bo,ai3,7nu&otracker=categorytree","https://www.flipkart.com/laptop-accessories/external-dvd-writers/pr?sid=6bo,ai3,w44&otracker=categorytree",
"https://www.flipkart.com/laptop-accessories/computer-accessories-combos/pr?sid=6bo,ai3,c1j&otracker=categorytree","https://www.flipkart.com/computers/network-components/access-points/pr?sid=6bo,70k,i5e&otracker=categorytree",
"https://www.flipkart.com/computers/network-components/internal-modems/pr?sid=6bo,70k,wvi&otracker=categorytree/computers/network-components/lan-adapters/pr?sid=6bo,70k,4j4&otracker=categorytree","https://www.flipkart.com/computers/network-components/network-interface-cards/pr?sid=6bo,70k,p4a&otracker=categorytree",
"https://www.flipkart.com/computers/network-components/router-ups/pr?sid=6bo,70k,lpq&otracker=categorytree","https://www.flipkart.com/computers/network-components/antenna-amplifiers/pr?sid=6bo,70k,7r9&otracker=categorytree",
"https://www.flipkart.com/computers/network-components/router-antennas-boosters/pr?sid=6bo,70k,hy1&otracker=categorytree","https://www.flipkart.com/computers/network-components/switches/pr?sid=6bo,70k,es5&otracker=categorytree",
"https://www.flipkart.com/computers/network-components/data-cards/pr?sid=6bo,70k,o47&otracker=categorytree","https://www.flipkart.com/computers/network-components/network-servers/pr?sid=6bo,70k,p1r&otracker=categorytree",
"https://www.flipkart.com/computers/network-components/wireless-usb-adapters/pr?sid=6bo,70k,85j&otracker=categorytree","https://www.flipkart.com/computers/network-components/cables/pr?sid=6bo,70k,nj6&otracker=categorytree",
"https://www.flipkart.com/computers/network-components/routers/pr?sid=6bo,70k,2a2&otracker=categorytree","https://www.flipkart.com/computers/network-components/voip-adapters/pr?sid=6bo,70k,hbh&otracker=categorytree",
"https://www.flipkart.com/computers/computer-peripherals/workstations/pr?sid=6bo,tia,zve&otracker=categorytree","https://www.flipkart.com/computers/computer-peripherals/portable-scanners/pr?sid=6bo,tia,fxa&otracker=categorytree",
 "https://www.flipkart.com/computers/computer-peripherals/printers-inks/pr?sid=6bo,tia,ffn&otracker=categorytree","https://www.flipkart.com/computers/computer-peripherals/projectors/pr?sid=6bo,tia,1hx&otracker=categorytree",
 
 "https://www.flipkart.com/computers/computer-peripherals/scanners/pr?sid=6bo,tia,b3v&otracker=categorytree","https://www.flipkart.com/computers/software/utilities/pr?sid=6bo,5hp,992&otracker=categorytree",
 "https://www.flipkart.com/computers/software/learn-software/pr?sid=6bo,5hp,45g&otracker=categorytree","https://www.flipkart.com/computers/software/business-productivity/pr?sid=6bo,5hp,upm&otracker=categorytree",
"https://www.flipkart.com/computers/software/hobbies/pr?sid=6bo,5hp,iqd&otracker=categorytree","https://www.flipkart.com/computers/software/multimedia/pr?sid=6bo,5hp,k45&otracker=categorytree",
"https://www.flipkart.com/computers/software/office-tools/pr?sid=6bo,5hp,cqk&otracker=categorytree","https://www.flipkart.com/computers/software/learn-programming/pr?sid=6bo,5hp,sbb&otracker=categorytree",
 "https://www.flipkart.com/computers/software/operating-system/pr?sid=6bo,5hp,w63&otracker=categorytree","https://www.flipkart.com/computers/software/educational-media/pr?sid=6bo,5hp,vxa&otracker=categorytree",
"https://www.flipkart.com/computers/software/security-software/pr?sid=6bo,5hp,lwb&otracker=categorytree","https://www.flipkart.com/computers/computer-components/spike-busters-surge-protectors/pr?sid=6bo,g0i,mt9&otracker=categorytree",
"https://www.flipkart.com/computers/computer-components/coolers/pr?sid=6bo,g0i,xcm&otracker=categorytree","https://www.flipkart.com/computers/computer-components/thermal-pastes/pr?sid=6bo,g0i,fyv&otracker=categorytree",
"https://www.flipkart.com/computers/computer-components/power-supply-units/pr?sid=6bo,g0i,qbk&otracker=categorytree","https://www.flipkart.com/computers/computer-components/graphic-cards/pr?sid=6bo,g0i,6sn&otracker=categorytree",
"https://www.flipkart.com/computers/computer-components/internal-sound-cards/pr?sid=6bo,g0i,01m&otracker=categorytree","https://www.flipkart.com/computers/computer-components/processors/pr?sid=6bo,g0i,17w&otracker=categorytree",
"https://www.flipkart.com/computers/computer-components/rams/pr?sid=6bo,g0i,s5u&otracker=categorytree","https://www.flipkart.com/computers/computer-components/motherboards/pr?sid=6bo,g0i,y7i&otracker=categorytree/computers/computer-components/combo-motherboards/pr?sid=6bo,g0i,ei5&otracker=categorytree",
"https://www.flipkart.com/computers/computer-components/internal-optical-drives/pr?sid=6bo,g0i,b7w&otracker=categorytree","https://www.flipkart.com/computers/computer-peripherals/printers-inks/toners/pr?sid=6bo,tia,ffn,own&otracker=categorytree",
"https://www.flipkart.com/computers/computer-peripherals/printers-inks/ink-bottles/pr?sid=6bo,tia,ffn,eqr&otracker=categorytree","https://www.flipkart.com/computers/computer-peripherals/printers-inks/ink-cartridges/pr?sid=6bo,tia,ffn,adt&otracker=categorytree",
"https://www.flipkart.com/computers/computer-peripherals/printers-inks/printers/pr?sid=6bo,tia,ffn,t64&otracker=categorytree","https://www.flipkart.com/computers/computer-peripherals/printers-inks/print-servers/pr?sid=6bo,tia,ffn,wur&otracker=categorytree",
"https://www.flipkart.com/computers/computer-peripherals/printers-inks/receipt-printers/pr?sid=6bo,tia,ffn,0kj&otracker=categorytree","https://www.flipkart.com/computers/computer-peripherals/printers-inks/pocket-printers/pr?sid=6bo,tia,ffn,w07&otracker=categorytree",
"https://www.flipkart.com/tablet-accessories/chargers/pr?sid=tyy,jgu,nwb&otracker=categorytree","https://www.flipkart.com/tablet-accessories/cases-covers/pr?sid=tyy,jgu,47g&otracker=categorytree",
"https://www.flipkart.com/tablet-accessories/keyboards/pr?sid=tyy,jgu,77o&otracker=categorytree","https://www.flipkart.com/tablet-accessories/bluetooth-headsets-mic/pr?sid=tyy,jgu,wka&otracker=categorytree",
 "https://www.flipkart.com/tablet-accessories/stylus-pens/pr?sid=tyy,jgu,k0m&otracker=categorytree","https://www.flipkart.com/tablet-accessories/keyboards/pr?sid=tyy,jgu,kbs&otracker=categorytree",
 "https://www.flipkart.com/tablet-accessories/screen-protectors/pr?sid=tyy,jgu,l8r&otracker=categorytree","https://www.flipkart.com/computers/desktop-pcs/all-in-one-pcs/pr?sid=6bo,nl4,igk&otracker=categorytree",
"https://www.flipkart.com/computers/desktop-pcs/mini-pcs/pr?sid=6bo,nl4,okr&otracker=categorytree","https://www.flipkart.com/computers/desktop-pcs/tower-pcs/pr?sid=6bo,nl4,dze&otracker=categorytree",
"https://www.flipkart.com/computers/routers/pr?sid=6bo,2a2&otracker=categorytree","https://www.flipkart.com/computers/data-cards/pr?sid=6bo,o47&otracker=categorytree",
"https://www.flipkart.com/computers/computer-components/monitors/pr?sid=6bo,g0i,9no&otracker=categorytree","https://www.flipkart.com/computers/storage/external-hard-disks/pr?sid=6bo,jdy,nl6&otracker=categorytree",
"https://www.flipkart.com/computers/storage/memory-cards/pr?sid=6bo,jdy,tby&otracker=categorytree","https://www.flipkart.com/computers/storage/pen-drives/pr?sid=6bo,jdy,uar&otracker=categorytree",
 "https://www.flipkart.com/computers/storage/internal-hard-drive/pr?sid=6bo,jdy,dus&otracker=categorytree","https://www.flipkart.com/computers/audio-players/audio-player-accessories/pr?sid=6bo,ord,713&otracker=categorytree",
"https://www.flipkart.com/computers/audio-players/mp4-video-mp3-players/pr?sid=6bo,ord,lhy&otracker=categorytree","https://www.flipkart.com/computers/audio-players/mp3-players/pr?sid=6bo,ord,h2k&otracker=categorytree",
"https://www.flipkart.com/computers/audio-players/ipods/pr?sid=6bo,ord,rrr&otracker=categorytree","https://www.flipkart.com/computers/audio-players/home-audio/pr?sid=6bo,ord,rlj&otracker=categorytree",
"https://www.flipkart.com/computers/video-players/pr?sid=6bo,xdz&otracker=categorytree/computers/tv-video-accessories/3d-video-glasses/pr?sid=6bo,ul6,52z&otracker=categorytree","https://www.flipkart.com/computers/tv-video-accessories/selector-smart-box/pr?sid=6bo,ul6,fcz&otracker=categorytree",
"https://www.flipkart.com/computers/tv-video-accessories/voltage-stabilizers/pr?sid=6bo,ul6,v9r&otracker=categorytree","https://www.flipkart.com/computers/tv-video-accessories/media-players/pr?sid=6bo,ul6,cel&otracker=categorytree",
"https://www.flipkart.com/computers/tv-video-accessories/slingbox/pr?sid=6bo,ul6,u44&otracker=categorytree","https://www.flipkart.com/computers/tv-video-accessories/remote-controllers/pr?sid=6bo,ul6,brg&otracker=categorytree"

] 

def make_tree(url):
    website = requests.get(url,timeout=500000,proxies=get_proxy())
    soupe = BeautifulSoup(website.content,"html.parser")
    # soupe = soupe.encode("utf-8")
    tree = etree.HTML(str(soupe))
    return tree

if __name__ == '__main__':
    # import pdb;pdb.set_trace()
    skiped_links = []
    skiped_products =[]
    counter = 1
    csv_writer = open('data5.csv','w',encoding='utf-8')
   
    for link in links:
        url = link
        try:
            main_tree = make_tree(url)
        except:
            skiped_links.append(url)
            continue
        # import pdb;pdb.set_trace()
        category = main_tree.xpath('//div[@class="_1AtVbE"]/descendant::a[3]/text()')
        if(0 < len(category)):
            category = category[0]
        else:
            category = "else"
        page_number = main_tree.xpath('//div[@class="_2MImiq"]/span[1]/text()')
        if( 0 < len(page_number)):
            page_number = page_number[0]
            page_number = page_number.split(" ")
            if (0< len(page_number)):
                page_number = page_number[-1].replace(",","")
                page_number = int(page_number)
            else:
                page_number = 1
            
            if category == 'Laptops':
                pages = page_number            
            elif page_number > 25:
                pages = 25
            else:
                pages = page_number
        else:
            pages = 2
        for page in range(1,pages):
            if page == 1:
                page_url = url
            else:
                page_url = "{}{}{}" .format(url,"&page=",page)
            page_tree = make_tree(page_url)
            products = page_tree.xpath('//a[@class="_2rpwqI"] | //a[@class="_1fQZEK"]')
            for i in range(len(products)):
                product_url = products[i].get("href")
                product_url = "{}{}" .format("https://www.flipkart.com",product_url)
                try:
                    product_tree = make_tree(product_url)
                except:
                    skiped_products.append(product_url)
                    continue

                images = product_tree.xpath("//div[@class='_2E1FGS']/img")
                title = product_tree.xpath('//h1/span/text()')
                if(0 < len(title)):
                    title = title[0]
                    title = str(title)
                    title = title.replace('\n' , " ")
                    title = title.replace(',' , ";")
                else:
                    title = "title not found"
                price = product_tree.xpath('//div[@class="_25b18c"]/div[1]/text()')
                
                if(0 < len(price)): 
                    price = price[0]
                    price = price.replace(',',"")
                    price = price[1:]

                else:
                    price = "price not found"
                
                source_url = product_url
                category = product_tree.xpath('//div[@class="_1AtVbE"]/descendant::a/text()')
                if (len(category) > 0):
                    category = ">".join(category)
                    category = category.replace(",", ";")
                else:
                    category = "Not found "
                

                brand = product_tree.xpath('//h1/span/text()[1]')
                if (0 < len(brand)):
                    brand = brand[0]
                    brand = brand.split(" ")
                    if (0 < len(brand)):
                        brand =  brand[0]
                else:
                    brand = "Not found"
                description = product_tree.xpath('//div[contains(@class,"_1mXcCf")]/text() |//div[contains(@class,"_1mXcCf")]/p/text()')
                if(description):
                    description = description[0]
                    description = str(description) 
                    description = description.replace('\n'," ")
                    description = description.replace(',',";")
                    
                else:
                    description = "Null"
                
                csv_writer.write('{}{}'.format(source_url,','))
                csv_writer.write('{}{}'.format(category,','))
                csv_writer.write('{}{}'.format(title,','))
                
                img = product_tree.xpath('//div[@class="CXW8mj _3nMexc"]/img')
                if (0 < len(img)):
                    csv_writer.write('{}{}'.format(img[0].get("src"),','))
                else:
                    csv_writer.write('{}{}'.format("image not found",','))

                if (1 < len(images)):
                    csv_writer.write('{}{}'.format(images[1].get("src"),','))
                else:
                    csv_writer.write('{}{}'.format("image not found",','))
                if (2 < len(images)):
                    csv_writer.write('{}{}'.format(images[2].get("src"),','))
                else:
                    csv_writer.write('{}{}'.format("image not found",','))
                if (3 < len(images)):
                    csv_writer.write('{}{}'.format(images[3].get("src"),','))
                else:
                    csv_writer.write('{}{}'.format("image not found",','))
                csv_writer.write('{}{}'.format(brand,','))
                csv_writer.write('{}{}{}'.format("INR ",price,','))
                csv_writer.write('{}{}'.format(description,'\n'))
                
                print(counter)
                counter = counter + 1

      
                
                
            

                