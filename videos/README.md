# AlterVNC — demo videos

Product clips for [AlterVNC](../README.md), kept in this public asset repository alongside release downloads.
The English and French showcases select light/dark GIFs with `<picture>`.

| Clip | Shows | MP4, full quality | GIF, README |
|---|---|---|---|
| `01-connect` · 10 s | Choose a favourite, connect, open the remote desktop and session toolbar | [Light](01-connect-light.mp4) · [Dark](01-connect-dark.mp4) | [Light](01-connect-light.gif) · [Dark](01-connect-dark.gif) |
| `02-keyboard` · 10 s | French AZERTY PC keystrokes produce `A 1 # € \| { _ ?` on the Mac | [Light](02-keyboard-light.mp4) · [Dark](02-keyboard-dark.mp4) | [Light](02-keyboard-light.gif) · [Dark](02-keyboard-dark.gif) |
| `03-clipboard` · 10 s | Copy on the PC, click Paste in AlterVNC, see the text on the Mac | [Light](03-clipboard-light.mp4) · [Dark](03-clipboard-dark.mp4) | [Light](03-clipboard-light.gif) · [Dark](03-clipboard-dark.gif) |
| `04-android` · 10 s | Landscape, Touch and Trackpad modes, movable floating toolbar | [Light](04-android-light.mp4) · [Dark](04-android-dark.mp4) | [Light](04-android-light.gif) · [Dark](04-android-dark.gif) |
| `05-updates` · 13 s | Version badge, Mue download, separate installation, confirmation and restart | [Light](05-updates-light.mp4) · [Dark](05-updates-dark.mp4) | [Light](05-updates-light.gif) · [Dark](05-updates-dark.gif) |

Each clip exists in **light and dark**, as an **MP4 (1920 × 1080, 60 fps)** and a looping
**GIF (960 × 540, 20 fps)**. UI labels and captions are in French. No audio.

All **10 GIFs are below 5 MB** (decimal): **0.341–0.788 MB** each. The largest is
`05-updates-light.gif` at **787,644 bytes**. The 20 media files total approximately **8.29 MB**.
Validation covers the encoded formats and **34 extracted MP4 frames**, including both sides of the Android tap.

Demo data only: `mac-studio`, `mac-studio.example.ts.net`, account `demo`, fictional release notes,
versions `0.9.0 → 0.9.1`, download size, timings and latency. Password dots have no underlying secret.
The remote desktop is generic, with no third-party logo. These are scripted UI reconstructions,
not recordings of a real VNC session or performance measurements.

Colours and Lucide icons follow AlterVNC’s `Theme.axaml`; desktop and mobile controls follow its XAML.
The update dialogs reproduce the Avalonia Mue integration with AlterVNC’s palette and the separate
download/install/confirmation steps. **Windows currently forces dark mode**: the light desktop clips
illustrate the project’s Light palette. Android supports both themes.

These files are **generated**. The private application repository’s `tools/MotionDemo/` contains
`render.mjs`, `clips/` and `shared/`, following the Mue/DockPad method: deterministic HTML replayed in
Chromium headless, then ffmpeg. With this repository next to the application worktree, the renderer writes
directly into `videos/` here. `npm run verify` checks the encoded media and extracts at least three frames
per clip and theme for visual review.

The separate [`video/`](../video/) directory retains the original brand intros, title cards and transparent logo animations.
