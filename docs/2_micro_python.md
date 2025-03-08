# MicroPython

## Connectiviteit

Net als met Python op jouw systeem kan je MicroPython op twee manieren gebruiken:

-   code in een bestand uitvoeren
-   interactief code uitvoeren

Bij de eerste manier schrijf je de code voor jouw programma in een bestand en laat je het vervolgens uitvoeren. Dit is wat je straks gaat doen om bijvoorbeeld een LED te bedienen of een sensor op het bord uit te lezen.

De tweede manier is wat je kent van bijvoorbeeld IPython, een interactieve Python prompt (REPL) en daar ga je nu eerst kennis mee maken.

### Seriële connectie

De micro USB aansluiting met het bord is een seriële connectie en deze is *bidirectioneel*, er kunnen zowel gegevens mee worden verstuurd als mee worden ontvangen. In het verleden werden seriële connecties gebruikt om bijvoorbeeld een muis of modem aan te sluiten, maar ook een beeldscherm (of *terminal*). Een beeldscherm kan natuurlijk niet op het bord worden aangesloten, maar kan wél met software worden nagebootst (*geëmuleerd*).

```{important}
Onder Linux zal je jezelf misschien moeten toevoegen aan de groep `dialout` om gebruik te kunnen maken van de seriële poort.
```

### Terminal

Het is tijd om Thonny op te starten nu je de microcontroller hebt aangesloten.


```{figure} ../images/thonny_1.png
:name: thonny-terminal

Thonny editor en terminal
```

Rechtsonder zal je zien dat Thonny is verbonden met de microcontroller en je zal ook een *shell* geopend zien waar je een interactieve Python prompt ziet (`>>>`). Probeer dit nu uit door de volgende Python code te typen om de wereld te begroeten!

```console
>>> print("Hello world!")
Hello world!
```

## MicroPython

Zoals eerder is gezegd, MicroPython heeft een aantal modulen die heel specifiek zijn voor een microcontroller als de Pico, onder andere voor het kunnen gebruiken van de pins. Twee van deze pins zijn *intern* aangesloten, dat wil zeggen dat je ze niet een fysieke pin hebben op het bord.

De microcontroller heeft hier een interne LED op aangesloten maar ook een temperatuursensor (waar we later mee gaan kennismaken). Als je goed op het bord kijkt dan zal je daar een ingebouwde LED kunnen ontdekken (naast de USB-aansluiting, zie {numref}`pico-devkit`)

```{figure} ../circuits/pico_w.png
:name: pico-devkit

Raspberry Pico W
```

Standaard staat deze ingebouwde LED uit, in de volgende stap ga je deze LED aan- en uitzetten.

### De module `machine`

De MicroPython module [`machine`](https://docs.micropython.org/en/v1.9.3/wipy/library/machine.html) bevat functies en klassen voor toegang tot de hardware, onder andere de klasse [`Pin`](https://docs.micropython.org/en/v1.9.3/wipy/library/machine.Pin.html) die alles te maken heeft met het kunnen gebruiken van de pins op het bord.

Alle pins zijn genummerd, over wát de verschillende pins zijn (per nummer) en wat ze precies kunnen volgt later meer.

Importeer nu de klasse `Pin` uit de module `machine`:

```text
>>> from machine import Pin
```

en maak als volgt een nieuwe instantie aan van deze klasse die je `led` noemt:

```text
>>> led = Pin("LED", Pin.OUT)
```

De pin waar de interne LED op is aangesloten kan je eenvoudig benaderen onder de naam "LED", en dit is het eerste argument dat je hier ziet. Het tweede argument betreft de *modus* van de pin, in dit geval `Pin.OUT` waarmee de pin wordt geconfigureerd voor output (stroom uit). Je kan je voorstellen dat `Pin.IN` wordt gebruikt voor invoer (stroom in), bijvoorbeeld als op een pin een sensor wordt aangesloten.

Zet nu als volgt de ingebouwde LED aan

```text
>>> led.on()
```

en vervolgens weer uit:

```text
>>> led.off()
```

Gefeliciteerd, je hebt jouw eerste handeling op de Pico uitgevoerd! Maar je kan je voorstellen dat je dit niet steeds handmatig wilt gaan herhalen, en het is nu tijd om een eerste programma te schrijven, dit op de Pico te plaatsen en vervolgens te laten uitvoeren.

```{tip}
In plaats van de methoden `on` en `off` zou je hier ook de methode `toggle` kunnen gebruiken. Ongeacht de staat van de LED (aan of uit) zal deze methode voor jou de LED omzetten naar de tegenovergestelde staat.
```

### Bestanden

MicroPython heeft een klein bestandssysteem waar je jouw bestanden op kan plaatsen. Open met Thonny nu een bestand en het zal je vragen *waar* je dit wilt doen, op jouw computer of op de Pico, zie {numref}`thonny-location`.

```{figure} ../images/thonny_2.png
:name: thonny-location

Lokaal of op Pico openen
```

Kies voor het openen op de Pico en je zal dan een of twee van de volgende bestandsnamen zien:

-   `boot.py`

    Als dit bestand aanwezig is dan zal het altijd als eerste worden uitgevoerd bij het opstarten van de microcontroller. Dit is een goede plek om code uit te laten voeren die *altijd* nodig is, bijvoorbeeld voor het configureren van een draadloze netwerkverbinding.

-   `main.py`

    Als dit bestand aanwezig is dan zal het worden uitgevoerd *nadat* `boot.py` is uitgevoerd. Dit is de plek waar jij jouw programma zal gaan schrijven.

Deze bestanden zijn al dan niet aanwezig, en zullen door jou moeten worden toegevoegd of aangepast! Als je nieuwsgierig bent naar de inhoud van deze bestanden kan je ze natuurlijk openen maar zullen nog niet veel bevatten.

Het wordt jouw taak om deze bestanden te gaan bewerken en dat ga je eerst op *jouw computer* doen om ze later over te zetten op de microcontroller.

### Een project

Het is nu tijd om een projectomgeving op te zetten, een directory (of *Map*) op jouw computer waar je Python code gaat schrijven voor deze workshop. Maak in deze directory een nieuw bestand `main.py` aan en kopieer daar het volgende in:

```python
from time import sleep
from machine import Pin

led = Pin("LED", Pin.OUT)

for _ in range(5):
    led.on()
    sleep(1)
    led.off()
    sleep(1)
```

Voer het uit door op de *run*-knop in Thonny te klikken, dit eenvoudige programma zal de ingebouwde LED op het bord 5 keer laten knipperen.

## Debuggen

Het proces van code schrijven op jouw machine, het overzetten naar het bord en vervolgens laten uitvoeren zal je vaak gaan herhalen. Het is een lastig proces omdat je niet op jouw machine kan testen of het werkt. Probeer daarom vertrouwd te raken met de MicroPython REPL, de interactieve prompt, om fragmenten uit te proberen die je later in jouw code kan opnemen.

Gebruik de seriële connectie (terminal) ook om foutmeldingen te laten tonen, bij het opnieuw opstarten of resetten van het bord zullen deze berichten zichtbaar worden. Het is om deze reden ook een goed idee om eventueel print statements in jouw code op te nemen, deze zullen ook zichtbaar zijn.
