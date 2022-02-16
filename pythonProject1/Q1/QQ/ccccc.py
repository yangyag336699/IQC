import requests
import json

url='http://localhost:8080/EasyBuy/Login'
dedr='loginName=admin&password=123456&action=login'

tt=requests.post(url=url,params=dedr)
# print(tt.text)
print(json.dumps(tt.json(),indent=4,ensure_ascii=False))




# import requests
# import json
#
# url='http://localhost:8080/EasyBuy/Login'
# data='loginName=admin&password=123456&action=login'
#
# #req=requests.request('POST',url=url,params=data)
# req=requests.post(url=url,params=data)
# print(req.text)
# #print(json.dumps(req.json(),indent=4, ensure_ascii=False))
