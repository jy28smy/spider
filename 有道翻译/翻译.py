import requests
from hashlib import md5
import time
import random

url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
word = input('输入要翻译的词句：')

random_num = random.randint(0, 9)
lts = str(int(time.time()*1000))
salt = lts + str(random_num)
data = "fanyideskweb" + word + salt + "Tbh5E8=q6U3EXe+&L[4c@"
md = md5()
md.update(data.encode())
sign = md.hexdigest()

formdata = {
        'i': word,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'lts': lts,
        'bv': 'eff2e73dc527a143fb4d0a678a264090',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
        }
# 如果出现 errorcode:50 先尝试更新cookie解决
cookie = 'DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; OUTFOX_SEARCH_USER_ID=570427431@116.53.58.99; JSESSIONID=abcOHJ94eb7MJ_XMxlBJx; OUTFOX_SEARCH_USER_ID_NCOO=1334789059.2964072; _ntes_nnid=a2201d5c6dad97aeb36c8ce5d7483338,1618584905689; ___rl__test__cookies=1618586910439'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
    'Referer': 'https://fanyi.youdao.com/?keyfrom=dict2.top',
    'Cookie': cookie
}

response = requests.post(url, data=formdata, headers=headers).json()
print(response['translateResult'][0][0]['tgt'])
