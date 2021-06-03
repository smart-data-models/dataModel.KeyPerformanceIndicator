Entidad: keyPerformanceIndicator  
================================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.KeyPerformanceIndicator/blob/master/keyPerformanceIndicator/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **Un indicador clave de rendimiento (KPI) es un tipo de medición del rendimiento. Los KPIs evalúan el éxito de una organización o de una actividad concreta a la que se dedica.**  

## Lista de propiedades  

- `address`: La dirección postal  - `aggregatedData`:  Entidad(es) y atributo(s) agregados por el KPI.  - `alternateName`: Un nombre alternativo para este artículo  - `area`: Con fines organizativos, permite añadir información geográfica textual adicional, como el distrito, el municipio o cualquier otra pista que pueda ayudar a identificar la cobertura del KPI.  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `businessTarget`: A efectos informativos, el objetivo empresarial con el que se relaciona este KPI.  - `calculatedBy`: La organización encargada de calcular el KPI.  - `calculationFormula`: A título informativo, la fórmula utilizada para el cálculo del indicador.  - `calculationFrequency`: Con qué frecuencia se calcula el KPI. Valores permitidos: uno de (cada hora, diario, semanal, mensual, anual, trimestral, bimensual, quincenal). O cualquier otro valor significativo para la aplicación y que no esté cubierto por la lista anterior.  - `calculationMethod`: El método de cálculo utilizado.  - `calculationPeriod`: Periodo de tiempo de los KPI's.  - `category`: Categoría del indicador. Valores permitidos: (cuantitativo, cualitativo, líder, rezagado, de entrada, de proceso, de salida, práctico, direccional, accionable, financiero). Consulte la Wikipedia para obtener una descripción de cada una de las categorías enumeradas anteriormente. - Cualquier otro valor significativo para la aplicación y que no esté cubierto por la lista anterior.  - `currentStanding`: La situación actual del KPI según su kpiValue. Valores permitidos: uno de (muy bueno, bueno, regular, malo, muy malo)  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateExpires`: La fecha en la que el KPI dejará de ser necesario o significativo.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `dateNextCalculation`: Fecha en la que debería estar disponible un nuevo cálculo del KPI.  - `description`: Una descripción de este artículo  - `effectiveSince`: La fecha en la que la organización creó este KPI. Esta fecha puede ser diferente de la fecha de creación de la entidad.  - `id`: Identificador único de la entidad  - `kpiValue`:  Puede ser de cualquier tipo.  - `location`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name`: El nombre de este artículo.  - `organization`: Organización del sujeto evaluado por el KPI  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `process`: Hay que definir el proceso o el producto  - `product`: Hay que definir el proceso o el producto  - `provider`: Proveedor del producto o servicio, si lo hay, que este KPI evalúa.  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen, o la URL del objeto de origen.  - `type`: Debe ser KeyPerformanceIndicator  - `updatedAt`: Fecha de la última actualización de los datos del KPI. Puede ser diferente a la última fecha de actualización del valor del KPI.    
Propiedades requeridas  
- `id`  - `type`  ## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
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
## Ejemplo de carga útil  
#### keyPerformanceIndicator NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un keyPerformanceIndicator en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### keyPerformanceIndicator NGSI-v2 normalizado Ejemplo  
Este es un ejemplo de un keyPerformanceIndicator en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### keyPerformanceIndicator NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un keyPerformanceIndicator en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### keyPerformanceIndicator NGSI-LD normalizado Ejemplo  
Este es un ejemplo de un keyPerformanceIndicator en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
