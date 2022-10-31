from socketlib2 import SocketUDP
from time import time

CLIENT_IP = "127.0.0.1"
CLIENT_PORT = 5407
MAX_ITERS = 10000
BUF_SIZE = 1024
TIMEOUT = None

PROXY_IP = "127.0.0.1"
PROXY_PORT = 5406

if __name__ == "__main__":
    client = SocketUDP(CLIENT_IP, CLIENT_PORT, BUF_SIZE, TIMEOUT)
    
    i = 0
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
        
        data = data.decode()
        print(f"[Client] | Receive : {data} | Spend time : {spend_time:5.3f} ms |")
        
        if data == f"World {MAX_ITERS}": break

    client.close()

    e = time()
    tt = round(e - s, 3)
    print("Spend time", tt, "secs")

