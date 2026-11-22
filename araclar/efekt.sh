#!/usr/bin/env bash
# ElevenLabs ile ses efekti üretir. Kullanım: araclar/efekt.sh "soft message pop notification" cikti.mp3 [saniye]
set -e
curl -sf -o "$2" "https://api.elevenlabs.io/v1/sound-generation?output_format=mp3_44100_128" \
  -H "xi-api-key: proxy-injected" -H "Content-Type: application/json" \
  -d "$(python3 -c 'import json,sys; print(json.dumps({"text":sys.argv[1],"duration_seconds":float(sys.argv[2]),"prompt_influence":0.5}))' "$1" "${3:-1.0}")"
echo "$2"
