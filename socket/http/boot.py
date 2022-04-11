import sys
import config
import network
from time import sleep

connection = network.WLAN(network.STA_IF)


def connect():

    if connection.isconnected():
        print("Already connected")
        return

    connection.active(True)
    connection.connect(config.WIFI_SSID, config.WIFI_PASSWORD)

    retry = 0
    while not connection.isconnected():  # wait until connection is complete
        if retry == 10:  # try 10 times
            sys.exit("Could not establish connection")
        retry += 1

        sleep(1)  # check again in a sec

    # what's our current connection status?
    if connection.isconnectec():
        print("Connection established")
        print(connection.ifconfig())  # connection details
    else:
        print("Could not establish connection, check your settings")


if __name__ == "__main__":
    connect()
