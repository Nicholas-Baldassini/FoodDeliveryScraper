import scrapy
from scrapy.http import request
from scrapy.http.request.form import FormRequest
from scrapy.http import FormRequest
import json
import os
from urllib.parse import unquote

class MenuSpider(scrapy.Spider):
    name = 'menu'
    apiUrl = "https://www.ubereats.com/_p/api/getStoreV1"
    start_urls = []

    url_directory = "../../scripts/Extreme-Uber-Eats-Scraping/scraped-data/restaurant-urls"
    for url_file in sorted(os.listdir(url_directory)):
        with open(f"{url_directory}/{url_file}") as f:
            start_urls.extend([url.strip().split(",")[0] for url in f.readlines()[1:]])
        break # only do 1 file for for development
    
    #start_urls = start_urls[0:6]

    head = {    "content-type":"application/json", 
                "x-csrf-token":"x", 
                "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.132 Safari/537.36", 
                "sec-ch-ua-platform":"\"Linux\"", 
                "accept":"*/*", 
                "accept-encoding":"gzip, deflate, br", 
            }

    print("\n".join(start_urls))

    def Print(self, val):
        # save space
        self.logger.warning("------------------------------------------------------------------------------------------------")
        self.logger.warning(val)
        self.logger.warning("------------------------------------------------------------------------------------------------")

    def start_requests(self): 
        for url in self.start_urls:
            yield scrapy.Request(url,
                                    method="GET", 
                                    callback=self.parseUuid,
                                    headers=self.head)
                             

    def parseMenu(self, response):
        resp = json.loads(response.text)
        status = resp["status"]
        if status != "success":
            raise Exception

        metaJson = json.loads(resp["data"]["metaJson"])
        address = metaJson["address"]
        coordinates = metaJson["geo"]
        ratings = metaJson["aggregateRating"]
        cuisineTypes = metaJson["servesCuisine"]
        restName = metaJson["name"]
        hours = metaJson["openingHoursSpecification"]
        menuInfo = metaJson["hasMenu"]["hasMenuSection"][0]


        yield {restName: menuInfo} # What goes into output.json
    
    def parseUuid(self, response):
        raw = str(response.text)
        storeUuidInd = raw.find("storeUuid")
        storeUuidrawUrl = raw[storeUuidInd+24:storeUuidInd+60]
        UuidDecoded = unquote(unquote(storeUuidrawUrl)).strip()

        self.Print(UuidDecoded)


        form_data = {"storeUuid": UuidDecoded}
        cookieJWT= {"jwt-session": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7Il9fand0X3JwY19wcm90ZWN0aW9uX2V4cGlyZXNfYXRfbXMiOjE2OTk5ODcyODIzOTgsIl9fand0X3JwY19wcm90ZWN0aW9uX3V1aWQiOiJhNThmZWQ1MC02ZjA1LTRlNzctODNiOC03N2Y2OTAxMGM2YjQiLCJfX2p3dF9ycGNfcHJvdGVjdGlvbl9jcmVhdGVkX2F0X21zIjoxNjk5ODk5ODgzNDU5fSwiaWF0IjoxNjk5ODk5ODgzLCJleHAiOjE2OTk5ODYyODN9.69dZGzvtzIgie1am8Rng92tlC-gHcTZAqjbWtjgtdJM"}
        request_body = json.dumps(form_data)
        yield scrapy.Request(self.apiUrl,
                            method="POST",
                            body=request_body,
                            headers=self.head,
                            cookies=cookieJWT,
                            callback=self.parseMenu)
