import config
import requests
from time import sleep
from boot import connection
from machine import Pin, ADC

ACTIVE = Pin("LED", Pin.OUT)
WARN = Pin(15, Pin.OUT)
TEMP = ADC(26)
URL = f"http://{config.SERVER}:{config.PORT}{config.ENDPOINT}"


def active(duration=0.1):
    """Indicate activity"""
    ACTIVE.on()
    sleep(duration)
    ACTIVE.off()


def warn(on=True):
    """Indicate warning"""
    if on:
        WARN.on()
    else:
        WARN.off()


def temperature():
    """Read temperature"""
    prop = 3.3 / 65535

    v_out = TEMP.read_u16() * prop

    temp = (100 * v_out) - 50

    return temp


while connection.isconnected():
    # read temperature
    value = temperature()

    data = {"value": value}

    # flash internal LED indicating sending a temperature
    active()

    # send temperature to server and read response
    response = requests.post(URL, json=data)

    message = response.json()

    print("Message received", message)

    # set or unset warning LED if server tells us to do so
    warn(message["warn"])

    # sleep a little until next temperature reading
    sleep(config.INTERVAL)
