from threading import Thread
from socketlib2 import SocketUDP
from time import time, sleep
import random
random.seed(time())

PROXY_IP = "127.0.0.1"
PROXY_PORT = 5406
MAX_ITERS = 10000
BUF_SIZE = 1024
TIMEOUT = None

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5405

def isOdd(val:int) -> bool:
    '''
    判斷傳入引數是否為奇數，並回傳布林值。
    '''
    return True if val % 2 else False

def probabilityGenerator(probability:int) -> bool:
    if probability <= 0 or probability > 100: return False

    randVal = random.randint(1, 100) # get a random value
    return True if randVal <= probability else False

def delay_send(data, ms):
    Thread(target=delay_send, args=[data, ms])

class Proxy(SocketUDP):
    def __init__(self, ip: str, port: int, buf_size: int, time_out=None) -> None:
        super().__init__(ip, port, buf_size, time_out)
        self.delay_list = []
        self.delay_i = 0

    def delay_send(self, data, secs):
        self.delay_list.append(Thread(target=self.thread_delay, args=[data, secs]))
        self.delay_list[self.delay_i].start()
        self.delay_i += 1

    def thread_delay(self, data, secs):
        sleep(secs)
        self.send(data, SERVER_IP, SERVER_PORT)


if __name__ == "__main__":
    proxy = Proxy(PROXY_IP, PROXY_PORT, BUF_SIZE, TIMEOUT)
    
    delay_num = 0
    drop_num = 0
    while True:
        # receive data from client and show
        data = proxy.receive()
          
        i = int(data.decode()[6:])
        if isOdd(i): # 判斷是否為奇數
            if probabilityGenerator(5):
                delay_num += 1
                proxy.delay_send(data, 0.1) # Condition : 5% 機率 -> delay 100 ms
                continue
        else:
            if probabilityGenerator(10): 
                drop_num += 1
                continue # Condition : 10% 機率 -> drop packet

        print(f"[Proxy] | Delay : {delay_num} | Drop : {drop_num} |")

        # send data to server
        proxy.send(data, SERVER_IP, SERVER_PORT)

        # break condition
        data = data.decode()
        if data == f"Hello {MAX_ITERS}": break

    for thread in proxy.delay_list:
        thread.join()
        
    proxy.close()