<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。关键性能指标（KeyPerformanceIndicator  
=================================<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.KeyPerformanceIndicator/blob/master/KeyPerformanceIndicator/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述。**关键绩效指标（KPI）是绩效衡量的一种类型。关键绩效指标评估一个组织或其所从事的某项活动的成功程度。  
版本：0.2.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `aggregatedData[array]`: 由KPI汇总的实体和属性。  - `alternateName[string]`: 这个项目的一个替代名称  - `area[string]`: 出于组织的目的，它允许添加额外的文本地理信息，如地区、行政区或任何其他提示，以帮助识别KPI覆盖范围。  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `businessTarget[string]`: 为提供信息，本KPI与之相关的业务目标。  - `calculatedBy[string]`: 负责计算KPI的组织。  - `calculationFormula[string]`: 为了提供信息，用于计算指标的公式。  - `calculationFrequency[string]`: KPI的计算频率。允许的值：其中一个（每小时、每天、每周、每月、每年、每季度、每两个月、每两个星期）。或任何其他对应用有意义且未被上述列表涵盖的值。  - `calculationMethod[string]`: 使用的计算方法。  - `calculationPeriod[object]`: KPI的时间段。  - `category[array]`: 指标类别。允许的值：（定量、定性、领先、滞后、输入、过程、输出、实用、定向、可操作、财务）。查看维基百科对上述每个类别的描述。- 任何其他对应用有意义且未被上述列表所涵盖的值。  - `currentStanding[string]`: 根据kpiValue，KPI的当前状态。允许的值：一个（非常好、好、一般、坏、非常坏）。  - `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateExpires[string]`: 该关键绩效指标不再需要或不再有意义的日期。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `dateNextCalculation[string]`: 应提供新的KPI计算的日期。  - `description[string]`: 对这个项目的描述  - `effectiveSince[string]`: 该组织创建该KPI的日期。该日期可能与实体创建日期不同。  - `id[*]`: 实体的唯一标识符  - `kpiValue[*]`: KPI的价值。它可以是任何类型。  - `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `name[string]`: 这个项目的名称。  - `organization[string]`: 由KPI评价的主体组织  . Model: [ https://schema.org/organization]( https://schema.org/organization)- `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `process[string]`: 必须定义过程或产品  - `product[string]`: 必须定义过程或产品  - `provider[string]`: 本KPI所评估的产品或服务的供应商（如有）。  . Model: [https://schema.org/provider](https://schema.org/provider)- `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 提供实体数据原始来源的一连串字符，作为一个URL。建议为源提供者的完全合格域名，或源对象的URL。  - `type[string]`: 它必须是KeyPerformanceIndicator。Enum:'KeyPerformanceIndicator'。  - `updatedAt[string]`: KPI数据的最后更新日期。这可能与KPI值的最后更新日期不同。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
KeyPerformanceIndicator:    
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
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
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
      type: array    
      x-ngsi:    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    area:    
      description: 'For organizational purposes, it allows to add extra textual geographical information such as district, borough, or any other hint which can help to identify the KPI coverage.'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    businessTarget:    
      description: 'For informative purposes, the business target to which this KPI is related to.'    
      type: string    
      x-ngsi:    
        type: Property    
    calculatedBy:    
      description: 'The organization in charge of calculating the KPI.'    
      type: string    
      x-ngsi:    
        type: Property    
    calculationFormula:    
      description: 'For informative purposes, the formula used for calculating the indicator.'    
      type: string    
      x-ngsi:    
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
      type: string    
      x-ngsi:    
        type: Property    
    calculationMethod:    
      description: 'The calculation method used.'    
      enum:    
        - manual    
        - automatic    
        - semiautomatic    
      type: string    
      x-ngsi:    
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
      type: object    
      x-ngsi:    
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
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateExpires:    
      description: 'The date on which the KPI will be no longer necessary or meaningful.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateNextCalculation:    
      description: 'Date on which a new calculation of the KPI should be available.'    
      format: date    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    effectiveSince:    
      description: 'The date on which the organization created this KPI. This date might be different than the entity creation date.'    
      format: date-time    
      type: string    
      x-ngsi:    
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
      x-ngsi:    
        type: Property    
    kpiValue:    
      description: 'Value of the KPI. It can be of any type.'    
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
      x-ngsi:    
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    organization:    
      description: 'Subject organization evaluated by the KPI'    
      type: string    
      x-ngsi:    
        model: ' https://schema.org/organization'    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *keyperformanceindicator_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    process:    
      description: 'Either process or product must be defined'    
      type: string    
      x-ngsi:    
        type: Property    
    product:    
      description: 'Either process or product must be defined'    
      type: string    
      x-ngsi:    
        type: Property    
    provider:    
      description: 'Provider of the product or service, if any, that this KPI evaluates.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/provider    
        type: Property    
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
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
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
      description: 'Last update date of the KPI data. This can be different than the last update date of the KPI''s value.'    
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
## ＃＃＃＃有效载荷的例子  
#### KeyPerformanceIndicator NGSI-v2 key-values 示例  
下面是一个以JSON-LD格式作为key-values的KeyPerformanceIndicator的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
#### KeyPerformanceIndicator NGSI-v2规范化示例  
下面是一个规范化的JSON-LD格式的KeyPerformanceIndicator的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
#### KeyPerformanceIndicator NGSI-LD关键值示例  
这里有一个JSON-LD格式的KeyPerformanceIndicator作为key-values的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
#### KeyPerformanceIndicator NGSI-LD规范化示例  
下面是一个规范化的JSON-LD格式的KeyPerformanceIndicator的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
            "@value": "2016-07-31Z"  
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
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
