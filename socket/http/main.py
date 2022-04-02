import config
from time import sleep
from machine import Pin, ADC
import urequests as requests

ACTIVE = Pin(2, Pin.OUT)
WARN = Pin(32, Pin.OUT)
TEMP = ADC(Pin(34, Pin.IN))
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
    prop = 1100 / 65535

    v_out = TEMP.read_u16() * prop

    temp = (v_out - 500) / 10

    return temp


while True:
    # read temperature
    value = temperature()

    data = {"value": value}

    # flash blue LED indicating sending a temperature
    active()

    # send temperature to server and read response
    response = requests.post(URL, json=data)

    message = response.json()

    print("Message received", message)

    # set or unset red LED if server tells us to do so
    warn(message["warn"])

    # sleep a little until next temperature reading
    sleep(config.INTERVAL)
