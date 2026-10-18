# RedMan concept video

8-second, 1920×1080, 30 fps preset concept demonstration. Nova joins a team, receives a brief, and presents a concept poster. The interface is an animation, not a live agent session.

Run the Render video workflow manually. It uses a standard public GitHub-hosted Ubuntu runner, no paid API, no cache, and no Actions artifacts. The verified MP4 is stored on the render-output branch. A 40 MB limit prevents oversized output.

Dependencies: Node 24, Hyperframes 0.8.171, GSAP 3.14.2, FFmpeg and Chromium.

Local commands: npm install --ignore-scripts; npm run lint; npm run check; npm run render.

Rendering and visual review are pending the first successful workflow run.
