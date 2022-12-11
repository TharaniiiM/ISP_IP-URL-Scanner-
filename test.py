import requests

url = "https://api.metadefender.com/v4/hash/fa26be19de6bff93f70bc2308434e4a440bbad02"

headers = {
    'apikey': "e4a75ced8cd1082843243107f33d9c83"
}

response = requests.request("GET", url, headers=headers)

rr = response.json()["scan_results"]["scan_details"]
c = 0
countofeng=0

for i in rr:
    c = c +1 #engine count
    if(rr[i]["threat_found"]) != "":
        countofeng=countofeng+1
        print(countofeng)

if countofeng > 0:
    print ("test")

elif countofeng > -1:
    print("test2")

        


print(c)