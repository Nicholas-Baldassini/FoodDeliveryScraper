import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

head = {
        "content-type":"application/json", 
        "x-csrf-token":"x", 
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.132 Safari/537.36", 
        "sec-ch-ua-platform":"\"Linux\"", 
        "accept":"*/*", 
        "accept-encoding":"gzip, deflate, br", 
        }


cookie = {
          "jwt-session": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7Il9fand0X3JwY19wcm90ZWN0aW9uX2V4cGlyZXNfYXRfbXMiOjE2OTk5ODcyODIzOTgsIl9fand0X3JwY19wcm90ZWN0aW9uX3V1aWQiOiJhNThmZWQ1MC02ZjA1LTRlNzctODNiOC03N2Y2OTAxMGM2YjQiLCJfX2p3dF9ycGNfcHJvdGVjdGlvbl9jcmVhdGVkX2F0X21zIjoxNjk5ODk5ODgzNDU5fSwiaWF0IjoxNjk5ODk5ODgzLCJleHAiOjE2OTk5ODYyODN9.69dZGzvtzIgie1am8Rng92tlC-gHcTZAqjbWtjgtdJM",
          }


proxies = {
        "http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"
        }
bod = {"storeUuid":"b6c6bc98-32d5-43e6-bd86-79db1800a538"}
#r = requests.request(url="https://www.ubereats.com/_p/api/getStoreV1", method="POST", json=bod, cookies=cookie, headers=head, proxies=proxies, verify=False)

#print(r)

#jsonObject = r.json()

#data = jsonObject["data"]
#meta = str(data["metaJson"])
#parsed = meta

#print(parsed)
#print("-------------------------------------------------------------------------------------------------------------------------------------------------")
#print(json.loads(parsed))
#print(json.dumps(parsed,  indent=2))
                #body=json.dumps(bod),
                #headers=head,
                #cookies=cookie,
                #)
from urllib.parse import unquote
url = "https://www.ubereats.com/abilene/food-delivery/cold-stone-creamery-4249-southwest-dr/Aczl6haTSI6Pazo2zX5FlQ"
r = requests.request(url=url, method="GET", proxies=proxies, verify=False)
raw = str(r.content)
storeUuidInd = raw.find("storeUuid")
storeUuidrawUrl = raw[storeUuidInd+24:storeUuidInd+60]
UuidDecoded = unquote(unquote(storeUuidrawUrl)).strip()

print(UuidDecoded)
print(unquote(unquote(str(r.content)[storeUuidInd+24:storeUuidInd+60])).strip())