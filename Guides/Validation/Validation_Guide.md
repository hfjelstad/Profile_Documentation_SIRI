# ✅ SIRI Validation Guide

## 1. 🎯 Introduction

Validating SIRI XML against the official schema catches structural errors, wrong element ordering, invalid references, and missing required elements before they cause issues downstream. This guide covers the validation process from schema setup to troubleshooting.

In this guide you will learn:

- 📦 Which schema entry point to use
- 🖥️ How to validate locally and in CI
- ❌ The most common validation errors and how to fix them
- 🔧 Troubleshooting tips

> For general SIRI structure and conventions, see the [General Information Guide](../GeneralInformation/GeneralInformation_Guide.md).

---

## 2. 📦 Schema Setup

### Entry Point

The main SIRI schema entry point is:

| File | Description |
|------|-------------|
| `siri.xsd` | Root schema — validates the full SIRI standard including all functional services |

> 💡 **Tip:** `siri.xsd` imports all service-specific schemas (ET, SX, VM, FM, etc.) automatically.

### Getting the Schema

Clone (or shallow-clone) the official SIRI XSD directly from the source:

```bash
git clone --depth=1 --branch v2.2 https://github.com/SIRI-CEN/SIRI.git siri-xsd
```

The entry point is then `siri-xsd/xsd/siri.xsd`.

> 💡 **Tip:** This gives you the official v2.2 schema. Re-run the clone (or `git -C siri-xsd pull`) to pick up updates.

> ⚠️ **Note:** The `siri-xsd/` folder is a working copy, not part of your project. It is already in `.gitignore`.

### Using a Specific Version

To validate against a particular SIRI release:

```bash
git clone https://github.com/SIRI-CEN/SIRI.git siri-xsd
cd siri-xsd
git tag -l            # list available versions (v2.0q, v2.1, v2.2)
git checkout v2.2     # switch to a specific release
```

### XSD Structure

The SIRI XSD is organized as follows:

```
xsd/
├── siri.xsd                              ← Main entry point
├── siri_all_functionalServices.xsd       ← All SIRI service imports
├── siri_estimatedTimetable_service.xsd   ← SIRI-ET
├── siri_situationExchange_service.xsd    ← SIRI-SX
├── siri_vehicleMonitoring_service.xsd    ← SIRI-VM
├── siri_facilityMonitoring_service.xsd   ← SIRI-FM
├── siri/                                 ← Common framework
├── siri_model/                           ← Service component models
├── siri_utility/                         ← Utility types
├── ifopt/                                ← Stop/station types
├── acsb/                                 ← Accessibility types
├── datex2/                               ← Location/road types
└── gml/                                  ← Geometry types
```

---

## 3. 🖥️ Running Validation

### Using This Repository's Script

The easiest way to validate:

```bash
# All XML files
./scripts/validate-xml.sh

# Only files changed vs main
./scripts/validate-xml.sh --changed

# Specific files
./scripts/validate-xml.sh Services/SIRI-ET/Examples/Example_ET_response.xml
```

The script will automatically clone the SIRI XSD if it is not already present.

### Using xmllint Directly

```bash
xmllint --noout \
  --schema "siri-xsd/xsd/siri.xsd" \
  Services/SIRI-ET/Examples/Example_ET_response.xml
```

### Using Python lxml

```python
from lxml import etree

schema = etree.XMLSchema(etree.parse("siri-xsd/xsd/siri.xsd"))
doc = etree.parse("Services/SIRI-ET/Examples/Example_ET_response.xml")

if schema.validate(doc):
    print("PASS")
else:
    for err in schema.error_log:
        print(err)
```

### CI Validation

Pull requests are automatically validated by [`.github/workflows/PR_Validator.yml`](../../.github/workflows/PR_Validator.yml) when XML files change. Always validate locally first to avoid CI failures.

---

## 4. ❌ Common Errors and Fixes

### 4a. Wrong Element Order

```
Element 'RecordedAtTime': This element is not expected.
Expected is one of ( LineRef, DirectionRef, ... )
```

**Cause:** SIRI XSD uses `xs:sequence` — elements must appear in a specific order.

**Fix:** Reorder elements to match the XSD sequence. Check the object's Table file for the correct order.

### 4b. Wrong Casing

```
Element 'EstimatedVehiclejourney': This element is not expected.
Expected is ( EstimatedVehicleJourney )
```

**Cause:** XML element names are case-sensitive.

**Fix:** Use the exact casing from the XSD. SIRI uses UpperCamelCase for elements.

### 4c. Invalid Element

```
Element 'CustomField': This element is not expected.
```

**Cause:** The element doesn't exist on this type in the XSD.

**Fix:** Remove the element or check the object's Table file for which elements are valid.

### 4d. Invalid Namespace

```
Element '{http://wrong.namespace}Siri': No matching global declaration available.
```

**Cause:** The root element uses the wrong namespace.

**Fix:** Use the correct SIRI namespace: `http://www.siri.org.uk/siri`

### 4e. Missing Required Element

```
Element 'EstimatedVehicleJourney': Missing child element(s).
Expected is ( ... )
```

**Cause:** A mandatory child element is missing.

**Fix:** Add the required element. Check the error message for what's expected, or consult the object's Description file.

### 4f. Invalid Enum Value

```
Element 'VehicleMode': 'airplane' is not a valid value.
```

**Cause:** The element value is not one of the allowed enum values in the XSD.

**Fix:** Check the XSD or the object's Table file for valid enum values.

---

## 5. 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| "Cannot find schema" | Ensure the XSD is available locally — clone from the official repo (see section 2) |
| Schema loads but nothing validates | Check you're using the correct entry point (`siri.xsd`) |
| Many errors cascade from one issue | Fix the first error only, then re-validate — later errors are often caused by the first |
| Validation passes locally, fails in CI | Ensure you've committed all changed files and pushed |
| xmllint not available (Windows) | Use Python lxml instead — `pip install lxml` |
| Import/include resolution errors | Use `--path` with the XSD directory when running xmllint |

---

## 6. 📋 Pre-Commit Checklist

Before committing XML changes:

- [ ] Run `./scripts/validate-xml.sh --changed` (or validate specific files)
- [ ] All files pass with 0 errors
- [ ] Correct SIRI namespace (`http://www.siri.org.uk/siri`) is used
- [ ] Element ordering follows the XSD sequence
- [ ] No elements outside the Nordic SIRI Profile scope

---

## 7. 🔗 Related Resources

### Guides

- [General Information](../GeneralInformation/GeneralInformation_Guide.md) — SIRI overview and Nordic Profile conventions
- [Get Started](../GetStarted/GetStarted_Guide.md) — First steps with the SIRI profile
- [Data Exchange](../DataExchange/DataExchange_Guide.md) — Pub/Sub and Request/Response patterns

### External

- [SIRI XSD Repository](https://github.com/SIRI-CEN/SIRI) — Official SIRI XML Schemas (CEN)
- [SIRI v2.2 XSD](https://github.com/SIRI-CEN/SIRI/tree/v2.2/xsd) — Current stable schema version
- [SIRI Examples](https://github.com/SIRI-CEN/SIRI/tree/v2.2/examples) — Official XML examples per service
