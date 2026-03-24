<!-- LLM AGENT: This is the authoritative source for documentation standards in the SIRI Profile Documentation repository -->

# SIRI Profile Documentation — LLM Agent Guidelines

## 1. Repository Purpose

This repository documents the **Nordic SIRI Profile** — a localisation of the SIRI 2.0 standard for real-time public transport data exchange. It covers three services: SIRI-ET (Estimated Timetable), SIRI-SX (Situation Exchange), and SIRI-VM (Vehicle Monitoring).

---

## 2. Documentation Structure

### Top-Level Folders

| Folder | Contents |
|--------|----------|
| `Guides/` | Conceptual overviews: GetStarted, GeneralInformation, DataExchange, Glossary |
| `Services/` | One folder per service: `SIRI-ET/`, `SIRI-SX/`, `SIRI-VM/` |
| `Objects/` | Shared data structures: ServiceDelivery, EstimatedVehicleJourney, etc. |
| `LLM/` | This folder — documentation standards, templates, agent guidelines |

### Three-File Pattern

Each service and object should have:
1. `Description_<Name>.md` — Purpose, structure overview, key elements, references, usage notes
2. `Table_<Name>.md` — Element-level specification with types, cardinality, and descriptions
3. XML examples (in `Examples/` subfolder for services, or inline in Description files)

---

## 3. SIRI-Specific Conventions

### ID Format
```
Codespace:ObjectType:Identifier
```
Examples: `NSB:ServiceJourney:1-2492-2343`, `NSR:Quay:709`, `RUT:Line:31`

### Cardinality Notation
Always use: `(1..1)` `(1..n)` `(0..1)` `(0..n)` — Never use "mandatory", "optional", "required"

### Icon Legend (Structure Overviews)
- `📄` = primitive element or attribute value
- `📁` = container/collection wrapper
- `🔗` = reference to another object

### References to Planned Data
All SIRI data references NeTEx planned objects. Always document which NeTEx object is referenced:
- `LineRef` → Line
- `FramedVehicleJourneyRef` → ServiceJourney + Date
- `StopPointRef` → Quay (NSR ID)
- `OperatorRef` → Operator
- `RouteRef` → Route

---

## 4. Profiles

The Nordic SIRI Profile is version 1.1, based on SIRI 2.0 XML Schema.

Three services are in scope:
- **SIRI-ET** — Estimated Timetable (same operating day timetable updates)
- **SIRI-SX** — Situation Exchange (disruption/deviation messages)
- **SIRI-VM** — Vehicle Monitoring (vehicle position and progress)

---

## 5. Writing Style

- **Conversational yet professional** — questions, tips, explanatory asides
- **Worked examples** — show XML before explaining it
- **Visual structure trees** — use `📄` `📁` `🔗` icons with cardinality
- **Cross-reference links** — extensive internal linking via relative markdown paths
- **Mermaid diagrams** — for relationship and flow visualisation

---

## 6. Markdown Conventions

### Headings
- `#` for document title, `##` for major sections, `###` for subsections
- Numbered sections: "## 1. Purpose", "## 2. Structure Overview"

### Links
- Pattern: `[Display Text](../../Objects/ObjectName/Description_ObjectName.md)`
- Relative paths only; never absolute URLs (except external resources)

### Tables
- Use pipe tables for element specifications
- Column order: Type indicator, Name, Type, Cardinality, Description

---

## 7. Docsify Interactive Features

### Flexible Alerts
```markdown
> [!NOTE]
> Informational callout (blue)

> [!WARNING]
> Warning callout with grouped bullets (orange):
> - **Bold label**: description
> - **Another label**: description

> [!TIP]
> Helpful tip (green)
```

### Tabs
```markdown
<!-- tabs:start -->
#### **Tab One**
Content for tab one
#### **Tab Two**
Content for tab two
<!-- tabs:end -->
```
Config: `{ persist: true, sync: true, theme: 'classic' }`

### Mermaid Diagrams
Use the blue palette for consistency:

| Role | Hex |
|------|-----|
| Darkest / root | `#0D47A1` |
| Primary | `#1565C0` |
| Secondary | `#1976D2` |
| Tertiary | `#1E88E5` |
| Quaternary | `#42A5F5` |
| Quinary | `#64B5F6` |
| Lightest | `#90CAF9` |

### Copy Code
All code blocks automatically get a "Copy" button.

### Glossary Tooltips
Terms defined in `Guides/Glossary/Glossary.md` will show tooltip definitions on hover (first occurrence only).

---

## 8. Validation

- XML examples should be well-formed and conform to SIRI 2.0 XSD
- All stop references should use valid NSR (National Stop Registry) IDs
- All journey references should use valid NeTEx codespace:type:id format
