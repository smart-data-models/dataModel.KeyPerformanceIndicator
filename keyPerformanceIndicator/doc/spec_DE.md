Entität: keyPerformanceIndicator  
================================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.KeyPerformanceIndicator/blob/master/keyPerformanceIndicator/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Ein Key Performance Indicator (KPI) ist eine Art der Leistungsmessung. KPIs bewerten den Erfolg einer Organisation oder einer bestimmten Aktivität, an der sie beteiligt ist.**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `aggregatedData`:  Entität(en) und Attribut(e), die durch den KPI aggregiert werden.  - `alternateName`: Ein alternativer Name für diesen Artikel  - `area`: Zu organisatorischen Zwecken können Sie zusätzliche geografische Textinformationen hinzufügen, z. B. Bezirk, Stadtteil oder andere Hinweise, die bei der Identifizierung der KPI-Abdeckung helfen können.  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `businessTarget`: Zu Informationszwecken das Unternehmensziel, auf das sich dieser KPI bezieht.  - `calculatedBy`: Die Organisation, die für die Berechnung des KPI zuständig ist.  - `calculationFormula`: Zu Informationszwecken wird die Formel zur Berechnung des Indikators verwendet.  - `calculationFrequency`: Wie oft der KPI berechnet wird. Erlaubte Werte: einer von (stündlich, täglich, wöchentlich, monatlich, jährlich, vierteljährlich, zweimonatlich, vierzehntägig). Oder jeder andere Wert, der für die Anwendung sinnvoll ist und nicht durch die obige Liste abgedeckt wird.  - `calculationMethod`: Die verwendete Berechnungsmethode.  - `calculationPeriod`: KPIs Zeitraum.  - `category`: Indikator-Kategorie. Erlaubte Werte: (quantitativ, qualitativ, führend, nachlaufend, Input, Prozess, Output, praktisch, richtungsweisend, umsetzbar, finanziell). Eine Beschreibung jeder oben aufgeführten Kategorie finden Sie in Wikipedia. - Jeder andere Wert, der für die Anwendung sinnvoll ist und nicht durch die obige Liste abgedeckt wird.  - `currentStanding`: Der aktuelle Stand des KPIs gemäß seinem kpiValue. Erlaubte Werte: einer von (sehr gut, gut, mittelmäßig, schlecht, sehr schlecht)  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateExpires`: Das Datum, an dem der KPI nicht mehr notwendig oder aussagekräftig sein wird.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `dateNextCalculation`: Datum, an dem eine neue Berechnung des KPIs verfügbar sein soll.  - `description`: Eine Beschreibung dieses Artikels  - `effectiveSince`: Das Datum, an dem die Organisation diesen KPI erstellt hat. Dieses Datum kann sich vom Erstellungsdatum der Entität unterscheiden.  - `id`: Eindeutiger Bezeichner der Entität  - `kpiValue`:  Sie kann von jedem Typ sein.  - `location`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name`: Der Name dieses Elements.  - `organization`: Subjektorganisation, die durch den KPI bewertet wird  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `process`: Entweder muss der Prozess oder das Produkt definiert werden  - `product`: Entweder muss der Prozess oder das Produkt definiert werden  - `provider`: Anbieter des Produkts oder Dienstes, falls vorhanden, den dieser KPI bewertet.  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `type`: Es muss KeyPerformanceIndicator sein  - `updatedAt`: Letztes Aktualisierungsdatum der KPI-Daten. Dies kann ein anderes Datum sein als das letzte Aktualisierungsdatum des KPI-Wertes.    
Erforderliche Eigenschaften  
- `id`  - `type`  ## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
keyPerformanceIndicator:    
  description: 'A Key Performance Indicator (KPI) is a type of performance measurement. KPIs evaluate the success of an organization or of a particular activity in which it engages.'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
    aggregatedData:    
      description: ' Entity(ies) and attribute(s) aggregated by the KPI.'    
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
      type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    area:    
      description: 'For organizational purposes, it allows to add extra textual geographical information such as district, borough, or any other hint which can help to identify the KPI coverage.'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    businessTarget:    
      description: 'For informative purposes, the business target to which this KPI is related to.'    
      type: Property    
    calculatedBy:    
      description: 'The organization in charge of calculating the KPI.'    
      type: Property    
    calculationFormula:    
      description: 'For informative purposes, the formula used for calculating the indicator.'    
      type: Property    
    calculationFrequency:    
      description: 'How often the KPI is calculated. Allowed values: one Of (hourly, daily, weekly, monthly, yearly, quarterly, bimonthly, biweekly). Or any other value meaningful for the application and not covered by the above list.'    
      enum:    
        - hourly    
        - daily    
        - weekly    
        - monthly    
        - yearly    
        - quarterly    
        - bimonthly    
        - biweekly    
      type: Property    
    calculationMethod:    
      description: 'The calculation method used.'    
      enum:    
        - manual    
        - automatic    
        - semiautomatic    
      type: Property    
    calculationPeriod:    
      description: 'KPI''s period of time.'    
      properties:    
        from:    
          format: date    
          type: string    
        to:    
          format: date    
          type: string    
      type: Property    
    category:    
      description: 'Indicator category. Allowed values: (quantitative, qualitative, leading, lagging, input, process, output, practical, directional, actionable, financial). Check Wikipedia for a description of each category listed above. - Any other value meaningful to the application and not covered by the above list.'    
      items:    
        enum:    
          - actionable    
          - directional    
          - financial    
          - input    
          - lagging    
          - leading    
          - quantitative    
          - qualitative    
          - output    
          - practical    
          - process    
        type: string    
      minItems: 1    
      type: Property    
    currentStanding:    
      description: 'The KPI''s current standing as per its kpiValue. Allowed values: one Of (very good, good, fair, bad, very bad)'    
      enum:    
        - veryGood    
        - good    
        - fair    
        - bad    
        - veryBad    
      type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateExpires:    
      description: 'The date on which the KPI will be no longer necessary or meaningful.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateNextCalculation:    
      description: 'Date on which a new calculation of the KPI should be available.'    
      format: date    
      type: Property    
    description:    
      description: 'A description of this item'    
      type: Property    
    effectiveSince:    
      description: 'The date on which the organization created this KPI. This date might be different than the entity creation date.'    
      format: date-time    
      type: Property    
    id:    
      anyOf: &keyperformanceindicator_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      type: Property    
    kpiValue:    
      description: ' It can be of any type.'    
      type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
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
          title: 'GeoJSON Point'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
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
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
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
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
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
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiPolygon'    
          type: object    
      type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: Property    
    organization:    
      description: 'Subject organization evaluated by the KPI'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/organization'    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *keyperformanceindicator_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    process:    
      description: 'Either process or product must be defined'    
      type: Property    
    product:    
      description: 'Either process or product must be defined'    
      type: Property    
    provider:    
      description: 'Provider of the product or service, if any, that this KPI evaluates.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/provider    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'It must be KeyPerformanceIndicator'    
      enum:    
        - KeyPerformanceIndicator    
      type: Property    
    updatedAt:    
      description: 'Last update date of the KPI data. This can be different than the last update date of the KPI''s value.'    
      format: date-time    
      type: Property    
  required:    
    - id    
    - type    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
#### keyPerformanceIndicator NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für einen keyPerformanceIndicator im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "kpi-2016-Ciudad-containers-faults",  
  "type": "KeyPerformanceIndicator",  
  "name": "Incidencias-Contenedores-Mensual",  
  "description": "Number of incidences raised on containers per month",  
  "category": ["quantitative"],  
  "organization": {  
    "name": "Ayuntamiento de Ciudad"  
  },  
  "provider": {  
    "name": "Cleaning Service Provider S.A."  
  },  
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
#### keyPerformanceIndicator NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen keyPerformanceIndicator im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "kpi-2016-Ciudad-containers-faults",  
  "type": "KeyPerformanceIndicator",  
  "category": {  
    "value": ["quantitative"]  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2016-06-29T15:59:09.224Z"  
  },  
  "calculationFrequency": {  
    "value": "monthly"  
  },  
  "description": {  
    "value": "Number of incidences raised on containers per month"  
  },  
  "currentStanding": {  
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
    "value": "automatic"  
  },  
  "provider": {  
    "value": {  
      "name": "Cleaning Service Provider S.A."  
    }  
  },  
  "organization": {  
    "value": {  
      "name": "Ayuntamiento de Ciudad"  
    }  
  },  
  "kpiValue": {  
    "value": 20  
  },  
  "name": {  
    "value": "Incidencias-Contenedores-Mensual"  
  },  
  "process": {  
    "value": "Garbage Collection"  
  }  
}  
```  
#### keyPerformanceIndicator NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für einen keyPerformanceIndicator im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:KeyPerformanceIndicator:kpi-2016-Ciudad-containers-faults",  
  "type": "KeyPerformanceIndicator",  
  "modifiedAt": "2016-06-29T15:59:09.224Z",  
  "category": {  
    "type": "Property",  
    "value": [  
      "quantitative"  
    ]  
  },  
  "calculationFrequency": {  
    "type": "Property",  
    "value": "monthly"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Number of incidences raised on containers per month"  
  },  
  "currentStanding": {  
    "type": "Property",  
    "value": "good"  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressLocality": "Ciudad",  
      "addressCountry": "ESP",  
      "type": "PostalAddress"  
    }  
  },  
  "calculationPeriod": {  
    "type": "Property",  
    "value": {  
      "to": "2016-06-30",  
      "from": "2016-06-01"  
    }  
  },  
  "dateNextCalculation": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-07-31Z"  
    }  
  },  
  "calculationMethod": {  
    "type": "Property",  
    "value": "automatic"  
  },  
  "provider": {  
    "type": "Property",  
    "value": {  
      "name": "Cleaning Service Provider S.A."  
    }  
  },  
  "organization": {  
    "type": "Property",  
    "value": {  
      "name": "Ayuntamiento de Ciudad"  
    }  
  },  
  "kpiValue": {  
    "type": "Property",  
    "value": 20  
  },  
  "name": {  
    "type": "Property",  
    "value": "Incidencias-Contenedores-Mensual"  
  },  
  "process": {  
    "type": "Property",  
    "value": "Garbage Collection"  
  },  
  "@context": [  
    "https://smart-data-models.github.io/data-models/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### keyPerformanceIndicator NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen keyPerformanceIndicator im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "@context": [  
    "https://smart-data-models.github.io/data-models/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "address": {  
    "addressCountry": "ESP",  
    "addressLocality": "Ciudad",  
    "type": "PostalAddress"  
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
  "dateNextCalculation": {  
    "@type": "DateTime",  
    "@value": "2016-07-31Z"  
  },  
  "description": "Number of incidences raised on containers per month",  
  "id": "urn:ngsi-ld:KeyPerformanceIndicator:kpi-2016-Ciudad-containers-faults",  
  "kpiValue": 20,  
  "modifiedAt": "2016-06-29T15:59:09.224Z",  
  "name": "Incidencias-Contenedores-Mensual",  
  "organization": {  
    "name": "Ayuntamiento de Ciudad"  
  },  
  "process": "Garbage Collection",  
  "provider": {  
    "name": "Cleaning Service Provider S.A."  
  },  
  "type": "KeyPerformanceIndicator"  
}  
```  
