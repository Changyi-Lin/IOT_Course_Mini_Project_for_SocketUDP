from socketlib2 import SocketUDP
from time import time

CLIENT_IP = "127.0.0.1"
CLIENT_PORT = 5407
MAX_ITERS = 10000
BUF_SIZE = 1024
TIMEOUT = 0.15

PROXY_IP = "127.0.0.1"
PROXY_PORT = 5406

if __name__ == "__main__":
    client = SocketUDP(CLIENT_IP, CLIENT_PORT, BUF_SIZE, TIMEOUT)
    
    i = 0
    drop = 0
    s = time()
    while True:
        # Send data to proxy
        i += 1
        msg = f"Hello {i}"
        start = time()
        client.send(msg.encode('utf-8'), CLIENT_IP, PROXY_PORT)

        # Receive data from server and show
        data = client.receive()
        end = time()
        spend_time = round((end - start) * 1000, 3)
        
        if data:
            data = data.decode()
            print(f"[Client] | Receive : {data} | Drop {drop} | Spend time : {spend_time:5.3f} ms |")
        
        else: drop += 1

        if data == f"World {MAX_ITERS}": break

    e = time()
    tt = round(e - s, 3)
    print("Spend time", tt, "secs")

    client.close()