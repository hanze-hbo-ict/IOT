import sys
import config
import network
from time import sleep


def connect():
    conn = network.WLAN(network.STA_IF)

    if conn.isconnected():
        print("Already connected")
        return

    conn.active(True)
    conn.connect(config.WIFI_SSID, config.WIFI_PASSWORD)

    retry = 0
    while not conn.isconnected():  # wait until connection is complete
        if retry == 10:  # try 10 times
            sys.exit("Could not establish connection")
        retry += 1

        sleep(1)  # check again in a sec

    print("Connection established")
    print(conn.ifconfig())  # connection details


if __name__ == "__main__":
    connect()
