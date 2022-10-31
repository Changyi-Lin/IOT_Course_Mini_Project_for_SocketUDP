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
    
    i = 1
    drop = 0
    s = time()
    while True:
        # Send data to proxy
        msg = f"Hello {i}"
        start = time()
        client.send(msg.encode('utf-8'), CLIENT_IP, PROXY_PORT)

        # Receive data from server and show
        data = client.receive()
        end = time()
        spend_time = round((end - start) * 1000, 3)
        
        data = data.decode()
        if data != "Loss":
            print(f"[Client] | Receive : {data} | Drop {drop} | Spend time : {spend_time:5.3f} ms |")
            i += 1

        if data == f"World {MAX_ITERS}": break

    e = time()
    tt = round(e - s, 3)
    print("Spend time", tt, "secs")

    client.close()