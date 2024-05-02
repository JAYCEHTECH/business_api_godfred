import requests
import json

url = "https://merchant.cloudhubgh.com/admin/api/initiate_ishare"

payload = json.dumps({
  "receiver": "0272266444",
  "data_volume": 50,
  "reference": "test123",
  "amount": "10"
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer 0v2NKQiUI7nrzjnStHu2oZFpv9AWHB3SdAH',
  'Cookie': '__cf_bm=AhkBpYou0SzQKVZvmy_TsgEg_N5zwzzNpmbkJhDiQ.s-1710156687-1.0.1.1-9LYxwlo5gQGXjr1DAea6zb2AE08Gk81aZGLX2mLycUUBonp6FJ1YJS8wGLHJkEOkBWgAPyG8kckx21FyTrnAFQ'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
