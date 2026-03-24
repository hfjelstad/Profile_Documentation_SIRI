# RecordedCall

## 1. Purpose

RecordedCall describes information regarding already-served stops in a VehicleJourney. Together with EstimatedCalls, RecordedCalls define all stops of a complete EstimatedVehicleJourney.

---

## 2. Structure Overview

```
📁 RecordedCall
├── 🔗 StopPointRef (1..1)
├── 📄 Order (1..1)
├── 📄 StopPointName (0..1)
├── 📄 Cancellation (0..1)
├── 📄 AimedArrivalTime (0..1)
├── 📄 ActualArrivalTime (0..1)
├── 📄 ArrivalPlatformName (0..1)
├── 📄 AimedDepartureTime (0..1)
├── 📄 ActualDepartureTime (0..1)
└── 📄 DeparturePlatformName (0..1)
```

---

## 3. Key Elements

- **StopPointRef** — Reference to Quay in the national stop place registry
- **ActualArrivalTime / ActualDepartureTime** — The actual recorded times at the stop
- **AimedArrivalTime / AimedDepartureTime** — The originally planned times

---

## 4. References

- [EstimatedVehicleJourney](../EstimatedVehicleJourney/Description_EstimatedVehicleJourney.md) — Parent journey
- [EstimatedCall](../EstimatedCall/Description_EstimatedCall.md) — Companion for upcoming stops
- [SIRI-ET Service](../../Services/SIRI-ET/Description_SIRI-ET.md) — Full service context

---

## 5. Usage Notes

> [!WARNING]
> - RecordedCalls and EstimatedCalls together must form the **complete** stop sequence (`IsCompleteStopSequence = true`)
> - RecordedCalls must precede all EstimatedCalls in chronological order
> - A stop missed from recording may remain as a correspondingly labeled EstimatedCall even after passing
