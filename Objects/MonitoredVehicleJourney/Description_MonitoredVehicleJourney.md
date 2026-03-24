# MonitoredVehicleJourney

## 1. Purpose

MonitoredVehicleJourney is the core data object in SIRI-VM. It contains real-time position, delay, status, and occupancy information for a vehicle operating a planned journey. It enriches existing NeTEx timetable data with live observations.

---

## 2. Structure Overview

```
📁 MonitoredVehicleJourney
├── 🔗 LineRef (1..1)
├── 📄 DirectionRef (0..1)
├── 🔗 FramedVehicleJourneyRef (0..1)
├── 📄 VehicleMode (0..1)
├── 🔗 OperatorRef (0..1)
├── 🔗 OriginRef (0..1)
├── 📄 OriginName (0..1)
├── 🔗 DestinationRef (0..1)
├── 📄 DestinationName (0..1)
├── 📄 Monitored (0..1)
├── 📄 DataSource (1..1)
├── 📁 VehicleLocation (1..1)
│   ├── 📄 Longitude (1..1)
│   └── 📄 Latitude (1..1)
├── 📄 Bearing (0..1)
├── 📄 Velocity (0..1)
├── 📄 Occupancy (0..1)
├── 📄 Delay (1..1)
├── 📄 InCongestion (0..1)
├── 📄 VehicleStatus (0..1)
├── 🔗 VehicleJourneyRef (0..1)
├── 🔗 VehicleRef (1..1)
├── 📁 MonitoredCall (0..1)
└── 📄 IsCompleteStopSequence (1..1) — always false
```

---

## 3. Key Elements

- **VehicleLocation** — GPS coordinates (WGS84) of the vehicle
- **Delay** — ISO 8601 duration (`PT0S` = on time, `PT5M` = 5 minutes late)
- **VehicleRef** — Unique identifier for the physical vehicle
- **VehicleStatus** — Operational state: `inProgress`, `atOrigin`, `completed`, `offRoute`, `cancelled`
- **MonitoredCall** — Current or most recent stop being served

---

## 4. References

- [VehicleActivity](../VehicleActivity/Description_VehicleActivity.md) — Parent container
- [FramedVehicleJourneyRef](../FramedVehicleJourneyRef/Description_FramedVehicleJourneyRef.md) — Journey reference
- [SIRI-VM Service](../../Services/SIRI-VM/Description_SIRI-VM.md) — Full service description

---

## 5. Usage Notes

> [!WARNING]
> - Either **FramedVehicleJourneyRef** or **VehicleJourneyRef** must be set (not both)
> - **VehicleRef** is mandatory — every vehicle must have a unique ID
> - **Delay** is mandatory — use `PT0S` when there is no delay
> - **IsCompleteStopSequence** must be `false` when only MonitoredCall is included
> - Vehicle coordinates must be in **WGS84** format
