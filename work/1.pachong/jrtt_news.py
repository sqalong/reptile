import json
import requests
from urllib.parse import urlencode
from lxml import etree


def parse_ajax_web():
    url = 'https://www.toutiao.com/api/search/content/?aid'
    headers = {
        'referer': 'https://www.toutiao.com/search/?keyword=%E6%96%B0%E5%9E%8B%E5%86%A0%E7%8A%B6%E7%97%85%E6%AF%92',
        'user - agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 78.0.3904.87Safari / 537.36',
        'cookie': 'tt_webid=6768772540023686669; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6768772540023686669; csrftoken=d0145303df0e33afaad73468b143b3d2; s_v_web_id=k67u751j_WKj8SxA4_1ihi_4vGF_83PO_DLozuf0TGmuG; __tasessionId=5sfwfx75u1580817961553; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1580817967; Hm_lpvt_eaa57ca47dacb4ad4f5a257001a3457c=1580818353'
    }
    # 每个ajax请求要传递的参数
    params = {
        'aid': '24',
        'app_name': 'web_search',
        'offset': '0',
        'format': 'json',
        'keyword': '新型冠状病毒',
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis',
        'timestamp': '1580818562943'
    }
    re = requests.get(url=url, params=params, headers=headers)
    re_str = re.text
    # print(re_str)
    re_json = json.loads(re_str)
    datas = re_json['data'][0]
    print(datas)
    # print(type(datas))
    # for data in datas:
    #     print(data)
        # display = datas['display']
        # print(display)
        # event_flow = display['event_flow'][0]
        # title = event_flow['title']
        # description = event_flow['description']
        # print(title,description)
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
