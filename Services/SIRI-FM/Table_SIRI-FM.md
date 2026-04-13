# SIRI-FM — Element Tables

## FacilityMonitoringDelivery

> A data type for the representation of one or more facility conditions, or updates on previously published conditions through FacilityConditions per FacilityMonitoringDelivery with the status and scope of the affected services.

**FacilityMonitoringDelivery** < [ServiceDelivery](../../Objects/ServiceDelivery/Description_ServiceDelivery.md)

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| attribute | version | xsd:NMTOKEN | 1:1 | Version ID for FacilityMonitoringDelivery |
| element | ResponseTimestamp | xsd:dateTime | 1:1 | Timestamp for when the dataset was created/published |
| element | FacilityCondition | [FacilityConditionStructure](#facilityconditionstructure) | 1:* | Data object for a facility condition which describes the current state or status changes of the monitored facility |

---

## FacilityConditionStructure

> Data structure for facility condition data.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| (choice) element | Facility | [FacilityStructure](#facilitystructure) | 1:1 | Facility affected by the condition |
| | FacilityRef | xsd:NMTOKEN | | Reference to the identifier of the facility |
| element | FacilityStatus | [FacilityStatusStructure](#facilitystatusstructure) | 1:1 | Current status of the facility |
| element | FacilityUpdatedPosition | [LocationStructure](#locationstructure) | 0:1 | New position of the facility referenced by the FacilityRef or described by the Facility (applicable only for mobile facilities) |
| element | MonitoredCounting | [MonitoredCountingStructure](#monitoredcountingstructure) | 0:* | Monitored counted values (e.g. seat availability or charging level) |
| element | MonitoringInfo | [MonitoringInformationStructure](#monitoringinformationstructure) | 0:1 | Description of the mechanism used to monitor the change of the facility status |
| element | Remedy | [RemedyStructure](#remedystructure) | 0:1 | Action how to fix the change of the facility status (if partially or completely unavailable) |
| element | SituationRef | [SituationRefStructure](#situationrefstructure) | 0:1 | Reference to a situation published earlier via [SIRI-SX](../SIRI-SX/Description_SIRI-SX.md) (used for linking a facility condition to a larger-scale situation) |
| element | ValidityPeriod | [HalfOpenTimestampInputRangeStructure](#halfopentimestampinputrangestructure) | 0:1 | Period (duration) of the facility condition |

---

## FacilityStructure

> Data structure with the information of a facility.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | FacilityCode | xsd:NMTOKEN | 0:1 | Identifier of the facility |
| element | Description | NaturalLanguageStringStructure | 0:* | Textual description(s) of the facility |
| element | FacilityClass | FacilityCategoryEnumeration | 0:* | Type(s) of the facility. Values: `unknown`, `fixedEquipment`, `mobileEquipment`, `serviceProvidedByIndividual`, `serviceForPersonalDevice`, `reservedArea`, `site`, `siteComponent`, `parkingBay`, `vehicle` |
| element | Features | [Features](#features) | 0:1 | Features of the facility |
| element | OwnerRef | xsd:NMTOKEN | 0:1 | Reference to the identifier of the owner of the facility |
| element | OwnerName | NaturalLanguageStringStructure | 0:1 | Textual description of the owner of the facility |
| element | ValidityCondition | [MonitoringValidityConditionStructure](#monitoringvalidityconditionstructure) | 0:1 | When the facility is normally available. If not specified, default is 'always' |
| element | FacilityLocation | [FacilityLocationStructure](#facilitylocationstructure) | 0:1 | Describes where the facility is located |
| element | Limitations | [Limitations](#limitations) | 0:1 | Static limitations for the accessibility of the facility |
| element | Suitabilities | [Suitabilities](#suitabilities) | 0:1 | Static suitabilities of the facility for specific passenger needs |
| element | AccessibilityAssessment | [AccessibilityAssessmentStructure](#accessibilityassessmentstructure) | 0:1 | Current accessibility of the facility |

---

## FacilityStatusStructure

> Data structure for the status of a facility.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | Status | FacilityStatusEnumeration | 1:1 | Status of the facility. Values: `unknown`, `available`, `notAvailable`, `partiallyAvailable`, `added`, `removed` |
| element | Description | NaturalLanguageStringStructure | 0:* | Description(s) of the facility status in natural language |
| element | AccessibilityAssessment | [AccessibilityAssessmentStructure](#accessibilityassessmentstructure) | 0:1 | Updated accessibility of the facility (how the current status affects the accessibility) |

---

## FacilityLocationStructure

> Data structure for a location of a facility. The actual location is defined by the referenced entities.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | LineRef | xsd:NMTOKEN | 0:1 | Reference to the identifier of a line |
| element | StopPointRef | xsd:NMTOKEN | 0:1 | Reference to the identifier of a stop point |
| element | VehicleRef | xsd:NMTOKEN | 0:1 | Reference to the identifier of a vehicle |
| element | CompoundTrainRef | xsd:NMTOKEN | 0:1 | Reference to the identifier of a compound train |
| element | TrainInCompoundTrainRef | xsd:NMTOKEN | 0:1 | Reference to the identifier of a train in a compound train |
| element | TrainRef | xsd:NMTOKEN | 0:1 | Reference to the identifier of a train |
| element | TrainComponentRef | xsd:NMTOKEN | 0:1 | Reference to the identifier of a train component |
| element | TrainElementRef | xsd:NMTOKEN | 0:1 | Reference to the identifier of a train element |
| element | EntranceToVehicleRef | xsd:NMTOKEN | 0:1 | Reference to the identifier of a vehicle entrance |
| element | DatedVehicleJourneyRef | xsd:NMTOKEN | 0:1 | Reference to the identifier of a dated vehicle journey |
| element | ConnectionLinkRef | xsd:NMTOKEN | 0:1 | Reference to the identifier of a connection link |
| element | InterchangeRef | xsd:NMTOKEN | 0:1 | Reference to the identifier of an interchange |
| element | StopPlaceRef | xsd:NMTOKEN | 0:1 | Reference to the identifier of a stop place |
| element | StopPlaceComponentId | xsd:NMTOKEN | 0:1 | Reference to the identifier of a stop place component |
| element | OperatorRef | xsd:NMTOKEN | 0:1 | Reference to the identifier of an operator (of a vehicle journey) |
| element | ProductCategoryRef | xsd:NMTOKEN | 0:1 | Reference to the identifier of a product category (classification of a vehicle journey) |
| element | ServiceFeatureRef | xsd:NMTOKEN | 0:* | Reference to the identifier of a service feature |
| element | VehicleFeatureRef | xsd:NMTOKEN | 0:* | Reference to the identifier of a vehicle feature |

---

## LocationStructure

> Data structure for the geospatial position of a facility.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| (choice) element | Longitude | xsd:decimal | 1:1 | Longitude (from -180.0 to 180.0) |
| | Latitude | xsd:decimal | | Latitude (from -90.0 to 90.0) |
| | Altitude | xsd:decimal | | Altitude as meters from the sea level (optional) |
| | Coordinates | xsd:NMTOKENS | | Coordinates in GML compatible format |
| element | Precision | xsd:nonNegativeInteger | 0:1 | Precision for position measurement in meters |
| attribute | id | xsd:NMTOKEN | 0:1 | Identifier of the position |
| attribute | srsName | xsd:string | 0:1 | Identifier of the data reference system for geocodes (if Coordinates element is present) |

---

## MonitoredCountingStructure

> Data structure for describing counted values to be monitored.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | CountingType | CountingTypeEnumeration | 1:1 | Describes what is being counted. Values: `availabilityCount`, `reservedCount`, `inUseCount`, `outOfOrderCount`, `presentCount`, `chargingLevel`, `availableRunningDistance`, `currentStateCount` |
| element | CountedFeatureUnit | CountedFeatureUnitEnumeration | 0:1 | Unit of the type what is being counted. Values: `bays`, `seats`, `otherSpaces`, `devices`, `vehicles`, `persons`, `litres`, `squareMeters`, `cubicMeters`, `meters`, `kWh`, `mAh`, `kW`, `kg`, `A`, `C`, `other` |
| element | TypeOfCountedFeature | [TypeOfValueStructure](#typeofvaluestructure) | 0:1 | Refined classification of what is being counted |
| (choice) element | Count | xsd:integer | 1:1 | Counted value |
| | Percentage | xsd:decimal | | Value as a percentage (from 0.0 to 100.0) of the maximum possible value |
| element | Trend | CountingTrendEnumeration | 0:1 | Trend of the counting results. Values: `unknown`, `decreasing`, `increasing`, `stable`, `unstable`, `increasingQuickly`, `increasingSlowly`, `decreasingQuickly`, `decreasingSlowly` |
| element | Accuracy | xsd:decimal | 0:1 | Accuracy of the counting, as a percentage (from 0.0 to 100.0), the percentage being a +/- maximum deviation from the provided value |
| element | Description | NaturalLanguageStringStructure | 0:* | Description of what is being counted in natural language |
| element | CountedItemsIdList | [CountedItemsIdList](#counteditemsidlist) | 0:1 | List of the internal IDs of the counted items |

---

## MonitoringInformationStructure

> Data structure for describing the mechanism for monitoring a facility status.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | MonitoringInterval | xsd:duration | 0:1 | Frequency of the measurements |
| element | MonitoringType | MonitoringTypeEnumeration | 0:1 | Monitoring mechanism type. Values: `unknown`, `manual`, `automatic` |
| element | MonitoringPeriod | [MonitoringValidityConditionStructure](#monitoringvalidityconditionstructure) | 0:1 | When the monitoring is in effect. If not defined, default is 'always' |

---

## MonitoringValidityConditionStructure

> Data structure for describing the validity conditions.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | Period | [HalfOpenTimestampOutputRangeStructure](#halfopentimestampoutputrangestructure) | 0:* | Date and time range within which the condition is available |
| element | Timeband | HalfOpenTimeRangeStructure | 0:* | Monitoring period within a single day (monitoring may not be available at night, or may only occur at certain time of day for manual monitoring, etc.) |
| element | DayType | DaysOfWeekEnumeration | 0:* | Day type for the monitoring availability. Values: `unknown`, `monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday`, `sunday`, `mondayToFriday`, `mondayToSaturday`, `weekdays`, `weekends` |
| element | HolidayType | HolidayTypeEnumeration | 0:* | Holiday type for the monitoring availability. Values: `holiday`, `publicHoliday`, `religiousHoliday`, `federalHoliday`, `regionalHoliday`, `nationalHoliday`, `sundaysAndPublicHolidays`, `schoolDays`, `everyDay`, `undefinedDayType` |

---

## RemedyStructure

> Data structure with the information regarding remedy actions.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | RemedyType | RemedyTypeEnumeration | 0:1 | Type of the remedy action. Values: `unknown`, `replace`, `repair`, `remove`, `otherRoute`, `otherLocation` |
| element | Description | NaturalLanguageStringStructure | 0:* | Description(s) of the set up remedy in natural language |
| element | RemedyPeriod | [HalfOpenTimestampOutputRangeStructure](#halfopentimestampoutputrangestructure) | 0:1 | Duration (timeframe) of the remedy |

---

## SituationRefStructure

> Reference to a related [SIRI-SX](../SIRI-SX/Description_SIRI-SX.md) situation.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | SituationSimpleRef | xsd:string | 0:1 | Reference to a previously published situation identifier in [SIRI-SX](../SIRI-SX/Description_SIRI-SX.md) |
| element | SituationFullRef | [SituationFullRefStructure](#situationfullrefstructure) | 0:1 | Full reference to a situation |

---

## SituationFullRefStructure

> Full reference to a related [SIRI-SX](../SIRI-SX/Description_SIRI-SX.md) situation.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | VersionCountryRef | xsd:NMTOKEN | 0:1 | Unique identifier of a country (two-letter NPTG country code), provides namespace for participant |
| element | ParticipantRef | xsd:NMTOKEN | 1:1 | Unique identifier of participant, provides namespace for situation |
| element | SituationNumber | xsd:anyURI | 1:1 | Identifier of a situation within a participant |

---

## AccessibilityAssessmentStructure

> Data structure for describing the accessibility characteristics of a facility as defined by ACSB.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | MobilityImpairedAccess | xsd:boolean | 1:1 | Summary indication whether the facility is considered to be accessible or not |
| element | Limitations | [Limitations](#limitations) | 0:1 | The limitations that apply to the facility |
| element | Suitabilities | [Suitabilities](#suitabilities) | 0:1 | The suitabilities of the facility to meet specific user needs |

---

## AccessibilityLimitationStructure

> Data structure for an accessibility limitation.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | LimitationId | xsd:NMTOKEN | 0:1 | Identifier of the limitation |
| element | ValidityCondition | [ValidityConditionStructure](#validityconditionstructure) | 0:1 | Validity condition governing the applicability of the limitation |
| element | WheelchairAccess | AccessibilityEnumeration | 1:1 | Whether the facility is wheelchair accessible. Values: `unknown`, `false`, `true` |
| element | StepFreeAccess | AccessibilityEnumeration | 0:1 | Whether the facility has step free access. Values: `unknown`, `false`, `true` |
| element | EscalatorFreeAccess | AccessibilityEnumeration | 0:1 | Whether the facility has escalator free access. Values: `unknown`, `false`, `true` |
| element | LiftFreeAccess | AccessibilityEnumeration | 0:1 | Whether the facility has lift free access. Values: `unknown`, `false`, `true` |
| element | AudibleSignalsAvailable | AccessibilityEnumeration | 0:1 | Whether the facility has audible signals available. Values: `unknown`, `false`, `true` |
| element | VisualSignsAvailable | AccessibilityEnumeration | 0:1 | Whether the facility has visual signals available. Values: `unknown`, `false`, `true` |

---

## SuitabilityStructure

> Data structure for an accessibility suitability.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | Suitable | SuitabilityEnumeration | 1:1 | Whether the facility is suitable. Values: `suitable`, `notSuitable` |
| element | UserNeed | UserNeedStructure | 1:1 | User need for which the suitability is specified |

---

## ValidityConditionStructure

> Data structure for a validity condition.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | FromDateTime | xsd:dateTime | 0:1 | Start date and time (inclusive) |
| element | ToDateTime | xsd:dateTime | 0:1 | End date and time (inclusive) |
| element | DayType | xsd:NMTOKEN | 0:1 | Day type for which the timebands apply. Default is all day types |
| element | Timebands | [TimebandStructure](#timebandstructure) | 0:* | Any timebands which further qualify the validity condition |

---

## TimebandStructure

> Data structure for a timeband.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | StartTime | xsd:dateTime | 1:1 | Start time (inclusive) |
| element | EndTime | xsd:dateTime | 0:1 | End time (inclusive) |

---

## HalfOpenTimestampInputRangeStructure

> Type for a range of date times.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | StartTime | xsd:dateTime | 1:1 | Start time for the period (inclusive) |
| element | EndTime | xsd:dateTime | 0:1 | End time for the period (inclusive) |
| element | EndTimePrecision | EndTimePrecisionEnumeration | 0:1 | Precision with which to interpret the inclusive end time. Default is to the second. Values: `day`, `hour`, `second`, `milliSecond` |

---

## HalfOpenTimestampOutputRangeStructure

> Type for a range of date times.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | StartTime | xsd:dateTime | 1:1 | Start time for the period (inclusive) |
| element | EndTime | xsd:dateTime | 0:1 | End time for the period (inclusive) |
| element | EndTimeStatus | EndTimeStatusEnumeration | 0:1 | If end time is not provided, whether to interpret range as long term, short term or unknown length of situation. Default is undefined. Values: `undefined`, `longTerm`, `shortTerm` |

---

## TypeOfValueStructure

> Data structure for a type of value (used for classification of value types).

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | TypeOfValueCode | xsd:NMTOKEN | 1:1 | Identifier of the type of value |
| element | NameOfClass | xsd:string | 1:1 | Name of class of which this entity is an instance |
| element | Name | NaturalLanguageStringStructure | 0:1 | Name of the type of value |
| element | ShortName | NaturalLanguageStringStructure | 0:1 | Short name of the type of value |
| element | Description | NaturalLanguageStringStructure | 0:1 | Description of the type of value |
| element | Image | xsd:anyURI | 0:1 | Image of the type of value |
| element | Url | xsd:anyURI | 0:1 | URL of the type of value |
| element | PrivateCode | xsd:normalizedString | 0:1 | Private code of the type of value |

---

## Features

> Data structure for facility features.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | Feature | [AllFacilitiesFeatureStructure](#allfacilitiesfeaturestructure) | 1:* | Descriptions of the features of the facility |

---

## AllFacilitiesFeatureStructure

> Data structure for a facility feature. One of the feature category elements must be chosen.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| (choice) element | AccessFacility | AccessFacilityEnumeration | 1:1 | Access related feature. Values: `unknown`, `lift`, `escalator`, `travelator`, `ramp`, `stairs`, `shuttle`, `narrowEntrance`, `barrier`, `palletAccess_lowFloor`, `validator` |
| | AccommodationFacility | AccommodationFacilityEnumeration | | Accommodation related feature. Values: `unknown`, `sleeper`, `couchette`, `specialSeating`, `freeSeating`, `recliningSeats`, `babyCompartment`, `familyCarriage` |
| | AssistanceFacility | AssistanceFacilityEnumeration | | Assistance related feature. Values: `unknown`, `police`, `firstAid`, `sosPoint`, `specificAssistance`, `unaccompaniedMinorAssistance`, `boardingAssistance` |
| | FareClassFacility | FareClassFacilityEnumeration | | Fare class related feature. Values: `unknown`, `firstClass`, `secondClass`, `thirdClass`, `economyClass`, `businessClass` |
| | HireFacility | HireFacilityEnumeration | | Hiring related feature. Values: `unknown`, `carHire`, `motorCycleHire`, `cycleHire`, `taxi`, `recreationDeviceHire` |
| | LuggageFacility | LuggageFacilityEnumeration | | Luggage related feature. Values: `unknown`, `bikeCarriage`, `baggageStorage`, `leftLuggage`, `porterage`, `baggageTrolleys` |
| | MobilityFacility | MobilityFacilityEnumeration | | Mobility related feature. Values: `unknown`, `suitableForWheelChairs`, `lowFloor`, `boardingAssistance`, `stepFreeAccess`, `tactilePlatformEdges`, `onboardAssistance`, `unaccompaniedMinorAssistance`, `audioInformation`, `visualInformation`, `displaysForVisuallyImpaired`, `audioForHearingImpaired` |
| | NuisanceFacility | NuisanceFacilityEnumeration | | Nuisance related feature. Values: `unknown`, `smoking`, `noSmoking`, `mobilePhoneUseZone`, `mobilePhoneFreeZone` |
| | ParkingFacility | ParkingFacilityEnumeration | | Parking related feature. Values: `unknown`, `carPark`, `parkAndRidePark`, `motorcyclePark`, `cyclePark`, `rentalCarPark`, `coachPark` |
| | PassengerCommsFacility | PassengerCommsFacilityEnumeration | | Passenger communications related feature. Values: `unknown`, `faccomms_1`, `passengerWifi`, `telephone`, `audioServices`, `videoServices`, `businessServices`, `internet`, `postoffice`, `letterbox` |
| | PassengerInformationFacility | PassengerInformationFacilityEnumeration | | Passenger information related feature. Values: `unknown`, `nextStopIndicator`, `stopAnnouncements`, `passengerInformationDisplay`, `audioInformation`, `visualInformation`, `tactilePlatformEdges`, `tactileInformation`, `walkingGuidance`, `journeyPlanning`, `lostFound`, `informationDesk`, `interactiveKioskDisplay`, `printedPublicNotice` |
| | RefreshmentFacility | RefreshmentFacilityEnumeration | | Refreshment related feature. Values: `unknown`, `restaurantService`, `snacksService`, `trolley`, `bar`, `foodNotAvailable`, `beveragesNotAvailable`, `bistro`, `foodVendingMachine`, `beverageVendingMachine` |
| | ReservedSpaceFacility | ReservedSpaceFacilityEnumeration | | Reserved space related feature. Values: `unknown`, `lounge`, `hall`, `meetingpoint`, `groupPoint`, `reception`, `shelter`, `seats` |
| | RetailFacility | RetailFacilityEnumeration | | Retail related feature. Values: `unknown`, `food`, `newspaperTobacco`, `recreationTravel`, `hygieneHealthBeauty`, `fashionAccessories`, `bankFinanceInsurance`, `cashMachine`, `currencyExchange`, `tourismService`, `photoBooth` |
| | SanitaryFacility | SanitaryFacilityEnumeration | | Sanitary related feature. Values: `unknown`, `toilet`, `noToilet`, `shower`, `wheelchairAccessToilet`, `babyChange` |
| | TicketingFacility | TicketingFacilityEnumeration | | Ticketing related feature. Values: `unknown`, `ticketMachines`, `ticketOffice`, `ticketOnDemandMachines`, `ticketSales`, `mobileTicketing`, `ticketCollection`, `centralReservations`, `localTickets`, `nationalTickets`, `internationalTickets` |

---

## Limitations

> Data structure for accessibility limitations.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | Limitation | [AccessibilityLimitationStructure](#accessibilitylimitationstructure) | 1:* | The accessibility limitations |

---

## Suitabilities

> Data structure for accessibility suitabilities.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | Suitability | [SuitabilityStructure](#suitabilitystructure) | 1:* | The accessibility suitabilities to meet a specific passenger need |

---

## CountedItemsIdList

> Data structure for a list of item identifiers.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | ItemId | xsd:NMTOKEN | 1:* | Identifier of the item |
