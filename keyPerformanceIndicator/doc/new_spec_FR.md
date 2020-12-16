Entité : keyPerformanceIndicator  
================================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.KeyPerformanceIndicator/blob/master/keyPerformanceIndicator/LICENSE.md)  
Description globale : **Un indicateur clé de performance (KPI) est un type de mesure de la performance. Les KPIs évaluent le succès d'une organisation ou d'une activité particulière dans laquelle elle s'engage.**  

## Liste des biens  

- `address`: L'adresse postale.  - `aggregatedData`:  Entité(s) et attribut(s) agrégés par l'ICP.  - `alternateName`: Un autre nom pour cet article  - `area`: À des fins organisationnelles, il permet d'ajouter des informations géographiques supplémentaires telles que le district, l'arrondissement ou tout autre indice qui peut aider à identifier la couverture des ICP.  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `businessTarget`: À titre d'information, la cible commerciale à laquelle ce KPI est lié.  - `calculatedBy`:  L'organisme chargé de calculer le KPI.  - `calculationFormula`: A titre indicatif, la formule utilisée pour le calcul de l'indicateur.  - `calculationFrequency`: La fréquence de calcul du KPI. Valeurs autorisées : l'une des valeurs suivantes (horaire, quotidienne, hebdomadaire, mensuelle, annuelle, trimestrielle, bimensuelle, bihebdomadaire). Ou toute autre valeur significative pour la demande et non couverte par la liste ci-dessus.  - `calculationMethod`: La méthode de calcul utilisée.  - `calculationPeriod`: La période de temps du KPI.  - `category`: Catégorie d'indicateur. Valeurs autorisées : (quantitatif, qualitatif, avancé, retardé, intrant, processus, résultat, pratique, directionnel, actionnable, financier). Consultez Wikipédia pour une description de chaque catégorie énumérée ci-dessus. - Toute autre valeur significative pour l'application et non couverte par la liste ci-dessus.  - `currentStanding`: Le statut actuel du KPI selon sa valeur kpi. Valeurs autorisées : l'une des valeurs suivantes (très bonne, bonne, moyenne, mauvaise, très mauvaise)  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateExpires`: La date à laquelle l'indicateur de performance clé ne sera plus nécessaire ou significatif.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateNextCalculation`: Date à laquelle un nouveau calcul du KPI devrait être disponible.  - `description`: Une description de cet article  - `effectiveSince`: La date à laquelle l'organisation a créé cet indicateur de performance clé. Cette date peut être différente de la date de création de l'entité.  - `id`: Identifiant unique de l'entité  - `kpiValue`:  Il peut être de n'importe quel type.  - `location`:   - `name`: Le nom de cet article.  - `organization`: Organisation du sujet évaluée par le KPI  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `process`: Il faut définir soit le procédé, soit le produit  - `product`: Il faut définir soit le procédé, soit le produit  - `provider`: Fournisseur du produit ou du service, le cas échéant, que cet indicateur de performance clé évalue.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `type`: Il doit s'agir d'un indicateur de performance clé (KeyPerformanceIndicator)  - `updatedAt`: Date de la dernière mise à jour des données du KPI. Cette date peut être différente de la date de dernière mise à jour de la valeur de l'indicateur de performance clé.    
Propriétés requises  
- `id`  - `type`  ## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
keyPerformanceIndicator:    
  description: 'A Key Performance Indicator (KPI) is a type of performance measurement. KPIs evaluate the success of an organization or of a particular activity in which it engages.'    
  properties:    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/Text'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/Text'''    
          type: string    
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/Text'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/Text'''    
          type: string    
      type: Property    
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
      description: ' The organization in charge of calculating the KPI.'    
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
          - quantitative    
          - qualitative    
          - leading    
          - lagging    
          - input    
          - process    
          - output    
          - practical    
          - directional    
          - actionable    
          - financial    
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
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
      title: 'GeoJSON Geometry'    
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
            - format: uri    
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
#### keyPerformanceIndicator NGSI V2 key-values Exemple  
Voici un exemple d'indicateur de performance clé au format JSON en tant que valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
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
#### keyPerformanceIndicator NGSI V2 normalisé Exemple  
Voici un exemple d'indicateur de performance clé au format JSON normalisé. Il est compatible avec NGSI V2 lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
#### keyPerformanceIndicator NGSI-LD key-values Exemple  
Voici un exemple d'indicateur de performance clé au format JSON-LD en tant que valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{"@context": ["https://smart-data-models.github.io/data-models/context.jsonld",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "address": {"addressCountry": "ESP",  
             "addressLocality": "Ciudad",  
             "type": "PostalAddress"},  
 "calculationFrequency": "monthly",  
 "calculationMethod": "automatic",  
 "calculationPeriod": {"from": "2016-06-01", "to": "2016-06-30"},  
 "category": ["quantitative"],  
 "currentStanding": "good",  
 "dateNextCalculation": {"@type": "DateTime", "@value": "2016-07-31Z"},  
 "description": "Number of incidences raised on containers per month",  
 "id": "urn:ngsi-ld:KeyPerformanceIndicator:kpi-2016-Ciudad-containers-faults",  
 "kpiValue": 20,  
 "modifiedAt": "2016-06-29T15:59:09.224Z",  
 "name": "Incidencias-Contenedores-Mensual",  
 "organization": {"name": "Ayuntamiento de Ciudad"},  
 "process": "Garbage Collection",  
 "provider": {"name": "Cleaning Service Provider S.A."},  
 "type": "KeyPerformanceIndicator"}  
```  
#### keyPerformanceIndicator NGSI-LD normalisé Exemple  
Voici un exemple d'indicateur de performance clé au format JSON-LD normalisé. Il est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
