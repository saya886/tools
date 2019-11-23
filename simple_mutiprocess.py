import time
start = time.time()
import sys
from multiprocessing import Process, Pool


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    p = Pool(10)
    for i in range(10):
        p.apply_async(run_proc, args=("name"))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
    print("Time used:",time.time() - start)