# 📘 General Information — Nordic SIRI Profile

## 1. Preface

A Nordic standard for exchanging uniform real-time data is valuable for:

- **Entur AS** (on behalf of Jernbanedirektoratet) — to efficiently collect all real-time data from each data provider, ensure consistency, and increase data quality for nationwide journey planning.
- **Travellers** — to receive relevant, up-to-date, high-quality journey suggestions.
- **Public transport operators** — to re-use data in journey planning, ticketing, and information systems.
- **Third party service providers** — to minimize costs related to supporting multiple exchange formats.

---

## 2. Service Interface for Real Time Information (SIRI)

SIRI is a CEN specification (CEN/TS 15531) for exchanging real-time data for public transport and vehicles. It was developed cooperatively between France, Germany (VDV), Scandinavia, and Great Britain (RTIG).

The standard is based on the reference model **Transmodel** (CEN TC278, EN12896) and contains a general model for real-time data with an XML Schema implementation.

SIRI defines a standardised communication layer with:
- **Openness** and **scalability**
- Content independent from transfer protocols
- Standardised publication and message handling (WebService HTTP/SOAP, WS-PubSub)
- Common mechanisms for access control, versioning, and error handling
- Configurable updating and filtering

> [!NOTE]
> The Nordic SIRI Profile is based on SIRI 2.0 XML Schema and specifies which parts of the wider format to use. Like the Nordic NeTEx Profile (which defines planned data), the SIRI profile describes **how** and **which** parts of the format to use.

---

## 3. Services Supported by the Nordic Profile

Real-time information is exchanged in three formats:

### SIRI-ET — Estimated Timetable
Continuous updates per line, restricted to the current operating day:
- Delays, cancellations, additional departures
- Overtakes or stops that are not going to be served

### SIRI-SX — Situation Exchange
Information on disruptions in public transport:
- Planned deviations (maintenance work on tracks)
- Unplanned deviations (accidents, unforeseen issues, severe weather)

### SIRI-VM — Vehicle Monitoring
Tracking the position of vehicles:
- Actual position of vehicles as they traverse a route (GPS data)

> [!TIP]
> SIRI also defines services **not** included in the Nordic profile:
> - **SIRI-PT** — Production Timetable (changes outside current operating day)
> - **SIRI-SM** — Stop Monitoring (arrival/transfer times for same operating day)
> - **SIRI-ST** — Stop Timetable (changes outside current operating day)
> - **SIRI-CM** — Connection Monitoring (guaranteed interchanges)
> - **SIRI-CT** — Connection Timetable (interchanges outside operating day)
> - **SIRI-GM** — General Messaging (general text-based information)
> - **SIRI-FM** — Facility Monitoring (equipment and service status)

---

## 4. Terminology

### SIRI-specific Objects and Formats

Terms and concepts in SIRI are defined according to the NeTEx format standard, based on Transmodel. All objects use English names; Norwegian terminology is for guidance only.

| Data Type | Description |
|-----------|-------------|
| **Encoding** | Primarily UTF-8, but ISO-8859-1 and ASCII can be handled |
| **Date/Time** | Local time according to ISO 8601 ("00:00" = midnight). Minimum granularity is seconds. |
| **Language** | Three-letter code (ISO 639-3 recommended) or two-letter code (ISO 639-1 / RFC 1766) |
| **Location** | WGS84/GML coordinates (normally EPSG:4326). Other formats must be converted. |
| **StopPoint** | Reference to a logical stop point (always referencing the national stop place registry) |
| **Destination** | Usually the final or an important intermediary stop place |
| **Origin** | Usually the first stop place in the route |

### General Requirements on Data

For real-time data delivered in XML, the structure and content must be well-formed in accordance with the SIRI 2.0 XML Schema:

> [!WARNING]
> - Values must be **trimmed** (no blanks first or last in data values)
> - Characters must be valid and in accordance with the encoding
> - All data fields must contain **meaningful information** and be correctly formatted
> - Test or dummy data must **never** be published in production environments

---

## 5. Using IDs

All IDs in SIRI and NeTEx datasets must be **constants** across real-time, stops, and timetable data to prevent mismatches.

- References to stops must always use IDs from the **national stop place registry**
- The data source is responsible for ensuring IDs are correctly linked between timetable and real-time data
- Unchanged objects should keep their IDs unchanged across datasets

---

## 6. Key Resources

| Resource | Link |
|----------|------|
| SIRI Official Site | [vdv.de/siri](https://www.vdv.de/siri.aspx) |
| Transmodel | [transmodel-cen.eu](http://transmodel-cen.eu/) |
| NeTEx | [netex-cen.eu](http://netex-cen.eu/) |
| Nordic NeTEx Profile | [Profile_Documentation_v2](https://github.com/hfjelstad/Profile_Documentation_v2) |
| Real-time API Documentation | [developer.entur.org](https://developer.entur.org/pages-real-time-intro) |
