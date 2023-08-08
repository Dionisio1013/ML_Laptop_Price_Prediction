import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup



def neweggscrape(link, csvname):

    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15"}

    page = requests.get(link, headers = headers)

    # Pulling in html contents from website
    Soup1 = BeautifulSoup(page.content, 'html.parser')
    # Prettify makes the 
    Soup2 = BeautifulSoup(Soup1.prettify(), 'html.parser')


    product_title_element = Soup2.find_all('a', {'class': 'item-title'})

    product_titles = []
    product_link = []
    brand = []

    for i, x in enumerate(product_title_element):
   
        # Getting description of comp
        title = x.text.strip() if x else "N/A"
        product_titles.append(title)

        # Getting the brand
        first_word = title.split()[0] if title else "N/A"
        brand.append(first_word)

        # Getting the link
        href_link = x['href'] if x else "N/A"
        product_link.append(href_link)


    df = {
        'Product_title': product_titles,
        'Brand': brand,
        'Links': product_link
    }

    basedf1 = pd.DataFrame(df)

    #print(basedf)


    link2 = []
    windows_version = []
    type_comp = []
    cpu_speed = []
    cpu_type_info = []
    ssd_info = []
    graphics_info = []
    ts_info = []
    resolution_info = []
    memory_info = []
    panel_info = []
    full_price = []


    specsdf = {
        'price': full_price,
        'type': type_comp,
        'link2': link2,
        'os': windows_version,
        'Ghz': cpu_speed,
        'Cpu': cpu_type_info,
        'Ssd': ssd_info,
        'graphics': graphics_info,
        'ts_info': ts_info,
        'resolution': resolution_info,
        'memory/ram': memory_info,
        'panel': panel_info
    }

    for s in basedf1['Links']:
        link2.append(s)

        page = requests.get(s, headers = headers)

        # Pulling in content from page
        Soup1 = BeautifulSoup(page.content, 'html.parser')

        Soup2 = BeautifulSoup(Soup1.prettify(), 'html.parser')

        rows = Soup1.select('table.table-horizontal tbody tr')

    # Loop through the rows to find the one containing "Windows 11 Pro"
        memory_once = False
        cpu_speed_once = False
        cpu_type_once = False
        ssd_once = False
        graphics_once = False
        panel_once = False
        ts_once = False
        resolution_once = False
        os_once = False
        type_once = False
        #weight_once = False

    # Based on the code we are creating a 
        windows_version_value = None
        memory_info_value = None
        cpu_speed_value = None
        cpu_type_info_value = None
        ssd_info_value = None
        graphics_info_value = None
        panel_info_value = None
        ts_info_value = None
        resolution_info_value = None
        full_price_value = None
        type_comp_value = None
        #weight_value = None

        try:
            price_element = Soup2.find('li', class_='price-current')
            if price_element is not None:
                price = price_element.strong.text.strip()
                cents = price_element.sup.text.strip()
                full_price_value = f"${price}{cents}"
            else:
                full_price_value = None
        except AttributeError:
            full_price_value = None

        # Assuming you have a list of rows
        for row in rows:
            th = row.find('th')

            if th and th.text.strip() == "Operating System" and not os_once:
                windows_version_value = row.find('td').text.strip()
                os_once = True

            if th and th.text.strip() == "Memory" and not memory_once:
                memory_info_value = (row.find('td').text.strip())
                memory_once = True

            if th and th.text.strip() == "CPU Speed" and not cpu_speed_once:
                cpu_speed_value = (row.find('td').text.strip())
                cpu_speed_once = True

            if th and th.text.strip() == "CPU Type" and not cpu_type_once:
                cpu_type_info_value = (row.find('td').text.strip())
                cpu_type_once = True

            if th and th.text.strip() == "SSD" and not ssd_once:
                ssd_info_value = (row.find('td').text.strip())
                ssd_once = True

            if th and th.text.strip() == "Graphics Card" and not graphics_once:
                graphics_info_value = (row.find('td').text.strip())
                graphics_once = True

            if th and th.text.strip() == "Panel" and not panel_once:
                panel_info_value = (row.find('td').text.strip())
                panel_once = True


            if th and th.text.strip() == "Touchscreen" and not ts_once:
                ts_info_value = (row.find('td').text.strip())
                ts_once = True

            if th and th.text.strip() == "Type" and not type_once:
                type_comp_value = (row.find('td').text.strip())
                type_once = True


            if th and th.text.strip() == "Resolution" and not resolution_once:
                resolution_info_value = (row.find('td').text.strip())
                resolution_once = True

        windows_version.append(windows_version_value)
        memory_info.append(memory_info_value)
        cpu_speed.append(cpu_speed_value)
        cpu_type_info.append(cpu_type_info_value)
        ssd_info.append(ssd_info_value)
        graphics_info.append(graphics_info_value)
        panel_info.append(panel_info_value)
        ts_info.append(ts_info_value)
        resolution_info.append(resolution_info_value)
        full_price.append(full_price_value)
        type_comp.append(type_comp_value)


    specsdf1 = pd.DataFrame(specsdf)
    basedf1.to_csv(csvname + 'based.csv', index=False)
    specsdf1.to_csv(csvname + '.csv', index=False)


page1 = "https://www.newegg.com/p/pl?d=laptops"
page2  = "https://www.newegg.com/p/pl?d=laptops&page=2"
page3 =  ""
new = "https://www.newegg.com/p/pl?N=100%204814&d=laptops"
newpage4 = "https://www.newegg.com/p/pl?N=4814&d=laptop&page=4"
newpage5 = "https://www.newegg.com/p/pl?N=4814&d=laptop&page=5"
newpage6 = "https://www.newegg.com/p/pl?N=4814&d=laptop&page=6"
newpage7 = "https://www.newegg.com/p/pl?N=4814&d=laptop&page=7"
newpage9 = "https://www.newegg.com/p/pl?N=4814&d=laptop&page=9"
twokpage1 = "https://www.newegg.com/p/pl?N=4814&d=laptop&LeftPriceRange=2000+"
twokpage2 = "https://www.newegg.com/p/pl?N=4814&d=laptop&LeftPriceRange=2000+&page=2"
twokpage3 = "https://www.newegg.com/p/pl?N=4814&d=laptop&page=3&LeftPriceRange=2000+"
onekpage1 = "https://www.newegg.com/p/pl?N=4814&d=laptop&LeftPriceRange=1000+2000"
onekpage2 = "https://www.newegg.com/p/pl?N=4814&d=laptop&LeftPriceRange=1000+2000&page=2"
onekpage3 = "https://www.newegg.com/p/pl?N=4814&d=laptop&page=3&LeftPriceRange=1000+2000"
onekpage4 = "https://www.newegg.com/p/pl?N=4814&d=laptop&page=4&LeftPriceRange=1000+2000&recaptcha=pass"
onekpage5 = "https://www.newegg.com/p/pl?N=4814&d=laptop&page=5&LeftPriceRange=1000+2000"
onekpage6 = "https://www.newegg.com/p/pl?N=4814&d=laptop&page=6&LeftPriceRange=1000+2000"
onekpage7 = "https://www.newegg.com/p/pl?N=4814&d=laptop&page=7&LeftPriceRange=1000+2000"
onekpage8 = "https://www.newegg.com/p/pl?N=4814&d=laptop&PageSize=96&LeftPriceRange=1000+2000&page=7"
onekpage9 = "https://www.newegg.com/p/pl?N=4814&d=laptop&PageSize=96&page=8&LeftPriceRange=1000+2000"
onekpage10 = "https://www.newegg.com/p/pl?N=4814&d=laptop&PageSize=96&page=9&LeftPriceRange=1000+2000"
onekpage11 = "https://www.newegg.com/p/pl?N=4814&d=laptop&PageSize=96&page=11&LeftPriceRange=1000+2000"
onekpage12 = "https://www.newegg.com/p/pl?N=4814&d=laptop&PageSize=96&page=12&LeftPriceRange=1000+2000"
onekpage13 = "https://www.newegg.com/p/pl?N=4814&d=laptop&PageSize=96&page=13&LeftPriceRange=1000+2000"
onekpage14 = "https://www.newegg.com/p/pl?N=4814&d=laptop&PageSize=96&page=14&LeftPriceRange=1000+2000"
sixhundredpage9 = "https://www.newegg.com/p/pl?N=4814&d=laptop&PageSize=96&page=9&LeftPriceRange=600+3000"
windows7_10 = 'https://www.newegg.com/p/pl?N=4814%20600555274%20600555279%20600641753%20100157995&d=laptop&PageSize=96&LeftPriceRange=600+3000'
windows_10page6 = 'https://www.newegg.com/p/pl?N=4814%20100157995%20600641753&d=laptop&PageSize=96&page=6'
 
microsoftpage1 = 'https://www.newegg.com/p/pl?N=50001149%204814&d=laptop&PageSize=96'
microsoftpage2 = 'https://www.newegg.com/p/pl?N=50001149%204814&d=laptop&PageSize=96&page=2'
microsoftpage3 = 'https://www.newegg.com/p/pl?N=50001149%204814&d=laptop&PageSize=96&page=3'

dellpage1 = 'https://www.newegg.com/p/pl?N=50010772%204814&d=laptop&PageSize=200'
dellpage4 = 'https://www.newegg.com/p/pl?N=50010772%204814&d=laptop&PageSize=96&page=4'
dellpage5 = 'https://www.newegg.com/p/pl?N=50010772%204814&d=laptop&PageSize=96&page=5'


testingset1 = 'https://www.newegg.com/p/pl?N=4814&d=laptop&PageSize=96&page=15&LeftPriceRange=1000+2000'
testingset2 = 'https://www.newegg.com/p/pl?N=4814&d=laptop&PageSize=96&page=16&LeftPriceRange=1000+2000'
testingset3 = 'https://www.newegg.com/p/pl?N=4814&d=laptop&PageSize=96'
testingset4 = 'https://www.newegg.com/p/pl?N=4814&d=laptop&PageSize=96&page=2'
testingset5 = 'https://www.newegg.com/p/pl?N=4814%204131%20600564377%20600564386%20601411482%20601360966%20601328394%20601333544%20601211658%20601386351%20601417035%20601417033%20601417037%20601417034%20601417036%20601334042%20601334041%20601334038%20601334035%20601398600%20601342544%20601348983%20601334048%20601408975%20601385033%20601393627%20601385306%20601404164%20601357218%20601346147%20601319657%20601303709%20601330730%20601311098%20601314115%20601332023%20601296173%20601319890%20601346149%20600565854%20601190643%20600004664%20601299212%20601107737%20601296163%20601273472%20601214461%20600551516%20601192828%20601281625%20601107792%20600453185%20600471074%20600451153%20600551521%20600327151%20601313803%20601292420%20601319872%20601301389%20600414617%20601306400%20601303146%20601296388%20601292422%20100157995&d=laptops&PageSize=96'
testingset6 = 'https://www.newegg.com/p/pl?N=4814%204131%20600564377%20600564386%20601411482%20601360966%20601328394%20601333544%20601211658%20601386351%20601417035%20601417033%20601417037%20601417034%20601417036%20601334042%20601334041%20601334038%20601334035%20601398600%20601342544%20601348983%20601334048%20601408975%20601385033%20601393627%20601385306%20601404164%20601357218%20601346147%20601319657%20601303709%20601330730%20601311098%20601314115%20601332023%20601296173%20601319890%20601346149%20600565854%20601190643%20600004664%20601299212%20601107737%20601296163%20601273472%20601214461%20600551516%20601192828%20601281625%20601107792%20600453185%20600471074%20600451153%20600551521%20600327151%20601313803%20601292420%20601319872%20601301389%20600414617%20601306400%20601303146%20601296388%20601292422%20100157995%20600364041%20600364043%20601388486%20600364040%20601281419&d=laptops&PageSize=96&recaptcha=pass'

neweggscrape(testingset6, "testingset6")




# In progress


# Done 
done = "https://www.newegg.com/p/pl?Submit=StoreIM&Category=223&N=100167749"

