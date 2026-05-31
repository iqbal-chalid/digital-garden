# Maritime

Collection of notes, references, ideas, and projects related to maritime technology.

## Vessel Search

Vessels can typically be searched using one of the following identifiers:

### Vessel Name

The human-readable name of the vessel.

**Example:**

```text
EVER GIVEN
MSC OSCAR
MAERSK ALABAMA
```

### IMO

**International Maritime Organization Number**

A unique identifier assigned to a vessel for its entire lifetime.

**Characteristics:**

- Usually 7 digits
- Does not change during the vessel's lifetime
- Remains the same even if the vessel changes name, owner, or flag

**Example:**

```text
IMO 9811000
```

### MMSI

**Maritime Mobile Service Identity**

A unique identifier used by AIS and marine communication systems.

**Characteristics:**

- 9 digits
- Transmitted by AIS devices
- Used for real-time vessel tracking
- Can change in some situations

**Example:**

```text
538009877
```

## Improvement Ideas

### User Mental Model

```text
Filter  = Show me fewer vessels
Alert   = Tell me when something happens
Overlay = Show me additional information on the map
```

**Note:** Don't put overlays inside filters.

### Alerts

Legend:

- ⭐ Easy
- ⭐⭐ Medium
- ⭐⭐⭐ Advanced

#### Severity Levels

- Info
- Warning
- Critical

> Severity levels are defaults and should be configurable by users.

#### Dashboard

Display:

```text
🔔 32
🔴 1
```

Where:

- 🔔 = Total active alerts
- 🔴 = Critical alerts

Group alerts by severity and display critical alerts first.

Example:

```text
Critical (1)
────────────
AIS Signal Lost

Warning (8)
───────────
ETA Delayed
Idle Vessel
...

Info (23)
─────────
Entered Zone
Exited Zone
...
```

#### Geofence Alerts ⭐

| Alert               | Default Severity |
| ------------------- | ---------------- |
| Vessel entered zone | Info             |
| Vessel exited zone  | Info             |

#### AIS Alerts ⭐

| Alert               | Default Severity |
| ------------------- | ---------------- |
| AIS signal lost     | Critical         |
| AIS signal restored | Info             |

#### ETA Alerts ⭐⭐

| Alert                  | Default Severity |
| ---------------------- | ---------------- |
| ETA delayed by X hours | Warning          |

#### Speed Alerts ⭐⭐

| Alert                           | Default Severity |
| ------------------------------- | ---------------- |
| Vessel stopped unexpectedly     | Warning          |
| Vessel exceeded speed threshold | Warning          |
| Vessel slowed significantly     | Warning          |

#### Idle Alerts ⭐

| Alert                              | Default Severity |
| ---------------------------------- | ---------------- |
| Vessel idle for X minutes          | Info             |
| Vessel idle outside port area      | Warning          |
| Vessel idle outside anchorage area | Warning          |

#### Advanced Alerts ⭐⭐⭐

| Alert                              | Default Severity |
| ---------------------------------- | ---------------- |
| Vessel stopped in unusual location | Critical         |
| High congestion near destination   | Warning          |
| Suspicious route deviation         | Critical         |
| Dark vessel detected               | Critical         |

### Filters

#### Dashboard

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

Users should be able to:

- View active filters
- Clear individual filters
- Clear all filters

#### Selection

- Allow users to filter vessels based on multiple criteria.
- Support combining multiple filter criteria.
- Support saving filter presets.
- Provide a quick way to clear all filters.

Examples:

- Vessel Type
- Speed
- Status
- Flag
- Destination

Example:

```text
Type = Tanker
Status = Underway
Speed > 10 knots
```

## 3D Vessel Icons

### Format

Use **GLB** as the standard format for 3D vessel icons.

**Why GLB?**

- Single file
- Easy to manage
- Small file size
- Fast loading
- Supports materials and textures
- Supports animations
- Supported by major 3D and mapping platforms
- Ideal for web applications

Supported by:

- Mapbox
- Cesium
- Three.js
- Babylon.js

### Generation

Recommended approach:

- Meshy
- Tripo AI
- Rodin

Why?

- Faster than manual 3D modeling
- No Blender knowledge required
- Can generate vessel models from text prompts
- Export directly to GLB
- Suitable for Mapbox integration

Example workflow:

```text
Prompt
    ↓
AI 3D Generator
    ↓
GLB
    ↓
Mapbox
```

### Example Prompt

```text
Create a low-poly tanker vessel.

Requirements:

- Low poly (< 2000 triangles)
- Suitable for Mapbox
- Gray material
- Export as GLB
```

### Possible Vessel Models

```text
container_ship.glb
tanker.glb
cargo_ship.glb
fishing_vessel.glb
tug_boat.glb
passenger_ship.glb
```

### Notes

Use low-poly models for better performance.

Users often view vessels from a distance, so extremely detailed models are usually unnecessary.

Generate a small set of vessel models and reuse them across the application.

tools
https://studio.tripo3d.ai/workspace/generate

Low-poly cargo ship for maritime tracking dashboard.

Requirements:

- General cargo vessel
- Clean and recognizable ship silhouette
- Optimized for top-down viewing
- Low polygon count
- Simple geometry
- Flat gray material
- No textures
- No logos
- No text markings
- No rust
- No weathering
- No water
- No ocean
- No environment
- No background

Visualization Requirements:

- Suitable for displaying hundreds or thousands of vessels simultaneously
- Strong vessel outline
- Slightly exaggerated bridge and superstructure for visibility
- Realistic proportions but simplified design

Output:

- Single vessel only
- Centered model
- Export-ready GLB
