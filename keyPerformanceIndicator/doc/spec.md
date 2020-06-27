# KeyPerformanceIndicator

# Key Performance Indicator

According to [Wikipedia](https://en.wikipedia.org/wiki/Performance_indicator) a
Key Performance Indicator (KPI) is a type of performance measurement. KPIs
evaluate the success of an organization or of a particular activity in which it
engages.

The present data model defines a type of NGSI entity which captures the value
and associated details of a key performance indicator. The data model is
flexible enough to accommodate different usage scenarios: An entity per KPI
calculation or a unique entity per KPI which value evolves along time. Please
note that in the latter case a historical module, such as the STH, would have to
take care of the KPI evolution.

## Data Model

The data model is defined as shown below:

-   `id` : Entity's unique identifier.

-   `type` : It must be `KeyPerformanceIndicator`.

-   `source` : A sequence of characters giving the source of the entity data.

    -   Attribute type: Property. Text or [URL](https://schema.org/URL)
    -   Optional

-   `dataProvider` : Specifies the URL to information about the provider of this
    information

    -   Attribute type: Property. [URL](https://schema.org/URL)
    -   Optional

-   `name` : Indicator's name which should be meaningful in the context of a
    project or organization. Example `KPI-2016-2018-Incidences-Street`.

    -   Attribute type: Property. [Text](https://schema.org/Text)
    -   Normative References: `https://uri.etsi.org/ngsi-ld/name` equivalent to
        [name](https://schema.org/name)
    -   Mandatory

-   `alternateName` : An alias for the KPI.

    -   Attribute type: Property. [Text](https://schema.org/Text)
    -   Normative References:
        [https://schema.org/alternateName](https://schema.org/alternateName)
    -   Optional

-   `organization` : Subject organization evaluated by the KPI.

    -   Attribute type: Property.
        [Organization](https://schema.org/Organization)
    -   Normative References:
        [https://schema.org/organization](https://schema.org/Organization)
    -   Mandatory

-   `process` : Subject process evaluated by the KPI.

    -   Attribute type: Property. [Text](http://schema.org/Text)
    -   Either `process` or `product` must be defined.

-   `product` : Subject _product or service_ evaluated by the KPI.

    -   Attribute type: Property. [Product](https://schema.org/Product)
    -   Either `process` or `product` must be defined.

-   `provider` : Provider of the product or service, if any, that this KPI
    evaluates.

    -   Attribute Type: Property. [Provider](http://schema.org/provider) -
        Normative references:
        [https://schema.org/provider](https://schema.org/provider)
    -   Optional

-   `businessTarget` : For informative purposes, the business target to which
    this KPI is related to.

    -   Attribute type: Property. [Text](http://schema.org/Text)
    -   Optional

-   `description` : Indicator's description.

    -   Attribute type: Property. [Text](https://schema.org/Text)
    -   Normative References: `https://uri.etsi.org/ngsi-ld/description`
        equivalent to [description](https://schema.org/description)
    -   Optional

-   `calculationFrequency` : How often the KPI is calculated.

    -   Attribute type: Property. [Text](http://schema.org/Text)
    -   Allowed values: one Of (`hourly`, `daily`, `weekly`, `monthly`,
        `yearly`, `quarterly`, `bimonthly`, `biweekly`)
        -   Or any other value meaningful for the application and not covered by
            the above list.
    -   Mandatory

-   `category` : Indicator's category.

    -   Attribute Type: List of [Text](http://schema.org/Text)
    -   Allowed values: (`quantitative`, `qualitative`, `leading`, `lagging`,
        `input`, `process`, `output`, `practical`, `directional`, `actionable`,
        `financial`). Check
        [Wikipedia](https://en.wikipedia.org/wiki/Performance_indicator#Categorization_of_indicators)
        for a description of each category listed above. - Any other value
        meaningful to the application and not covered by the above list.
    -   Mandatory

-   `calculatedBy` : The organization in charge of calculating the KPI.

    -   Attribute type: Property.
        [Organization](https://schema.org/organization)
    -   Normative References:
        [https://schema.org/organization](https://schema.org/organization)
    -   Optional

-   `calculationMethod` : The calculation method used.

    -   Attribute type: Property. [Text](http://schema.org/Text)
    -   Allowed values: oneOf ( `manual`, `automatic`, `semiautomatic`)
        -   Any other value meaningful to the application and not covered by the
            above list.
    -   Optional

-   `calculationFormula` : For informative purposes, the formula used for
    calculating the indicator.

    -   Attribute type: Property. [Text](http://schema.org/Text)
    -   Optional

-   `aggregatedData` : Entity(ies) and attribute(s) aggregated by the KPI.

    -   Attribute type: Property. List of
        [StructuredValue](https://schema.org/StructuredValue).
        -   Subproperties:
            -   `entityType` : Entity type which data is aggregated.
                -   Type: [Text](http://schema.org/Text)
            -   `attrs` : Attributes which value is aggregated.
                -   Type: List of [Text](http://schema.org/Text)
    -   Optional

-   `calculationPeriod` : KPI's period of time.

    -   Attribute type: Property.
        [StructuredValue](https://schema.org/StructuredValue)
    -   Subproperties:
        -   `from` : Period start
            -   Type: [DateTime](http://schema.org/DateTime)
        -   `to` : Period end
            -   Type: [DateTime](http://schema.org/DateTime)

-   `currentStanding` : The KPI's current standing as per its `kpiValue`.

    -   Attribute type: Property. [Text](http://schema.org/Text)
    -   Attribute metadata:
        -   `timestamp`: Timestamp when the last update of the attribute
            happened.
            -   Type: [DateTime](http://schema.org/DateTime)
    -   Allowed values: one Of (`very good`, `good`, `fair`, `bad`, `very bad`)
    -   Optional

-   `kpiValue` :

    -   Attribute type: Property. It can be of any type.
    -   Attribute metadata:
        -   `timestamp`: Timestamp when the last update of the attribute
            happened.
            -   Type: [DateTime](http://schema.org/DateTime)
    -   Mandatory

-   `effectiveSince` : The date on which the organization created this KPI. This
    date might be different than the entity creation date.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Optional

-   `dateCreated` : Entity's creation timestamp.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Read-Only. Automatically generated.

-   `dateNextCalculation` : Date on which a new calculation of the KPI should be
    available.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Optional

-   `dateExpires` : The date on which the KPI will be no longer necessary or
    meaningful.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Optional

-   `updatedAt` : Last update date of the KPI data. This can be different than
    the last update date of the KPI's value.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Optional

-   `dateModified` : Last update timestamp of this entity.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Read-Only. Automatically generated.

-   `location` : Location of the area to which the KPI refers to.

    -   Attribute type: GeoProperty. `geo:json`.
    -   Normative References:
        [https://tools.ietf.org/html/rfc7946](https://tools.ietf.org/html/rfc7946)
    -   Optional

-   `address` : Civic address of the area to which the KPI refers to.

    -   Attribute type:
        [https://schema.org/PostalAddress](https://schema.org/PostalAddress)
    -   Optional

-   `area` : For organizational purposes, it allows to add extra textual
    geographical information such as district, burough, or any other hint which
    can help to identify the KPI coverage.
    -   Attribute type: Property. [Text](http://schema.org/Text)
    -   Optional

**Note**: JSON Schemas are intended to capture the data type and associated
constraints of the different Attributes, regardless their final representation
format in NGSI(v2, LD).

## Examples

### Normalized Example

Normalized NGSI response

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
    }
}
```

### key-value pairs Example

Sample uses simplified representation for data consumers `?options=keyValues`

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
    }
}
```

### LD Example

Sample uses the NGSI-LD representation

```json
{
    "id": "urn:ngsi-ld:KeyPerformanceIndicator:kpi-2016-Ciudad-containers-faults",
    "type": "KeyPerformanceIndicator",
    "modifiedAt": "2016-06-29T15:59:09.224Z",
    "category": {
        "type": "Property",
        "value": ["quantitative"]
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
        "https://schema.lab.fiware.org/ld/context",
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
    ]
}
```

## Test it with a real service

## Open issues

-   Taxonomy of services / products / processes for smart cities
-   Taxonomy of success values
