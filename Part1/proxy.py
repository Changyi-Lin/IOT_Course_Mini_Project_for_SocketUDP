from socketlib2 import SocketUDP

PROXY_IP = "127.0.0.1"
PROXY_PORT = 5406
MAX_ITERS = 10000
BUF_SIZE = 1024
TIMEOUT = None

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5405

if __name__ == "__main__":
    proxy = SocketUDP(PROXY_IP, PROXY_PORT, BUF_SIZE, TIMEOUT)
    
    while True:
        # receive data from client and show
        data = proxy.receive()
          
        # send data to server
        proxy.send(data, SERVER_IP, SERVER_PORT)

        # break condition
        data = data.decode() 
        if data == f"Hello {MAX_ITERS}": break

    proxy.close()