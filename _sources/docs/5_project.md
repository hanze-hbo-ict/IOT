# Project

In dit deel ga je de microcontroller met aangesloten *actuatoren* (led's) en *sensor* (temperatuurmeter) gebruiken waar de microcntroller een temperatuur gaat versturen over een netwerk.

De ESP32 heeft ingebouwde Wifi connectiviteit en deze zal je later configureren, eerst ga je in meer detail kijken naar het probleem en de verschillende onderdelen van het systeem dat je zal moeten gaan uitwerken.

## Architectuur

Het beschrijven van een softwareoplossing kan op vele manieren, wij gebruiken hier het [C4 model](https://c4model.com/) als hulpmiddel om het te visualiseren en waar we in een drietal stappen met steeds meer detail inzoomen op het probleem (en we zo komen tot een beschrijving van een *software architectuur*).

```{tip}
Het [C4 model](https://c4model.com/) model is een eenvoudige en gemakkelijk te leren benadering van software architectuur diagrammen die je ook kan gebruiken in andere projecten. Diagrammen helpen bij communicatie binnen teams, maar ook daar buiten, bijvoorbeeld met een opdrachtgever of andere belanghebbenden. De C4 [Wikipedia pagina](https://en.wikipedia.org/wiki/C4_model) geeft een bekopt overzicht van dit model.
```

### Context

Met context wordt het grotere beeld van het systeem bedoeld en in het bijzonder de relatie met gebruikers en andere systemen, zie figuur {numref}`c4-iot-context`.

```{figure} ../diagrams/c4_iot_context.svg
:name: c4-iot-context

Systeem context diagram
```

De context van het probleem is niet complex, in dit geval heb je te maken met een enkele gebruiker (jij!) en ben je ook niet afhankelijk van andere systemen, bijvoorbeeld cloud- of andere diensten.

De opdracht van het systeem is ook beperkt, namelijk het lezen van een temperatuur en een visuele waarschuwing geven als de temperatuur boven een bepaalde waarde komt.

### Container

Een systeem valt uiteen in onderling verbonden *containers*, waar een container bijvoorbeeld een toepassing of gegevensopslag vertegenwoordigt.

```{figure} ../diagrams/c4_iot_container.svg
:name: c4-iot-container

Container diagram
```

In figuur {numref}`c4-iot-container` kan je zien dat het probleem uit *twee* afzonderlijke (maar van elkaar afhankelijke) onderdelen bestaat. Ten eerste heb je te maken met een apparaat (de microcontroller) dat temperatuur moet lezen en versturen, en ook zal moeten kunnen reageren op een antwoord.

Ten tweede heb je te maken met een dienst die de metingen kan ontvangen en reageert met een antwoord. Deze dienst zal in de praktijk een andere machine zijn (en meer concreet, jouw machine!).

### Componenten

Containers zijn tot slot te ontleden in onderling samenhangende *componenten*, waar de individuele componenten eventueel weer te relateren zijn aan andere containers of systemen.

In ons geval blijven verdere relaties beperkt en kan het in een enkel diagram worden weergegeven, zoals je in figuur {numref}`c4-iot-component` kan zien.

```{figure} ../diagrams/c4_iot_component.svg
:name: c4-iot-component

Componenten diagram
```

Je ziet hier nu al héél veel detail over de verschillende onderdelen en waar je onder andere al kan afleiden dat

-   het een client/server oplossing is waar gecommuniceerd wordt over HTTP,
-   de client temperatuur als *json* geëncodeerd bericht naar de server stuurt,
-   de client bij elk verstuurd bericht activiteit aangeeft (*blauwe* led)
-   de server een *json* geëncodeerd antwoord teruggeeft,
-   als het antwoord aangeeft dat de temperatuur te hoog is de client een waarschuwing zal moeten tonen (*rode* led).

De componenten worden concreet in de code die je gaat schrijven en dit zal je in de volgende bestanden gaan doen

-   `config.py`

    Dit bestand zal configuratie bevatten, onder andere voor een Wifi verbinding.

-   `boot.py`

    Dit bestand zal de Wifi verbinding van de microcotroller opzetten.

-   `main.py`

    In dit bestand schrijf je de client die temperatuur gaat versturen.

-   `app.py`

    Dit bestand zal de server bevatten die temperatuur van de client gaat ontvangen.

De bestanden `config.py`, `boot.py` en `main.py` zullen op de microcontroller gaan leven, `app.py` blijft op jouw systeem.

## Netwerk

Als je kijkt naar de componenten van *device* (de ESP32 microcontroller) dan zal het je misschien zijn opgevallen dat naast de *client* die nog moet worden geschreven alleen de *connectiviteit* nog ontbreekt (Wifi), want de andere componenten (sensor en led's) heb je in de vorige delen al uitgewerkt.

In deze stap ga je de Wifi van jouw machine als een mobile hotspot configureren en waar de ESP32 vervolgens gebruik van kan gaan maken. Je zal een netwerknaam en wachtwoord gaan opgeven, en noteer deze, je zal het later nodig hebben voor de ESP32 WiFi-configuratie.

Een mobiele hotspot creëert een intern netwerk waar ook jouw machine een [*IP adres*](https://en.wikipedia.org/wiki/IP_address) op krijgt. Volg de instructies voor jouw besturingssysteem voor het aanmaken van een WiFi hotspot en hoe je het adres van jouw machine op dit netwerk kan bepalen, ook deze zal je later nodig hebben.

```{tabbed} Windows
Volg de instructies zoals beschreven op
["Uw pc Windows gebruiken als mobiele hotspot"](https://support.microsoft.com/nl-nl/windows/uw-pc-windows-gebruiken-als-mobiele-hotspot-c89b0fad-72d5-41e8-f7ea-406ad9036b85).

 Bepaal het WiFi IP adres van jouw machine, bijvoorbeeld op de command line met `ipconfig` en noteer het.
```

```{tabbed} macOS
Volg de instructies zoals beschreven op ["De internetverbinding op de Mac delen met andere netwerkgebruikers"](https://support.apple.com/nl-nl/guide/mac-help/mchlp1540/mac).

Bepaal het WiFi IP adres van jouw machine, bijvoorbeeld op de command line met `ifconfig` en noteer het.
```

```{tabbed} Linux
Volg bijvoorbeeld de Ubuntu instructies zoals beschreven op ["Create a wireless hotspot"](https://help.ubuntu.com/stable/ubuntu-help/net-wireless-adhoc.html.en).

Op de meeste Linux distributies zal  NetworkManager geïnstalleerd zijn, met de bijbehorende `nmcli` commmand line applicatie is ook eenvoudig een hotspot aan te maken, zie bijvoorbeeld ["Create Wi-Fi Hotspot on Ubuntu / Debian / Fedora / CentOS / Arch"](https://computingforgeeks.com/create-wi-fi-hotspot-on-ubuntu-debian-fedora-centos-arch/).

Bepaal het WiFi IP adres van jouw machine, bijvoorbeeld op de command line met  `ip a` en noteer het.
```

```{note}
De bovenstaande instructies voor jouw systeem zijn algemeen en verwijzen naar comand line tools die altijd beschikbaar zijn.

Vanzelfsprekend bestaan grafische interfaces, bijvoorbeeld voor het bepalen van het IP adres van jouw systeem, maar wij gaan hier geen uitgebreide beschrijvingen van geven, deze verschillen te veel per besturingssysteem en bovendien ook vaak per versie.

Met andere woorden, leer jouw systeem kennen en gebruik de gereedschappen waar je het meest vertrouwd en gemakkelijk mee bent.
```

Maak nu in jouw project een nieuw bestand `config.py` aan waar je de Wifi hotspot **naam** (of SSID, *Service Set Identifier*), **wachtwoord** en het IP **adres** van jouw machine in definiëert

```python
WIFI_SSID = "<name>"
WIFI_PASSWORD = "<password>"
SERVER = "<address>"
```

Let op, vervang hier `<name>`, `<password>` en `<address>` met jouw waarden!

Plaats dit bestand nu op de microcontroller met `ampy`.

### Connectiviteit

Je eerder gezien dat het bestand `boot.py` altijd eerst door MicroPython wordt uitgevoerd en dit is een geschikte plek om een Wifi verbinding te maken met jouw hotspot.

Open een bestand `boot.py` (als je deze nog niet in jouw project hebt) en neem het volgende over. Plaats het vervolgens met `ampy` op het bord.

```python
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

    print("Connection established")
    print(connection.ifconfig())  # connection details


if __name__ == "__main__":
    connect()

```

Net als jouw machine kan de Wifi interface van de microcontroller op twee manieren worden gebruikt, als Access Point Interface (als een *hotspot*) of als Station Interface (als *gebruiker* van een hotspot). Het laatste is natuurlijk wat je nodig hebt en dit herken je in de `network.STA_IF` parameter die wordt doorgegeven als configuratie-optie voor de Wifi interface van de controller.

````{important}
Je hebt een werkende Wifi verbinding nodig voor wat gaat volgen. Mocht je problemen hebben met het maken van een verbinding bedenk dat je de bovenstaande handelingen ook op de MicroPython REPL kan uitvoeren, bijvoorbeeld

```python
import network

connection = network.WLAN(network.STA_IF)
connection.active(True)
connection.scan()  # list visible networks, should include your hotspot

connection.connect(<wifi ssid>, <wifi password>)
connection.config()  # should list your connection details
```
````

```{tip}
Je ziet hier dat je de gegevens gebruikt die je eerder aan `config.py` hebt toegevoegd, het is zowel een *configuratiebestand* als een Python *module* die je elders kan importeren en gebruiken.

Later zal je een temperatuur over het netwerk gaan versturen, maar hoe vaak? Eén keer per minuut, of per seconde? Jij zal deze beslissing nemen en kan ook heel goed een optie zijn die je aan `config.py` wilt toevoegen om in jouw code te gebruiken. Op deze manier houd je configuratie gescheiden van de logica van jouw applicatie, een goede gewoonte!
```

## Client

De client ga je schrijven in `main.py`, dit wordt het programma dat een temperatuur gaat versturen en zal reageren op een antwoord van een server.

Je hebt in `main.py` al eerder code geschreven, onder andere voor het aansturen van een LED. Kopiëer dit eventeel naar een kladbestand want het bevat misschien fragmenten die je kan hergebruiken.

De basis van de client is als volgt, jouw taak wordt om de verschillende onderdelen in te vullen:

```python
from boot import connection

while connection.isconnected():
    # read temperature

    # send temperature to server

    # flash blue LED indicating temperature was sent

    # read server response

    # set or unset red LED if server tells us to do so

    # sleep a little until next temperature reading
```

In de beschrijving van de architectuur heb je gezien dat berichten worden verstuurd over HTTP en dat voor het formaat JSON wordt gebruikt. We staan kort bij beide stil.

### HTTP

Een *browser* is niet de enige software die HTTP verzoeken kan versturen en ontvangen. Hypertext Transfer Protocol (HTTP) is zoals de naam zegt een *protocol*, een set van afspraken hóe data moet worden verstuurd. Een browser implementeert deze afspraken, maar ook andere software.

Voor MicroPython raden we de module [`urequests`](https://makeblock-micropython-api.readthedocs.io/en/latest/public_library/Third-party-libraries/urequests.html) aan voor het versturen van data over HTTP.

```python
import config
import urequests as requests

url = f"http://{config.SERVER}:{config.PORT}{config.ENDPOINT}"

# POST data
response = requests.post(url, json=data)
# Answer recieved
answer = response.json()
```

Het bovenstaande fragment toont hoe je data met een HTTP POST request kan versturen naar een webadres (url). Je ziet ook dat een server-configuratie (het adres van jouw machine, de poort en endpoint, of route) wordt gebruikt, we staan later bij deze verdere details stil als we server gaan bespreken.

Voor het versturen van data zal je jezelf het volgende moeten afvragen

-   wélke data ga ik versturen
-   en in welk formaat?

### JSON

Je zag in het bovenstaande voorbeeld dat *twee* keer *json* gebruikt wordt, voor het versturen van data én voor het onvangen van een antwoord van de server. HTTP is een tekst gebaseerd protocol en dit betekent dat je niet zomaar een temperatuur (een *float*) kan versturen, het zal eerst moeten worden omgezet naar een *string* representatie.

Voor een enkele waarde is dit eenvoudig, maar wordt lastiger als het meer complex is, bijvoorbeeld in het geval van een *dictionary*. [Javascript Object Notation](https://en.wikipedia.org/wiki/JSON) (JSON) is een formaat voor het *encoderen* van deze complexe structuren naar een string en omgekeerd (*decoderen*).

Hier zie je een voorbeeld hoe deze omzetting werkt

```python
import json

data = {
    "count": 100
}

# encode
encoded = json.dumps(data)
# decode
decoded = json.loads(encoded)

assert data == decoded
```

JSON wordt zo vaak gebruikt dat veel Python modulen het encoderen en decoderen van data al voor jou doen. Bijvoorbeeld, in een eerder voorbeeld zag je het volgende

```python
requests.post(url, json=data)
```

Je ziet hier een `json` *named* parameter waarmee data word doorgegeven,  `urequests` zal hiermee jouw data JSON geencodeerd versturen. Je zult straks zien dat dit voor de server ook het geval is en daarmee jouw werk een stuk eenvoudiger maakt.

Tot zover over HTTP en JSON, de vraag die nog moet worden beantwoord is wát de data is die moet worden verstuurd. Bedenk dat naast de temperatuur je misschien meer informatie wilt versturen, bijvoorbeeld

-   de status van de rode LED (aan of uit)
-   het tijdstip van de meting

Aan jou de keus hoe je dit gaat vormgeven, de server zal er in ieder geval van moeten weten!

## Server

De client is nu klaar. Het enige dat nog nodig is is een server die temeratuurmetingen kan ontvangen en een JSON geencodeerd bericht terugstuurt. Je hebt eerder HTTP servers geschreven met [Flask](https://flask.palletsprojects.com/en/2.0.x/) en dat ga je ook hier gebruiken. Neem het volgende over in een bestand `app.py`

```python
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/temperature", methods=["POST"])
def temperature():
    """An endpoint accepting a temperature reading"""

    data = request.json  # temperature reading

    # if temperature exceeds a certain treshold (e.g. 20 °C),
    # reply with a warning so the client can set the red LED

    # else just reply all is well and maybe signal that
    # the red LED should be switched off


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
```

Een *route* (of *endpoint*) hebben we al voor jou gedefiniëerd en deze zal je verder moeten invullen. Verder zie je een paar details die van belang zijn:

-   **host** is "0.0.0.0", dit betekent dat de server op alle adressen zal gaan luisteren, dus niet alleen naar standaard *localhost* ("127.0.0.1") maar óók naar het adres van jouw machine op de hotspot

-   **port** is 5000 (de standaard poort die Flask gebruikt)

De client heeft dit poortnummer nodig én het endpoint (`/temperature`) om een volledige url op te kunnen bouwen. Voeg deze waarden toe aan `config.py` van de client zodat je deze waarden kan gebruiken (en vergeet niet met `ampy` deze wijziging op de micocontroller te plaatsen!).

### JSON

De client verstuurt JSON geencodeerde data, en Flask kan deze data voor ons decoderen. Je kan zien dat we dit al voor jou hebben ingevuld (`data = request.json`), maar de server zal ook een JSON bericht terug moeten terugsturen.

Net als bij de client zal je hier goed na moeten denken welke data je terug wilt sturen als antwoord voor de client. Op basis van dit antwoord zal de client bijvoorbeeld de rode LED aan moeten zetten (of niet).

Gebruik `jsonify` om een JSON bericht terug te sturen, bijvoorbeeld

```python
data = ...

return jsonify(data)
```

## Testen

Zoals eerder gezegd is het lastig om code op de microcontroller te testen. De communicatie tussen client en server kan je echter eenvoudig testen door ook een kleine lokale client te schrijven die je kan uitvoeren op jouw systeem om te communiceren met de server, bijvoorbeeld om de JSON communicatie te testen.

Een voorbeeld dat je zou kunnen gebruiken is als volgt

```python
import config
import requests

# endpoint url
url = f"http://{config.SERVER}:{config.PORT}{config.ENDPOINT}"

# client data
data = ...

# expected server data
expected = ...

# POST data
response = requests.post(url, json=data)
# Answer recieved
answer = response.json()

# test
assert answer == expected
```

en vul hier bij `...` in welke data je als client verstuurt en het antwoord dat je van de server verwacht.

````{note}
Het enige verschil is dat hier gebruik wordt gemaakt van `requests` in plaats van `urequests`. MicroPython's `urequests` is een implementatie van `requests` met beperkte functionaliteit.

[`requests`](https://docs.python-requests.org/en/latest/) is een veelgebruikte Python HTTP client package die misschien nog niet op jouw systeem aanwezig is, installeer het indien nodig als volgt

```text
pip install requests
```
````

## Tot slot

Start nu de Flask `app.py` server en plaats `main.py` met `ampy` op de microcontroller. Als het goed is zal je zien dat de server berichten ontvangt van de microcontroller.
