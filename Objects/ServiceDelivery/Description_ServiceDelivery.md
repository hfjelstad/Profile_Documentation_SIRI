# ServiceDelivery

## 1. Purpose

ServiceDelivery is the top-level container for all SIRI functional service deliveries. It wraps one of the three SIRI service types (ET, SX, VM) along with common metadata about the producer and timestamp.

Every SIRI message flows through this container.

---

## 2. Structure Overview

```
📁 ServiceDelivery
├── 📄 ResponseTimestamp (1..1)
├── 📄 ProducerRef (1..1)
└── (choice) one of:
    ├── 📁 EstimatedTimetableDelivery (1..1)
    ├── 📁 SituationExchangeDelivery (1..1)
    └── 📁 VehicleMonitoringDelivery (1..1)
```

---

## 3. Key Elements

- **ResponseTimestamp** — When the dataset was generated/published
- **ProducerRef** — Codespace identifying the data producer (e.g. `NSB`, `RUT`)
- **Delivery choice** — Exactly one of the three delivery types per message

---

## 4. References

- [EstimatedTimetableDelivery](../../Services/SIRI-ET/Table_SIRI-ET.md) — SIRI-ET delivery
- [SituationExchangeDelivery](../../Services/SIRI-SX/Table_SIRI-SX.md) — SIRI-SX delivery 
- [VehicleMonitoringDelivery](../../Services/SIRI-VM/Table_SIRI-VM.md) — SIRI-VM delivery

---

## 5. Usage Notes

> [!WARNING]
> - **ProducerRef** must be a valid codespace identifier
> - Each ServiceDelivery contains exactly **one** delivery type
> - **ResponseTimestamp** must reflect the actual time of data generation, not a cached or placeholder time
