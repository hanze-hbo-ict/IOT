# Sensoren

Sensoren komen in allerlei soorten en maten, bekend zijn beweging-, licht- en temperatuursensoren. De Pico heeft een ingebouwde temperatuursensor waarmee je de temperatuur van de chip kan uitlezen en in dit onderdeel ga je daar eerst een programma voor schrijven.

Als tweede stap ga je het ontwerp uitbreiden met een extra temperatuursensor om de temperatuur van de buitenlucht te meten.

## Temperatuur meten

Het is een vereenvoudiging van de werkelijkheid maar een temperatuursensor zou je als een weerstand kunnen zien. Er gaat stroom in en op basis van de temperatuur zal het een weerstand geven, en die weerstand (en daarmee het stroomverlies) kan dan worden gerelateerd aan een aantal graden Celsius.

De Pico zal op een interne pin analoge *input* ontvangen van de temperatuursensor, en je zal deze *analoge* waarde moeten converteren naar een *digitale* representatie die je uiteindelijk kan gebruiken voor het bepalen van de temperatuur in graden Celsius.

Laten we dit stap voor stap doen, het is aan te raden om dit met MicroPython REPL uit te voeren. Later kan je deze stappen in jouw code overnemen.

### Analoog naar digitaal

Je zal hier de klasse [`ADC`](https://docs.micropython.org/en/latest/library/machine.ADC.html) uit de module `machine` voor de analoog naar digitale conversie voor gaan gebruiken.

```python
from machine import ADC
```

Vervolgens heb je een instantie van de klasse `ADC` nodig en noem deze bijvoorbeeld `sensor`. Je ziet dat pin 4 wordt gebruikt, het interne pin nummer van de temperatuursensor.

```python
sensor = ADC(4)
```

De klasse `ADC` heeft een methode [`read_u16`](https://docs.micropython.org/en/latest/library/machine.ADC.html#machine.ADC.read_u16) en deze zal een 16-bit waarde teruggeven op basis van de analoge input die het van de pin (sensor) ontvangt.

```{attention}
De nieuwere methode `ADC.read_u16` biedt een meer uniforme benadering voor het uitvoeren van analoge lezingen waarbij een waarde tussen 0 en 65535 wordt teruggegeven. MicroPython beveelt deze nieuwe methode aan in plaats van de methode `ADC.read` die je in veel tutorials nog gebruikt ziet worden.
```

De vraag is nu waar deze 16-bit waarde voor staat, het kan tussen de 0 en 65535 liggen. Het geeft een verhouding aan tot iets, maar tot wat? Dit is het zogenaamde *reference voltage* en dat is 3,3V.
In de [datasheet](https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf) zal je dit onder het kopje "Temperature Sensor" kunnen vinden (en ook dat pin 4 moet worden gebruikt!).

Definieer nu dit verhoudingsgetal en vermenigvuldig het met de 16-bit waarde en bewaar het resultaat.

```python
prop = 3.3 / 65535

v_out = adc.read_u16() * prop
```

Het resultaat `v_out` is een waarde in millivolt en de vraag is nu hoe dit voltage kan worden omgezet naar een temperatuur. In de documentatie kan je vervolgens het volgende lezen:

> The temperature sensor measures the Vbe voltage of a biased bipolar diode, connected to the fifth ADC channel (AINSEL=4). Typically, Vbe = 0.706V at 27 degrees C, with a slope of -1.721mV per degree. Therefore the temperature can be approximated as follows:
>
> T = 27 - (ADC_voltage - 0.706)/0.001721

De bepaling van de temperatuur is nu eenvoudig, wat volgt is de allerlaatste stap waar `temp` de waarde in graden Celsius zal zijn.

```python
temp = 27 - (v_out - 0.706) / 0.001721

print(temp)
```

Je hebt nu een sensor kunnen gebruiken en uitlezen. In de volgende stap ga je een extra temperatuursensor aansluiten om de temperatuur van de buitenlucht te kunnen meten.

## Voorbereiding

In tegenstelling tot een LED die aangesloten werd op een GPIO-pin (die aan- en uit kon worden gezet) is een continue stroomtoevoer voor een sensor een betere keus. Op het bord zie je een **3V3** pin die deze stroomtoevoer biedt (zie ook figuur {numref}`pico-devkit` voor meer detail).

```{figure} ../circuits/pico_w_step_6.png
:name: 3v3-connect-wire

3V3 kabel aansluiten
```

Sluit deze pin nu aan op het bord, zie {numref}`3v3-connect-wire`.

## Temperatuursensor

```{figure} ../images/tmp36.png
:name: tmp36-sensor

tmp36 temperatuursensor
```

De temperatuursensor heeft 3 aansluitingen, als je de kant met het label voor je houdt is **links** is de input (stroom in $+$), **midden** is *analoge output* en **rechts** is aarding (stroom uit $-$).

```{attention}
Let goed op hoe je de sensor plaatst en waar je de stroom- en aarding op gaat aansluiten, keer je deze aansluitingen om dan zal de sensor gaan opwarmen!
```

```{figure} ../circuits/pico_w_step_7.png
:name: tmp36-in-out

temp36 in- en output
```

Plaats de sensor op het bord en sluit de in- en output aan, zie figuur {numref}`tmp36-in-out`.


```{figure} ../circuits/pico_w_step_8.png
:name: tmp36-analog-out

temp36 analoge output
```

Voor de middelste aansluiting, de analoge output, zal ook net als bij de LED weer een keus moeten worden gemaakt welke pin te gebruiken. Omdat we een analoge output van de sensor willen lezen en deze naar een digitale waarde gaan omzetten gebruiken we pin 26 (GP26), en je ziet in {numref}`pinout-diagram` dat deze ook een tweede functie heeft als een ADC (ADC0, analoog naar digitale conversie). Sluit deze nu aan en verbindt het met de middelste aansluiting van de sensor, zie {numref}`tmp36-analog-out`.

## Nogmaals meten

De sensor is nu aangesloten maar als je de vorige code gaat gebruiken zal je bijzondere waarden gaan vinden. De tmp36 is een heel andere sensor dan die van de Pico en relatie voltage en temperatuur zal anders worden bepaald. Ook hier zal documentatie moeten worden geraadpleegd en in de [documentatie](https://www.analog.com/media/en/technical-documentation/data-sheets/TMP35_36_37.pdf) zal je een grafiek kunnen vinden die deze relatie duidelijk maat, zie  {numref}`tmp36-voltage-temp`.

```{figure} ../images/tmp36_output_temperature.png
:name: tmp36-voltage-temp

Relatie output voltage en temperatuur
```

Let hier in het bijzonder op lijn *b* die het gedrag van de tmp36 weergeeft. We zien daar het volgende:

- Bij **0,75V** is de temperatuur **25°C**.
- Bij **1,00V** is de temperatuur **50°C**.

Omdat er een **rechtlijnig verband** is tussen spanning en temperatuur, kunnen we de volgende eenvoudige formule gebruiken:

$$
T = (100 \times V_{out}) - 50
$$

De code die je eerder hebt geschreven voor het uitlezen van de interne sensor heeft nu nog *twee* kleine aanpassing nodig:

```python
from machine import ADC

sensor = ADC(26)  # gewijzigde pin
prop = 3.3 / 65535

v_out = adc.read_u16() * prop

temp = (100 * v_out) - 50  # gewijzigde berekening

print(temp)
```

Probeer dit nu uit in de MicroPython REPL om te controleren of alles juist is aangesloten en de temperatuur te meten.

Je hebt nu succesvol LED's kunnen aansturen en een temperatuursensor kunnen uitlezen! Deze handelingen gaan in het volgende deel samenkomen in een klein project waar de microcontroller temperatuurmetingen over een netwerk gaat versturen en zal moeten reageren op berichten.
