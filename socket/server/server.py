from socketserver import TCPServer, BaseRequestHandler


class EchoHandler(BaseRequestHandler):
    def handle(self):
        print("Connection from", self.client_address)

        while message := self.request.recv(100):
            print(f"Received {message}")

            self.request.sendall(message)

        print("Closing connection")


def main(host, port):
    with TCPServer((host, port), EchoHandler) as server:
        print(f"Serving on {server.socket.getsockname()}")
        server.serve_forever()


if __name__ == "__main__":
    main("127.0.0.1", 65432)
