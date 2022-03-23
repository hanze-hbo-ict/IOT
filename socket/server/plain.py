import socket


def main(host, port):
    with socket.socket(
        socket.AF_INET,  # set protocol family to 'Internet' (INET)
        socket.SOCK_STREAM,  # set socket type to 'stream' (i.e. TCP)
    ) as sock:
        sock.bind((host, port))
        sock.listen()

        print(f"Serving on {sock.getsockname()}")

        while True:
            conn, addr = sock.accept()
            print(f"Connection from {addr}")

            with conn:
                while data := conn.recv(100):
                    message = data.decode()
                    print(f"Received {message}")

                    conn.sendall(data)

            print("Closing connection")


if __name__ == "__main__":
    main("127.0.0.1", 65432)
