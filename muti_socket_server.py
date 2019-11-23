

import socketserver
import socket
import binascii
import time
import threading

# request_list 里面时request_item_obj 的 示例. 里面的都是在线的设备, 如果设备不在列表里面则为离线状态
request_list = []

class request_item_obj():
    # 使用request_item_obj 的时候需要先判断 is_using
    # 示例代码
    
           
    # 如果锁上
    is_using = False
    # 如果超时
    is_timeout = False

    def __init__(self, socket_instance, device_id):
        # socket_instance 是一个sock 对象 使用它来 进行 send 和 recv
        self.socket_instance =socket_instance
        # device_id 是在 设备连接上 服务器后,给服务器发送的 设备凭证, 用于在遍历request_list列表时判断tcp连接是连接的哪一个设备,以及判断设备是否在线
        self.device_id = device_id

    def send_and_recv(self, command):
        # commnd type is bytes
        # 发送单次数据 , 然后客户端必须响应
        
        try:
            # 发送数据 时间
            print("---------------------------")
            data = ""
            self.socket_instance.settimeout(3.0)
            start = time.time()
            self.socket_instance.sendall(command)
            print("send time used:",time.time() - start)
            print("send data is  " + binascii.hexlify(command).decode())

            # 接收数据时间
            start = time.time()
            data = self.socket_instance.recv(1024)
            print("recv time used:",time.time() - start)
            data = binascii.hexlify(data).decode()
            print("recv data is " + data)
            print("---------------------------")

        except ConnectionResetError as e:
            print('ConnectionResetError')
            self.close_socket()
            return False,""
        except BrokenPipeError as e:
            print('BrokenPipeError')
            self.close_socket()
            return False,""
        except socket.timeout as e:
            print('socket.timeout')
            self.close_socket()
            return False,""
        except:
            print('unkonw error')
            self.close_socket()
            return False,""

        return True,data
        
    
    def send_and_recv_list(self, command_list):
        #给予一个命令列表
        #实现是遍历调用 send_and_recv
        #如果一次命令失败 则直接 中断任务 返回失败
    
        #没有锁 执行命令列表 此函数 响应时间在0-5秒之间
        if self.is_using == False:
            # 锁上资源
            self.is_using = True
            # command_list 内为 command_item
            # command_item 的结构如下
            # command_item = {
            #         "command" : "", 命令  bytes
            #         "res" : "",返回结果 str
            #         "status": False 是否执行成功 boolen
            #     }
            for i in command_list:
                status,res = self.send_and_recv(i["command"])
                # command_list中的任务 只要一个执行失败, 则直接中断 然后返回结果
                if status == False:
                    self.close_socket()
                    self.is_using = False
                    return False,command_list
                i["status"] = status
                i["res"] = res

            self.is_using = False
            return True,command_list
        else:
            #有锁 尝试等待
            count = 0
            while True:
                # 最大等待5 秒
                if count > 5:
                    break
                check_status = self.is_using
                if check_status:
                    #执行命令代码
                    self.send_and_recv_list(command_list)
                else:
                    # 等待100毫秒
                    count = count + 1
                    time.sleep(1)
            return False,command_list

    def close_socket(self):
        # 设置完is_timeout, 在MyServer handle 的while 循环中会读取is_timeout, 如果is_timeout == True 则结束socket
        self.is_timeout = True

class MyServer(socketserver.BaseRequestHandler):
    """
    必须继承socketserver.BaseRequestHandler类
    """
    def handle(self):
        """
        必须实现这个方法！
        :return:
        """
        conn = self.request         # request里封装了所有请求的数据
        
        
        try:
            self.socket_instance.settimeout(3.0)
            data = conn.recv(1024).decode()
            print("来自%s的客户端 id 是：%s" % (self.client_address, data))

            # TODO 判断设备是否注册
            is_vaild = True
            if is_vaild:
                request_item_obj_instance = request_item_obj(conn, data)
                request_list.append(request_item_obj_instance)
            else:
                # 设备没有注册 直接return 结束函数,即断开tcp连接
                return

        except socket.timeout as e:
            print('socket.timeout on device first connect server')
            return 
            # request_item_obj_instance.is_timeout = True

        while not request_item_obj_instance.is_timeout:
            try:
                # 维持 while 循环 保持连接
                time.sleep(1)
                print(str(self.client_address[0]) + " looping ------")
                # conn.sendall(b'\x01\x03\x00\x00\x00\x02\xc4\x0b')

            except ConnectionResetError as e:
                print('ConnectionResetError')
                break
            except BrokenPipeError as e:
                print('BrokenPipeError')
                break
            except socket.timeout as e:
                print('socket.timeout')
                break
            except:
                print('unkonw error')
                break

        print("device close connect " + str(self.client_address[0]) + " .....")
        request_list.remove(request_item_obj_instance)

def exec_command(request_list):
    while True:
        print("!!!!!!!")
        time.sleep(2)
        print(request_list)
        if len(request_list) > 0 :
            command_list = []
            command_item = {
                                "command" : b'\x01\x03\x00\x00\x00\x02\xc4\x0b',
                                "res" : "",
                                "status": False
                            }
            command_list.append(command_item)
            request_list[0].send_and_recv_list(command_list)

if __name__ == '__main__':
    # 创建一个多线程TCP服务器
    server = socketserver.ThreadingTCPServer(('0.0.0.0', 9991), MyServer)
    print("启动socketserver服务器！")
    threading.Thread(target=exec_command,args=(request_list,)).start()
    # 启动服务器，服务器将一直保持运行状态
    server.serve_forever()
    print("@@@@@")
    



