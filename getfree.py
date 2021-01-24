import time
import requests
today = time.strftime("%m%d")

url = f'https://raw.githubusercontent.com/pojiezhiyuanjun/freev2/master/{today}clash.yml'
info1 = requests.get(url)
if info.status_code == 200:
    with open('free01.yml', 'w', encoding = 'UTF-8') as f:
        f.write(info1.text)
else:
    print (f'{today} no data')

url = f'https://raw.githubusercontent.com/ssrsub/ssr/master/Clash.yml'
info2 = requests.get(url)
if info.status_code == 200:
    with open('free02.yml', 'w', encoding = 'UTF-8') as f:
        f.write(info2.text)
else:
    print (f'{today} no data')

url = f'https://proxypoolss.tk/clash/proxies'
info3 = requests.get(url)
if info.status_code == 200:
    with open('free03.yml', 'w', encoding = 'UTF-8') as f:
        f.write(info3.text)
else:
    print (f'{today} no data')
