import requests

url = "https://api.metadefender.com/v4/domain/www.onlinehacking.xyz"

headers = {
    'apikey': "c6e6819b5d24c6d10dd462d2ba36805f"
}

response = requests.request("GET", url, headers=headers)

print(response.text)