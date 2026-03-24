# 🔄 Data Exchange Patterns

## 1. Overview

Communication of SIRI data must be implemented via REST-based services over HTTP. The exchange mechanism is identical for all service types (SIRI-ET, SIRI-SX, SIRI-VM).

Three forms of data acquisition are supported:

```mermaid
graph LR
    subgraph "Asynchronous"
        DD["Direct Delivery<br/>(Publish/Subscribe)"]
        FD["Fetched Delivery<br/>(Publish/Subscribe)"]
    end
    
    subgraph "Synchronous"
        RR["Request/Response"]
    end
    
    Producer["Data<br/>Producer"] -->|"push"| DD
    DD -->|"stream"| Consumer["Data<br/>Consumer"]
    
    Producer -->|"notify"| FD
    FD -->|"fetch"| Consumer
    
    Consumer -->|"request"| RR
    RR -->|"response"| Producer

    style DD fill:#1565C0,stroke:#0D47A1,color:#fff
    style FD fill:#1976D2,stroke:#0D47A1,color:#fff
    style RR fill:#1E88E5,stroke:#0D47A1,color:#fff
    style Producer fill:#42A5F5,stroke:#1565C0,color:#fff
    style Consumer fill:#64B5F6,stroke:#1976D2,color:#fff
```

---

## 2. Asynchronous — Publish/Subscribe

The service continuously delivers data updates to all subscribed consumers. All Publish/Subscribe services must send **heartbeats** in accordance with the subscription request (`HeartbeatInterval`) to verify service availability.

### Direct Delivery

Data is continuously streamed to all subscribers immediately after release. The recipient acknowledges with HTTP 200 "OK".

```mermaid
sequenceDiagram
    participant P as Producer
    participant C as Consumer
    
    C->>P: Subscribe
    P->>C: SubscriptionResponse
    loop On data change
        P->>C: ServiceDelivery
        C->>P: HTTP 200 OK
    end
    loop Heartbeat interval
        P->>C: HeartbeatNotification
    end
```

### Fetched Delivery

Data is only sent when the receiving system has verified it is ready. The producer must keep data available until the consumer has explicitly fetched it.

```mermaid
sequenceDiagram
    participant P as Producer
    participant C as Consumer
    
    C->>P: Subscribe
    P->>C: SubscriptionResponse
    loop On data change
        P->>C: DataReadyNotification
        C->>P: DataReadyAcknowledgement
        C->>P: DataSupplyRequest
        P->>C: ServiceDelivery
    end
```

---

## 3. Synchronous — Request/Response

Explicit fetching of datasets based on service type, time, and filtering parameters.

```mermaid
sequenceDiagram
    participant C as Consumer
    participant P as Producer
    
    C->>P: ServiceRequest (with filters)
    P->>C: ServiceDelivery
```

---

## 4. General Requirements

### Standard Values
All fields used when setting up a data stream or calling services must have meaningful values, defaults, and comply with request parameters (time intervals, filtering, change-before-update).

### Data Correctness

> [!WARNING]
> - Data must comply with requirements in the Nordic SIRI Profile
> - Data should be semantically appropriate and interpretable by consumers
> - Empty data must not be submitted, even when technically not prohibited
> - Published real-time information must contain **genuine updates**
> - Test or dummy data must **never** be published in production environments

### Data Completeness
Real-time data builds upon NeTEx planned data, which it supports, enriches, or replaces. However, each SIRI message should be complete and self-contained within its XML file.

### Data Content
When no input parameters are present in a request, a full dataset is expected. When parameters are specified, data is filtered accordingly.

### Data Freshness
New messages should be published as soon as feasible after source data changes:
- Changes in stops (EstimatedCall → RecordedCall)
- Quay determination or changes
- Adjustments in estimated arrivals or departures

> [!TIP]
> Normal data deliveries should contain only updates/changes since the most recent push/request. If messages contain previously delivered data, mechanisms must prevent duplication.
