/* (Beta) Export of data model KeyPerformanceIndicator of the subject dataModel.KeyPerformanceIndicator for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE KeyPerformanceIndicator_calculationFrequency_type AS ENUM ('hourly', 'daily', 'weekly', 'monthly', 'yearly', 'quarterly', 'bimonthly', 'biweekly');
CREATE TYPE KeyPerformanceIndicator_calculationMethod_type AS ENUM ('manual', 'automatic', 'semiautomatic');
CREATE TYPE KeyPerformanceIndicator_currentStanding_type AS ENUM ('veryGood', 'good', 'fair', 'bad', 'veryBad');
CREATE TYPE KeyPerformanceIndicator_type AS ENUM ('KeyPerformanceIndicator');
CREATE TABLE KeyPerformanceIndicator (
  "address" JSON,
  "aggregatedData" JSON,
  "alternateName" TEXT,
  "area" TEXT,
  "areaServed" TEXT,
  "businessTarget" TEXT,
  "calculatedBy" TEXT,
  "calculationFormula" TEXT,
  "calculationFrequency" KeyPerformanceIndicator_calculationFrequency_type,
  "calculationMethod" KeyPerformanceIndicator_calculationMethod_type,
  "calculationPeriod" JSON,
  "category" JSON,
  "currentStanding" KeyPerformanceIndicator_currentStanding_type,
  "dataProvider" TEXT,
  "dateCreated" TIMESTAMP,
  "dateExpires" TIMESTAMP,
  "dateModified" TIMESTAMP,
  "dateNextCalculation" DATE,
  "description" TEXT,
  "effectiveSince" TIMESTAMP,
  "id" TEXT PRIMARY KEY,
  "kpiValue" JSON,
  "location" JSON,
  "name" TEXT,
  "organization" TEXT,
  "owner" JSON,
  "process" TEXT,
  "product" TEXT,
  "provider" TEXT,
  "seeAlso" JSON,
  "source" TEXT,
  "type" KeyPerformanceIndicator_type,
  "updatedAt" TIMESTAMP
);