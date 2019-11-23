data_js_1 = '''
    if (!Array.indexOf) {{
        Array.prototype.indexOf = function (obj) {{
            for (var i = 0; i < this.length; i++) {{
                if (this[i] == obj) {{
                    return i;
                }}
            }}
            return -1;
        }}
    }}

    var td_obj = document.getElementById('personData');
    var table_objs = td_obj.children;
    var hidden_table = table_objs(0);
    var tmp_div = document.createElement("DIV");
    //alert(hidden_table.innerHTML);
    tmp_div.innerHTML = hidden_table.innerHTML;
    
    // 更改dom结构
    
    // 园区 默认值
    tmp_div.getElementsByTagName("select")[4].selectedIndex = 34
    
    // 国籍 默认值
    tmp_div.getElementsByTagName("select")[1].selectedIndex = 1
    // 企业类别 默认值
    tmp_div.getElementsByTagName("select")[5].selectedIndex = 3
    // 是否申请副本 默认值
    tmp_div.getElementsByTagName("select")[6].selectedIndex = 1
    
    
    // 类别
    owner_type_index = ["自然人","","其他组织","其他","","","","","","","","","","","","","","","","","企业法人","机关法人","事业单位法人","社会团体法人"].indexOf("{owner_type}")
    if(owner_type_index == -1){{
        tmp_div.getElementsByTagName("select")[0].selectedIndex = 1
    }}
    else{{
        tmp_div.getElementsByTagName("select")[0].selectedIndex = owner_type_index+1
    }}
    // 证件类型
    // value=1 居民身份证
    // value=2 军官证
    // value=3 营业执照
    // value=4 护照
    // value=5 企业法人营业执照
    // value=6 组织机构代码证书
    // value=7 事业单位法人证书
    // value=8 社团法人证书
    // value=9 其他有效证件
    owner_id_type_index = ["居民身份证","军官证","营业执照","护照","企业法人营业执照","组织机构代码证书","事业单位法人证书","社团法人证书","其他有效证件"].indexOf("{owner_id_type}")
    if(owner_id_type_index == -1){{
        tmp_div.getElementsByTagName("select")[3].selectedIndex = 5
    }}
    else{{
        tmp_div.getElementsByTagName("select")[3].selectedIndex = owner_id_type_index+1
    }}
    
    
    //  省份
    // value=境外 境外 
    // value=北京 北京 
    // value=上海 上海 
    // value=天津 天津 
    // value=内蒙古 内蒙古 
    // value=山西 山西 
    // value=河北 河北 
    // value=辽宁 辽宁 
    // value=吉林 吉林 
    // value=黑龙江 黑龙江 
    // value=江苏 江苏 
    // value=安徽 安徽 
    // value=山东 山东 
    // value=浙江 浙江 
    // value=江西 江西 
    // value=福建 福建 
    // value=湖南 湖南 
    // value=湖北 湖北 
    // value=河南 河南 
    // value=广东 广东 
    // value=海南 海南 
    // value=广西 广西 
    // value=贵州 贵州 
    // value=四川 四川 
    // value=云南 云南 
    // value=陕西 陕西 
    // value=甘肃 甘肃 
    // value=宁夏 宁夏 
    // value=青海 青海 
    // value=新疆 新疆 
    // value=西藏 西藏 
    // value=重庆 重庆 
    // value=香港 香港 
    // value=澳门 澳门 
    // value=台湾 台湾 
    owner_province_index = ["境外","北京","上海","天津","内蒙古","山西","河北","辽宁","吉林","黑龙江","江苏","安徽","山东","浙江","江西","福建","湖南","湖北","河南","广东","海南","广西","贵州","四川","云南","陕西","甘肃","宁夏","青海","新疆","西藏","重庆","香港","澳门","台湾"].indexOf("{owner_province}")
    if(owner_province_index == -1){{
        tmp_div.getElementsByTagName("select")[2].selectedIndex = 2
    }}
    else{{
        tmp_div.getElementsByTagName("select")[2].selectedIndex = owner_province_index+1
    }}
    
    
    // 著作权人名
    tmp_div.getElementsByTagName("textarea")[0].value = "{owner_name}"
    // 城市
    tmp_div.getElementsByTagName("input")[0].value = "{owner_city}"
    // 证件号码
    tmp_div.getElementsByTagName("input")[1].value = "{owner_code}"
    
    // 添加到document里
    td_obj.appendChild(tmp_div);
'''
data_js_0 ='''
var data_list = [
    {{
        "index":"10",
        "desc":"软件全称",
        "value":"{full_name}"
    }},
    {{
        "index":"11",
        "desc":"简称",
        "value":"{short_name}"
    }},
    {{
        "index":"12",
        "desc":"分类号",
        "value":"30200-0000"
    }},
    {{
        "index":"14",
        "desc":"版本号",
        "value":"{version}"
    }},
    {{
        "index":"21",
        "desc":"开发完成日期",
        "value":"{finish_time}"
    }},
    {{
        "index":"24",
        "desc":"首次发表日期",
        "value":"{push_time}"
    }},
    {{
        "index":"25",
        "desc":"发表国家",
        "value":"中国"
    }},
    {{
        "index":"26",
        "desc":"城市",
        "value":"{push_addr}"
    }},
    {{
        "index":"51",
        "desc":"硬件环境",
        "value":"{hardware_env}"
    }},
    {{
        "index":"52",
        "desc":"软件环境",
        "value":"{software_env}"
    }},
    {{
        "index":"53",
        "desc":"编程语言",
        "value":"{language}"
    }},
    {{
        "index":"54",
        "desc":"源程序量",
        "value":"{row_length}"
    }},
    {{
        "index":"55",
        "desc":"主要功能",
        "value":"{main_desc}"
    }},
    {{
        "index":"71",
        "desc":"著作权人单位名称",
        "value":"{first_owner_name}"
    }},
    {{
        "index":"69",
        "desc":"著作权人类别",
        "value":"{first_owner_type}"
    }},
    {{
        "index":"70",
        "desc":"国籍",
        "value":"中国"
    }},
    {{
        "index":"72",
        "desc":"省份",
        "value":"{first_owner_province}"
    }},
    {{
        "index":"73",
        "desc":"城市",
        "value":"{first_owner_city}"
    }},
    {{
        "index":"74",
        "desc":"证件类型",
        "value":"{first_owner_id_type}"
    }},
    {{
        "index":"75",
        "desc":"证件号码",
        "value":"{first_owner_code}"
    }},
    {{
        "index":"77",
        "desc":"企业类别",
        "value":"私营企业"
    }},
    {{
        "index":"76",
        "desc":"其他园区",
        "value":"其他园区"
    }},
    {{
        "index":"83",
        "desc":"单位名称",
        "value":"{proposer_name}"
    }},
    {{
        "index":"84",
        "desc":"详细地址",
        "value":"{proposer_addr}"
    }},
    {{
        "index":"85",
        "desc":"邮政编码",
        "value":"{proposer_area_code}"
    }},
    {{
        "index":"86",
        "desc":"联系人",
        "value":"{proposer_linkman_name}"
    }},
    {{
        "index":"87",
        "desc":"电话号码",
        "value":"{proposer_tel}"
    }},
    {{
        "index":"88",
        "desc":"邮箱",
        "value":"{proposer_email_addr}"
    }},
    {{
        "index":"89",
        "desc":"手机号码",
        "value":"{proposer_phone}"
    }},
    {{
        "index":"92",
        "desc":"委托事项",
        "value":"委托办理软件著作权登记，直至取得证书"
    }},
    {{
        "index":"93",
        "desc":"姓名单位名称",
        "value":"孙钦豪"
    }},
    {{
        "index":"94",
        "desc":"详细地址",
        "value":"上海市浙桥路277号3号楼"
    }},
    {{
        "index":"95",
        "desc":"邮政编码",
        "value":"200000"
    }},
    {{
        "index":"96",
        "desc":"联系人",
        "value":"孙钦豪"
    }},
    {{
        "index":"97",
        "desc":"电话号码",
        "value":"13262247131"
    }},
    {{
        "index":"98",
        "desc":"邮箱",
        "value":"1614056450@qq.com"
    }},
    {{
        "index":"99",
        "desc":"手机号码",
        "value":"13262247131"
    }},
    {{
        "index":"78",
        "desc":"著作权人",
        "value":false,
        "type":"radio"
    }},
    {{
        "index":"79",
        "desc":"代理人",
        "value":true,
        "type":"radio"
    }},
    {{
        "index":"22",
        "desc":"已发表",
        "value":true,
        "type":"radio"
    }},
    {{
        "index":"23",
        "desc":"未发表",
        "value":false,
        "type":"radio"
    }}
]

var person_2 = {{
    "name":"孙钦豪1",
    "addr":"上海市浙桥路277号3号楼",
    "mail":"1614056450@qq.com",
    "phone":"13262247131",
    "id":"412828199506032114"
}}

var form_list = document.forms[0];

// 配置代理人
//data_list[22].value = person_2.name;
//data_list[25].value = person_2.name;
//data_list[26].value = person_2.phone;
//data_list[27].value = person_2.mail;
//data_list[28].value = person_2.phone;

 
auto_task = function(){{
    for(i in data_list){{
        if(data_list[i]["type"] == "radio"){{
            
            form_list[data_list[i]["index"]].checked = data_list[i]["value"];
        }}
        else{{
            form_list[data_list[i]["index"]].value = data_list[i]["value"];
        }}
    }}
}}
auto_task();
saveForm();
'''