import time
start = time.time()
import sys
from multiprocessing import Process, Pool
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

login_js = '''
document.getElementById("loginId").value = "rango";
document.getElementById("password").value = "67C2i4"
login1();'''

data_js = '''alert("hello")'''

class auto_obj(object):
    def __init__(self, login_js, data_js):
        self.login_js = login_js
        self.data_js = data_js

    def task_1(self):
        print("123")
if __name__=='__main__':
    p = Pool(10)
    for i in range(10):
        auto_obj_instance = auto_obj(login_js, data_js) 
        p.apply_async(auto_obj_instance.task_1, args=("name"))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
    print("Time used:",time.time() - start)