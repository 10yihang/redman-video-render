# RedMan concept video

8-second, 1920×1080, 30 fps preset concept demonstration. Nova joins a team, receives a brief, and presents a concept poster. The interface is an animation, not a live agent session.

## Rendered result

[Watch or download the MP4](https://github.com/10yihang/redman-video-render/blob/render-output/RedMan-Core-1080p.mp4)

[Successful workflow run](https://github.com/10yihang/redman-video-render/actions/runs/39142396967)

Verified: 8.000 seconds, 240 frames, H.264 1920×1080 at 30 fps, AAC 48 kHz stereo, 1,850,491 bytes. Hyperframes checks and full FFmpeg decode passed. Sixteen sampled frames were visually reviewed.

## Rendering

Run the Render video workflow manually. It uses a standard public GitHub-hosted Ubuntu runner, no paid API, no GitHub Actions cache, and no Actions artifacts. The MP4 is stored on the render-output branch. A 40 MB limit prevents oversized output.

Dependencies: Node 24, Hyperframes 0.8.171, GSAP 3.14.2, FFmpeg and Chromium.

Local commands: npm install --ignore-scripts; npm run lint; npm run check; npm run render.
