# [Service Name] — Service Description Template

## 1. Purpose

[2-3 sentence explanation of the service's role in the SIRI ecosystem. What real-time data does it provide?]

---

## 2. Structure Overview

[Mermaid diagram showing the hierarchy from ServiceDelivery down to the leaf elements]

```
📄 [Service]Delivery (1..1)
├── 📄 version (1..1)
├── 📄 ResponseTimestamp (1..1)
└── 📁 [Container] (1..n)
    └── 📁 [CoreObject] (1..n)
        ├── 🔗 [ref element] (1..1)
        └── 📄 [child element] (0..1)
```

---

## 3. Data Requirements

> [!NOTE]
> [Key requirement about data completeness, ordering, or structure]

- [Bullet list of specific data requirements]

---

## 4. Key Use Cases

### [Use Case 1]
[Brief description with inline XML if helpful]

### [Use Case 2]
[Brief description]

---

## 5. Example

```xml
[Complete, well-formed XML example demonstrating the service]
```

> [!WARNING]
> - [Common pitfall 1]
> - [Common pitfall 2]

---

## 6. Components Reference

| Component | Description | Documentation |
|-----------|-------------|---------------|
| [Name] | [Brief description] | [Link to table/description] |

---

## 7. Related Examples

| Example | Description | Link |
|---------|-------------|------|
| [Name] | [Use case it demonstrates] | [Link] |
