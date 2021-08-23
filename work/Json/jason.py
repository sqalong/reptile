import requests
import json
import pprint
url = "https://pic.sogou.com/pics?query=%C3%A8&mode=1&start=48&reqType=ajax&reqFrom=result&tn=0"

res = requests.get(url)
ans = json.loads(res.text )
# pprint.pprint(ans)
for i in range(40):
    print(ans['items'][i]['ch_site_name'])


