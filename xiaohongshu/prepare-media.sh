#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p private-media composition/assets
curl -L --fail --retry 2 --max-time 180 'https://videos.pexels.com/video-files/6693575/6693575-uhd_2160_4096_25fps.mp4' -o private-media/clay-original.mp4
curl -L --fail --retry 2 --max-time 180 'https://videos.pexels.com/video-files/9032810/9032810-uhd_2160_3840_24fps.mp4' -o private-media/coffee-original.mp4
for item in clay coffee; do
 ffmpeg -hide_banner -loglevel error -y -i "private-media/${item}-original.mp4" -t 9 -vf 'scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30' -an -c:v libx264 -preset fast -crf 20 "composition/assets/${item}.mp4"
done
