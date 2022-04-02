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

    while not conn.isconnected():  # wait until connection is complete
        sleep(0.1)  # check again in 100 milliseconds

    print("Connection established")
    print(conn.ifconfig())  # connection details


if __name__ == "__main__":
    connect()
