Raw = """sec-ch-ua: "Chromium";v="117", "Not;A=Brand";v="8"
content-type: application/json
x-uber-client-gitref: 551d143d9deafbc387f2a171d7fe6a55f7ecc665
x-csrf-token: x
sec-ch-ua-mobile: ?0
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.132 Safari/537.36
sec-ch-ua-platform: "Linux"
accept: */*
origin: https://www.ubereats.com
sec-fetch-site: same-origin
sec-fetch-mode: cors
sec-fetch-dest: empty
referer: https://www.ubereats.com/ca/store/south-st-burger-john-st/tsa8mDLVQ-a9hnnbGAClOA
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9"""



#Cookie1 = """dId=aedd96d3-6a40-498f-a826-255d1e6adcfb; marketing_vistor_id=17ff07a1-3728-4c04-ae64-896877f9b7b0; uev2.gg=true; CONSENTMGR=c1:1%7Cc2:1%7Cc3:1%7Cc4:1%7Cc5:1%7Cc6:1%7Cc7:1%7Cc8:1%7Cc9:1%7Cc10:1%7Cc11:1%7Cc12:1%7Cc13:1%7Cc14:1%7Cc15:1%7Cts:1698264825567%7Cconsent:true; _scid=ccb10732-4e74-48bb-a9b8-a403b354e044; _gcl_au=1.1.71845391.1698264826; _fbp=fb.1.1698264830996.1090244431; _tt_enable_cookie=1; _ttp=VUaT1EG1uS2mDIcM_DtPMO5rlHt; uev2.id.xp=6027701d-47ec-4f83-9fef-4e3f118f1dec; uev2.id.session=6a4e4a42-2dee-46bd-8222-b59c2647c555; uev2.ts.session=1699454469537; jwt-session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7Il9fand0X3JwY19wcm90ZWN0aW9uX2V4cGlyZXNfYXRfbXMiOjE2OTk1NDEzODY1NTksIl9fand0X3JwY19wcm90ZWN0aW9uX3V1aWQiOiIxMjFjMTYzZC1hN2YxLTQyMmYtYTA2Zi0wODE2YWZkYTg5ZmQiLCJfX2p3dF9ycGNfcHJvdGVjdGlvbl9jcmVhdGVkX2F0X21zIjoxNjk5NDU0NDY5NTU5fSwiaWF0IjoxNjk5NDU0NDY5LCJleHAiOjE2OTk1NDA4Njl9.WdCtwpOCY0kcMqxUA7C-YkhGxNvTrQn4yj6CbDtFUqk; utag_main_v_id=018b6878bebf0013efc1bfe9592902074001b06c00b78; utag_main__sn=2; utag_main_ses_id=1699454471827%3Bexp-session; utag_main__pn=1%3Bexp-session; utm_medium=undefined; fm_conversion_id=undefined; utm_source=undefined; utag_main__ss=0%3Bexp-session; _userUuid=; _scid_r=ccb10732-4e74-48bb-a9b8-a403b354e044; _gid=GA1.2.1425708050.1699454472; _ga=GA1.1.1393685174.1698264826; _sctr=1%7C1699419600000; _yjsu_yjad=1699454473.444621f1-b44a-4a20-851a-727b2e4e3f74; uev2.diningMode=DELIVERY; mcd_restaurant=Healthy Planet (322 Yonge Street, Toronto); _gat_tealium_0=1; utag_main__se=10%3Bexp-session; utag_main__st=1699456849323%3Bexp-session; _uetsid=dd7acb807e4411eeafd7a52d19975f6d; _uetvid=0359ed60737311ee8d412fbd4d3b5e99; _ga_P1RM71MPFP=GS1.1.1699454472.3.1.1699455050.59.0.0"""
Cookie2 = """dId=aedd96d3-6a40-498f-a826-255d1e6adcfb; marketing_vistor_id=17ff07a1-3728-4c04-ae64-896877f9b7b0; uev2.gg=true; CONSENTMGR=c1:1%7Cc2:1%7Cc3:1%7Cc4:1%7Cc5:1%7Cc6:1%7Cc7:1%7Cc8:1%7Cc9:1%7Cc10:1%7Cc11:1%7Cc12:1%7Cc13:1%7Cc14:1%7Cc15:1%7Cts:1698264825567%7Cconsent:true; _scid=ccb10732-4e74-48bb-a9b8-a403b354e044; _gcl_au=1.1.71845391.1698264826; _fbp=fb.1.1698264830996.1090244431; _tt_enable_cookie=1; _ttp=VUaT1EG1uS2mDIcM_DtPMO5rlHt; utag_main_v_id=018b6878bebf0013efc1bfe9592902074001b06c00b78; _sctr=1%7C1699419600000; _yjsu_yjad=1699454473.444621f1-b44a-4a20-851a-727b2e4e3f74; uev2.id.session=3de81dfe-dc8d-4b4c-a488-e119e429c9b3; uev2.ts.session=1699899883438; utag_main__sn=3; utag_main_ses_id=1699899885148%3Bexp-session; utag_main__ss=0%3Bexp-session; _gid=GA1.2.981576573.1699899886; uev2.loc=%7B%22address%22%3A%7B%22address1%22%3A%22South%20St.%20Burger%22%2C%22address2%22%3A%2220%20John%20St%2C%20Toronto%2C%20M5V%200G5%22%2C%22aptOrSuite%22%3A%22%22%2C%22eaterFormattedAddress%22%3A%2220%20John%20St%2C%20Toronto%2C%20ON%20M5V%200G5%2C%20CA%22%2C%22subtitle%22%3A%2220%20John%20St%2C%20Toronto%2C%20M5V%200G5%22%2C%22title%22%3A%22South%20St.%20Burger%22%2C%22uuid%22%3A%22%22%7D%2C%22latitude%22%3A43.644504%2C%22longitude%22%3A-79.3892045%2C%22reference%22%3A%2297c73339-0e2c-3abc-b637-800e689c73f7%22%2C%22referenceType%22%3A%22uber_places%22%2C%22type%22%3A%22uber_places%22%2C%22addressComponents%22%3A%7B%22city%22%3A%22Toronto%22%2C%22countryCode%22%3A%22CA%22%2C%22firstLevelSubdivisionCode%22%3A%22ON%22%2C%22postalCode%22%3A%22M5V%200G5%22%7D%2C%22categories%22%3A%5B%22AMERICAN%22%2C%22BURGERS%22%2C%22SHOPS_AND_SERVICES%22%2C%22RESTAURANT%22%2C%22point_of_interest%22%2C%22FAST_FOOD%22%2C%22FOOD_AND_BEVERAGE%22%5D%2C%22originType%22%3A%22user_autocomplete%22%2C%22source%22%3A%22manual_auto_complete%22%7D; uev2.id.xp=d3fdfcc3-523f-4a0d-88ed-aa9365f5afbf; utm_medium=undefined; fm_conversion_id=undefined; utm_source=undefined; u.bdc=62c94fd1e06e315eeab9f46d958a5fb6:7NygYd3Ptn2GMncJ:PV55Gpn+geJZnyikzjiSWX8S7c7gaQnTgcOd9EiV/SoeG/J2:JR0DU6+MmGYfrQ1lCgq+uw==; jwt-session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7Il9fand0X3JwY19wcm90ZWN0aW9uX2V4cGlyZXNfYXRfbXMiOjE2OTk5ODcyODIzOTgsIl9fand0X3JwY19wcm90ZWN0aW9uX3V1aWQiOiJhNThmZWQ1MC02ZjA1LTRlNzctODNiOC03N2Y2OTAxMGM2YjQiLCJfX2p3dF9ycGNfcHJvdGVjdGlvbl9jcmVhdGVkX2F0X21zIjoxNjk5ODk5ODgzNDU5fSwiaWF0IjoxNjk5ODk5ODgzLCJleHAiOjE2OTk5ODYyODN9.69dZGzvtzIgie1am8Rng92tlC-gHcTZAqjbWtjgtdJM; uev2.diningMode=DELIVERY; utag_main__pn=3%3Bexp-session; _userUuid=; _ga_P1RM71MPFP=GS1.1.1699899885.4.1.1699901243.24.0.0; _ga=GA1.2.1393685174.1698264826; _scid_r=ccb10732-4e74-48bb-a9b8-a403b354e044; utag_main__se=18%3Bexp-session; utag_main__st=1699903074518%3Bexp-session; _gat_tealium_0=1; _uetsid=ec828060825111ee8eebcf95a2c8ffb2; _uetvid=0359ed60737311ee8d412fbd4d3b5e99"""



# Cookie version
#Raw=Raw.replace("=", "\": \"").replace("; ", "\",\n\"").replace("=", "\" \"")
#Cookie1 = Cookie1.replace("=", "\": \"").replace("; ", "\",\n\"").replace("=", "\" \"")
Cookie2 = Cookie2.replace("=", "\": \"").replace("; ", "\",\n\"").replace("=", "\" \"")
#print(Cookie1)
print(Cookie2)

# Header version
#Raw = Raw.replace(":", "\":\"").replace("\n", "\", \n \"")
#print("{\"" +Raw +"\"}")