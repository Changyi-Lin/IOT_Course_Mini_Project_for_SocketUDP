from socketlib2 import SocketUDP

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5405
MAX_ITERS = 10000
BUF_SIZE = 1024
TIMEOUT = 0.001

CLIENT_IP = "127.0.0.1"
CLIENT_PORT = 5407

if __name__ == "__main__":
    server = SocketUDP(SERVER_IP, SERVER_PORT, BUF_SIZE, TIMEOUT)
    
    last_i = 0
    while True:
        # receive data from proxy and show
        data = server.receive()

        if data:
            data = data.decode()
            i = int(data[6:])
            if i > last_i:
                print(f"[Server] | Receive : {data} |")
                msg = f"World {i}"
                last_i = i

            else: continue

        else: msg = "Loss"

        # send data to client        
        server.send(msg.encode('utf-8'), CLIENT_IP, CLIENT_PORT)
        
        # break condition
        if msg == f"World {MAX_ITERS}": break

    server.close()