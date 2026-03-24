# Affects

## 1. Purpose

Affects is the structure within a PtSituationElement that describes **what** is impacted by a situation. It provides a choice of four target types: networks (lines/operators), stop places, stop points (with conditions), and vehicle journeys.

---

## 2. Structure Overview

```
📁 Affects
├── (choice) one or more of:
│   ├── 📁 Networks (1..n)
│   │   └── 📁 AffectedNetwork
│   │       ├── 📁 AffectedOperator (0..1)
│   │       ├── 🔗 NetworkRef (1..1)
│   │       ├── 📄 VehicleMode + Submode (0..1)
│   │       └── (choice):
│   │           ├── 📁 AffectedLine (1..n)
│   │           └── 📄 AllLines
│   ├── 📁 StopPlaces (1..n)
│   │   └── 📁 AffectedStopPlace
│   │       ├── 📁 AccessibilityAssessment (0..1)
│   │       ├── 🔗 StopPlaceRef (1..1)
│   │       └── 📁 AffectedComponents (0..n)
│   ├── 📁 StopPoints (1..n)
│   │   └── 📁 AffectedStopPoint
│   │       ├── 🔗 StopPointRef (1..1)
│   │       └── 📄 StopCondition (0..n)
│   └── 📁 VehicleJourneys (1..n)
│       └── 📁 AffectedVehicleJourney
│           ├── 🔗 VehicleJourneyRef (1..1) [choice]
│           ├── 📁 Route (1..n)
│           └── 📄 OriginAimedDepartureTime (0..1)
```

---

## 3. Key Elements

- **Networks** — Affect lines and operators within a network
- **StopPlaces** — Affect physical stop locations with accessibility information
- **StopPoints** — Affect logical stop points with boarding/alighting conditions
- **VehicleJourneys** — Affect specific trips with route details

---

## 4. References

- [PtSituationElement](../PtSituationElement/Description_PtSituationElement.md) — Parent container
- [SIRI-SX Service](../../Services/SIRI-SX/Description_SIRI-SX.md) — Full service description

---

## 5. Usage Notes

> [!WARNING]
> - **Affects** must have content unless `Progress=closed`
> - When using **AffectedNetwork**, either `AffectedLine` or `AllLines` must be specified
> - **StopCondition** defaults to `stop` (all interactions) if not specified
> - **AffectedVehicleJourney** requires `Route` even if blank (when entire journey affected)
