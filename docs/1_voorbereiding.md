# Voorbereiding

Voor deze workshop heb je *hardware*, *software*, *firmware* en *documentatie* nodig. De hardware is (onder andere) de microcontroller, de software heeft alles te maken met het voorbereiden en kunnen gebruiken van deze hardware met jouw systeem (jouw machine en ontwikkelomgeving) en de firmware om de microcontroller te kunnen besturen. Documentatie tot slot geeft jou informatie over de microcontroller, bijvoorbeeld over functionaliteit en hoe sensoren of LED's kunnen worden aangesloten.

## Hardware

Je hebt het volgende nodig om deze workshop te kunnen volgen

-   [Raspberry Pico WH](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html#picow-technical-specification) ontwikkelbord
-   5mm LED
-   Eén weerstand (minimaal 220 $\Omega$)
-   [tmp36](https://www.analog.com/en/products/tmp36.html) temperatuursensor
-   Een [breadboard](https://en.wikipedia.org/wiki/Breadboard) (*half-size*)
-   Minimaal 7 draadverbindingen (*jumper wires*)

Al deze onderdelen zal je kunnen vinden in de aanbevolen Hanze IoT workshop [configuratie](https://www.okaphone.com/artikel.xhtml?id=499374).


```{important}
Het kan zijn dat je al een ontwikkelbord hebt, misschien een [ESP32](https://www.espressif.com/en/products/socs/esp32) of een [Arduino](https://www.arduino.cc/). Je kan deze gebruiken voor de workshop, maar houd wel rekening met het volgende:

-   het moet kunnen worden aangesloten op sensoren en bijvoorbeeld LED's
-   het moet kunnen worden geprogrammeerd met Python (een generieke- of bord specifieke versie)

In deze workshop gebruiken we [MicroPython](https://micropython.org/), maar [CircuitPython](https://circuitpython.org/) zou misschien voor jouw bord beter geschikt zijn. In ieder geval, we verwachten dat als je een eigen bord gebruikt dat je weet wat je doet en zullen daar verder geen aanvullende instructies voor geven.
```

## Software

Je zal jouw systeem én de microcontroller eerst moeten voorbereiden voor gebruik en je gaat daar de volgende stappen voor doorlopen:

-   *software* installeren op jouw machine
-   *firmware* plaatsen op de microcontroller

### Ontwikkelomgeving

Je gaat in deze workshop Python code schrijven voor het aansturen van de microcontroller. Later zal je een Python versie op de microcontroller installeren (*firmware*) die speciaal voor dit type processoren geschikt is, [MicroPython](https://en.wikipedia.org/wiki/MicroPython).

Als editor gaan we in deze workshop [Thonny](https://en.wikipedia.org/wiki/Thonny) gebruiken. Thonny noemt zichzelf een *Python IDE for beginners* maar laat je niet verrassen, het biedt bijzonder veel functionaliteit en integreert uitstekend met de Pico!

Download en installeer nu [Thonny](https://thonny.org/) voor jouw systeem, dit zal in de meeste gevallen de *installer* versie zijn.

```{note}
Waarom Thonny en niet bijvoorbeeld [Visual Studio Code](https://code.visualstudio.com/) (VSCode) of [PyCharm](https://www.jetbrains.com/pycharm/)? We willen het in deze workshop eenvoudig houden en Thonny biedt meer dan genoeg functionaliteit om snel en eenvoudig aan de slag te gaan. Bovendien zal je in veel online tutorials ook Thonny gebruikt zien worden.

Dit wil niet zeggen dat je andere editors niet mag gebruiken! VSCode biedt bijvoorbeeld met de [MicroPico](https://marketplace.visualstudio.com/items?itemName=paulober.pico-w-go) extensie prima ondersteuning en PyCharm ook met de [MicroPython Plugin](https://plugins.jetbrains.com/plugin/9777-micropython).
```

## Firmware

Een microcontroller heeft ook software nodig (een besturingssysteem) en dit is MicroPython. MicroPython is een voor microcontrollers geoptimaliseerde versie van Python en bevat een aantal modules die heel specifiek zijn voor microcontrollers, bijvoorbeeld het kunnen gebruiken van de pinnen of WiFi.

MicroPython is *firmware*, dat wil zeggen dat het software is die in de hardware ingeprogrammeerd wordt en de volgende stap is het plaatsen (of *flashen*) van deze firmware op de microcontroller.

### Firmware downloaden

De MicroPython firmware is microcontroller specifiek, download deze nu eerst voor de [Raspberry Pico W](https://micropython.org/download/rp2-pico-w/rp2-pico-w-latest.uf2).

```{attention}
In de Hanze IoT kit is een Raspberry Pico W microcontroller opgenomen met een [RP2040](https://en.wikipedia.org/wiki/RP2040) processor. Inmiddels (sinds november 2024) is een Raspberry Pico W versie 2 uitgebracht met een [RP2350](https://en.wikipedia.org/wiki/RP2350) processor. Functioneel zijn ze gelijk, maar mocht jij toevallig deze versie hebben dan zal je rekening moeten houden met een andere [MicroPython](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html) firmware versie.
```

### Firmware flashen

Je zal nu de MicroPython firmware die je eerder hebt gedownload naar het permanente geheugen van de microcontroller gaan schrijven, oftewel *flashen*. Dit gaat heel eenvoudig:

1. Sluit de USB kabel aan op de microcontroller
2. Houd op de microcontroller de BOOTSEL knop ingedrukt (het kleine witte knopje) en sluit de kabel aan op jouw computer
3. De microcontroller zal nu zichtbaar worden als een extra schijf met de naam RPI-RP2 (het knopje kan je nu loslaten!)
4. Kopieer de firmware die je eerder hebt gedownload naar deze schijf
5. De microcontroller zal herstarten en is nu klaar voor gebruik

:::{figure} ../images/MicroPython.mp4
:name: firmware-install
MicroPython firmware installatie
:::

```{note}
Het aansluiten van de Pico met de BOOTSEL knop ingedrukt is alleen noodzakelijk voor het plaatsen van de firmware, in alle volgende stappen zal dit niet meer nodig zijn.
```

Jouw Pico is nu klaar voor gebruik!

## Documentatie

Tijdens deze workshop zullen we regelmatig verwijzen naar de (technische) documentatie van de microcontroller. Ook als je met een eigen project verder gaat zal je ongetwijfeld dingen moeten gaan opzoeken over de functionaliteit.

De technische documentatie van de microcontroller kan je via deze [link](https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf) vinden, we adviseren je om deze te bookmarken.


