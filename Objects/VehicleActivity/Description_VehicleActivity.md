# VehicleActivity

## 1. Purpose

VehicleActivity is the container element in SIRI-VM that wraps a single vehicle's monitoring data with timestamps. Each VehicleActivity includes exactly one MonitoredVehicleJourney and optional progress information.

---

## 2. Structure Overview

```
📁 VehicleActivity
├── 📄 RecordedAtTime (1..1)
├── 📄 ValidUntilTime (1..1)
├── 📁 ProgressBetweenStops (0..1)
│   ├── 📄 LinkDistance (0..1)
│   └── 📄 Percentage (1..1)
└── 📁 MonitoredVehicleJourney (1..1)
```

---

## 3. Key Elements

- **RecordedAtTime** — When the position/status was recorded
- **ValidUntilTime** — When this data expires (consumers should discard after this time)
- **ProgressBetweenStops** — How far between the previous and next stop (percentage and distance)

---

## 4. References

- [MonitoredVehicleJourney](../MonitoredVehicleJourney/Description_MonitoredVehicleJourney.md) — The journey data
- [SIRI-VM Service](../../Services/SIRI-VM/Description_SIRI-VM.md) — Full service description
