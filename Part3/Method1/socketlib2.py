import socket

class SocketUDP:
    def __init__(self, ip:str, port:int, buf_size:int, time_out=None) -> None:
        self.IP = ip
        self.PORT = port
        self.BUF_SIZE = buf_size

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Socket UDP
        self.socket.bind((self.IP, self.PORT))
        if time_out != None: self.socket.settimeout(time_out) # Set timeout

    def receive(self) -> str:
        try:
            data, _ = self.socket.recvfrom(self.BUF_SIZE)
            return data
        except socket.error:
            return False

    def send(self, data, ip:str, port:int) -> None:
        self.socket.sendto(data, (ip, port))

    def close(self):
        self.socket.close()