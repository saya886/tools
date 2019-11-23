
import time
start = time.time()
from multiprocessing import Process, Pool
import os
import datetime
import sys

import comtypes.client

wdFormatPDF = 17



# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

def make_pdf(in_path,out_path):
    print("making " + out_path + " .....")
    in_file = os.path.abspath(in_path)
    out_file = os.path.abspath(out_path)

    word = comtypes.client.CreateObject('Word.Application')
    doc = word.Documents.Open(in_file)
    doc.SaveAs(out_file, FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()
    print(out_path + " finish.....")

if __name__=='__main__':

    in_path = ".\\word"
    # out_path = "C:\\Users\\rango\\Documents\\code\\pdf2word\\pdf\\abc.pdf"
    out_path = ".\\pdf"

    pool_length = len(os.listdir(in_path))
    p = Pool(pool_length)

    for file in os.listdir(in_path):
        file_name = os.path.splitext(file)[0]
        extension_name = os.path.splitext(file)[1]
        if extension_name == '.docx' or extension_name == "doc":
            p.apply_async(make_pdf, args=(in_path+"\\"+file_name+extension_name,out_path+"\\"+file_name+".pdf"))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
    print("Time used:",time.time() - start)