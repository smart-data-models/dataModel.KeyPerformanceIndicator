<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティKeyPerformanceIndicator  
=============================<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.KeyPerformanceIndicator/blob/master/KeyPerformanceIndicator/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな説明**重要業績評価指標（KPI）は、業績測定の一種である。KPIは、ある組織やその組織が従事している特定の活動の成功を評価するものである。  
バージョン: 0.2.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティのリスト  

<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 番地がある地域と、その地域に含まれる地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: その地域がある地域、またその国がある地域  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区とは行政区画の一種で、国によっては地方自治体によって管理されている。    
	- `postOfficeBoxNumber[string]`: 私書箱の住所のための私書箱番号。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 郵便番号。例：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 番地  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `aggregatedData[array]`: KPI によって集約されるエンティティおよび属性。  - `alternateName[string]`: この項目の別名  - `area[string]`: 組織的な目的のために、KPI の対象範囲を特定するのに役立つ地区、行政区、その他のヒントなど、追加のテキスト地理情報を追加することができます。  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `businessTarget[string]`: 参考までに、この KPI が関連する事業目標を以下に示す。  - `calculatedBy[string]`: KPIの算出を担当する組織  - `calculationFormula[string]`: 参考までに、この指標の計算式を以下に示す。  - `calculationFrequency[string]`: KPI の計算頻度。許可される値：いずれか 1 つ（毎時、毎日、毎週、毎月、毎年、四半期、隔月、隔週）。または、アプリケーションにとって意味があり、上記のリストに含まれないその他の値。  - `calculationMethod[string]`: 使用される計算方法  - `calculationPeriod[object]`: KPIの期間  	- `from`:     
- `category[array]`: 指標のカテゴリー。使用可能な値：（定量的、定性的、先行、遅行、入力、プロセス、出力、実用的、方向性、実行可能、財務）。上記の各カテゴリの説明については、ウィキペディアを確認してください。- 上記のリストでカバーされていない、アプリケーションにとって意味のあるその他の値。  - `currentStanding[string]`: kpiValue に従った KPI の現在の状態。許可される値: 1 つ (非常に良い、良い、まあまあ、悪い、非常に悪い)  - `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateExpires[date-time]`: KPI が必要でなくなる日、または意味がなくなる日。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateNextCalculation[date]`: KPI の新しい計算が利用可能になる日付。  - `description[string]`: この商品の説明  - `effectiveSince[date-time]`: 組織がこの KPI を作成した日付。この日付は、エンティティの作成日と異なる場合があります。  - `id[*]`: エンティティの一意識別子  - `kpiValue[*]`: KPIの値。任意のタイプを指定できます。  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `name[string]`: このアイテムの名前  - `organization[string]`: KPIで評価される対象組織  . Model: [ https://schema.org/organization]( https://schema.org/organization)- `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `process[string]`: プロセスか製品のどちらかを定義しなければならない  - `product[string]`: プロセスか製品のどちらかを定義しなければならない  - `provider[string]`: この KPI が評価する製品またはサービスがある場合は、その提供者。  . Model: [https://schema.org/provider](https://schema.org/provider)- `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `type[string]`: KeyPerformanceIndicatorでなければならない。Enum:'KeyPerformanceIndicator'。  - `updatedAt[date-time]`: KPI データの最終更新日。これは、KPI の値の最終更新日と異なる場合があります。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
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
## ペイロードの例  
#### KeyPerformanceIndicator NGSI-v2 キー値の例  
KeyPerformanceIndicatorのJSON-LD形式のkey-valuesの例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。  
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
#### KeyPerformanceIndicator NGSI-v2 正規化例  
以下は、正規化されたJSON-LD形式のKeyPerformanceIndicatorの例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキスト・データを返します。  
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
#### KeyPerformanceIndicator NGSI-LD キー値の例  
以下はKeyPerformanceIndicatorをJSON-LD形式でkey-valuesとした例である。options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返す。  
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
#### KeyPerformanceIndicator NGSI-LD 正規化例  
以下は、正規化されたJSON-LD形式のKeyPerformanceIndicatorの例である。これは、オプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
