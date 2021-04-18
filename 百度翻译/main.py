'''
=====================日期：2021年04月18日=====================
时间：12:01 
作者：jy28smy
@file:main
@Software：PyCharm
——————————————————————————————————————————————————————————————————————————
'''
import execjs
import requests

def get_sign(word):
    with open('test.js', 'r', encoding='utf-8') as f:
        fjs = f.read()
    js = execjs.compile(fjs)
    rus = js.call('e', word)
    return rus

cookies = 'BIDUPSID=C0520F8CED27AC10AD5568C0ED51B04C; PSTM=1611753557; BAIDUID=C0520F8CED27AC109845A39A57B83A90:FG=1; __yjs_duid=1_56943c62aadbc072fc9ffba69dab63bb1617723700710; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; HISTORY_SWITCH=1; BAIDUID_BFESS=C0520F8CED27AC109845A39A57B83A90:FG=1; H_PS_PSSID=33839_33242_31253_33689_33848_33758_33855_33811; delPer=0; PSINO=7; BA_HECTOR=8ga58h0105ak85250p1g7nbq70q; BCLID=9675459839671386519; BDSFRCVID=544OJexroG38EYQef1jQ5Iv0__weG7bTDYLEOwXPsp3LGJLVJeC6EG0Pts1-dEu-EHtdogKKX2OTHNtF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tbujoKL-JD-3HPnuq4OSb4AVb2TJ2b8sBmcr2hcH0KLKEnRL0McxbfIW24PtBR593GRXs43MQUb1MRLR3R0-Qxr05lQ-Kh3y2JvLKq5TtUtWJKnTDMRh-6K9DlQyKMniynr9-pnkbpQrh459XP68bTkA5bjZKxtq3mkjbPbDfn02eCKuDjRDKICV-frb-C62aKDs2qOIBhcqJ-ovQT-WQqFubfD8-PJu3g3a3qR55l0bHxbeWfvpXn-R0hbjJM7xWeJpaJ5nJq5nhMJmKTLVbML0qto7-P3y523ihIovQpnFfhQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xXj_0DjPVKgTa54cbb4o2WbCQJC-M8pcN2b5oQTJbQJrIK4KD2HCta4LMXM7beq06-lOUWfAkXpJvQnJjt2JxaqRCWJ5TMl5jDh3MKToDb-otexQ7bIny0hvcyIocShn85MjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQh-p52f60eJJA83f; BCLID_BFESS=9675459839671386519; BDSFRCVID_BFESS=544OJexroG38EYQef1jQ5Iv0__weG7bTDYLEOwXPsp3LGJLVJeC6EG0Pts1-dEu-EHtdogKKX2OTHNtF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tbujoKL-JD-3HPnuq4OSb4AVb2TJ2b8sBmcr2hcH0KLKEnRL0McxbfIW24PtBR593GRXs43MQUb1MRLR3R0-Qxr05lQ-Kh3y2JvLKq5TtUtWJKnTDMRh-6K9DlQyKMniynr9-pnkbpQrh459XP68bTkA5bjZKxtq3mkjbPbDfn02eCKuDjRDKICV-frb-C62aKDs2qOIBhcqJ-ovQT-WQqFubfD8-PJu3g3a3qR55l0bHxbeWfvpXn-R0hbjJM7xWeJpaJ5nJq5nhMJmKTLVbML0qto7-P3y523ihIovQpnFfhQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xXj_0DjPVKgTa54cbb4o2WbCQJC-M8pcN2b5oQTJbQJrIK4KD2HCta4LMXM7beq06-lOUWfAkXpJvQnJjt2JxaqRCWJ5TMl5jDh3MKToDb-otexQ7bIny0hvcyIocShn85MjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQh-p52f60eJJA83f; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1618669114,1618718539; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1618718539; __yjs_st=2_YTlmZjBlNDBmMTE5NWExZWU5NTRhYjhjZmU5N2U1ZTg4ZTUwYTEwZDFjMDI3OTYyYWVlYTZiYzAwZTYxNWI1MjM3ODQ4ZmJlYTY2ODhiNGVkZWRkNzRkNDEzYzFkZmFiODkzODVmN2IzMWI2NmEwYjhiZTdhNzE0ZTYwNGY0Y2RkNDg1MWI0MTJlN2U0MGVjZWVmZThlZWZhNDg2OGRkZDgwZjA0YjA1N2MzZWVkMjA2NDAyNmU2MDVmMzMwNGZlODc5MDllMmJjZDBkMTFiYzU5MWZhYWEzNTRhOWY1NjRiMGMxMGUwODRiOGE5NDc1MDJkNjE1ZTNiNDBhNThiNl83X2I5NTU0MjQ5; ab_sr=1.0.0_ZjZiNDk5MTYxZGZlMGNmNDk1MDhjYzE4NmRiYWEzNzFkNTdjOGEzMDEzYTM2YjkxNGUxNjU3Zjc0ZjM5ODQ3YzhiOGM3OGZhYmExN2YxMzgzMjA1NGViYjFlYmYyMzM2'
url = 'https://fanyi.baidu.com/v2transapi?'
word = input('把英文翻译成中文：')

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
    'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
    'Cookie': cookies
}

formdata = {
        'from': 'en',
        'to': 'zh',
        'query': word,
        'transtype': 'realtime',
        'simple_means_flag': '3',
        'sign': get_sign(word),
        'token': '47460235b6fcba47e5d7ca0f48eec2e0',
        'domain': 'common'
}

resp = requests.post(url, data=formdata, headers=headers).json()
print(resp)