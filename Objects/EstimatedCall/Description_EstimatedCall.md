# EstimatedCall

## 1. Purpose

EstimatedCall represents the estimated arrival and departure information for a single stop in an EstimatedVehicleJourney. It provides current predictions for stops that have not yet been served.

Together with RecordedCalls, EstimatedCalls form the complete stop sequence of a journey.

---

## 2. Structure Overview

```
📁 EstimatedCall
├── 🔗 StopPointRef (1..1)
├── 📄 Order (1..1)
├── 📄 StopPointName (0..1)
├── 📄 Cancellation (0..1)
├── 📄 RequestStop (0..1)
├── 📄 AimedArrivalTime (0..1)
├── 📄 ExpectedArrivalTime (0..1)
├── 📄 ArrivalStatus (0..1)
├── 📄 ArrivalBoardingActivity (0..1)
├── 📁 ArrivalStopAssignment (0..1)
├── 📄 AimedDepartureTime (0..1)
├── 📄 ExpectedDepartureTime (0..1)
├── 📄 DepartureStatus (0..1)
├── 📄 DepartureBoardingActivity (0..1)
└── 📁 DepartureStopAssignment (0..1)
```

---

## 3. Key Elements

- **StopPointRef** — Reference to Quay in the national stop place registry (NSR)
- **Order** — The position of this stop in the journey sequence
- **Cancellation** — Set to `true` when this specific stop is cancelled
- **ArrivalStatus / DepartureStatus** — Current status: `onTime`, `early`, `delayed`, `cancelled`, `noReport`
- **ArrivalBoardingActivity / DepartureBoardingActivity** — `boarding`, `noBoarding`, `alighting`, `noAlighting`

---

## 4. References

- [EstimatedVehicleJourney](../EstimatedVehicleJourney/Description_EstimatedVehicleJourney.md) — Parent journey
- [RecordedCall](../RecordedCall/Description_RecordedCall.md) — Companion for already-served stops
- [SIRI-ET Service](../../Services/SIRI-ET/Description_SIRI-ET.md) — Full service context

---

## 5. Usage Notes

> [!WARNING]
> - **StopPointRef** must always reference a valid ID from the national stop place registry
> - For cancelled stops: set `<Cancellation>true</Cancellation>` together with `<ArrivalStatus>cancelled</ArrivalStatus>` and `<DepartureStatus>cancelled</DepartureStatus>`
> - The final stop in a journey does **not** have `DepartureStatus` or `DepartureTime` elements
> - All EstimatedCalls must be in **strict chronological order**
