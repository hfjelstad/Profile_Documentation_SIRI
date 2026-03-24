# 📖 SIRI Glossary

## Core Concepts

| Term | Definition |
|------|-----------|
| **SIRI** | Service Interface for Real Time Information — a European CEN standard for exchanging real-time public transport data (CEN/TS 15531) |
| **NeTEx** | Network Timetable Exchange — the companion standard for planned/static public transport data (CEN/TS 16614) |
| **Transmodel** | The European reference model for public transport data (EN 12896). Both SIRI and NeTEx are based on Transmodel. |
| **Nordic SIRI Profile** | A localisation of SIRI 2.0 for the Nordic countries specifying which services and elements to use |
| **Codespace** | A namespace prefix that identifies the data owner (e.g. `NSB`, `RUT`, `NSR`) |

## Services

| Term | Definition |
|------|-----------|
| **SIRI-ET** | Estimated Timetable — continuous updates to planned timetable data within the current operating day |
| **SIRI-SX** | Situation Exchange — textual traffic situation messages about disruptions and deviations |
| **SIRI-VM** | Vehicle Monitoring — real-time vehicle positions and progress information |
| **ServiceDelivery** | The top-level container wrapping all SIRI data deliveries |

## SIRI-ET Terms

| Term | Definition |
|------|-----------|
| **EstimatedVehicleJourney** | A journey object containing real-time timetable updates for a single VehicleJourney |
| **EstimatedCall** | Estimated arrival/departure information for a stop not yet served |
| **RecordedCall** | Recorded arrival/departure information for an already-served stop |
| **EstimatedJourneyVersionFrame** | Container grouping one or more EstimatedVehicleJourneys with a timestamp |
| **ExtraJourney** | A replacement or additional departure not in the original timetable |
| **IsCompleteStopSequence** | Boolean confirming the message contains all stops in the journey |

## SIRI-SX Terms

| Term | Definition |
|------|-----------|
| **PtSituationElement** | A single situation (disruption/deviation) with structured impact data |
| **SituationNumber** | Unique identifier for a situation. Format: `CODESPACE:SituationNumber:ID` |
| **Progress** | Workflow status of a situation: `open` (active) or `closed` (resolved) |
| **ReportType** | Classification: `general` (informational) or `incident` (impacts operation) |
| **Affects** | Structure describing what is impacted: networks, stops, or journeys |
| **AffectedNetwork** | Reference to network, operator, and lines affected by a situation |
| **StopCondition** | Specifies which passengers a stop-level message applies to (boarding, alighting, etc.) |
| **ValidityPeriod** | Time range during which a situation is active |
| **Severity** | Impact level: `noImpact`, `verySlight`, `slight`, `normal`, `severe`, `verySevere` |

## SIRI-VM Terms

| Term | Definition |
|------|-----------|
| **VehicleActivity** | Container for a vehicle's monitoring data with timestamps and validity |
| **MonitoredVehicleJourney** | Real-time position, delay, and status data for a monitored vehicle journey |
| **VehicleLocation** | GPS coordinates (WGS84) of the vehicle |
| **ProgressBetweenStops** | How far the vehicle has progressed between the previous and next stop |
| **MonitoredCall** | Information about the current or most recent stop |
| **Delay** | ISO 8601 duration representing deviation from planned time (`PT0S` = on time) |
| **VehicleStatus** | Operational state: `assigned`, `atOrigin`, `inProgress`, `completed`, `offRoute`, `cancelled` |

## Data Exchange Terms

| Term | Definition |
|------|-----------|
| **Direct Delivery** | Publish/Subscribe — data continuously pushed to subscribers |
| **Fetched Delivery** | Publish/Subscribe — producer notifies, consumer fetches when ready |
| **Request/Response** | Synchronous — consumer explicitly requests data |
| **HeartbeatNotification** | Periodic signal confirming service availability |
| **FramedVehicleJourneyRef** | Reference combining a ServiceJourney ID with an operating date |
| **DataFrameRef** | The operating date (YYYY-MM-DD) used in FramedVehicleJourneyRef |

## General Terms

| Term | Definition |
|------|-----------|
| **Operating Day** | The day on which a service operates (may differ from calendar day) |
| **NSR** | National Stop place Registry — the authoritative source for stop IDs in Norway |
| **WGS84** | World Geodetic System 1984 — the standard coordinate reference system (EPSG:4326) |
| **Quay** | A platform or boarding area at a StopPlace |
| **StopPlace** | A physical location where passengers can board/alight (may contain multiple Quays) |
