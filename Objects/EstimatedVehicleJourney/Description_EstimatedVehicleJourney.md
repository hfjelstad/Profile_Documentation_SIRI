# EstimatedVehicleJourney

## 1. Purpose

EstimatedVehicleJourney is the core data object in SIRI-ET. It represents continuously updated timetable data for a single VehicleJourney within the current operating day, including its estimated arrival and departure times at stops.

Each EstimatedVehicleJourney references a planned journey from NeTEx and provides the real-time deviations from the plan.

---

## 2. Structure Overview

```
📁 EstimatedVehicleJourney
├── 📄 RecordedAtTime (1..1)
├── 🔗 LineRef (1..1)
├── 📄 DirectionRef (1..1)
├── (choice) Journey reference:
│   ├── 🔗 DatedVehicleJourneyRef (1..1)
│   ├── 🔗 FramedVehicleJourneyRef (1..1)
│   └── 📄 EstimatedVehicleJourneyCode (1..1)
├── (choice) Status:
│   ├── 📄 ExtraJourney (0..1)
│   └── 📄 Cancellation (0..1)
├── 🔗 JourneyPatternRef (0..1)
├── 📄 VehicleMode (0..1)
├── 🔗 RouteRef (0..1)
├── 📄 PublishedLineName (0..1)
├── 🔗 GroupOfLinesRef (0..1)
├── 🔗 ExternalLineRef (0..1)
├── 📄 OriginName (0..1)
├── 📄 DestinationName (0..1)
├── 🔗 OperatorRef (0..1)
├── 📁 PublicContact (0..1)
├── 📁 OperationsContact (0..1)
├── 🔗 SituationRef (0..n)
├── 📄 Monitored (0..1)
├── 📄 PredictionInaccurate (0..1)
├── 📄 DataSource (1..1)
├── 📄 Occupancy (0..1)
├── 🔗 BlockRef (0..1)
├── 🔗 VehicleJourneyRef (0..1)
├── 🔗 AdditionalVehicleJourneyRef (0..n)
├── 📁 RecordedCalls (0..1)
│   └── 📁 RecordedCall (1..n)
├── 📁 EstimatedCalls (0..1)
│   └── 📁 EstimatedCall (1..n)
├── 📄 IsCompleteStopSequence (1..1) — always true
└── 📁 JourneyRelations (0..1)
```

---

## 3. Key Elements

- **LineRef** — Reference to the NeTEx Line this journey operates on
- **FramedVehicleJourneyRef** — The primary way to reference the planned journey (ServiceJourney + Date)
- **Cancellation** — Set to `true` only when the **entire** journey is cancelled
- **DataSource** — Codespace identifying the data source
- **IsCompleteStopSequence** — Must always be `true`

---

## 4. References

- [Line](https://github.com/hfjelstad/Profile_Documentation_v2/blob/main/Objects/Line/Description_Line.md) — Planned line in NeTEx
- [FramedVehicleJourneyRef](../FramedVehicleJourneyRef/Description_FramedVehicleJourneyRef.md) — Journey reference structure
- [EstimatedCall](../EstimatedCall/Description_EstimatedCall.md) — Per-stop estimated data
- [RecordedCall](../RecordedCall/Description_RecordedCall.md) — Per-stop recorded data
- [SIRI-ET Service](../../Services/SIRI-ET/Description_SIRI-ET.md) — Full service description

---

## 5. Usage Notes

> [!WARNING]
> - **IsCompleteStopSequence** must always be `true` — the message must contain **all** stops
> - For **replacement departures**: `VehicleMode`, `RouteRef`, `GroupOfLinesRef`, and `ExternalLineRef` become mandatory
> - **Cancellation** at journey level means the **whole** journey is cancelled. For partial cancellations, use `Cancellation` on individual EstimatedCalls
> - **DirectionRef** is mandatory but not used — set to `0` if no direction information is available
