# Xiaohongshu recruitment v2
25 seconds / 1080x1920 / 30 fps. Element-level HTML, SVG and GSAP animation, based on three approved visual directions.

Sequence:
0–4s independently scrolling discovery columns.
4–6.5s search focus and pointer selecting the city note.
6.5–8.5s the same city card expands to detail; shell/header/actions assemble around it.
9–13s bookmark toggles, comment appears.
14.4–18s product/technology/design annotations connect to interface work.
18.1–21.5s shared city cover shrinks into a recruitment note as a second cover enters and recruitment text assembles.
21.5–25s clean readable recruitment destination hold.

Run python3 create-score.py (numpy), npm install --ignore-scripts, npm run lint, npm run check, npm run render. Output Xiaohongshu-Recruitment-v2-1080x1920.mp4. Requires FFmpeg and Chromium; local environment cannot launch Chromium so CI performs pixel checks and render. Preserve old movies; this is a separate v2 deliverable.
