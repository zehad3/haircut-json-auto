import os
import requests
import json

url = "https://google.serper.dev/images"
s_key = os.getenv("SERPERAPI_KEY")
payload = json.dumps({
  "q": "man haircurt"
})
headers = {
  'X-API-KEY': s_key,
  'Content-Type': 'application/json'
}
print("✅ API KEY IS: " + (s_key if s_key else "❌ NOT FOUND"))
response = requests.request("POST", url, headers=headers, data=payload)
data =  response.json()
data = [{"url":img['imageUrl']} for img in data['images']]
with open("public/haircuts.json", "w", encoding="utf8") as f:
    json.dump(data, f, indent=2)
