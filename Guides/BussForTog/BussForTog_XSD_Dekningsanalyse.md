# Dekningsanalyse — Buss-for-tog-attributter mot SIRI v2.2 XSD

Denne analysen mapper attributter fra buss-for-tog-strømmene (020, 024, 028, 032, 034, BUSK, PAT) mot SIRI v2.2 XSD for å identifisere hva som er dekket, delvis dekket, og ikke dekket.

---

## Reise- og turidentifikasjon

| Attributt | SIRI-dekning | XSD-element | Tjeneste | Kommentar |
|---|---|---|---|---|
| BusID | ✅ Dekket | `VehicleRef` | ET, VM | Unik kjøretøy-ID |
| VersionNr | ✅ Dekket | `version` (attributt på `EstimatedVehicleJourney`) | ET | Meldingsversjonering |
| TrainOperator | ✅ Dekket | `OperatorRef` | ET, VM | I `ServiceInfoGroup` |
| ReplaceTrain | ⚠️ Indirekte | `FramedVehicleJourneyRef` + `ExtraJourney=true` | ET | Refererer til den erstattede togturen; ingen dedikert «replaces»-felt |
| ReplaceLine | ⚠️ Indirekte | `LineRef` + `PublishedLineName` | ET | Settes til toglinjen bussen erstatter |
| Date | ✅ Dekket | `DataFrameRef` (i `FramedVehicleJourneyRef`) | ET | Operasjonsdag |
| AssociatedTrain | ⚠️ Indirekte | `TrainNumberRef` (i `TrainNumbers`) | ET | Kan referere til tilknyttet tognummer |
| DisruptionID | ✅ Dekket | `SituationRef` / `SituationSimpleRef` | ET, SX | Kobler til SIRI-SX-situasjon |

---

## Kjøretøyinformasjon

| Attributt | SIRI-dekning | XSD-element | Tjeneste | Kommentar |
|---|---|---|---|---|
| VehicleStatus | ✅ Dekket | `VehicleStatus` | VM | Enum: `expected`, `cancelled`, `assigned`, `signedOn`, `atOrigin`, `inProgress`, `aborted`, `completed`, `notRun` m.fl. |
| VehicleType | ✅ Dekket | `VehicleMode` | ET, VM | Enum: `bus`, `coach`, `taxi` etc. Merk: «Minibus» og «Minitaxi» finnes ikke som egne enum-verdier |
| SeatCapacity | ✅ Dekket | `SeatingCapacity` (i `PassengerCapacityStructure`) | ET (call-nivå) | Siden SIRI 2.1 |
| SeatCapacityChild | ⚠️ Delvis | `PassengerCategory` + `SeatingCapacity` | ET | Kan spesifiseres per passasjerkategori via `VehicleOccupancyStructure` |
| SeatHandicap | ⚠️ Delvis | `SpecialPlacesOccupied` / `WheelchairsOnboardCount` | ET | Telling av HC-plasser, men ikke kapasitet direkte |
| VehicleCompany | ✅ Dekket | `OperatorRef` | ET, VM | Bussforetak = operatør |
| DriverPhoneNr | ❌ Ikke dekket | — | — | Ingen felt for telefonnummer i XSD |
| Licenseplate | ⚠️ Delvis | `VehicleNumber` (i `TrainElementGroup`) | ET | Ment for UIC-nummer, men kan brukes for registreringsnummer |

---

## Rute og stopp

| Attributt | SIRI-dekning | XSD-element | Tjeneste | Kommentar |
|---|---|---|---|---|
| Kjøremønster/Trase | ⚠️ Indirekte | `JourneyPatternRef` + `ExtraJourney` | ET | Shuttle/SingleJourney/Reserved finnes ikke som enum-verdier |
| Destination | ✅ Dekket | `DestinationRef` + `DestinationName` | ET, VM | |
| FrontDisplay | ✅ Dekket | `DestinationDisplay` | ET | Overstyrer skiltmål per call |
| RemarkText | ⚠️ Indirekte | `Description` (fri tekst) eller `SituationRef` | ET, SX | Ingen dedikert «remark»-felt på call-nivå |
| StopName | ✅ Dekket | `StopPointName` | ET, VM | |
| Plattform | ✅ Dekket | `ArrivalPlatformName` / `DeparturePlatformName` | ET | NSR:Quay via `StopPointRef` |
| StopOrder | ✅ Dekket | `Order` | ET | 1, 2, 3… |
| StopActivity | ✅ Dekket | `ArrivalBoardingActivity` / `DepartureBoardingActivity` | ET | `alighting`, `boarding`, `noAlighting`, `noBoarding`, `passThru` |

---

## Tider

| Attributt | SIRI-dekning | XSD-element | Tjeneste |
|---|---|---|---|
| ScheduledTimeOfArrival | ✅ Dekket | `AimedArrivalTime` | ET |
| ScheduledTimeOfDeparture | ✅ Dekket | `AimedDepartureTime` | ET |
| EstimatedTimeOfArrival | ✅ Dekket | `ExpectedArrivalTime` | ET |
| EstimatedTimeOfDeparture | ✅ Dekket | `ExpectedDepartureTime` | ET |
| ActualTimeOfArrival | ✅ Dekket | `ActualArrivalTime` | ET |
| ActualTimeOfDeparture | ✅ Dekket | `ActualDepartureTime` | ET |
| IsArrivalCancelled | ✅ Dekket | `Cancellation` (call-nivå) + `ArrivalStatus=cancelled` | ET |
| IsDepartureCancelled | ✅ Dekket | `Cancellation` (call-nivå) + `DepartureStatus=cancelled` | ET |

---

## Sanntid og telemetri

| Attributt | SIRI-dekning | XSD-element | Tjeneste | Kommentar |
|---|---|---|---|---|
| TotalDrivenKM | ❌ Ikke dekket | — | — | Ingen kilometerteller i XSD. `DistanceFromStop` finnes, men måler avstand til neste stopp |
| GPS | ✅ Dekket | `VehicleLocation` (`Longitude`, `Latitude`) + `Bearing` | VM | I `MonitoredVehicleJourney` |
| PassengerCount | ✅ Dekket | `Occupancy` (enum) / `OccupancyPercentage` / `OnboardCount` | ET, VM | `OnboardCount` gir eksakt passasjertall (siden SIRI 2.1) |

---

## Oppsummering

| Status | Antall attributter | Andel |
|---|---|---|
| ✅ **Fullt dekket** | 22 | 69% |
| ⚠️ **Delvis / indirekte** | 8 | 25% |
| ❌ **Ikke dekket** | 2 | 6% |

### Attributter uten XSD-dekning

| Attributt | Begrunnelse |
|---|---|
| **DriverPhoneNr** | Personopplysning — hører ikke hjemme i en åpen sanntidsstandard |
| **TotalDrivenKM** | Drifts-/kontraktsdata — ikke del av sanntidsinformasjon til passasjerer |

### Attributter med begrensninger

| Attributt | Utfordring | Mulig løsning |
|---|---|---|
| **ReplaceTrain** | Ingen eksplisitt «erstatter»-referanse | Bruk `ExtraJourney=true` + `FramedVehicleJourneyRef` til opprinnelig tog |
| **ReplaceLine** | Bussen arver toglinjen | Sett `LineRef` til toglinjen, legg busslinje i `ExternalLineRef` |
| **AssociatedTrain** | `TrainNumberRef` er ment for tognummer | Fungerer, men semantikken er «dette toget», ikke «tilknyttet tog» |
| **VehicleType** | `VehicleMode` har ikke «Minibus» / «Minitaxi» | Bruk `bus` + `ProductCategoryRef` for underkategorisering |
| **SeatCapacityChild** | Ikke eget felt | Bruk `PassengerCategory` = «child» i `VehicleOccupancyStructure` |
| **SeatHandicap** | Bare telling, ikke kapasitet | `WheelchairsOnboardCount` for antall ombord; kapasitet via `SpecialPlacesOccupied` |
| **Licenseplate** | `VehicleNumber` er primært for UIC-nummer | Kan brukes for registreringsnummer i profilen |
| **Kjøremønster** | Shuttle/Reserved finnes ikke som enum | Beskriv i fri tekst via `JourneyPatternName` eller `Description` |
| **RemarkText** | Ingen dedikert felt på call-nivå | Bruk `Description` eller koble til `SituationRef` med fritekst i SIRI-SX |
