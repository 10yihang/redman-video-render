# Xiaohongshu recruitment concept

25 seconds, 1080 × 1920, 30 fps, original stereo score. Unofficial concept with stock life footage. Not actual office or employee footage.

Sequence: share a moment (0–3.5 s), a possibility (3.5–7), technology/connection (7–10.5), design/experience (10.5–14), creativity/life (14–18), converging possibilities (18–21.5), recruitment destination (21.5–25).

Install pinned dependencies from package.json; run bash prepare-media.sh; npm run lint; npm run check; npm run render. Output: Xiaohongshu-Recruitment-1080x1920.mp4. FFmpeg and a working Chromium are required. Do not upload private-media or composition/assets/*.mp4 to source control. Render only with lawful source downloads.

No local browser render is claimed: Chromium is blocked in the preparation environment. Static checks and soundtrack/media checks precede CI render. Review representative rendered frames and the final audio/video before delivery.
