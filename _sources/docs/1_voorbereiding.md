# Voorbereiding

Voor deze workshop heb je zowel *hardware*, *software* als *firmware* nodig. De hardware is (onder andere) de ESP32 microcontroller, de software heeft alles te maken met het voorbereiden en kunnen gebruiken van deze hardware met jouw systeem (jouw machine en ontwikkelomgeving) en de firmware om de microcontroller te kunnen besturen.

## Hardware

Je hebt het volgende nodig om deze workshop te kunnen volgen

-   [ESP32](https://www.espressif.com/en/products/socs/esp32) ontwikkelbord (30 pins)
-   5mm LED
-   Eén weerstand (minimaal 220 $\Omega$)
-   [tmp36](https://www.analog.com/en/products/tmp36.html) temperatursensor
-   Een [breadboard](https://en.wikipedia.org/wiki/Breadboard) (*half-size*)
-   Minimaal 6 draadverbindingen (*jumper wires*)

Al deze onderdelen zal je kunnen vinden in de aanbevolen Hanze IoT workshop [configuratie](https://www.okaphone.com/artikel.asp?id=493625).


```{important}
Het kan zijn dat je al een onwikkelbord hebt, misschien een eerdere versie van de ESP32 (bijvoorbeeld een [ESP8266](https://en.wikipedia.org/wiki/ESP8266)) of misschien een [Arduino](https://www.arduino.cc/)- of [Rasberry](https://www.raspberrypi.com/). Je kan deze gebruiken voor de workshop, maar houd wel rekening met het volgende:

-   het moet kunnen worden aangesloten op sensoren en bijvoorbeeld LED's
-   het moet kunnen worden geprogrammeerd met Python (een generieke- of bord specifieke versie)

In deze workshop gebruiken we [MicroPython](https://micropython.org/), maar [CircuitPython](https://circuitpython.org/) zou misschien voor jouw bord beter geschikt zijn. In ieder geval, we verwachten dat als je een eigen bord gebruikt dat je weet wat je doet en zullen daar verder geen aanvullende instructies voor geven.
```

## Software

Je zal jouw systeem én de microcontroller eerst moeten voorbereiden voor gebruik en je gaat daar de volgende stappen voor doorlopen

-   *Software* installeren op jouw machine
-   *Firmware* plaatsen op de ESP32

```{note}
Houd er rekening mee dat je deze stappen en alles wat verder gaat volgen met een *command line* gaat uitvoeren. Een editor als [Visual Studio Code](https://code.visualstudio.com/) (VSCode) is voor deze workshop geschikt omdat je én Python code gaat schrijven en met de ingebouwde terminal met de microcontroller gaat communiceren.
```

### Ontwikkelomgeving

Je gaat in deze workshop Python code schrijven voor het aansturen van de microcontroller. Later zal je een Python versie op de microcontroller installeren die speciaal voor dit type processoren geschikt is, [MicroPyhon](https://micropython.org/).

MicroPython is een voor microcontrollers geoptimaliseerde versie van Python en bevat een aantal modules die heel specifiek zijn voor microcontrollers, bijvoorbeeld het kunnen gebruiken van de pinnen of WiFi. Deze zijn *niet* op jouw systeem geïnstalleerd, editors als VSCode zullen je daarom voor deze specifieke MicroPython modules geen *contextuele* hulp kunnen bieden (bijvoorbeeld functies aanvullen) want ze kennen alleen maar modules in jouw geïnstalleerde (standaard) Python versie.

Installeer met het volgende een aparte Python package om jouw editor wél kennis te laten hebben van MicroPython specfieke modules:

```text
pip install huas-micropython[all]
```

Dit zal tegelijkertijd voor jou *twee* andere packages installeren, [`adafruit-ampy`](https://pypi.org/project/adafruit-ampy/) en [`esptool`](https://pypi.org/project/esptool/). De *eerste* heb je nodig voor het kunnen overzetten van de code die je gaat schrijven naar de microcontroller, de *tweede* is nodig voor het plaatsen van MicroPython (de *firmware*) op de microntroller en dit is de eerstvolgende stap die je gaat uitvoeren.

````{attention}
Het kan zijn dat je [PyCharm](https://www.jetbrains.com/pycharm/) gebruikt in combinatie met de Micropython [plugin](https://plugins.jetbrains.com/plugin/9777-micropython). Deze plugin installeert dezelfde MicroPyton type informatie als [`huas-micropython`](https://pypi.org/project/huas-micropython/) en verder `adafruit-ampy`, maar niet `esptool`. De laatste zal je zelf moeten installeren met:

```text
pip install esptool
```

Windows gebruikers kunnen mogelijk de waarschuwing krijgen dat *Microsoft Visual c++* aanwezig moet zijn om `esptool` te kunnen installeren. Zie in dit geval [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) voor aanvullende software.
````

Controleer voordat je naar de volgende stap gaat eerst of alles correct is geïnstalleerd. Voor het plaatsen van de *firmware* op de microcontroller zal je straks `esptool.py` op de command line het moeten kunnen uitvoeren, probeer dit nu met

```text
esptool.py -h
```

en als het goed is zal je een uitvoer zien vergelijkbaar met het volgende:

```console
usage: esptool [-h]
               [--chip {auto,esp8266,esp32,esp32s2,esp32s3beta2,esp32s3,esp32c3,esp32c6beta,esp32h2,esp8684}]
               [--port PORT] [--baud BAUD]
               [--before {default_reset,usb_reset,no_reset,no_reset_no_sync}]
               [--after {hard_reset,soft_reset,no_reset,no_reset_stub}]
               [--no-stub] [--trace] [--override-vddsdio [{1.8V,1.9V,OFF}]]
               [--connect-attempts CONNECT_ATTEMPTS]
               {load_ram,dump_mem,read_mem,write_mem,write_flash,run,image_info,make_image,elf2image,read_mac,chip_id,flash_id,read_flash_status,write_flash_status,read_flash,verify_flash,erase_flash,erase_region,merge_bin,version,get_security_info}
               ...

esptool.py v3.2 - ESP8266 ROM Bootloader Utility
...
```

## Firmware

De microcontroller heeft ook software nodig (een besturingssysteem) en dit is MicroPython. MicroPython is *firmware*, dat wil zeggen dat het software is die in hardware ingeprogrammeerd is en de eerste stap is het plaatsen (of *flashen*) van deze firmware op de microcontroller.

### Firmware downloaden

De MicroPython firmware is microcontroller specifiek, op [https://micropython.org/download/esp32/](https://micropython.org/download/esp32/) vind je de versie voor de ESP32 microcontroller. Download de laatste firmware release (*latest*), je zal deze later op het ontwikkelbord gaan plaatsen.

### Seriële communicatie

Sluit het bord aan met de Micro USB kabel, deze aansluiting is zowel voor voeding als *seriële* communicatie. Een eerste test of de communicatie met het ontwikkelbord slaagt is om het aan te sluiten, waarna een *rode led* op het bord zal moeten oplichten.

Voordat je de firmware kan flashen zal je eerst moeten weten op *welke* [seriële poort](https://en.wikipedia.org/wiki/Serial_port) het bord is aangesloten. In het kort volgen nu instructies voor jouw besturingssysteem, meer uitgebreide informatie kan je vinden in de [ESP32 documentie](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/establish-serial-connection.html) over seriële communicatie met de microcontroller.

````{tabbed} Windows
De meest eenvoudige manier om een overzicht van actuele seriële poortnamen op te vragen is om op de command line het volgende uit te voeren:

```text
mode
```

waar de uitvoer vergelijkbaar zal zijn met het volgende

<!-- TODO uitvoer met aangesloten board -->

```console
Status for device COM1:
-----------------------
    Baud:            1200
    Parity:          None
    Data Bits:       7
    Stop Bits:       1
    Timeout:         OFF
    XON/XOFF:        OFF
    CTS handshaking: OFF
    DSR handshaking: OFF
    DSR sensitivity: OFF
    DTR circuit:     ON
    RTS circuit:     ON

...
```

Je zal hier vooral geïnteresseerd in de genummerde `COM`-poorten en het is waarschijnlijk dat het laatst aangesloten seriële apparaat (de ESP32) het hoogste getal heeft, bijvoorbeeld `COM2`. Onthoud of noteer deze waarde, je zal het later nodig hebben voor het *flashen* van de MicroPyton firmware en het plaatsen van jouw programmacode op de microcontroller.

```{important}
Het kan zijn dat een nieuwe `COM`-poort niet zichtbaar is. Dit kan betekenen dat niet de juiste stuurprogramma’s zijn geïnstalleerd, of dat dat Windows deze niet automatisch kan vinden.

Download en installeer in dit geval de [CP210x USB to UART Bridge VCP Drivers](https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers) en probeer het opnieuw.
```

Twijfel je over de poortnaam? Koppel het bord dan los, voer `mode` uit en noteer de huidige namen. Sluit vervolgens het bord weer aan en controleer weer met `mode` welke poortnaam is toegevoegd (dit zal jouw bord zijn).

````

````{tabbed} macOS / Linux
De seriële poortnaam onder Linux of macOS kan je als *pseudo terminal* device vinden in het virtuele filesystem `/dev`. Voer het volgende twee keer uit, eerst *zonder* het bord te hebben aangesloten en vervolgens mét om te zien welke poortnaam is toegevoegd:

**Linux**

```text
ls /dev/tty*
```

**macOS**

```text
ls /dev/cu.*
```

De poortnaam zal voor Linux zichtbaar zijn als bijvoorbeeld `/dev/ttyUSB0`, of voor macOS bijvoorbeeld `/dev/cu.SLAB_USBtoUART7`. Let op, dit zijn *voorbeelden*, de namen kunnen voor jouw systeem verschillen!

```{important}
Onder Linux zal je jezelf moeten toevoegen aan de groep `dialout` om gebruik te kunnen maken van de seriële poort. Als macOS gebruiker zal je misschien ook extra stappen moeten ondernemen als je geen poortnaam ziet, het kan dan zijn dat tóch nog een driver moet worden geïnstalleerd of dat permissies moeten worden gezet om de driver te mogen gebruiken. Lees in dit geval de [ESP32 documentie](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/establish-serial-connection.html) voor meer informatie.
```
````

Let op, mocht je de kabel later op een andere USB-poort aansluiten dan is de kans groot dat seriële poortnaam wijzigt, houd hier rekening mee!

De seriële poortnaam zal je vaak nodig hebben, niet alleen voor het flashen van de MicroPython firmware, maar ook later als je jouw code op het het bord gaat plaatsen!

### Geheugen wissen

De firmware zal naar het permanente geheugen van de microcontroller worden geschreven, maar voordat je dit gaat doet zal je het geheugen eerst moeten wissen. Voer het volgende uit op de command line:

```text
esptool.py --port <name> erase_flash
```

Vervang hier  `<name>` met de seriële poortnaam die je eerder hebt bepaald, bijvoorbeeld `COM2` (Windows) of `/dev/ttyUSB0` (Linux).

### Firmware flashen

Eindelijk het laatste deel! Je zal nu de MicroPython firmware die je eerder hebt gedownload naar het permanente geheugen van de microcontroller gaan schrijven, oftewel *flashen*. Voer het volgende uit op de command line:

```text
esptool.py --port <name> write_flash -z 0x1000 <firmware>
```

Vervang ook hier `<name>` met de seriële poortnaam en `<firmware>` met de bestandsnaam van de firmware die je eerder hebt gedownload (bijvoorbeeld `esp32-20220117-v1.18.bin`).

Jouw ESP32 is nu klaar voor gebruik!
