# MicroPython

## Connectiviteit

Sluit de ESP32 aan op de micro USB poort, je zal een rode LED zien branden. In de vorige stap heb je gezien hoe je de seriële poortnaam op jouw systeem kan bepalen, deze zal je nu ook nodig hebben om te kunnen communiceren met het bord.

Net als met Python op jouw systeem kan je MicroPython op twee manieren gebruiken:

-   code in een bestand uitvoeren
-   interactief code uitvoeren

Bij de eerste manier schrijf je de code voor jouw programma in een bestand en laat je het vervolgens uitvoeren. Dit is wat je straks gaat doen om bijvoorbeeld een LED te bedienen of een sensor op het bord uit te lezen.

De tweede manier is wat je kent van bijvoorbeeld IPython, een interactieve Python prompt (REPL) en daar ga je nu eerst kennis mee maken.

### Seriële connectie

De micro USB aansluiting met het bord is een seriële connectie en deze is *bidirectioneel*, er kunnen zowel gegevens mee worden verstuurd als mee worden ontvangen. In het verleden werden seriële connecties gebruikt om bijvoorbeeld een muis of modem aan te sluiten, maar ook een beeldscherm (of *terminal*). Een beeldscherm kan natuurlijk niet op het bord worden aangesloten, maar kan wél met software worden nagebootst (*geëmuleerd*).

### Terminal

Een bekende terminal-emulator is [PuTTY](https://www.putty.org/) die voor zowel Windows, Linux en macOS beschikbaar is. Download en installeer PuTTY, en als je het opstart zal het je vragen om een configuratie voor de verbinding die je wilt maken, zie figuur {numref}`putty-config`.

```{figure} ../images/putty_config.png
:name: putty-config

PuTTY configuratie
```

Kies voor *Serial* als type connectie en vul bij *Serial line* de poortnaam in (bijvoorbeeld `COM2` onder Windows of `/dev/ttyUSB0` onder Linux). De snelheid (*Speed*) van de verbinding op zet je op 115200. Tip, geef deze configuratie een naam en bewaar het zodat je dit niet elke keer weer moet instellen.

Open nu de connectie en je zal een interactieve Python prompt zien (`>>>`). Probeer dit nu uit door de volgende Python code te typen om de wereld te begroeten!

```console
>>> print("Hello world!")
Hello world!
```

Sluit de sessie nog niet af want je hebt deze nodig voor de volgende stap!

## MicroPython

Zoals eerder is gezegd, MicroPython heeft een aantal modulen die heel specifiek zijn voor een microcontroller als de ESP32, onder andere voor het kunnen gebruiken van de pins. Twee van deze pins zijn *intern* aangesloten, dat wil zeggen dat je ze niet een fysieke pin hebben op het bord.

Met de eerste interne pin heb je al kennisgemaakt, dit is waar de *rode* LED op aangesloten is (en gaat branden zodra je het bord aansluit). Op de tweede interne pin is een *blauwe* LED aangesloten (tegenover de rode led, zie figuur {numref}`esp32-devkit`).

```{figure} ../circuits/esp32.png
:name: esp32-devkit

ESP32 Devkit V1
```

Standaard staat deze blauwe LED uit, in de volgende stap ga je deze LED aan- en uitzetten.

### De module `machine`

De MicroPython module [`machine`](https://docs.micropython.org/en/v1.9.3/wipy/library/machine.html) bevat functies en klassen voor toegang tot de hardware, onder andere de klasse [`Pin`](https://docs.micropython.org/en/v1.9.3/wipy/library/machine.Pin.html) die alles te maken heeft met het kunnen gebruiken van de pins op het bord.

Alle pins zijn genummerd, zoals je ook op de zijkant van het bord kan zien (bijvoorbeeld D32, D33 etc.). Over wát de verschillende pins (kunnen) doen volgt later meer.

Importeer nu de klasse `Pin` uit de module `machine`:

```text
>>> from machine import Pin
```

en maak als volgt een nieuwe instantie aan van deze klasse die je `led` noemt:

```text
>>> led = Pin(2, Pin.OUT)
```

De interne pin waar de blauwe LED op is aangesloten heeft nummer 2, en dit is het eerste argument dat je hier ziet. Het tweede argument betreft de *modus* van de pin, in dit geval `Pin.OUT` waarmee de pin wordt geconfigureerd voor output (stroom uit). Later zal je ook `Pin.IN` gebruiken voor invoer (stroom in), bijvoorbeeld als op een pin een sensor wordt aangesloten.

Zet nu als volgt de blauwe LED aan

```text
>>> led.on()
```

en vervolgens weer uit:

```text
>>> led.off()
```

Gefeliciteerd, je hebt jouw eerste handeling op de ESP32 uitgevoerd! Maar je kan je voorstellen dat je dit niet steeds handmatig wilt gaan herhalen, en het is nu tijd om een eerste programma te schrijven, dit op de ESP32 te plaatsen en vervolgens te laten uitvoeren.

De terminal sessie kan je nu beëindigen (maar laat de ESP32 wel aangesloten), je gaat in de volgende stappen op jouw laptop of computer verder werken.

### `ampy`

MicroPython heeft een klein bestandssysteem waar je jouw bestanden op kan plaatsen. Tijdens de voorbereiding heb je ook de Python package [`adafruit-ampy`](https://pypi.org/project/adafruit-ampy/) geïnstalleerd en deze bevat het programma `ampy` die je zal gaan gebruiken voor bestandsbeheer en een aantal andere eenvoudige taken. Controleer als volgt of `ampy` correct is geïnstalleerd

```text
ampy --help
```

de uitvoer zal vergelijkbaar met het volgende zijn:

```console
Usage: ampy [OPTIONS] COMMAND [ARGS]...

  ampy - Adafruit MicroPython Tool

  Ampy is a tool to control MicroPython boards over a serial connection.
  Using ampy you can manipulate files on the board's internal filesystem and
  even run scripts.

Options:
  -p, --port PORT    Name of serial port for connected board.  Can optionally
                     specify with AMPY_PORT environment variable.  [required]
  -b, --baud BAUD    Baud rate for the serial connection (default 115200).
                     Can optionally specify with AMPY_BAUD environment
                     variable.
  -d, --delay DELAY  Delay in seconds before entering RAW MODE (default 0).
                     Can optionally specify with AMPY_DELAY environment
                     variable.
  --version          Show the version and exit.
  --help             Show this message and exit.

Commands:
  get    Retrieve a file from the board.
  ls     List contents of a directory on the board.
  mkdir  Create a directory on the board.
  put    Put a file or folder and its contents on the board.
  reset  Perform soft reset/reboot of the board.
  rm     Remove a file from the board.
  rmdir  Forcefully remove a folder and all its children from the board.
  run    Run a script and print its output.
```

Met `ampy` kan je een aantal commando's uitvoeren, onder andere voor het tonen (`ls`) en plaatsen (`put`) van bestanden. Je ziet dat je ook hier weer een poortnaam moet opgeven. Voer nu het volgende uit om de bestanden te tonen:

```text
ampy -p <portname> ls
```

Vervang ook hier `<portname>` met de naam van jouw seriële poort. De uitvoer zal *twee* bestandsnamen tonen,

-   `boot.py`

    Als dit bestand aanwezig is dan zal het altijd als eerste worden uitgevoerd bij het opstarten van de microcontroller. Dit is een goede plek om code uit te laten voeren die *altijd* nodig is, bijvoorbeeld voor het configureren van een draadloze netwerkverbinding.

-   `main.py`

    Als dit bestand aanwezig is dan zal het worden uitgevoerd *nadat* `boot.py` is uitgevoerd. Dit is de plek waar jij jouw programma zal gaan schrijven.

Deze twee bestanden zijn dus al aanwezig, maar zullen door jou moeten worden aangepast! Als je nieuwsgierig bent naar de inhoud van deze bestanden kan je ze met het `get` commando naar jouw machine "downloaden", bijvoorbeeld:

```text
ampy -p <portname> get main.py
```

````{tip}
Je zal `ampy` vaak gaan gebruiken, en het kan handig zijn een configuratiebestand aan te maken waar je een aantal opties in kan definiëren, bijvoorbeeld de poortnaam.

Maak in jouw home directory een bestand `.ampy` aan met de volgende inhoud en vervang `<portname>` met de naam van jouw seriële poort:

```text
AMPY_PORT=<portname>
```

De eerstvolgende keer dat je `ampy` gebruikt kan je de poortnaam nu weglaten, bijvoorbeeld:

```text
ampy get main.py
```
````

### Een project

Het is nu tijd om een projectomgeving op te zetten, een directory waar je Python code gaat schrijven voor deze workshop. Maak in deze directory een nieuw bestand `main.py` aan en kopieer daar het volgende in:

```python
from time import sleep
from machine import Pin

led = Pin(2, Pin.OUT)

for _ in range(5):
    led.on()
    sleep(1)
    led.off()
    sleep(1)
```

Dit eenvoudige programma zal de blauwe LED op het bord 5 keer laten knipperen. Plaats dit bestand nu op het bord met het volgende commando:

```python
ampy -p <portname> put main.py
```

Als het bestand is overgezet zal de blauwe LED gaan knipperen, `main.py` is uitgevoerd! Het bord heeft ook twee knoppen, EN en BOOT, zie figuur  {numref}`esp32-devkit`. BOOT zal het bord opnieuw opstarten, en daarmee opnieuw `main.py` uitvoeren.

## Debuggen

Het proces van code schrijven op jouw machine, het overzetten naar het bord en vervolgens laten uitvoeren zal je vaak gaan herhalen. Het is een lastig proces omdat je niet op jouw machine kan testen of het werkt. Probeer daarom vertrouwd te raken met de MicroPyton REPL, de interactieve prompt, om fragmenten uit te proberen die je later in jouw code kan opnemen.

Gebruik de seriële connectie ook om foutmeldingen te laten tonen, bij het opnieuw opstarten of resetten van het bord (de EN knop) zullen deze berichten zichtbaar worden. Het is om deze reden ook een goed idee om eventueel print statements in jouw code op te nemen, deze zullen ook zichtbaar zijn.
