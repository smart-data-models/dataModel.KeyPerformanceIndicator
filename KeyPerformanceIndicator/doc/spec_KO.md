<!-- 10-Header -->
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)      

============================
<!-- 15-License -->


<!-- /15-License -->
<!-- 20-Description -->


<!-- /20-Description -->
<!-- 30-PropertiesList -->


- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)      
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)      
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.        
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)      
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)      
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)      
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호        
- `aggregatedData[array]`:  KPI에 의해 집계된 엔티티 및 속성  
	- `to`:         
- `category[array]`: 지표 카테고리. 허용되는 값: (정량적, 정성적, 선행, 후행, 투입, 프로세스, 산출, 실용적, 방향성, 실행 가능, 재무). 위에 나열된 각 카테고리에 대한 설명은 위키백과를 참조하세요. - 애플리케이션에 의미가 있고 위 목록에 포함되지 않은 기타 모든 값  
<!-- 35-RequiredProperties -->

- `id`  
<!-- 40-RequiredProperties -->
<!-- /40-RequiredProperties -->
<!-- 50-DataModelHeader -->


<!-- /50-DataModelHeader -->
<!-- 60-ModelYaml -->
<details><summary><strong>full yaml details</strong></summary>        

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



<details><summary><strong>show/hide example</strong></summary>        


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


<details><summary><strong>show/hide example</strong></summary>        


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


<details><summary><strong>show/hide example</strong></summary>        


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


<details><summary><strong>show/hide example</strong></summary>        


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

<!-- /95-Units -->
<!-- 97-LastFooter -->
---      
