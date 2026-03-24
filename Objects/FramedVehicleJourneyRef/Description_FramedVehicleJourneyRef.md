# FramedVehicleJourneyRef

## 1. Purpose

FramedVehicleJourneyRef is a reference structure that identifies a VehicleJourney on a specific date. It combines a date frame (`DataFrameRef`) with a journey reference (`DatedVehicleJourneyRef`), ensuring that journeys with the same ID but on different dates can be distinguished.

This is the primary mechanism for linking SIRI real-time data to planned NeTEx timetable data.

---

## 2. Structure Overview

```
📁 FramedVehicleJourneyRef
├── 📄 DataFrameRef (1..1)
└── 🔗 DatedVehicleJourneyRef (1..1)
```

---

## 3. Key Elements

- **DataFrameRef** — The operating date in ISO format (YYYY-MM-DD), in local time
- **DatedVehicleJourneyRef** — The ServiceJourney ID matching the corresponding object in NeTEx

---

## 4. References

- [EstimatedVehicleJourney](../EstimatedVehicleJourney/Description_EstimatedVehicleJourney.md) — Used in SIRI-ET
- [MonitoredVehicleJourney](../MonitoredVehicleJourney/Description_MonitoredVehicleJourney.md) — Used in SIRI-VM
- [Affects](../Affects/Description_Affects.md) — Used in SIRI-SX AffectedVehicleJourney

---

## 5. Usage Notes

> [!WARNING]
> - **DataFrameRef** must be the operating date, not the calendar date (operating days may differ from calendar days)
> - **DatedVehicleJourneyRef** must match the ID of the corresponding VehicleJourney in NeTEx exactly
> - In SIRI-VM, either `FramedVehicleJourneyRef` or the separate `VehicleJourneyRef` must be set (not both)

> [!TIP]
> The `FramedVehicleJourneyRef` approach is preferred over `DatedVehicleJourneyRef` alone because it explicitly includes the date, making it unambiguous for journeys that cross midnight or operate on different days with the same ID.
