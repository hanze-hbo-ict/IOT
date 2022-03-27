# Sensoren

Sensoren komen in allerlei soorten en maten, bekend zijn beweging-, licht- en temperatuursensoren. In dit onderdeel ga je het ontwerp uitbreiden met een temperatuursensor.

## Voorbereiding

In tegenstelling tot een led die aangesloten werd op een GPIO-pin (die aan- en uit kon worden gezet) is een continue stroomtoevoer voor een sensor een betere keus. Rechtsonder op het bord zie je een **3V3** pin die deze stroomtoevoer biedt (zie ook figuur {numref}`esp32-devkit` voor meer detail).

```{figure} ../circuits/esp32_step_6_bb.png
:name: 3v3-connect

3V3 pin aansluiten
```

Het begint op het breadboard al aardig druk te worden met een led, kabels en een weerstand. De 3V3 pin bevindt zich aan de onderkant van het ravijn, we kiezen er voor om deze pin aan te sluiten op de onderste verticale strip, zie figuur {numref}`3v3-connect`. Je zal hier de ESP32 even van het board moeten halen om de kabel te plaatsen, zorg er voor dat je een gaatje recht boven de 3V3 pin gebruikt zodat pin en kabel verticaal op de strip zijn aangesloten.

## Temperatuursensor plaatsen

```{figure} ../images/tmp36.png
:name: red-led

tmp36 temperatuursensor
```

De tmp36 sensor heeft 3 aansluitingen, als je de kant met het label voor je houdt is **links** is de input (stroom in $+$), **midden** is *analoge output* en **rechts** is aarding (stroom uit $-$).

```{figure} ../circuits/esp32_step_7_bb.png
:name: tmp36-in-out

temp36 in- en output
```

Plaats de tmp36 op het bord en sluit de in- en output aan, zie figuur {numref}`tmp36-in-out`.

```{figure} ../circuits/esp32_step_8_bb.png
:name: tmp36-analog-out

temp36 analoge output
```

Voor de middelste aansluiting, de analoge output, zal ook net als bij de led weer een keus moeten worden gemaakt welke pin te gebruiken. Wij hebben hier gekozen voor GPIO-pin nummer 34, zie figuur {numref}`tmp36-analog-out`.

## Temperatuur

De ESP32 zal op de pin analoge *input* ontvangen van de temperatuursensor, en je zal deze *analoge* waarde moeten converteren naar een *digitale* representatie die je uiteindelijk kan gebruiken voor het bepalen van de temperatuur in graden celsius.

Laten we dit stap voor stap doen, het is aan te raden om dit met MicroPython REPL uit te voeren. Later kan je deze stappen in jouw code overnemen.

### Analoog naar digitaal

Om te beginnen zal je ook hier weer de klasse `Pin` moeten gebruiken én de klasse [`ADC`](https://docs.micropython.org/en/latest/library/machine.ADC.html) uit de module `machine` voor de analoog naar digitale conversie.

```python
from machine import Pin, ADC
```

Vervolgens heb je een instantie van de klasse `Pin` nodig, en noem deze bijzoorbeeld `tmp36`. Let op dat de modus `Pin.IN` is, want je gaat input *lezen*.

```python
tmp36 = Pin(34, Pin.IN)
```

Maak een instantie van de klasse `ADC` aan en noem deze bijvoorbeeld `adc`. De klasse accepteert als argument een `Pin` instantie.

```python
adc = ADC(tmp36)
```

De klasse `ADC` heeft een methode [`read_u16`](https://docs.micropython.org/en/latest/library/machine.ADC.html#machine.ADC.read_u16) en deze zal een 16-bit waarde teruggeven op basis van de analoge input die het van de pin (sensor) ontvangt.

```{attention}
De nieuwere methode `ADC.read_u16` biedt een meer uniforme aanpak voor het uitvoeren van analoge lezingen waarbij een waarde tussen 0 en 65535 wordt teruggegeven. MicroPython beveelt deze nieuwe methode aan in plaats van de methode `ADC.read` die je in veel tutorials nog gebruikt ziet worden.
```

De vraag is nu waar deze waarde voor staat, het kan tussen de 0 en 65535 liggen. Het geeft een verhouding aan tot iets, maar tot wat? Dit blijkt het [*ADC reference voltage*](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/adc.html#adc-calibration) (Vref) te zijn, een gekalibreerd voltage, in het geval van de ESP32 is dit 1100 mV (millivolt).

Definiëer nu dit verhoudingsgetal en vermenigvuldig het met de 16-bit waarde en bewaar het resultaat.

```python
prop = 1100 / 65535

v_out = adc.read_u16() * prop
```

Het resultaat `v_out` is een waarde in millivolt en de vraag is nu hoe dit voltage kan worden omgezet naar een temperatuur. Dit kan worden beantwoord met behulp van de tmp36 technische [documentatie](https://www.analog.com/media/en/technical-documentation/data-sheets/TMP35_36_37.pdf).

```{figure} ../images/tmp36_output_temperature.png
:name: tmp36-voltage-temp

Relatie output voltage en temperatuur
```

In deze documentatie is een grafiek opgenomen die de relatie voltage (in millivolt) ten opzichte van temperatuur in graden celsius aangeeft, zie figuur {numref}`tmp36-voltage-temp`. Let hier in het bijzonder op lijn *b* die het gedrag van de tmp36 weergeeft. Op basis van deze informatie blijkt dat je de onderstaande formule kan toepassen om het voltage om te zetten naar temperatuur:

$$
^oC = (V_{out} - 500) / 10
$$

De bepaling van de temperatuur is nu eenvoudig, wat volgt is de allerlaatste stap waar `temp` de waarde in graden celsius zal zijn.

```python
temp = (v_out - 500) / 10

print(temp)
```

Je hebt nu succesvol led's kunnen aansturen en een temperatuursensor kunnen uitlezen! Deze handelingen gaan in het volgende deel samenkomen in een klein project waar de microcontroller temperatuurmetingen over een netwerk gaat versturen en zal moeten reageren op berichten.
