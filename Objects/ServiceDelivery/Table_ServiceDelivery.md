# ServiceDelivery — Element Table

| | Name | Type | Cardinality | Description |
|---|------|------|-------------|-------------|
| element | ResponseTimestamp | xsd:dateTime | 1:1 | Time when the dataset was generated/published |
| element | ProducerRef | xsd:NMTOKEN | 1:1 | Codespace for dataset producer |
| (choice) | EstimatedTimetableDelivery | EstimatedTimetableDeliveryStructure | 1:1 | Data for Estimated Timetable (SIRI-ET) |
| | SituationExchangeDelivery | SituationExchangeDeliveryStructure | | Data for Situation Exchange (SIRI-SX) |
| | VehicleMonitoringDelivery | VehicleMonitoringDeliveryStructure | | Data for Vehicle Monitoring (SIRI-VM) |
