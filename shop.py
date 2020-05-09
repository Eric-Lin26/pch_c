import urllib.request as request
import json
import time

i = 1
switch_data = []
while i <= 5:
    src = "https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=%E5%81%A5%E8%BA%AB%E7%92%B0&page="+str(i)+"=sort=sale/dc"
    req = request.Request(src, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
    })

    with request.urlopen(req) as response: 
        data = json.load(response) 
    webdata = data["prods"]
    
    for line in webdata:
        #if line["price"] < 7000:
        title = line["name"]
        time.sleep(5) 
        url = "https://24h.pchome.com.tw/prod/" + line["Id"]
        switch_data.append(title + "," + url + "\n" + "\n")
    i += 1

with open("switch.txt", "w", encoding="utf-8") as f:
    for line in switch_data:
        f.write(line)

