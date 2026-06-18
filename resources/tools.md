# Tools

Collection of useful tools, platforms, and services related to development, design, and AI workflows.

---

## App Development

### FlutterFlow

- https://app.flutterflow.io/

Visual app builder for creating Flutter-based mobile and web applications.

### FlutterFlow Designer

- https://designer.flutterflow.io/

AI-assisted UI generation tool from FlutterFlow.

---

## Design Tools

### Visily

- https://www.visily.ai/

Beginner-friendly UI/UX design and wireframing tool for quickly creating app and web mockups.

#### Personal Notes

- Much easier to learn compared to Figma for non-designers.
- Great for quickly visualizing ideas and creating mockups.
- Feels more practical and approachable for developers who are not dedicated UI/UX designers.
- Personally used more as a design/productivity tool rather than for its AI features.

### jitter.video

- https://jitter.video/

Online motion design and animation tool for creating UI animations and visual content.

#### Personal Notes

- The UI feels much more intuitive compared to https://lottiefiles.com/.
- It may not be as advanced, but it seems sufficient for most common animation needs.
- The free tier is relatively generous.

## 3D Model Tools

### glTF.report

- https://gltf.report/

Online tool for inspecting and fixing GLB/glTF 3D models.

#### Personal Notes

- I use this tool to fix GLB files before displaying them on Mapbox maps.
- It helped resolve positioning issues when rendering GLB models on top of the map.

### Babylon.js Sandbox

- https://sandbox.babylonjs.com/

Online 3D model viewer and testing environment for GLB/glTF files.

#### Personal Notes

- Very useful for quickly previewing GLB models without installing any software.
- Supports drag-and-drop loading of GLB files.
- Allows inspecting animations, materials, lighting, and model hierarchy.

## Diagramming / Whiteboard

### Excalidraw

- https://excalidraw.com/

Virtual whiteboard for creating hand-drawn style diagrams, architecture sketches, workflows, and system designs.

## Development & Networking

### Cloudflared

- https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/downloads/

Cloudflare Tunnel client for securely exposing local services to the internet without opening firewall ports.

Useful for:

- Testing local APIs with FlutterFlow
- Sharing local development servers
- Temporary public URLs for demos
- Replacing ngrok for API testing

Example:

```bash
cloudflared tunnel --url http://localhost:8000
```

Generates a temporary public URL:

```text
https://example.trycloudflare.com
```

which can be used by FlutterFlow, mobile devices, and external services to access a local development server.
