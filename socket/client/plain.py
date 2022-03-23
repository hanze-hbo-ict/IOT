import time
import random
import socket


def random_value():
    """Return an integer value

    Returns a random integer between 15 and 30 (inclusive)
    """
    value = random.randint(15, 30)  # could be a temperature reading?
    return value


def main(host, port):
    with socket.socket(
        socket.AF_INET,  # set protocol family to 'Internet' (INET)
        socket.SOCK_STREAM,  # set socket type to 'stream' (i.e. TCP)
    ) as sock:
        sock.connect((host, port))
        print(f"Connected to {sock.getpeername()}")

        for _ in range(10):
            value = random_value()

            print(f"Sending {value}")
            message = str(value).encode()  # int as string, to bytes
            sock.sendall(message)

            data = sock.recv(100)
            response = data.decode()  # from bytes to string
            print("Received", response)

            time.sleep(1)


if __name__ == "__main__":
    main("127.0.0.1", 65432)
