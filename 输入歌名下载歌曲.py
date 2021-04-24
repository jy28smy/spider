'''
=====================日期：2021年04月24日=====================
'''
import requests
import json
import re

s = requests.session()
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Host": "www.kuwo.cn",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"
}
def get_rid(url, headers):
    r = s.get('http://www.kuwo.cn', headers=headers)
    csrf_dict = r.cookies.get_dict()

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "csrf": csrf_dict['kw_token'],
        "Host": "www.kuwo.cn",
        "Referer": "http://www.kuwo.cn/search/list?key=%E9%94%99%E4%BD%8D%E6%97%B6%E7%A9%BA",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"
    }

    response = s.get(url, headers=headers).text
    rid = re.search(r'"rid":(\d+)', response).group(1)
    return rid

def get_mp3(rid):
    url = 'http://www.kuwo.cn/url?format=mp3&rid={}&type=convert_url3'.format(rid)
    mp3_url_massage = s.get(url, headers=headers).text
    mp3_url = json.loads(mp3_url_massage)['url']
    print(mp3_url)
    mp3 = requests.get(mp3_url).content
    return mp3

def save_mp3(mp3, title):
    with open(title + '.mp3', 'wb') as f:
        f.write(mp3)
    print('下载成功！')



if __name__ == '__main__':
    title = input('输入歌名：')
    url = 'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn=1&rn=30&httpsStatus=1&reqId=b7b26871-a4e9-11eb-aa27-aff8df92de7d'.format(title)
    rid = get_rid(url, headers)
    mp3 = get_mp3(rid)
    save_mp3(mp3, title)


