# SIRI-SX — Element Tables

## SituationExchangeDelivery

> A data type for the representation of one or more situations, or updates on previously published situations.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| attribute | version | xsd:NMTOKEN | 1:1 | Version ID for SituationExchangeDelivery |
| element | ResponseTimestamp | xsd:dateTime | 1:1 | Timestamp for when the dataset was created/published |
| element | Situations | PtSituationElement | 1:n | Data objects for Public Transport Situation Exchange |

---

## PtSituationElement

> A container element for situation data.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | CreationTime | xsd:dateTime | 1:1 | Timestamp for when the situation was created |
| element | ParticipantRef | ParticipantCode | 1:1 | Codespace of the data source |
| element | SituationNumber | xsd:anyURI | 1:1 | Unique situation ID. Format: `CODESPACE:SituationNumber:ID` |
| element | Version | xsd:integer | 0:1 | Version number for the message |
| element | Source | SituationSource | 1:1 | Information on the source of the message |
| element | VersionedAtTime | xsd:dateTime | 0:1 | Timestamp when the situation was updated |
| element | Progress | WorkflowStatusEnumeration | 1:1 | Status: `open` or `closed` |
| element | ValidityPeriod | HalfOpenTimestampRangeStructure | 1:n | Validity period(s). All but last must have EndTime. |
| element | UndefinedReason | Reason | 1:1 | Always `<UndefinedReason/>`. Mandatory but not used. |
| element | Severity | SeverityEnumeration | 0:1 | Values: `noImpact`, `verySlight`, `slight`, `normal` (default), `severe`, `verySevere` |
| element | Priority | xsd:nonNegativeInteger | 0:1 | 1–10. 1 = highest priority ("extremelyUrgent"). Blank = "normal urgency". |
| element | ReportType | ReportTypeEnumeration | 1:1 | `general` (information only) or `incident` (impacts operation) |
| element | Planned | xsd:boolean | 0:1 | Whether the situation is due to planned events |
| element | Summary | NaturalLanguageStringStructure | 1:n | Max 160 characters. One per language. Can be 0 when `Progress=closed` |
| element | Description | NaturalLanguageStringStructure | 0:n | Expanded description. Do not repeat Summary. |
| element | Advice | NaturalLanguageStringStructure | 0:n | Advice on how passengers should respond |
| element | InfoLinks | InfoLinks | 0:1 | Links to further information |
| element | Affects | Affects | 1:1 | What the situation affects. Can be empty when `Progress=closed` |

---

## SituationSource

> Information on the source of the message.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | SourceType | SourceType | 1:1 | Always `directReport`. Required but not used. |

---

## HalfOpenTimestampRangeStructure

> Period can be open- or closed-ended.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | StartTime | xsd:dateTime | 1:1 | Start time for the period |
| element | EndTime | xsd:dateTime | 0:1 | End time for the period |

---

## InfoLinks

> Collection of information links.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | InfoLink | InfoLink | 1:1 | Link to further information |

---

## InfoLink

> Link to a website with further information on the situation.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | Uri | xsd:anyURI | 1:1 | URL to further information |
| element | Label | NaturalLanguageStringStructure | 0:1 | Label for the link |

---

## Affects

> Description of what the situation affects.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| (choice) | Networks | AffectedNetwork | 1:n | Network with operators and lines affected. Can be 0 when `Progress=closed` |
| | StopPlaces | AffectedStopPlace | | Stops affected by the situation |
| | StopPoints | AffectedStopPoint | | Stops with relevance criteria |
| | VehicleJourneys | AffectedVehicleJourney | | Trips affected by the situation |

---

## AffectedNetwork

> References to affected Network element(s).

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | AffectedOperator | AffectedOperatorStructure | 0:1 | Reference to affected operator |
| element | NetworkRef | xsd:NMTOKEN | 1:1 | Reference to affected Network |
| element | VehicleMode | VehicleModesOfTransportEnumeration | 0:1 | Affected modality. Must include Submode when applicable. |
| (choice) | AirSubmode | AirSubmodesEnumeration | 0:1 | `domesticFlight`, `helicopterService`, `internationalFlight` |
| | BusSubmode | BusSubmodesEnumeration | | `airportLinkBus`, `expressBus`, `localBusService`, `nightBus`, `railReplacementBus`, `regionalBus`, `schoolBus`, `shuttleBus`, `sightseeingBus` |
| | CoachSubmode | CoachSubmodesEnumeration | | `internationalCoachService`, `nationalCoachService`, `touristCoachService` |
| | MetroSubmode | MetroSubmodesEnumeration | | `metro`, `urbanRailway` |
| | RailSubmode | RailSubmodesEnumeration | | `interRegionalRailService`, `local`, `longDistanceTrain`, `sleeperRailService`, `regionalRail`, `specialTrainService`, `touristRailway` |
| | TramSubmode | TramSubmodesEnumeration | | `localTramService` |
| | WaterSubmode | WaterSubmodesEnumeration | | `highSpeedPassengerService`, `highSpeedVehicleService`, `internationalCarFerryService`, `internationalPassengerFerry`, `localCarFerryService`, `localPassengerFerry`, `nationalCarFerryService`, `sightseeingService` |
| (choice) | AffectedLine | AffectedLineStructure | 1:n | Reference to affected line(s) |
| | AllLines | xsd:string (empty) | 1:1 | All lines affected |

---

## AffectedOperatorStructure

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | OperatorRef | xsd:NMTOKEN | 1:1 | Reference to an affected operator |

---

## AffectedLineStructure

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | LineRef | xsd:NMTOKEN | 1:1 | Reference to Line (NeTEx ID) |
| element | Routes | AffectedRoute | 0:n | Affected routes, when not the entire Line |
| element | Sections | AffectedSection | 0:n | Affected sections |

---

## AffectedRouteStructure

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | RouteRef | xsd:NMTOKEN | 0:1 | Reference to Route (NeTEx ID) |
| (choice) | StopPoints | AffectedStopPoint | 0:n | Affected stops in the route |
| | Sections | AffectedSection | 0:n | Affected sections |

---

## AffectedStopPoint

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | StopPointRef | xsd:NMTOKEN | 1:1 | Reference to Quay (NSR ID). May use StopPlace ID if quay is unknown. |
| element | StopPointName | NaturalLanguageStringStructure | 0:1 | Name (optional, for readability) |
| element | StopCondition | RoutePointTypeEnumeration | 0:n | `exceptionalStop`, `destination`, `notStopping`, `requestStop`, `startPoint`, `stop` (default) |

---

## AffectedStopPlace

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | AccessibilityAssessment | AccessibilityAssessment | 0:1 | Changed availability for users with special needs |
| element | StopPlaceRef | xsd:NMTOKEN | 1:1 | Reference to StopPlace or Quay (NSR ID) |
| element | PlaceName | NaturalLanguageStringStructure | 0:1 | Name (optional, for readability) |
| element | AffectedComponents | AffectedComponent | 0:n | Which parts of the stop are affected |

---

## AccessibilityAssessment

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | MobilityImpairedAccess | xsd:boolean | 1:1 | Whether still available for users with special needs |
| element | Limitations | AccessibilityLimitation | 1:1 | Specific limitations |

---

## AccessibilityLimitation

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | WheelchairAccess | AccessibilityEnumeration | 1:1 | `true`, `false`, `unknown` |
| element | StepFreeAccess | AccessibilityEnumeration | 1:1 | `true`, `false`, `unknown` |
| element | EscalatorFreeAccess | AccessibilityEnumeration | 1:1 | `true`, `false`, `unknown` |
| element | LiftFreeAccess | AccessibilityEnumeration | 1:1 | `true`, `false`, `unknown` |

---

## AffectedComponent

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | ComponentRef | xsd:NMTOKEN | 0:1 | Reference to Quay (NSR ID). Used when ComponentType is `quay` |
| element | ComponentType | StopPlaceComponentTypeEnumeration | 1:1 | `accessSpace`, `boardingPosition`, `entrance`, `quay` |
| element | AccessFeatureType | AccessibilityFeatureEnumeration | 0:1 | `escalator`, `lift`, `narrowEntrance`, `ramp`, `stairs` |

---

## AffectedVehicleJourney

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| (choice) | VehicleJourneyRef | xsd:NMTOKEN | 1:1 | Reference to affected VehicleJourney |
| | DatedVehicleJourneyRef | xsd:NMTOKEN | | Reference to affected DatedVehicleJourney |
| | FramedVehicleJourneyRef | FramedVehicleJourneyRefStructure | | Reference with date |
| element | Operator | AffectedOperatorStructure | 0:1 | Affected operator (optional, for readability) |
| element | LineRef | xsd:NMTOKEN | 0:1 | Affected line (optional, for readability) |
| element | Route | AffectedRouteStructure | 1:n | Affected routes. Mandatory but can be blank if entire journey affected. |
| element | OriginAimedDepartureTime | xsd:dateTime | 0:1 | Originally planned departure from first stop |
