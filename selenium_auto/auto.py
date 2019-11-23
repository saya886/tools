from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time
import xlrd
import random
import requests
import json
import copy
from data_js import data_js_0,data_js_1

from pynput.keyboard import Key, Controller
from multiprocessing import Process
import os


keyboard = Controller()

login_js = '''
document.getElementById("loginId").value = "rango";
document.getElementById("password").value = "67C2i4"
login1();'''

login_js = '''
document.getElementById("loginId").value = "qidehao";
document.getElementById("password").value = "Qdh828"
login1();'''

class auto_obj(object):
    def __init__(self, login_js, data_js_list,file_anme):
        #data_js_list 的第一个需要填写基础数据  剩余需要填写多个著作权信息
        self.login_js = login_js
        self.data_js_list = data_js_list
        self.file_anme = file_anme

    def task_1(self):
        try:
            driver = webdriver.Ie()
            driver.get("http://apply.ccopyright.com.cn/cpcc/column_list_bqdj.jsp")
 
            driver.execute_script(login_js)
            time.sleep(3)
            driver.get("http://apply.ccopyright.com.cn/cpcc/regquery/onlineRegisterForms.jsp")
            time.sleep(3)
            driver.get("http://apply.ccopyright.com.cn/goadatadic/getR11List.do")

            for i in self.data_js_list:
                
                driver.execute_script(i)
                time.sleep(2)

            print("1")
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)

            print("2")
            time.sleep(3)
            driver.find_element_by_name("button_submit").click()
            
            print("3")
            time.sleep(1)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            
            print("4")
            time.sleep(1)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)

            print("5")
            time.sleep(1)
            driver.find_element_by_name("button_print").click()

            print("6")
            time.sleep(2)  
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)

            print("7")
            time.sleep(2)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)

            time.sleep(3)
            print("8")
            keyboard.type(self.file_anme)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(1)
            driver.close()
            print("task success ..........")
        except Exception as s:
            print(s)
            print("task failed ..........")
        
def parse_float_to_str(float_str):
    # 格式化时间
    if float_str == "":
        return " "
    
    date_tuple = xlrd.xldate_as_tuple(float(float_str), 0)

    return str(date_tuple[0]) +"-" + str(date_tuple[1]) + "-" + str(date_tuple[2])

def get_obj_form_str(data_str):
    return json.loads(data_str)

def read_from_execl(begin_index, end_index):
    #返回 dict 列表
    data = xlrd.open_workbook("编写记录.xlsx")
    table = data.sheets()[0]
    data_list = []
    while(begin_index < end_index):

        data_list.append(table.row_values(begin_index))
        begin_index  = begin_index +1
    
    parsed_data = []
    for i in data_list:
        copy_data_dict = {}
        copy_data_dict["full_name"] = i[9]
        copy_data_dict["version"] = i[12]
        copy_data_dict["finish_time"] = parse_float_to_str(i[13])
        copy_data_dict["push_time"] = parse_float_to_str(i[14])
        copy_data_dict["push_addr"] = i[16]

        copy_data_dict["owner_name"] = i[20]
        copy_data_dict["owner_type"] = "企业法人"
        copy_data_dict["owner_id_type"] = "企业法人营业执照"
        copy_data_dict["owner_code"] = i[21]
        copy_data_dict["owner_province"] = i[16] 

        copy_data_dict["hardware_env"] = i[17]
        copy_data_dict["software_env"] = i[18]
        copy_data_dict["language"] = i[19]
        copy_data_dict["row_length"] = random.randint(30000,100000)
        copy_data_dict["main_desc"] = i[11]

        copy_data_dict["proposer_name"] = i[20]
        copy_data_dict["proposer_addr"] = i[22]
        copy_data_dict["proposer_linkman_name"] = i[20]
        copy_data_dict["proposer_email_addr"] = i[24]
        copy_data_dict["proposer_tel"] = int(i[23])
        copy_data_dict["proposer_area_code"] = "200000"
        copy_data_dict["proposer_phone"] = int(i[23])
        parsed_data.append(copy_data_dict)
    return parsed_data

def read_from_api():
    username = "shengchanzhuguan"
    password = "adc6847f56510b6310750cf53cc07fe1"
    # api_base_url = "http://192.168.18.142:8000"
    # api_base_url = "http://erp.qidehao.net:8001"
    api_base_url = "http://203.86.254.94:8001"

    payload = {'username': username, 'password': password}
    login_url = api_base_url+"/auth/login/"
    cookies = requests.post(login_url, data=payload).cookies

    get_list_url = api_base_url+"/flow/tasks/?fn=GetTaskListOnAudit"
    get_detail_url = api_base_url+"/order/sinfobase/{}"
    get_owner_url = api_base_url+"/flow/tasks/?fn=getSinfoDetailById&id={}"

    parsed_data = []

    data_list = get_obj_form_str(requests.get(get_list_url,cookies=cookies).text)
    for i in data_list:
        print(i)
        detail_dict = get_obj_form_str(requests.get(get_detail_url.format(str(i["sinfo"])), cookies=cookies).text)
        owner_list = get_obj_form_str(requests.get(get_owner_url.format(i["sinfo"]), cookies=cookies).text)

        data_dict = {}
        data_dict["full_name"] = detail_dict["name"]
        data_dict["short_name"] = detail_dict["shorterName"]
        data_dict["version"] = detail_dict["version"]
        data_dict["finish_time"] = detail_dict["completionDate"]
        data_dict["push_time"] = detail_dict["publicDate"]
        # 第一个著作权人的城市
        data_dict["push_addr"] = owner_list["obligees"][0]["city"]

        data_dict["hardware_env"] = detail_dict["hardwareEnv"]
        data_dict["software_env"] = detail_dict["softwareEnv"]
        data_dict["language"] = detail_dict["developmentLanguage"]
        data_dict["row_length"] = random.randint(30000,100000)
        data_dict["main_desc"] = detail_dict["mainDesc"]

        # 申请人
        data_dict["proposer_name"] = owner_list["applicant"]["company"]
        data_dict["proposer_addr"] = owner_list["applicant"]["addr"]
        data_dict["proposer_linkman_name"] =owner_list["applicant"]["name"]
        data_dict["proposer_email_addr"] = ["3302271681@qq.com","rango.lzp1@qq.com","shanghaiwa@qq.com"][random.randint(0,2)]
        data_dict["proposer_tel"] = owner_list["applicant"]["phone"]
        data_dict["proposer_area_code"] = owner_list["applicant"]["postalCode"]
        data_dict["proposer_phone"] = owner_list["applicant"]["phone"]

        swap_list = []
        for j in owner_list["obligees"]:
            owner_data_dict = {}
            owner_data_dict["owner_name"] = j["name"]
            owner_data_dict["owner_type"] = j["type"]
            owner_data_dict["owner_id_type"] = j["documentType"]
            owner_data_dict["owner_code"] = j["documentNum"]
            owner_data_dict["owner_province"] = j["province"]
            owner_data_dict["owner_city"] = j["city"]
            swap_list.append(owner_data_dict)
        #著作权人 列表
        data_dict["owner_list"] = swap_list

        parsed_data.append(data_dict)
        # except Exception as e:
        #     print(e)
        #     print("except an exception")
    return parsed_data
            

def make_data_js_from_dict(data_dict_list):
    data_js_str_list = []
    for i in data_dict_list:

        # 没有著作权人
        if len(i["owner_list"]) == 0:
            return False,data_js_str_list
        else:
            
            # parse 著作权人
            owner_js = ""
            for j in i["owner_list"][1:]:
                copy_data_js_1 = copy.deepcopy(data_js_1)
                owner_js = owner_js + copy_data_js_1.format(**j)

            # parse 基本数据
            i["first_owner_name"] = i["owner_list"][0]["owner_name"]
            
            i["first_owner_type"] = ["自然人","","其他组织","其他","","","","","","","","","","","","","","","","","企业法人","机关法人","事业单位法人","社会团体法人"].index(i["owner_list"][0]["owner_type"])+1
            i["first_owner_id_type"] = ["居民身份证","军官证","营业执照","护照","企业法人营业执照","组织机构代码证书","事业单位法人证书","社团法人证书","其他有效证件"].index(i["owner_list"][0]["owner_id_type"])+1
            i["first_owner_code"] = i["owner_list"][0]["owner_code"]
            i["first_owner_province"] = i["owner_list"][0]["owner_province"]
            i["first_owner_city"] = i["owner_list"][0]["owner_city"]

            copy_data_js_0 = copy.deepcopy(data_js_0)

            # print(i)
            copy_data_js_0 = copy_data_js_0.format(**i)

            copy_data_js_0 = copy_data_js_0.replace("{{","{").replace("}}","}")
            
            res_dict = {}
            res_dict["file_name"] = i["full_name"]
            res_dict["js_str"] = owner_js+copy_data_js_0
            data_js_str_list.append(res_dict)

    return True,data_js_str_list

# auto_obj(login_js,data_js).task_1()

# read_from_execl/read_from_api > make_data_js_from_dict > auto_obj

# username = "shengchanzhuguan"
# password = "adc6847f56510b6310750cf53cc07fe1"
# # api_base_url = "http://192.168.18.142:8000"
# api_base_url = "http://62.234.87.47:8001"

# payload = {'username': username, 'password': password}
# login_url = api_base_url+"/auth/login/"
# cookies = requests.post(login_url, data=payload)
# print(cookies.cookies)

status,data_js_list = make_data_js_from_dict(read_from_api())


for i in data_js_list:
    auto_obj(login_js,[i["js_str"]],i["file_name"]).task_1()





