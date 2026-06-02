# Improvement Ideas

## User Mental Model

```text
Filter  = Show me fewer vessels
Alert   = Tell me when something happens
Overlay = Show me additional information on the map
```

### Design Principle

Keep filters, alerts, and overlays separate.

- Filters control which vessels are displayed.
- Alerts notify users when events occur.
- Overlays provide additional map context.

Do not place overlays inside filter menus.

---

## Alerts

### Complexity Legend

- ⭐ Easy
- ⭐⭐ Medium
- ⭐⭐⭐ Advanced

### Severity Levels

- Info
- Warning
- Critical

> Default severities should be configurable by users.

### Dashboard Summary

Display:

```text
🔔 32
🔴 1
```

Where:

- 🔔 Total active alerts
- 🔴 Critical alerts

### Alert List

Display critical alerts first.

Example:

```text
Critical (1)
────────────
AIS Signal Lost

Warning (8)
───────────
ETA Delayed
Idle Vessel

Info (23)
─────────
Entered Zone
Exited Zone
```

### Geofence Alerts ⭐

| Alert               | Default Severity |
| ------------------- | ---------------- |
| Vessel entered zone | Info             |
| Vessel exited zone  | Info             |

### AIS Alerts ⭐

| Alert               | Default Severity |
| ------------------- | ---------------- |
| AIS signal lost     | Critical         |
| AIS signal restored | Info             |

### ETA Alerts ⭐⭐

| Alert                  | Default Severity |
| ---------------------- | ---------------- |
| ETA delayed by X hours | Warning          |

### Speed Alerts ⭐⭐

| Alert                           | Default Severity |
| ------------------------------- | ---------------- |
| Vessel stopped unexpectedly     | Warning          |
| Vessel exceeded speed threshold | Warning          |
| Vessel slowed significantly     | Warning          |

### Idle Alerts ⭐

| Alert                              | Default Severity |
| ---------------------------------- | ---------------- |
| Vessel idle for X minutes          | Info             |
| Vessel idle outside port area      | Warning          |
| Vessel idle outside anchorage area | Warning          |

### Advanced Alerts ⭐⭐⭐

| Alert                              | Default Severity |
| ---------------------------------- | ---------------- |
| Vessel stopped in unusual location | Critical         |
| High congestion near destination   | Warning          |
| Suspicious route deviation         | Critical         |
| Dark vessel detected               | Critical         |

---

## Filters

### Purpose

Filters determine which vessels are visible on the map.

### Dashboard Summary

Display:

```text
[Filter] 3
```

Where:

- Filter icon = Filter configuration
- Number = Active filters

Example:

```text
Type = Tanker
Status = Underway
Speed > 10 knots
```

### Requirements

Users should be able to:

- View active filters
- Remove individual filters
- Clear all filters
- Save filter presets
- Load saved presets

### Filter Criteria

Examples:

- Vessel Type
- Speed
- Status
- Flag
- Destination
- Length
- Draft
- AIS Class

### Example

```text
Type = Tanker
Status = Underway
Speed > 10 knots
```

---

## Overlays

### Purpose

Overlays provide additional information on the map without affecting vessel visibility.

Examples:

- Weather
- Wind
- Wave height
- Sea current
- Port boundaries
- Anchorage areas
- Traffic density
- EEZ boundaries
- Shipping lanes
- Satellite imagery

### Design Principle

Turning an overlay on or off should never change the vessel list.

Overlays add context, while filters control visibility.
