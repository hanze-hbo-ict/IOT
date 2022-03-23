# Project

In dit deel ga je de microcontroller met aangesloten *actuatoren* (led's) en *sensor* (temperatuurmeter) gebruiken waar de microcntroller een temperatuur gaat versturen over een netwerk.

De ESP32 heeft ingebouwde Wifi connectiviteit en deze zal je later configureren, eerst ga je in meer detail kijken naar het probleem en de verschillende onderdelen van het systeem die je zal moeten gaan uitwerken.

## Architectuur

Het beschrijven van een software oplossing kan op vele manieren, wij gebruiken hier het [C4 model](https://c4model.com/) als hulpmiddel om het te visualiseren, waar we in een drietal stappen met steeds meer detail inzoomen op de oplossing van het probleem (de *software architectuur*).

```{tip}
Het C4 model is een eenvoudige en gemakkelijk te leren benadering van software architectuur diagrammen en zou je zelf ook kunnen gebruiken in projecten. Diagrammen helpen bij communicatie binnen teams, maar ook daar buiten.

De C4 [Wikipedia pagina](https://en.wikipedia.org/wiki/C4_model) geeft een bekopt overzicht, neem even de tijd om het door te nemen.
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

In figuur {numref}`c4-iot-container` kan je zien dat het probleem uit *twee* afzonderlijke (maar van elkaar afhankelijke) onderdelen bestaat. Ten eerste heb je te maken met het apparaat (ESP32) die temperatuur moet kunnen lezen en versturen, en ook moet kunnen reageren op een antwoord.

Ten tweede heb je te maken met een dienst die de metingen kan ontvangen en eventueel reageert met een antwoord. Deze dienst zal in de praktijk een andere machine zijn (en meer concreet, jouw machine!).

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
-   de client bij elk verstuurd bericht activiteit aangeeft (blauwe led)
-   de server een *json* geëncodeerd antwoord teruggeeft,
-   als het antwoord aangeeft dat de temperatuur te hoog is een waarschuwing moet worden getoond (rode led).

## Netwerk

## Client

## Server
