# PtSituationElement

## 1. Purpose

PtSituationElement is the core data object in SIRI-SX. It represents a single situation (planned or unplanned disruption) that affects public transport services. Each element contains structured information about what is affected, the severity, textual descriptions, and validity periods.

---

## 2. Structure Overview

```
📁 PtSituationElement
├── 📄 CreationTime (1..1)
├── 📄 ParticipantRef (1..1)
├── 📄 SituationNumber (1..1)
├── 📄 Version (0..1)
├── 📁 Source (1..1)
│   └── 📄 SourceType (1..1) — always "directReport"
├── 📄 VersionedAtTime (0..1)
├── 📄 Progress (1..1) — open | closed
├── 📁 ValidityPeriod (1..n)
│   ├── 📄 StartTime (1..1)
│   └── 📄 EndTime (0..1)
├── 📄 UndefinedReason (1..1) — always empty
├── 📄 Severity (0..1)
├── 📄 Priority (0..1)
├── 📄 ReportType (1..1) — general | incident
├── 📄 Planned (0..1)
├── 📄 Summary (1..n)
├── 📄 Description (0..n)
├── 📄 Advice (0..n)
├── 📁 InfoLinks (0..1)
│   └── 📁 InfoLink (1..1)
└── 📁 Affects (1..1)
    ├── 📁 Networks → AffectedNetwork
    ├── 📁 StopPlaces → AffectedStopPlace
    ├── 📁 StopPoints → AffectedStopPoint
    └── 📁 VehicleJourneys → AffectedVehicleJourney
```

---

## 3. Key Elements

- **SituationNumber** — Unique ID in format `CODESPACE:SituationNumber:ID` (e.g. `ABC:SituationNumber:123`)
- **Progress** — `open` (active) or `closed` (resolved)
- **ReportType** — `general` (informational) or `incident` (impacts operation)
- **Summary** — Max 160 characters. One per language.
- **Affects** — Describes exactly what is impacted (networks, stops, journeys)

---

## 4. References

- [Affects](../Affects/Description_Affects.md) — What the situation impacts
- [SIRI-SX Service](../../Services/SIRI-SX/Description_SIRI-SX.md) — Full service description
- [FramedVehicleJourneyRef](../FramedVehicleJourneyRef/Description_FramedVehicleJourneyRef.md) — Used in AffectedVehicleJourney

---

## 5. Usage Notes

> [!WARNING]
> - **SituationNumber** must be unique and constant — updates to a situation reuse the same ID
> - **Summary** should be max 160 characters to keep messages readable
> - **Description** should not repeat information already in Summary or structured data
> - **Advice** is for actionable guidance to passengers, not a repeat of the description
> - When closing: `Progress=closed` requires `EndTime` ≥ 5 hours in the future
> - `UndefinedReason` is mandatory but always empty (`<UndefinedReason/>`)
