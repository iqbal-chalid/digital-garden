# Vessel Search

Vessels can typically be searched using one of the following identifiers.

## Vessel Name

The human-readable name of the vessel.

### Characteristics

- Easy for users to remember
- Most common search method
- Not guaranteed to be unique
- Can change during the vessel's lifetime

### Examples

```text
EVER GIVEN
MSC OSCAR
MAERSK ALABAMA
```

---

## IMO Number

**International Maritime Organization Number**

A unique identifier assigned to a vessel for its entire lifetime.

### Characteristics

- Usually 7 digits
- Globally unique
- Does not change during the vessel's lifetime
- Remains the same even if the vessel changes name, owner, or flag

### Example

```text
IMO 9811000
```

---

## MMSI

**Maritime Mobile Service Identity**

A unique identifier used by AIS and marine communication systems.

### Characteristics

- 9 digits
- Transmitted by AIS devices
- Used for real-time vessel tracking
- Can change in some situations
- Often used by AIS providers and tracking systems

### Example

```text
538009877
```

---

## Recommended Search Behavior

Support searching by:

- Vessel Name
- IMO Number
- MMSI

The search field should automatically detect the identifier type.

Examples:

```text
EVER GIVEN     → Vessel Name
9811000        → IMO Number
538009877      → MMSI
```

Users should not need to select the search type manually.
