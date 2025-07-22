# import re
# from typing import List, Tuple
# from kerykeion import AstrologicalSubject
# from kerykeion.aspects.synastry_aspects import SynastryAspects

# # import all your per‐body interpreters
# from sun_synastry_aspects import SunSynastryAspects
# from moon_synastry_aspects import MoonSynastryAspects
# from mercury_synastry_aspects import MercurySynastryAspects
# from venus_synastry_aspects import VenusSynastryAspects
# from mars_synastry_aspects import MarsSynastryAspects
# from jupiter_synastry_aspects import JupiterSynastryAspects
# from saturn_synastry_aspects import SaturnSynastryAspects
# from uranus_synastry_aspects import UranusSynastryAspects
# from neptune_synastry_aspects import NeptuneSynastryAspects
# from pluto_synastry_aspects import PlutoSynastryAspects
# from ascendant_synastry_aspects import AscendantSynastryAspects
# from medium_coeli_synastry_aspects import MediumCoeliSynastryAspects

# # 1) define your two charts:
# john = AstrologicalSubject(
#     name="Florian Bargues",
#     year=1999, month=12, day=3,
#     hour=22, minute=59,
#     lat=48.8566, lng=-2.3522,
#     city="Paris",
#     tz_str="Europe/Paris"
# )

# paul = AstrologicalSubject(
#     name="Sarah Arias",
#     year=2002, month=4, day=3,
#     hour=14, minute=0,
#     lat=4.6243, lng=-74.0636,
#     city="Bogota",
#     tz_str="America/Bogota"
# )

# # 2) compute synastry aspects
# synastry = SynastryAspects(john, paul)
# all_aspects = synastry.all_aspects

# # 3) instantiate each interpreter once
# interpreters = {
#     "Sun":          SunSynastryAspects(),
#     "Moon":         MoonSynastryAspects(),
#     "Mercury":      MercurySynastryAspects(),
#     "Venus":        VenusSynastryAspects(),
#     "Mars":         MarsSynastryAspects(),
#     "Jupiter":      JupiterSynastryAspects(),
#     "Saturn":       SaturnSynastryAspects(),
#     "Uranus":       UranusSynastryAspects(),
#     "Neptune":      NeptuneSynastryAspects(),
#     "Pluto":        PlutoSynastryAspects(),
#     "Ascendant":    AscendantSynastryAspects(),
#     "Medium_Coeli": MediumCoeliSynastryAspects(),
# }

# # valid aspect types to include
# valid_aspects = {"conjunction", "opposition", "square", "trine", "sextile"}

# # helper to turn names like "Medium_Coeli" → "Medium Coeli"
# def display_name(raw):
#     return raw.replace("_", " ")

# def parse_aspects(text: str) -> List[Tuple[str, str, str, float]]:
#     """
#     Parse astrological aspects from text into structured format.
#     Returns list of (planet1, planet2, aspect, orb) tuples.
#     """
#     aspects = []
    
#     # Regular expression to match aspect lines
#     aspect_pattern = re.compile(
#         r"([A-Za-z]+)\s+"          # Planet 1
#         r"(Conjunction|Trine|Sextile|Square|Opposition)\s+"  # Aspect type
#         r"([A-Za-z]+)\s*"          # Planet 2
#         r"\(orb:\s*([+-]?\d+\.\d+)"  # Orb value
#     )
    
#     # Alternative pattern for aspects with different wording
#     alt_pattern = re.compile(
#         r"🌟\s*"  # Optional star emoji
#         r"([A-Za-z]+)\s+"          # Planet 1
#         r"(Conjunction|Trine|Sextile|Square|Opposition)\s+"  # Aspect type
#         r"([A-Za-z]+)\s*"          # Planet 2
#         r"\(orb:\s*([+-]?\d+\.\d+)"  # Orb value
#     )
    
#     for line in text.split('\n'):
#         line = line.strip()
#         if not line:
#             continue
            
#         # Try both patterns
#         for pattern in [aspect_pattern, alt_pattern]:
#             match = pattern.search(line)
#             if match:
#                 planet1 = match.group(1).lower()
#                 aspect = match.group(2).lower()
#                 planet2 = match.group(3).lower()
#                 orb = abs(float(match.group(4)))  # Take absolute value
                
#                 # Handle special cases (like "Medium Coeli")
#                 planet1 = planet1.replace("medium coeli", "medium_coeli")
#                 planet2 = planet2.replace("medium coeli", "medium_coeli")
#                 planet1 = planet1.replace("ascendant", "ascendant")
#                 planet2 = planet2.replace("ascendant", "ascendant")
                
#                 aspects.append((planet1, planet2, aspect, orb))
#                 break
                
#     return aspects

# def generate_aspect_text(filtered_aspects):
#     """
#     Generates the aspect text output that can later be parsed by parse_aspects()
#     Returns the formatted text as a string
#     """
#     aspect_text = []
    
#     for asp in filtered_aspects:
#         p1_raw = asp["p1_name"]
#         p2_raw = asp["p2_name"]
#         rel = asp["aspect"]     # e.g. "trine", "conjunction"
#         orb = asp["orbit"]
        
#         p1 = display_name(p1_raw)
#         p2 = display_name(p2_raw)
        
#         # Build the aspect line
#         aspect_line = f"🌟 {p1} {rel.title()} {p2} (orb: {orb:.2f}°)"
#         interpretation = f"→ {interpret_aspect(p1_raw, rel, p2_raw)}"
        
#         # Add to our text buffer
#         aspect_text.append(aspect_line)
#         aspect_text.append(interpretation)
#         aspect_text.append("")  # Empty line for separation
    
#     return "\n".join(aspect_text)

# def interpret_aspect(p1_raw, aspect, p2_raw):
#     p1 = display_name(p1_raw)
#     p2 = display_name(p2_raw)
#     key = f"{p1} {aspect.title()} {p2}"
#     interp = interpreters[p1_raw]  # safe since we filtered by raw name
#     result = interp.get_aspect_interpretation(key)
#     if result != "Aspect interpretation not found.":
#         return result
#     return f"{key} — no interpretation defined."

# # 4) filter: only keep if p1 & p2 are known bodies AND aspect is one of the five
# filtered_aspects = [
#     asp for asp in all_aspects
#     if (
#         asp["p1_name"] in interpreters
#         and asp["p2_name"] in interpreters
#         and asp["aspect"].lower() in valid_aspects
#     )
# ]


# aspect_output_text = generate_aspect_text(filtered_aspects)
# detected_aspects = parse_aspects(aspect_output_text)

# #print(detected_aspects)


# # Output
# for asp in filtered_aspects:
#     p1 = asp["p1_name"]
#     aspect = asp["aspect"]
#     p2 = asp["p2_name"]
#     orb = asp["orbit"]
#     print(f"🌟 {p1} {aspect} {p2} (orb: {orb:.2f}°)")
#     print("→", interpret_aspect(p1, aspect, p2))
#     print()

import re
import json
from typing import List, Tuple
from kerykeion import AstrologicalSubject
from kerykeion.aspects.synastry_aspects import SynastryAspects

# import all your per‐body interpreters
from .sun_synastry_aspects import SunSynastryAspects
from .moon_synastry_aspects import MoonSynastryAspects
from .mercury_synastry_aspects import MercurySynastryAspects
from .venus_synastry_aspects import VenusSynastryAspects
from .mars_synastry_aspects import MarsSynastryAspects
from .jupiter_synastry_aspects import JupiterSynastryAspects
from .saturn_synastry_aspects import SaturnSynastryAspects
from .uranus_synastry_aspects import UranusSynastryAspects
from .neptune_synastry_aspects import NeptuneSynastryAspects
from .pluto_synastry_aspects import PlutoSynastryAspects
from .ascendant_synastry_aspects import AscendantSynastryAspects
from .medium_coeli_synastry_aspects import MediumCoeliSynastryAspects

# 2) prepare interpreters and filters
interpreters = {
    "Sun":          SunSynastryAspects(),
    "Moon":         MoonSynastryAspects(),
    "Mercury":      MercurySynastryAspects(),
    "Venus":        VenusSynastryAspects(),
    "Mars":         MarsSynastryAspects(),
    "Jupiter":      JupiterSynastryAspects(),
    "Saturn":       SaturnSynastryAspects(),
    "Uranus":       UranusSynastryAspects(),
    "Neptune":      NeptuneSynastryAspects(),
    "Pluto":        PlutoSynastryAspects(),
    "Ascendant":    AscendantSynastryAspects(),
    "Medium_Coeli": MediumCoeliSynastryAspects(),
}

valid_aspects = {"conjunction", "opposition", "square", "trine", "sextile"}


# 4) Define the 10-category map
CATEGORY_MAP = {
    "Identity & Self":            ["Sun"],
    "Emotions & Bonding":         ["Moon"],
    "Communication & Intellect":  ["Mercury"],
    "Love & Affection":           ["Venus"],
    "Passion & Drive":            ["Mars"],
    "Growth & Expansion":         ["Jupiter"],
    "Commitment & Structure":     ["Saturn"],
    "Power & Transformation":     ["Pluto"],
    "Dreams & Freedom":           ["Neptune", "Uranus"],
    "Public Persona & Ambitions": ["Ascendant", "Medium_Coeli"],
}


def display_name(raw: str) -> str:
    return raw.replace("_", " ")

def interpret_aspect(p1_raw: str, aspect: str, p2_raw: str) -> str:
    key = f"{display_name(p1_raw)} {aspect.title()} {display_name(p2_raw)}"
    interp = interpreters[p1_raw].get_aspect_interpretation(key)
    return interp if interp != "Aspect interpretation not found." else f"{key} — no interpretation defined."

def get_synastry_json(subject1: AstrologicalSubject,
                      subject2: AstrologicalSubject) -> List[dict]:
    """
    Compute synastry, filter for valid bodies & aspects, and return
    a JSON-serializable list of interpretations.
    """
    syn = SynastryAspects(subject1, subject2)
    all_asps = syn.all_aspects

    filtered = [
        asp for asp in all_asps
        if (
            asp["p1_name"] in interpreters
            and asp["p2_name"] in interpreters
            and asp["aspect"].lower() in valid_aspects
        )
    ]

    results = []
    for asp in filtered:
        p1 = asp["p1_name"]
        p2 = asp["p2_name"]
        aspect = asp["aspect"].lower()
        orb = asp["orbit"]
        interp = interpret_aspect(p1, aspect, p2)

        results.append({
            "p1": display_name(p1),
            "p2": display_name(p2),
            "aspect": aspect,
            "orb": round(orb, 2),
            "interpretation": interp
        })

    return results

def categorize_synastry(synastry_list: List[dict]) -> dict:
    # Initialize all categories plus an "Others" catch-all
    categories = {cat: [] for cat in CATEGORY_MAP}
    categories["Others"] = []

    for asp in synastry_list:
        placed = False
        for cat, bodies in CATEGORY_MAP.items():
            if asp["p1"] in bodies:
                categories[cat].append(asp)
                placed = True
                break
        if not placed:
            categories["Others"].append(asp)

    return categories

# if __name__ == "__main__":
#     synastry_data = get_synastry_json(first_person, second_person)
#     # Print a nicely indented JSON string
#     print(json.dumps(synastry_data, indent=2, ensure_ascii=False))
