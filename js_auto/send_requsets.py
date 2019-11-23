import requests
from data import *
import pprint

def parse_str(arg_str):
    res_obj = {}
    for i in arg_str.splitlines():
        split_list = i.split(":")

        if len(split_list) < 2:
            continue
        print(split_list)
        res_obj[split_list[0].strip( ' ' )] = split_list[1].strip( ' ' )
    return res_obj

url = "http://apply.ccopyright.com.cn/r11applicationforms/save.do"
payload = parse_str(content_str)
headers = parse_str(headers_str)
print(headers)
# cookies = parse_str(cookies_str)

r = requests.post(url,data=payload,headers=headers)
pprint.pprint(r.text)