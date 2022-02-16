import requests
import json
import jsonpath

url='http://localhost:8080/EasyBuy/Login'

tt = {
    'username':'admin',
    'password':'admin'
}
ee = requests.post(url=url,json=tt)
print(json.dump(ee.json(),indent=4,ensure_ascii=False))  #使用json包,打印json格式换行并且前面空四个空格，通过ascii防止乱码
print('***************************************')

urllogin='http://localhost:8080/EasyBuy/Login'
token = 'Bearer '+jsonpath.jsonpath(tt.json(),'$..token')[0]
headers={
    'Authorization':token
}
