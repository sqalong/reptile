import json
import requests
from urllib.parse import urlencode
from lxml import etree


def parse_ajax_web():
    url = 'https://www.toutiao.com/api/search/content/?aid'
    headers = {
        'referer': 'https://www.toutiao.com/search/?keyword=%E5%93%88%E5%A3%AB%E5%A5%87',
        'user - agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 78.0.3904.87Safari / 537.36',
        'cookie': 'tt_webid=6768772540023686669; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6768772540023686669; csrftoken=d0145303df0e33afaad73468b143b3d2; s_v_web_id=004af76d9dacd7250ea79b7dd26e5881; __tasessionId=rop1lb1401576771063390'
    }
    # 每个ajax请求要传递的参数
    params = {
        'aid': '24',
        'app_name': 'web_search',
        'offset': '0',
        'format': 'json',
        'keyword': '哈士奇',
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis',
        'timestamp': '1576771069981'
    }
    re = requests.get(url=url, params=params, headers=headers)
    re_str = re.text
    print(re_str)
    re_json = json.loads(re_str)
    datas = re_json['data'][0]
    print(datas)
    print(type(datas))
    for data in datas:
        titil = datas['title']
        print(titil)
    # print(re.text)
    # titles = ye.xpath('data[""0""].title')
    # print(titles)
    # data = json.loads(re.text)
    # print(json.dumps(data, sort_keys=True, indent=4, separators=(', ', ': '), ensure_ascii=False))
    # w = json.dumps(data)
    # resp = urllib.request.urlopen(ajax_url)
    # ele_json = json.loads(resp.read())
    # print(data)
    # print(response)
    # # ajax请求返回的是json数据，通过调用json()方法得到json数据
    # json =etree.HTML(re.text)
    # print(json)
    # print(json.keys())
    # data = json.get('data')


parse_ajax_web()
