from docxtpl import DocxTemplate
import csv
import xlrd
import random


data_dict = {
'full_name':'123',
'short_name':'123',
'version':'V1.0',
'finish_time':'2019年1月1日',
'push_time':'123',
'push_addr':'123',

'owner_name':'123',
'owner_type':'123',
'owner_id_type':'123',
'owner_code':'123',
'owner_province':'123',

'hardware_env':'123',
'software_env':'123',
'language':'java',
'row_length':'123',
'main_desc':'123',

'proposer_name':'123',
'proposer_addr':'123',
'proposer_linkman_name':'123',
'proposer_email_addr':'123',
'proposer_tel':'123',
'proposer_area_code':'123',
'proposer_phone':'123'
}


def parse_float_to_str(float_str):

    if float_str == "":
        return " "
    
    date_tuple = xlrd.xldate_as_tuple(float(float_str), 0)

    return str(date_tuple[0]) +"年" + str(date_tuple[1]) + "月" + str(date_tuple[2]) + "日"


def make_docx_from_template(data_dict):
    doc = DocxTemplate('t3.docx') #加载模板文件
    doc.render(data_dict) #填充数据
    doc.save(data_dict["full_name"]+' 申请表.docx') #保存目标文件
    print(data_dict["full_name"] + "   make finish ...")

def read_data_from_csv(begin_index, end_index):
    data = xlrd.open_workbook("编写记录.xlsx")
    table = data.sheets()[0]
    data_list = []
    while(begin_index < end_index):

        data_list.append(table.row_values(begin_index))
        begin_index  = begin_index +1
    return data_list
    
def parse_data(data_list):
    parsed_data = []
    copy_data_dict = {}
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

def render_docx(data_list):
    for i in data_list:
        make_docx_from_template(i)



def main():
    #for i in read_data_from_csv():
    render_docx(parse_data(read_data_from_csv(65,92)))
    # parse_data(read_data_from_csv(87,91))

main()
