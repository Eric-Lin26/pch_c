
import urllib.request as request 
import json
import time
i = 1
switch_data = []
while i <=10:
    src = "https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=%E5%81%A5%E8%BA%AB%E7%92%B0&page="+str(i)+"=sort=sale/dc"
    with request.urlopen(src) as response: 
        data=json.load(response) 
    webdata = data["prods"]
    
    for line in webdata:
        if line["price"] <= 2550:
            title = line["name"] 
            url = "https://24h.pchome.com.tw/prod/" + line["Id"]
            switch_data.append(title + "," + url + "\n" + "\n")
    time.sleep(5)
    i += 1
with open("switch.txt", "w", encoding="utf-8") as f:
    for line in switch_data:
        f.write(line)

