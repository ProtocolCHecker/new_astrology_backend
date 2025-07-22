#!/usr/bin/env python3
import itertools
import json
import sys

# Make sure Python can find your interpreter script
# Adjust the path below so that it points at the folder
# containing main_aspects_interpreter.py
sys.path.append("birth_chart/aspects")

from main_aspects_interpreter import get_aspect_json

MAINS   = ["Ascendant","Sun","Moon","Mercury","Venus","Mars","Jupiter","Saturn","Uranus","Neptune","Pluto"]
ASPECTS = ["conjunction","sextile","trine","square","opposition"]
GENDERS = ["male","female","other"]

failures = []

for main, other, asp, gen in itertools.product(MAINS, MAINS, ASPECTS, GENDERS):
    if main.lower() == other.lower():
        continue
    result = get_aspect_json(main, other, asp, gen)
    if result is None:
        failures.append({
            "main": main,
            "other": other,
            "aspect": asp,
            "gender": gen
        })

print(f"Tested {len(MAINS)*(len(MAINS)-1)*len(ASPECTS)*len(GENDERS)} combinations.")
if failures:
    print(f"{len(failures)} failures:")
    print(json.dumps(failures, indent=2))
    sys.exit(1)
else:
    print("✅ All combinations returned a valid interpretation.")
    sys.exit(0)
