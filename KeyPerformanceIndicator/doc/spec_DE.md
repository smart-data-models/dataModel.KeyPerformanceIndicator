<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: KeyPerformanceIndicator  
================================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.KeyPerformanceIndicator/blob/master/KeyPerformanceIndicator/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Ein wichtiger Leistungsindikator (KPI) ist eine Art der Leistungsmessung. KPIs bewerten den Erfolg einer Organisation oder einer bestimmten Aktivität, in der sie tätig ist.**  
Version: 0.2.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.  
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Das Land. Zum Beispiel, Spanien  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: Die Ortschaft, in der sich die Adresse befindet, und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: Die Region, in der sich der Ort befindet, und die auf dem Land liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird.    
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: Die Straßenanschrift  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `aggregatedData[array]`:  Entität(en) und Attribut(e), die durch den KPI aggregiert werden  - `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `area[string]`: Zu organisatorischen Zwecken können zusätzliche geografische Informationen wie Bezirk, Stadtteil oder andere Hinweise hinzugefügt werden, die zur Identifizierung der KPI-Abdeckung beitragen können.  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `businessTarget[string]`: Zu Informationszwecken: Das Unternehmensziel, auf das sich dieser KPI bezieht  - `calculatedBy[string]`: Die für die Berechnung des KPIs zuständige Organisation  - `calculationFormula[string]`: Zu Informationszwecken wird die Formel zur Berechnung des Indikators  - `calculationFrequency[string]`: Wie oft der KPI berechnet wird. Erlaubte Werte: einer von (stündlich, täglich, wöchentlich, monatlich, jährlich, vierteljährlich, zweimonatlich, vierzehntägig). Oder jeder andere für die Anwendung sinnvolle Wert, der nicht in der obigen Liste enthalten ist.  - `calculationMethod[string]`: Die verwendete Berechnungsmethode  - `calculationPeriod[object]`: KPIs Zeitspanne  	- `from`:     
- `category[array]`: Kategorie des Indikators. Erlaubte Werte: (quantitativ, qualitativ, führend, nachlaufend, Input, Prozess, Output, praktisch, richtungsweisend, umsetzbar, finanziell). Eine Beschreibung jeder der oben aufgeführten Kategorien finden Sie in Wikipedia. - Jeder andere Wert, der für die Anwendung von Bedeutung ist und nicht durch die obige Liste abgedeckt wird  - `currentStanding[string]`: Der aktuelle Stand des KPI gemäß seinem kpiValue. Erlaubte Werte: einer von (sehr gut, gut, mittelmäßig, schlecht, sehr schlecht)  - `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateExpires[date-time]`: Das Datum, an dem der KPI nicht mehr notwendig oder aussagekräftig sein wird  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `dateNextCalculation[date]`: Datum, an dem eine neue Berechnung der KPI verfügbar sein sollte  - `description[string]`: Eine Beschreibung dieses Artikels  - `effectiveSince[date-time]`: Das Datum, an dem die Organisation diesen KPI erstellt hat. Dieses Datum kann sich vom Erstellungsdatum der Entität unterscheiden  - `id[*]`: Eindeutiger Bezeichner der Entität  - `kpiValue[*]`: Wert des KPI. Er kann von beliebigem Typ sein  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels  - `organization[string]`: Durch den KPI bewertete Fachorganisation  . Model: [ https://schema.org/organization]( https://schema.org/organization)- `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `process[string]`: Entweder muss der Prozess oder das Produkt definiert werden  - `product[string]`: Entweder muss der Prozess oder das Produkt definiert werden  - `provider[string]`: Anbieter des Produkts oder der Dienstleistung, das/die mit dieser Kennzahl bewertet wird, falls vorhanden  . Model: [https://schema.org/provider](https://schema.org/provider)- `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `type[string]`: Es muss KeyPerformanceIndicator sein. Enum:'KeyPerformanceIndicator'  - `updatedAt[date-time]`: Letztes Aktualisierungsdatum der KPI-Daten. Dies kann ein anderes Datum sein als das letzte Aktualisierungsdatum des KPI-Werts  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
KeyPerformanceIndicator:    
  description: A Key Performance Indicator (KPI) is a type of performance measurement. KPIs evaluate the success of an organization or of a particular activity in which it engages.    
  properties:    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: 'The country. For example, Spain'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: 'The locality in which the street address is, and which is in the region'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: 'The region in which the locality is, and which is in the country'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: 'The post office box number for PO box addresses. For example, 03578'    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: 'The postal code. For example, 24004'    
          type: string    
          x-ngsi:    
            model: https://schema.org/https://schema.org/postalCode    
            type: Property    
        streetAddress:    
          description: The street address    
          type: string    
          x-ngsi:    
            model: https://schema.org/streetAddress    
            type: Property    
        streetNr:    
          description: Number identifying a specific property on a public street    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    aggregatedData:    
      description: ' Entity(ies) and attribute(s) aggregated by the KPI'    
      items:    
        properties:    
          attrs:    
            items:    
              type: string    
            minItems: 1    
            type: array    
          entityType:    
            type: string    
        type: object    
      minItems: 1    
      type: array    
      x-ngsi:    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    area:    
      description: 'For organizational purposes, it allows to add extra textual geographical information such as district, borough, or any other hint which can help to identify the KPI coverage'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    businessTarget:    
      description: 'For informative purposes, the business target to which this KPI is related to'    
      type: string    
      x-ngsi:    
        type: Property    
    calculatedBy:    
      description: The organization in charge of calculating the KPI    
      type: string    
      x-ngsi:    
        type: Property    
    calculationFormula:    
      description: 'For informative purposes, the formula used for calculating the indicator'    
      type: string    
      x-ngsi:    
        type: Property    
    calculationFrequency:    
      description: 'How often the KPI is calculated. Allowed values: one Of (hourly, daily, weekly, monthly, yearly, quarterly, bimonthly, biweekly). Or any other value meaningful for the application and not covered by the above list'    
      enum:    
        - hourly    
        - daily    
        - weekly    
        - monthly    
        - yearly    
        - quarterly    
        - bimonthly    
        - biweekly    
      type: string    
      x-ngsi:    
        type: Property    
    calculationMethod:    
      description: The calculation method used    
      enum:    
        - manual    
        - automatic    
        - semiautomatic    
      type: string    
      x-ngsi:    
        type: Property    
    calculationPeriod:    
      description: KPI's period of time    
      properties:    
        from:    
          format: date    
          type: string    
        to:    
          format: date    
          type: string    
      type: object    
      x-ngsi:    
        type: Property    
    category:    
      description: 'Indicator category. Allowed values: (quantitative, qualitative, leading, lagging, input, process, output, practical, directional, actionable, financial). Check Wikipedia for a description of each category listed above. - Any other value meaningful to the application and not covered by the above list'    
      items:    
        enum:    
          - actionable    
          - directional    
          - financial    
          - input    
          - lagging    
          - leading    
          - output    
          - practical    
          - process    
          - qualitative    
          - quantitative    
        type: string    
      minItems: 1    
      type: array    
      x-ngsi:    
        type: Property    
    currentStanding:    
      description: 'The KPI''s current standing as per its kpiValue. Allowed values: one Of (very good, good, fair, bad, very bad)'    
      enum:    
        - veryGood    
        - good    
        - fair    
        - bad    
        - veryBad    
      type: string    
      x-ngsi:    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateExpires:    
      description: The date on which the KPI will be no longer necessary or meaningful    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateNextCalculation:    
      description: Date on which a new calculation of the KPI should be available    
      format: date    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    effectiveSince:    
      description: The date on which the organization created this KPI. This date might be different than the entity creation date    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    kpiValue:    
      description: Value of the KPI. It can be of any type    
      oneOf:    
        - type: string    
        - type: number    
        - type: boolean    
        - type: object    
        - type: array    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: Geojson reference to the item. Point    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    organization:    
      description: Subject organization evaluated by the KPI    
      type: string    
      x-ngsi:    
        model: ' https://schema.org/organization'    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    process:    
      description: Either process or product must be defined    
      type: string    
      x-ngsi:    
        type: Property    
    product:    
      description: Either process or product must be defined    
      type: string    
      x-ngsi:    
        type: Property    
    provider:    
      description: 'Provider of the product or service, if any, that this KPI evaluates'    
      type: string    
      x-ngsi:    
        model: https://schema.org/provider    
        type: Property    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'It must be KeyPerformanceIndicator. Enum:''KeyPerformanceIndicator'''    
      enum:    
        - KeyPerformanceIndicator    
      type: string    
      x-ngsi:    
        type: Property    
    updatedAt:    
      description: Last update date of the KPI data. This can be different than the last update date of the KPI's value    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.KeyPerformanceIndicator/blob/master/KeyPerformanceIndicator/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.KeyPerformanceIndicator/keyPerformanceIndicator/schema.json    
  x-model-tags: ""    
  x-version: 0.2.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### KeyPerformanceIndicator NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für einen KeyPerformanceIndicator im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "kpi-2016-Ciudad-containers-faults",  
  "type": "KeyPerformanceIndicator",  
  "name": "Incidencias-Contenedores-Mensual",  
  "description": "Number of incidences raised on containers per month",  
  "category": [  
    "quantitative"  
  ],  
  "organization": "Ayuntamiento de Ciudad",  
  "provider": "Cleaning Service Provider S.A.",  
  "kpiValue": 20,  
  "currentStanding": "good",  
  "calculationPeriod": {  
    "from": "2016-06-01",  
    "to": "2016-06-30"  
  },  
  "calculationMethod": "automatic",  
  "calculationFrequency": "monthly",  
  "dateModified": "2016-06-29T15:59:09.224Z",  
  "dateNextCalculation": "2016-07-31",  
  "address": {  
    "addressLocality": "Ciudad",  
    "addressCountry": "ESP"  
  },  
  "process": "Garbage Collection"  
}  
```  
</details>  
#### KeyPerformanceIndicator NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen KeyPerformanceIndicator im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "kpi-2016-Ciudad-containers-faults",  
  "type": "KeyPerformanceIndicator",  
  "category": {  
    "type": "array",  
    "value": [  
      "quantitative"  
    ]  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2016-06-29T15:59:09.224Z"  
  },  
  "calculationFrequency": {  
    "type": "Text",  
    "value": "monthly"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Number of incidences raised on containers per month"  
  },  
  "currentStanding": {  
    "type": "Text",  
    "value": "good"  
  },  
  "address": {  
    "type": "PostalAddress",  
    "value": {  
      "addressLocality": "Ciudad",  
      "addressCountry": "ESP"  
    }  
  },  
  "calculationPeriod": {  
    "type": "StructuredObject",  
    "value": {  
      "to": "2016-06-30",  
      "from": "2016-06-01"  
    }  
  },  
  "dateNextCalculation": {  
    "type": "DateTime",  
    "value": "2016-07-31"  
  },  
  "calculationMethod": {  
    "type": "Text",  
    "value": "automatic"  
  },  
  "provider": {  
    "type": "Text",  
    "value": "Cleaning Service Provider S.A."  
  },  
  "organization": {  
    "type": "Text",  
    "value": "Ayuntamiento de Ciudad"  
  },  
  "kpiValue": {  
    "type": "Number",  
    "value": 20  
  },  
  "name": {  
    "type": "Text",  
    "value": "Incidencias-Contenedores-Mensual"  
  },  
  "process": {  
    "type": "Text",  
    "value": "Garbage Collection"  
  }  
}  
```  
</details>  
#### KeyPerformanceIndicator NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für einen KeyPerformanceIndicator im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:KeyPerformanceIndicator:kpi-2016-Ciudad-containers-faults",  
    "type": "KeyPerformanceIndicator",  
    "address": {  
        "addressCountry": "ESP",  
        "addressLocality": "Ciudad"  
    },  
    "calculationFrequency": "monthly",  
    "calculationMethod": "automatic",  
    "calculationPeriod": {  
        "from": "2016-06-01",  
        "to": "2016-06-30"  
    },  
    "category": [  
        "quantitative"  
    ],  
    "currentStanding": "good",  
    "dateNextCalculation": "2016-07-31Z",  
    "description": "Number of incidences raised on containers per month",  
    "kpiValue": 20,  
    "modifiedAt": "2016-06-29T15:59:09.224Z",  
    "name": "Incidencias-Contenedores-Mensual",  
    "organization": "Ayuntamiento de Ciudad",  
    "process": "Garbage Collection",  
    "provider": "Cleaning Service Provider S.A.",  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.KeyPerformanceIndicator/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### KeyPerformanceIndicator NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen KeyPerformanceIndicator im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:KeyPerformanceIndicator:kpi-2016-Ciudad-containers-faults",  
  "type": "KeyPerformanceIndicator",  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressLocality": "Ciudad",  
      "addressCountry": "ESP",  
      "type": "PostalAddress"  
    }  
  },  
  "calculationFrequency": {  
    "type": "Property",  
    "value": "monthly"  
  },  
  "calculationMethod": {  
    "type": "Property",  
    "value": "automatic"  
  },  
  "calculationPeriod": {  
    "type": "Property",  
    "value": {  
      "to": "2016-06-30",  
      "from": "2016-06-01"  
    }  
  },  
  "category": {  
    "type": "Property",  
    "value": [  
      "quantitative"  
    ]  
  },  
  "currentStanding": {  
    "type": "Property",  
    "value": "good"  
  },  
  "dateNextCalculation": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-07-31T15:59:09.224Z"  
    }  
  },  
  "description": {  
    "type": "Property",  
    "value": "Number of incidences raised on containers per month"  
  },  
  "kpiValue": {  
    "type": "Property",  
    "value": 20  
  },  
  "modifiedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-06-29T15:59:09.224Z"  
    }  
  },  
  "name": {  
    "type": "Property",  
    "value": "Incidencias-Contenedores-Mensual"  
  },  
  "organization": {  
    "type": "Property",  
    "value": "Ayuntamiento de Ciudad"  
  },  
  "process": {  
    "type": "Property",  
    "value": "Garbage Collection"  
  },  
  "provider": {  
    "type": "Property",  
    "value": "Cleaning Service Provider S.A."  
  },  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.KeyPerformanceIndicator/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
