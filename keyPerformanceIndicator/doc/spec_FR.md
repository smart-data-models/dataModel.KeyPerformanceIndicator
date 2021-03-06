Entité : keyPerformanceIndicator  
================================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.KeyPerformanceIndicator/blob/master/keyPerformanceIndicator/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Un indicateur clé de performance (ICP) est un type de mesure de la performance. Les KPI évaluent le succès d'une organisation ou d'une activité particulière dans laquelle elle s'engage.**  

## Liste des propriétés  

- `address`: L'adresse postale  - `aggregatedData`:  Entité(s) et attribut(s) agrégés par le KPI.  - `alternateName`: Un nom alternatif pour cet élément  - `area`: À des fins d'organisation, il permet d'ajouter des informations géographiques textuelles supplémentaires telles que le district, l'arrondissement ou tout autre indice qui peut aider à identifier la couverture de l'indicateur de performance clé.  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `businessTarget`: A titre informatif, l'objectif commercial auquel ce KPI est lié.  - `calculatedBy`: L'organisation en charge du calcul de l'ICP.  - `calculationFormula`: A titre informatif, la formule utilisée pour le calcul de l'indicateur.  - `calculationFrequency`: Fréquence de calcul de l'indicateur de performance clé. Valeurs autorisées : une parmi (horaire, quotidien, hebdomadaire, mensuel, annuel, trimestriel, bimensuel, bihebdomadaire). Ou toute autre valeur significative pour l'application et non couverte par la liste ci-dessus.  - `calculationMethod`: La méthode de calcul utilisée.  - `calculationPeriod`: Période de temps des indicateurs clés de performance.  - `category`: Catégorie d'indicateur. Valeurs autorisées : (quantitatif, qualitatif, avancé, retardé, entrée, processus, sortie, pratique, directionnel, actionnable, financier). Consultez Wikipedia pour obtenir une description de chaque catégorie énumérée ci-dessus. - Toute autre valeur significative pour l'application et non couverte par la liste ci-dessus.  - `currentStanding`: L'état actuel de l'ICP selon sa valeur kpiValue. Valeurs autorisées : un parmi (très bon, bon, moyen, mauvais, très mauvais).  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateExpires`: La date à laquelle le KPI ne sera plus nécessaire ou significatif.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `dateNextCalculation`: Date à laquelle un nouveau calcul de l'ICP devrait être disponible.  - `description`: Une description de cet article  - `effectiveSince`: La date à laquelle l'organisation a créé ce KPI. Cette date peut être différente de la date de création de l'entité.  - `id`: Identifiant unique de l'entité  - `kpiValue`:  Il peut être de n'importe quel type.  - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `name`: Le nom de cet élément.  - `organization`: Organisation concernée évaluée par le KPI  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `process`: Il faut définir soit le processus, soit le produit  - `product`: Il faut définir soit le processus, soit le produit  - `provider`: Fournisseur du produit ou du service, le cas échéant, que cet ICP évalue.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `type`: Il doit s'agir de KeyPerformanceIndicator  - `updatedAt`: Date de la dernière mise à jour des données de l'ICP. Elle peut être différente de la dernière date de mise à jour de la valeur de l'ICP.    
Propriétés requises  
- `id`  - `type`  ## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
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
## Exemples de charges utiles  
#### keyPerformanceIndicator Valeurs-clés NGSI-v2 Exemple  
Voici un exemple de keyPerformanceIndicator au format JSON-LD en tant que key-values. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### keyPerformanceIndicator NGSI-v2 normalisé Exemple  
Voici un exemple d'un keyPerformanceIndicator au format JSON-LD tel que normalisé. Il est compatible avec la NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### keyPerformanceIndicator Valeurs-clés NGSI-LD Exemple  
Voici un exemple de keyPerformanceIndicator au format JSON-LD en tant que key-values. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### indicateur de performance des clés NGSI-LD normalisé Exemple  
Voici un exemple d'un keyPerformanceIndicator au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
