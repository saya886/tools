import requests
import time
import json

url1 = "http://yun.cheelink.com/wsjc/Device/getDeviceData.do?userID=666888&userPassword=666888"
url2 = "http://data.qz12316.com/farm/api/insertFarmInfo/?"


while True:

    # 格式化字符串

    r1 = requests.get(url1)
    data_obj = json.loads(r1.text)
    time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 

    data_str = "light={0}&humidity={1}&temperature={2}&soilTem={3}&soilWater={4}&co2={5}&ph={6}&accTem={7}&avgTem={8}&lastUpdateTimeStr={9}&area=a1&privatekey=dghshzs".format(data_obj[1]["DevHumiValue"],data_obj[0]["DevHumiValue"],data_obj[0]["DevTempValue"],"0",data_obj[5]["DevHumiValue"],data_obj[2]["DevHumiValue"],data_obj[6]["DevHumiValue"],data_obj[0]["DevTempValue"],data_obj[0]["DevTempValue"],time_str)

    print(data_str)
    r2 = requests.post(url2+data_str)

    print(r2.text)
    time.sleep(60*30)
  