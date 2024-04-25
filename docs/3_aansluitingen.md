# Aansluitingen

Tot nu toe heb je alleen nog maar met een interne pin gewerkt (waar een blauwe LED op is aangesloten), in het volgende ga je de externe pins gebruiken om apparaten op aan te sluiten.

## Sensoren en actuatoren

Wat je op het bord kan aansluiten valt uiteen in twee categoriën, *sensoren* en *actuatoren*. Een sensor (van het Engelse woord *sense*) kan je zien als een zintuig, iets dat waarneemt. Voorbeelden zijn een bewegingssensor of een temperatuursensor, de laatste ga je in deze workshop gebruiken.

Een sensor neemt waar, maar handelt niet, daar is een actuator (van het Engelse woord *act*) voor nodig. Een actuator is met andere woorden een apparaat dat dingen doet of in actie zet. Voorbeelden zijn een elektromotor of andere apparaten waar spanning op wordt gezet zoals een lamp. In dit onderdeel ga je een LED als actuator aansluiten.

## Schakelingen ontwerpen

Als een elektronische schakeling wordt opgebouwd dan is daar normaal gesproken een printplaat voor ontworpen. Op zo'n printplaat hebben alle onderdelen een aangewezen plek waar ze moeten worden gemonteerd.

Het ontwerpen van een printplaat gebeurt alleen als er veel identieke elektronische circuits moeten worden opgebouwd en ook alleen als het zeker is dat het ontwerp correct is.

In deze workshop ga je geen printplaat ontwerpen, maar ga je gebruik maken van een *breadboard* (zie figuur {numref}`breadboard`) voor het flexibel plaatsen van de ESP32 microcontroller en het aansluiten van een sensor en actuator.

```{figure} ../images/breadboard_half.png
:name: breadboard

Een half-size *breadboard*
```

Je ziet op een breadboard veel gaatjes waar pinnen en draden in kunnen worden gestoken, maar aan de buitenkant zie je niet zien hoe de contacten lopen. De contacten worden gevormd door metalen strips die de gaatjes onderling verbinden per rij, in figuur {numref}`breadboard` zie je een aantal van deze strips waar de *richting* van de verbinding van de rijen zijn aangegeven met rode lijnen.

De buitenste gaatjes zijn *horizontaal* met elkaar verbonden en de binnenste gaatjes zijn *verticaal* met elkaar verbonden. Je ziet ook dat de binnenste gaatjes verdeeld zijn over twee vlakken die worden gescheiden door een "ravijn".

### ESP32 plaatsen

```{figure} ../circuits/esp32_step_0_bb.png
:name: esp32-placement

Plaatsing van de ESP32
```

Plaats nu de ESP32 op het breadboard zoals aangegeven in {numref}`esp32-placement`, het zal wat lichte druk nodig hebben om de pins in de gaatjes te laten vallen. Je mag de ESP32 ook anders plaatsen, in ons voorbeeld proberen we zoveel mogelijk ruimte aan de rechterkant van het board over te houden omdat daar een sensor en actuator moeten worden bijgeplaatst. Zorg er in ieder geval voor dat de twee pin-rijen aan verschillende zijden van het ravijn zitten.

### Aarding aansluiten

```{figure} ../circuits/esp32_step_1_bb.png
:name: ground-connect

Aansluiten van aarding
```

Een eerstvolgende stap in het ontwerp is de aarding aanleggen (de $-$ aansluiting) en dit doe je door met een (korte) kabel de pin GND (*ground*) aan te sluiten op het board. In figuur {numref}`ground-connect` zie je dat daar de bovenste rij voor is gekozen, en je ziet dat horizontaal de rij nu verbonden is (de rij gaatjes is met groen aangegeven).

Dit tot zover de eerste voorbereiding, je gaat nu een LED aansluiten op dit circuit.

## Een LED ansluiten

De basis is gereed, nu ga je een LED aansluiten en het circuit verder compleet maken.

```{figure} ../images/red_led.png
:name: red-led

Een LED diode
```

Een LED heeft twee pinnen en als je goed kijkt zie je dat één langer is dan de ander en dit heeft een reden. Op de **lange** kant wordt spanning aangesloten ($+$) en op de **korte** kant de aarding ($-$).

```{figure} ../circuits/esp32_step_2_bb.png
:name: led-connect

Een LED aansluiten
```

Plaats nu een LED op het board, bijvoorbeeld zoals in figuur {numref}`led-connect`. Je ziet in deze figuur nu ook dat verticaal twee rijen groen gemarkeerd zijn om aan te geven dat deze gaatjes met elkaar in verbinding staan.

```{figure} ../circuits/esp32_step_3_bb.png
:name: ground-led

Een LED aansluiten op aarding
```

Een volgende stap is om de LED aan te sluiten op de aarding, verbind met een kabel de horizontale aarding die je eerder hebt aangelegd met de korte kant van de led, zie figuur {numref}`ground-led`.

```{figure} ../circuits/esp32_step_4_bb.png
:name: led-resistor

Een weerstand plaatsen
```

LED's hebben weerstanden nodig om de stroom die er doorheen gaat te beperken zodat ze niet beschadigd raken. Elke LED heeft een stroomsterkte die niet mag worden overschreden en weerstanden hebben de mogelijkheid de stroom te beperken tot onder de maximaal toegestane stroom voor de LED.

Plaats nu een weerstand op het bord zoals aangegeven in figuur {numref}`led-resistor`. Je kunt elke weerstandswaarde tussen 220 Ω en 500 Ω gebruiken, en de LED zal helder oplichten.

```{attention}
Weerstanden hebben kleurcodes die de weerstandswaarde in Ω (Ohm) aangeven. Gebruik bijvoorbeeld [https://resistorcolorcodecalc.com](https://resistorcolorcodecalc.com/) om te bepalen welke weerstand je nodig hebt.

In figuur {numref}`led-resistor` zie je dat de kleurcode rood-rood-bruin wordt gebruikt wat gelijk staat aan 220 Ω.
```

Het circuit is nu bijna compleet, de weerstand zal nog moeten worden aangesloten op een pin van de ESP32 die stroom kan leveren, maar welke pin?

```{figure} ../images/esp32_devkit_v1_pins.png
:name: pinout-diagram

Pinout diagram ESP32
```

De ESP32 biedt heel véél aansluitingsmogelijkheden en sommige pins kunnen ook nog eens verschillende rollen spelen. In het geval van een LED waar je stroom nodig hebt zal je op zoek moeten gaan naar een van de *General Purpose I/O* (GPIO) pins. In figuur {numref}`pinout-diagram` vind je per pin welke mogelijkheid het biedt (<a href="../reference/ESP32-Devkit-Pinout-Rev-12.pdf">klik hier</a> voor een grotere versie).

```{figure} ../circuits/esp32_step_5_bb.png
:name: power-led

Aansluiten op een GPIO pin
```

Als laatste stap sluit je nu de weerstand aan op een GPIO pin, in figuur {numref}`power-led` kan je zien dat wij hebben gekozen voor pin nummer 32.

```{note}
Het kiezen van de juiste pin blijft lastig, naast het pinout diagram dat we hier aanbieden kan het behulpzaam zijn om online gidsen door te nemen waar in verder detail wordt beschreven wat elke pin doet (of kan doen), bijvoorbeeld [Complete guide on ESP32 Pinout reference: what GPIO pins do you use?](https://www.electrorules.com/esp32-pinout-reference/).
```

### MicroPython

Hoe kan je nu controleren of jouw circuit met LED werkt? Wat je in de bovenstande stappen hebt gedaan is precies dezelfde manier hoe de interne pin met de blauwe LED is opgebouwd. Dit betekent dat je in de code die je eerder hebt geschreven maar één waarde hoeft aan te passen, namelijk het pinnummer:

```python
from time import sleep
from machine import Pin

led = Pin(32, Pin.OUT)  # gewijzigd pinnummer

for _ in range(5):
    led.on()
    sleep(1)
    led.off()
    sleep(1)
```

Pas `main.py` met deze wijziging aan en plaats het met `ampy put` op het bord. In plaats van de ingebouwde blauwe LED zal nu jouw zojuist aangesloten LED 5 keer gaan knipperen.

In de volgende stap ga je dit ontwerp uitbreiden met een temperatuursensor.
