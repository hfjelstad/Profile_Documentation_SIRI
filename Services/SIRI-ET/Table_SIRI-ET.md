# SIRI-ET — Element Tables

## EstimatedTimetableDelivery

> A data type for representing information about timetable changes for one or more VehicleJourneys on the same operating day.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| attribute | version | xsd:NMTOKEN | 1:1 | Version ID for EstimatedTimetableDelivery |
| element | ResponseTimestamp | xsd:dateTime | 1:1 | Timestamp for when the dataset was created/published |
| element | EstimatedJourneyVersionFrame | EstimatedJourneyVersionFrame | 1:n | Container for sending one or more Estimated Timetable with a timestamp |

---

## EstimatedJourneyVersionFrame

> Container element for returning an Estimated Timetable comprised of one or more EstimatedVehicleJourney.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | RecordedAtTime | xsd:dateTime | 1:1 | The time when the data object was created/published |
| element | EstimatedVehicleJourney | EstimatedVehicleJourney | 1:n | Object for Estimated Timetable dataset |

---

## EstimatedVehicleJourney

> Continuously updated timetable data with changes in the current operating day for a VehicleJourney and its estimated arrival times at stops.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | RecordedAtTime | xsd:dateTime | 1:1 | The time when this individual journey was recorded |
| element | LineRef | xsd:NMTOKEN | 1:1 | Reference to the Line (ID to corresponding NeTEx object) |
| element | DirectionRef | xsd:NMTOKEN | 1:1 | Direction reference. Mandatory but not used as a free standing data type; set to `0` if not used |
| (choice) | DatedVehicleJourneyRef | xsd:NMTOKEN | 1:1 | Reference to DatedServiceJourney-ID |
| | FramedVehicleJourneyRef | FramedVehicleJourneyRefStructure | | Reference with date to VehicleJourney |
| | EstimatedVehicleJourneyCode | xsd:NMTOKEN | | New codespace-unique ID for replacement departures |
| (choice) | ExtraJourney | xsd:boolean | 0:1 | `true` if this is a replacement departure |
| | Cancellation | xsd:boolean | | `true` only if the **entire** VehicleJourney is cancelled |
| element | JourneyPatternRef | xsd:NMTOKEN | 0:1 | Reference to JourneyPattern (NeTEx ID) |
| element | VehicleMode | VehicleModesEnumeration | 0:1 | Transport type. **Mandatory for replacement departures.** Values: `air`, `bus`, `coach`, `ferry`, `metro`, `rail`, `tram`, `taxi` |
| element | RouteRef | xsd:NMTOKEN | 0:1 | Reference to Route. **Mandatory for replacement departures.** |
| element | PublishedLineName | NaturalLanguageStringStructure | 0:1 | Public line name. Only for replacement departures with new LineRef |
| element | GroupOfLinesRef | xsd:NMTOKEN | 0:1 | Reference to Network/GroupOfLines. **Mandatory for replacement departures.** |
| element | ExternalLineRef | xsd:NMTOKEN | 0:1 | Reference to Line being replaced. **Required for replacement departures.** |
| element | OriginName | NaturalLanguageStringStructure | 0:1 | Name of first stop (optional, for readability) |
| element | DestinationName | NaturalLanguageStringStructure | 0:1 | Name of last stop (optional, for readability) |
| element | OperatorRef | xsd:NMTOKEN | 0:1 | Reference to Operator. **Mandatory for replacement departures with changed operator.** |
| element | PublicContact | SimpleContactStructure | 0:1 | Public contact point (if different from planned data) |
| element | OperationsContact | SimpleContactStructure | 0:1 | Administrative contact details |
| element | SituationRef | SituationRefStructure | 0:n | Reference to related SIRI-SX situation(s) |
| element | Monitored | xsd:boolean | 0:1 | Whether the vehicle is currently reporting real-time data |
| element | PredictionInaccurate | xsd:boolean | 0:1 | Whether time estimates are uncertain (traffic jams etc.) |
| element | DataSource | xsd:string | 1:1 | Codespace of the data source |
| element | Occupancy | OccupancyEnumeration | 0:1 | Seat availability. Values: `unknown`, `manySeatsAvailable`, `fewSeatsAvailable`, `standingAvailable`, `full`, `notAcceptingPassengers` |
| element | BlockRef | xsd:NMTOKEN | 0:1 | Reference to block (internal, non-public) |
| element | VehicleJourneyRef | xsd:NMTOKEN | 0:1 | Reference to replaced VehicleJourney. **Only for unplanned replacement departures.** |
| element | AdditionalVehicleJourneyRef | FramedVehicleJourneyRefStructure | 0:n | Reference to other affected VehicleJourneys |
| element | RecordedCalls | RecordedCall | 0:1 | Full sequence of already served stops (chronological order) |
| element | EstimatedCalls | EstimatedCall | 0:1 | Full sequence of affected stops (chronological order) |
| element | IsCompleteStopSequence | xsd:boolean | 1:1 | Must always be `true` |
| element | JourneyRelations | JourneyRelation | 0:1 | Relations with other journeys (joining/splitting etc.) |

---

## SimpleContactStructure

> Contact details to be presented to the public when planned timetable information is no longer valid.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | PhoneNumber | xsd:string | 0:1 | Phone number |
| element | Url | xsd:anyURI | 0:1 | URL |

---

## SituationRefStructure

> Reference to a related Situation Element in an existing SIRI-SX message.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | SituationSimpleRef | xsd:string | 1:1 | Unique reference to SituationNumber for a published PtSituationElement |
