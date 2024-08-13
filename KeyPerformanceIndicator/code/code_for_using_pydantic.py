from __future__ import annotations

from datetime import date
from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, RootModel, constr


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class AggregatedDatum(BaseModel):
    attrs: Optional[List[str]] = Field(None, min_length=1)
    entityType: Optional[str] = None


class CalculationFrequency(Enum):
    hourly = 'hourly'
    daily = 'daily'
    weekly = 'weekly'
    monthly = 'monthly'
    yearly = 'yearly'
    quarterly = 'quarterly'
    bimonthly = 'bimonthly'
    biweekly = 'biweekly'


class CalculationMethod(Enum):
    manual = 'manual'
    automatic = 'automatic'
    semiautomatic = 'semiautomatic'


class CalculationPeriod(BaseModel):
    from_: Optional[date] = Field(None, alias='from')
    to: Optional[date] = None


class CategoryEnum(Enum):
    actionable = 'actionable'
    directional = 'directional'
    financial = 'financial'
    input = 'input'
    lagging = 'lagging'
    leading = 'leading'
    output = 'output'
    practical = 'practical'
    process = 'process'
    qualitative = 'qualitative'
    quantitative = 'quantitative'


class CurrentStanding(Enum):
    veryGood = 'veryGood'
    good = 'good'
    fair = 'fair'
    bad = 'bad'
    veryBad = 'veryBad'


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class Type6(Enum):
    KeyPerformanceIndicator = 'KeyPerformanceIndicator'


class KeyPerformanceIndicator(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    aggregatedData: Optional[List[AggregatedDatum]] = Field(
        None,
        description=' Entity(ies) and attribute(s) aggregated by the KPI',
        min_length=1,
    )
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    area: Optional[str] = Field(
        None,
        description='For organizational purposes, it allows to add extra textual geographical information such as district, borough, or any other hint which can help to identify the KPI coverage',
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    businessTarget: Optional[str] = Field(
        None,
        description='For informative purposes, the business target to which this KPI is related to',
    )
    calculatedBy: Optional[str] = Field(
        None, description='The organization in charge of calculating the KPI'
    )
    calculationFormula: Optional[str] = Field(
        None,
        description='For informative purposes, the formula used for calculating the indicator',
    )
    calculationFrequency: Optional[CalculationFrequency] = Field(
        None,
        description='How often the KPI is calculated. Allowed values: one Of (hourly, daily, weekly, monthly, yearly, quarterly, bimonthly, biweekly). Or any other value meaningful for the application and not covered by the above list',
    )
    calculationMethod: Optional[CalculationMethod] = Field(
        None, description='The calculation method used'
    )
    calculationPeriod: Optional[CalculationPeriod] = Field(
        None, description="KPI's period of time"
    )
    category: Optional[List[CategoryEnum]] = Field(
        None,
        description='Indicator category. Allowed values: (quantitative, qualitative, leading, lagging, input, process, output, practical, directional, actionable, financial). Check Wikipedia for a description of each category listed above. - Any other value meaningful to the application and not covered by the above list',
        min_length=1,
    )
    currentStanding: Optional[CurrentStanding] = Field(
        None,
        description="The KPI's current standing as per its kpiValue. Allowed values: one Of (very good, good, fair, bad, very bad)",
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateExpires: Optional[AwareDatetime] = Field(
        None,
        description='The date on which the KPI will be no longer necessary or meaningful',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    dateNextCalculation: Optional[date] = Field(
        None,
        description='Date on which a new calculation of the KPI should be available',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    effectiveSince: Optional[AwareDatetime] = Field(
        None,
        description='The date on which the organization created this KPI. This date might be different than the entity creation date',
    )
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    kpiValue: Optional[Union[str, float, bool, Dict[str, Any], List]] = Field(
        None, description='Value of the KPI. It can be of any type'
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    organization: Optional[str] = Field(
        None, description='Subject organization evaluated by the KPI'
    )
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    process: Optional[str] = Field(
        None, description='Either process or product must be defined'
    )
    product: Optional[str] = Field(
        None, description='Either process or product must be defined'
    )
    provider: Optional[str] = Field(
        None,
        description='Provider of the product or service, if any, that this KPI evaluates',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    type: Optional[Type6] = Field(
        None,
        description="It must be KeyPerformanceIndicator. Enum:'KeyPerformanceIndicator'",
    )
    updatedAt: Optional[AwareDatetime] = Field(
        None,
        description="Last update date of the KPI data. This can be different than the last update date of the KPI's value",
    )
