# 3D Vessel Icons

## Format

Use **GLB** as the standard format for 3D vessel icons.

### Why GLB?

- Single file
- Easy to manage
- Small file size
- Fast loading
- Supports materials and textures
- Supports animations
- Supported by major 3D and mapping platforms
- Well suited for Mapbox applications

### Supported Platforms

- Mapbox
- Cesium
- Three.js
- Babylon.js

## Generation

Recommended AI tools:

- Meshy (not tested)
- Tripo AI
- Rodin (not tested)

### Benefits

- Faster than manual 3D modeling
- No Blender knowledge required
- Generate vessel models from text prompts
- Export directly to GLB
- Easy integration with Mapbox

### Workflow

```text
Prompt
    ↓
AI 3D Generator
    ↓
GLB
    ↓
Mapbox
```

## Tools

### Tripo AI

https://studio.tripo3d.ai/workspace/generate

### glTF.report

https://gltf.report/

#### Personal Notes

- I use this tool when working with GLB models in Mapbox.
- It helped fix model positioning issues when rendering 3D objects on the map.

## Example Prompt (Tripo AI)

```text
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
```

## Possible Vessel Models

```text
container_ship.glb
tanker.glb
cargo_ship.glb
fishing_vessel.glb
tug_boat.glb
passenger_ship.glb
```

## Notes

- Use low-poly models for better performance.
- Vessel icons are usually viewed from a distance, so excessive detail is unnecessary.
- Generate a small set of reusable vessel models and use them across the application.
- Prioritize silhouette recognition over visual detail.
