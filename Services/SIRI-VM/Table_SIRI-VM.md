# SIRI-VM — Element Tables

## VehicleMonitoringDelivery

> A data type for representing vehicle monitoring for one or more VehicleJourneys.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| attribute | version | xsd:NMTOKEN | 1:1 | Version ID for VehicleMonitoringDelivery |
| element | ResponseTimestamp | xsd:dateTime | 1:1 | Timestamp for when the dataset was created/published |
| element | VehicleActivity | VehicleActivity | 1:n | Container for one or more VehicleActivity |

---

## VehicleActivity

> Container element for returning one or more VehicleActivity.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | RecordedAtTime | xsd:dateTime | 1:1 | Timestamp when position/status was recorded |
| element | ValidUntilTime | xsd:dateTime | 1:1 | Validity expiration of the dataset |
| element | ProgressBetweenStops | ProgressBetweenStops | 0:1 | Progress along current ServiceLink |
| element | MonitoredVehicleJourney | MonitoredVehicleJourney | 1:1 | Real-time monitored VehicleJourney data |

---

## ProgressBetweenStops

> Progress of the vehicle between the previous stop and the next ScheduledStopPoint.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | LinkDistance | xsd:decimal | 0:1 | Distance in meters between previous and next stop |
| element | Percentage | xsd:decimal | 1:1 | Percentage of total distance traversed |

---

## MonitoredVehicleJourney

> Data object describing a real-time monitored VehicleJourney with supplementary location data.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | LineRef | xsd:NMTOKEN | 1:1 | Reference to Line (NeTEx ID) |
| element | DirectionRef | xsd:NMTOKEN | 0:1 | Direction reference |
| element | FramedVehicleJourneyRef | FramedVehicleJourneyRefStructure | 0:1 | Reference with date. **Either this or VehicleJourneyRef must be set.** |
| element | VehicleMode | VehicleModesEnumeration | 0:1 | Transport type |
| element | OperatorRef | xsd:NMTOKEN | 0:1 | Reference to Operator (NeTEx ID) |
| element | OriginRef | xsd:NMTOKEN | 0:1 | Reference to origin Quay (NSR ID) |
| element | OriginName | NaturalLanguagePlaceNameStructure | 0:1 | Name of origin |
| element | DestinationRef | xsd:NMTOKEN | 0:1 | Reference to destination Quay (NSR ID) |
| element | DestinationName | NaturalLanguagePlaceNameStructure | 0:1 | Name of destination |
| element | Monitored | xsd:boolean | 0:1 | Whether vehicle is reporting real-time data |
| element | DataSource | xsd:string | 1:1 | Codespace of the data source |
| element | VehicleLocation | Location | 1:1 | Geospatial position of the vehicle |
| element | Bearing | xsd:float | 0:1 | Current compass bearing |
| element | Velocity | xsd:nonNegativeInteger | 0:1 | Vehicle speed (actual or average) |
| element | Occupancy | OccupancyEnumeration | 0:1 | Seat availability status |
| element | Delay | xsd:duration | 1:1 | Delay time. `PT0S` = no delay |
| element | InCongestion | xsd:boolean | 0:1 | Whether affected by traffic jams |
| element | VehicleStatus | VehicleStatusEnumeration | 0:1 | `assigned`, `atOrigin`, `cancelled`, `completed`, `inProgress`, `offRoute` |
| element | VehicleJourneyRef | VehicleJourneyRefStructure | 0:1 | Reference to DatedServiceJourney. **Either this or FramedVehicleJourneyRef must be set.** |
| element | VehicleRef | xsd:NMTOKEN | 1:1 | Reference to the vehicle (NeTEx ID) |
| element | MonitoredCall | MonitoredCallStructure | 0:1 | Information on the current/most recent stop |
| element | IsCompleteStopSequence | xsd:boolean | 1:1 | Always `false` when only MonitoredCall is included |

---

## Location

> Specifies location as a geospatial point.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| attribute | srsName | xsd:string | 0:1 | Reference system. Use WGS84 (e.g. "EPSG:4326") |
| (choice) | Longitude | xsd:decimal | 1:1 | Longitude (-180 to 180) |
| | Latitude | xsd:decimal | | Latitude (-90 to 90) |
| | Coordinates | xsd:NMTOKENS | | GML coordinate format |

---

## MonitoredCallStructure

> Information about the current stop for the VehicleJourney.

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | StopPointRef | xsd:NMTOKEN | 1:1 | Reference to Quay (NSR ID) |
| element | StopPointName | NaturalLanguageStringStructure | 0:1 | Name of stop (optional, for readability) |
| element | VehicleAtStop | xsd:boolean | 0:1 | Whether the vehicle is at the stop |
| element | VehicleLocationAtStop | Location | 0:1 | Where the vehicle is at the stop (for significant deviations) |
