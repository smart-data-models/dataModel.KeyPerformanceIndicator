<!-- 10-Header -->      
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)      
Entité : Indicateur de performance clé      
======================================<!-- /10-Header -->      
<!-- 15-License -->      
[Licence ouverte] (https://github.com/smart-data-models//dataModel.KeyPerformanceIndicator/blob/master/KeyPerformanceIndicator/LICENSE.md)      
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)      
<!-- /15-License -->      
<!-- 20-Description -->      
Description globale : **Un indicateur clé de performance (ICP) est un type de mesure de la performance. Les ICP évaluent le succès d'une organisation ou d'une activité particulière dans laquelle elle s'engage**.      
version : 0.2.1      
<!-- /20-Description -->      
<!-- 30-PropertiesList -->      
## Liste des propriétés      
<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.      
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Le pays. Par exemple, l'Espagne  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)      
	- `addressLocality[string]`: La localité dans laquelle se trouve l'adresse postale et qui se trouve dans la région  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)      
	- `addressRegion[string]`: La région dans laquelle se trouve la localité et qui se trouve dans le pays  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)      
	- `district[string]`: Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local.        
	- `postOfficeBoxNumber[string]`: Le numéro de la boîte postale pour les adresses de boîtes postales. Par exemple, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)      
	- `postalCode[string]`: Le code postal. Par exemple, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)      
	- `streetAddress[string]`: L'adresse de la rue  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)      
- `aggregatedData[array]`:  Entité(s) et attribut(s) agrégés par l'ICP  - `alternateName[string]`: Un nom alternatif pour ce poste  - `area[string]`: À des fins organisationnelles, il permet d'ajouter des informations géographiques textuelles supplémentaires telles que le district, l'arrondissement ou tout autre indice permettant d'identifier la couverture de l'ICP.  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `calculatedBy[string]`: L'organisation chargée de calculer l'ICP  - `calculationFormula[string]`: A titre d'information, la formule utilisée pour le calcul de l'indicateur  - `calculationFrequency[string]`: Fréquence de calcul de l'ICP. Valeurs autorisées : une des valeurs suivantes (horaire, quotidienne, hebdomadaire, mensuelle, annuelle, trimestrielle, bimestrielle, bihebdomadaire). Ou toute autre valeur significative pour l'application et non couverte par la liste ci-dessus.  - `calculationMethod[string]`: La méthode de calcul utilisée  - `calculationPeriod[object]`: Période de l'ICP  	- `from`:         
- `category[array]`: Catégorie d'indicateur. Valeurs autorisées : (quantitatif, qualitatif, avancé, retardé, entrée, processus, sortie, pratique, directionnel, actionnable, financier). Consultez Wikipedia pour obtenir une description de chaque catégorie énumérée ci-dessus. - Toute autre valeur significative pour l'application et non couverte par la liste ci-dessus.  - `currentStanding[string]`: Situation actuelle de l'indicateur de performance clé, conformément à sa valeur (kpiValue). Valeurs autorisées : un de (très bon, bon, moyen, mauvais, très mauvais)  - `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateExpires[date-time]`: Date à laquelle l'ICP ne sera plus nécessaire ou significatif  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `dateNextCalculation[date]`: Date à laquelle un nouveau calcul de l'ICP devrait être disponible  - `description[string]`: Une description de l'article  - `effectiveSince[date-time]`: Date à laquelle l'organisation a créé cet ICP. Cette date peut être différente de la date de création de l'entité.  - `id[*]`: Identifiant unique de l'entité  - `kpiValue[*]`: Valeur de l'ICP. Elle peut être de n'importe quel type  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément  - `organization[string]`: Organisme évalué par l'ICP  . Model: [ https://schema.org/organization]( https://schema.org/organization)- `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `process[string]`: Le processus ou le produit doit être défini  - `product[string]`: Le processus ou le produit doit être défini  - `provider[string]`: Fournisseur du produit ou du service, le cas échéant, que cet ICP évalue  . Model: [https://schema.org/provider](https://schema.org/provider)- `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `type[string]`: Il doit s'agir de KeyPerformanceIndicator. Enum : "KeyPerformanceIndicator" (Indicateur de performance des clés)  - `updatedAt[date-time]`: Date de la dernière mise à jour des données de l'ICP. Cette date peut être différente de la date de la dernière mise à jour de la valeur de l'ICP.  <!-- /30-PropertiesList -->      
<!-- 35-RequiredProperties -->      
Propriétés requises      
- `id`  - `type`  <!-- /35-RequiredProperties -->      
<!-- 40-RequiredProperties -->      
<!-- /40-RequiredProperties -->      
<!-- 50-DataModelHeader -->      
## Modèle de données description des propriétés      
Classés par ordre alphabétique (cliquez pour plus de détails)      
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
## Exemples de charges utiles      
#### KeyPerformanceIndicator Valeurs clés de l'INSG-v2 Exemple      
Voici un exemple de KeyPerformanceIndicator au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.      
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
#### KeyPerformanceIndicator NGSI-v2 normalisé Exemple      
Voici un exemple de KeyPerformanceIndicator au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec la NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.      
<details><summary><strong>show/hide example</strong></summary>        
```json  
{  
  "id": "kpi-2016-Ciudad-containers-faults",  
  "type": "KeyPerformanceIndicator",  
  "category": {  
    "type": "StructuredValue",  
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
    "type": "StructuredValue",  
    "value": {  
      "addressLocality": "Ciudad",  
      "addressCountry": "ESP"  
    }  
  },  
  "calculationPeriod": {  
    "type": "StructuredValue",  
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
#### KeyPerformanceIndicator Valeurs clés NGSI-LD Exemple      
Voici un exemple d'indicateur de performance clé au format JSON-LD sous forme de valeurs clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.      
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
  "dateNextCalculation": "2016-07-31",  
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
#### KeyPerformanceIndicator NGSI-LD normalisé Exemple      
Voici un exemple de KeyPerformanceIndicator au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.      
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
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.      
<!-- /95-Units -->      
<!-- 97-LastFooter -->      
---      
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->      
