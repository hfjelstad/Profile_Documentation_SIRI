# Table of Contents

## Guides

| Guide | Description | Link |
|-------|-------------|------|
| Get Started | Introduction to SIRI and the Nordic Profile | [GetStarted_Guide.md](../../Guides/GetStarted/GetStarted_Guide.md) |
| General Information | SIRI overview, terminology, and conventions | [GeneralInformation_Guide.md](../../Guides/GeneralInformation/GeneralInformation_Guide.md) |
| Data Exchange | Communication patterns: Pub/Sub, Request/Response | [DataExchange_Guide.md](../../Guides/DataExchange/DataExchange_Guide.md) |
| Glossary | Terminology and definitions | [Glossary.md](../../Guides/Glossary/Glossary.md) |

---

## Services

| Service | Code | Description | Link |
|---------|------|-------------|------|
| Estimated Timetable | SIRI-ET | Real-time timetable updates | [Description](../../Services/SIRI-ET/Description_SIRI-ET.md) · [Table](../../Services/SIRI-ET/Table_SIRI-ET.md) |
| Situation Exchange | SIRI-SX | Disruption and deviation messages | [Description](../../Services/SIRI-SX/Description_SIRI-SX.md) · [Table](../../Services/SIRI-SX/Table_SIRI-SX.md) |
| Vehicle Monitoring | SIRI-VM | Vehicle position and progress | [Description](../../Services/SIRI-VM/Description_SIRI-VM.md) · [Table](../../Services/SIRI-VM/Table_SIRI-VM.md) |

---

## Objects

| Object | Service | Description | Link |
|--------|---------|-------------|------|
| ServiceDelivery | All | Top-level message container | [Description](../../Objects/ServiceDelivery/Description_ServiceDelivery.md) · [Table](../../Objects/ServiceDelivery/Table_ServiceDelivery.md) |
| EstimatedVehicleJourney | SIRI-ET | Journey-level real-time timetable data | [Description](../../Objects/EstimatedVehicleJourney/Description_EstimatedVehicleJourney.md) |
| EstimatedCall | SIRI-ET | Per-stop estimated arrival/departure | [Description](../../Objects/EstimatedCall/Description_EstimatedCall.md) |
| RecordedCall | SIRI-ET | Per-stop recorded arrival/departure | [Description](../../Objects/RecordedCall/Description_RecordedCall.md) |
| PtSituationElement | SIRI-SX | Core situation data object | [Description](../../Objects/PtSituationElement/Description_PtSituationElement.md) |
| Affects | SIRI-SX | What a situation impacts | [Description](../../Objects/Affects/Description_Affects.md) |
| MonitoredVehicleJourney | SIRI-VM | Real-time vehicle journey data | [Description](../../Objects/MonitoredVehicleJourney/Description_MonitoredVehicleJourney.md) |
| VehicleActivity | SIRI-VM | Vehicle activity container | [Description](../../Objects/VehicleActivity/Description_VehicleActivity.md) |
| FramedVehicleJourneyRef | All | Journey reference with date | [Description](../../Objects/FramedVehicleJourneyRef/Description_FramedVehicleJourneyRef.md) |
