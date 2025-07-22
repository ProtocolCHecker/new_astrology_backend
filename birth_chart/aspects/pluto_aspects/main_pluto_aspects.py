# # main_pluto_aspect_interpreter.py
# from .pluto_and_moon_aspect_interpretation import pluto_moon_aspects
# from .pluto_and_sun_aspect_interpretation import pluto_sun_aspects
# from .pluto_and_mercury_aspect_interpretation import pluto_mercury_aspects
# from .pluto_and_venus_aspect_interpretation import pluto_venus_aspects
# from .pluto_and_mars_aspect_interpretation import pluto_mars_aspects
# from .pluto_and_jupiter_aspect_interpretation import pluto_jupiter_aspects
# from .pluto_and_saturn_aspect_interpretation import pluto_saturn_aspects
# from .pluto_and_neptune_aspect_interpretation import pluto_neptune_aspects
# from .pluto_and_ascendant_aspect_interpretation import pluto_ascendant_aspects
# from .pluto_and_uranus_aspect_interpretation import pluto_uranus_aspects

# # Dictionary mapping planets to their aspect interpretations
# PLUTO_ASPECTS = {
#     "Sun": pluto_sun_aspects,
#     "Moon": pluto_moon_aspects,
#     "Mercury": pluto_mercury_aspects,
#     "Venus": pluto_venus_aspects,
#     "Mars": pluto_mars_aspects,
#     "Jupiter": pluto_jupiter_aspects,
#     "Saturn": pluto_saturn_aspects,
#     "Neptune": pluto_neptune_aspects,
#     "Ascendant": pluto_ascendant_aspects,
#     "Uranus": pluto_uranus_aspects
# }

# VALID_ASPECTS = ["Conjunction", "Sextile", "Trine", "Square", "Opposition"]
# VALID_PLANETS = list(PLUTO_ASPECTS.keys())

# # def get_pluto_aspect_interpretation(planet, aspect, gender_expression="other"):
# #     """
# #     Get Pluto aspect interpretation for a specific planet and aspect
    
# #     Parameters:
# #     - planet (str): The planet to check aspect with Pluto (e.g., "Moon", "Venus")
# #     - aspect (str): The aspect type (e.g., "Conjunction", "Square")
# #     - gender_expression (str): "male", "female", or "other" (default)
    
# #     Returns:
# #     - dict: Contains all interpretation components
# #     - None: If invalid inputs are provided
# #     """
# #     # Validate inputs
# #     planet = planet.capitalize()
# #     aspect = aspect.capitalize()
# #     gender_expression = gender_expression.lower()
    
# #     if planet not in VALID_PLANETS:
# #         print(f"Invalid planet. Choose from: {', '.join(VALID_PLANETS)}")
# #         return None
    
# #     if aspect not in VALID_ASPECTS:
# #         print(f"Invalid aspect. Choose from: {', '.join(VALID_ASPECTS)}")
# #         return None
    
# #     if gender_expression not in ["male", "female", "other"]:
# #         print("Invalid gender expression. Choose 'male', 'female', or 'other'")
# #         return None
    
# #     # Get the specific interpretation
# #     aspect_data = PLUTO_ASPECTS[planet].get(aspect)
# #     if not aspect_data:
# #         return None
    
# #     # Prepare the response
# #     interpretation = {
# #         "planet": planet,
# #         "aspect": aspect,
# #         "hook": aspect_data.hook,
# #         "core_interpretation": aspect_data.core_interpretation,
# #         "expression": getattr(aspect_data, f"{gender_expression}_expression")
# #     }
    
# #     return interpretation

# def get_pluto_aspect_interpretation(
#     planet: str,
#     aspect: str,
#     gender_expression: str = "other"
# ) -> dict:
#     """
#     Unified return for Pluto–planet aspects.

#     Always returns a dict with exactly:
#       - hook               : str
#       - core_description   : str
#       - gender_description : str
#     """
#     # 1) Lookup the aspects dict for this planet
#     planet_aspects = PLANET_ASPECTS.get(planet)
#     if not planet_aspects:
#         raise ValueError(f"No interpretations for Pluto–{planet}")

#     # 2) Find the specific aspect object
#     interp = planet_aspects.get(aspect)
#     if not interp:
#         raise ValueError(f"No {aspect} for Pluto–{planet}")

#     # 3) Choose gendered phrasing
#     attr = f"{gender_expression.lower()}_expression"
#     if not hasattr(interp, attr):
#         attr = "other_expression"
#     expr = getattr(interp, attr)

#     # 4) Return only the three standardized fields
#     return {
#         "hook": interp.hook,
#         "core_description": interp.core_interpretation,
#         "gender_description": expr
#     }

# def print_interpretation(interpretation):
#     """Helper function to nicely format and print an interpretation"""
#     if not interpretation:
#         print("No interpretation available for these parameters.")
#         return
    
#     print(f"\nPLUTO-{interpretation['planet']} {interpretation['aspect']}")
#     print("=" * 50)
#     print(f"HOOK: {interpretation['hook']}")
#     print(f"\nCORE MEANING:\n{interpretation['core_interpretation']}")
#     print(f"\nEXPRESSION:\n{interpretation['expression']}")
#     print("=" * 50)


# main_pluto_aspects.py

# Import all aspect interpretation dictionaries
from .pluto_and_sun_aspect_interpretation       import pluto_sun_aspects
from .pluto_and_moon_aspect_interpretation      import pluto_moon_aspects
from .pluto_and_mercury_aspect_interpretation   import pluto_mercury_aspects
from .pluto_and_venus_aspect_interpretation     import pluto_venus_aspects
from .pluto_and_mars_aspect_interpretation      import pluto_mars_aspects
from .pluto_and_jupiter_aspect_interpretation   import pluto_jupiter_aspects
from .pluto_and_saturn_aspect_interpretation    import pluto_saturn_aspects
from .pluto_and_neptune_aspect_interpretation   import pluto_neptune_aspects
from .pluto_and_ascendant_aspect_interpretation import pluto_ascendant_aspects
from .pluto_and_uranus_aspect_interpretation    import pluto_uranus_aspects

# Map each body to its aspect dictionary
PLANET_ASPECTS = {
    'Sun':       pluto_sun_aspects,
    'Moon':      pluto_moon_aspects,
    'Mercury':   pluto_mercury_aspects,
    'Venus':     pluto_venus_aspects,
    'Mars':      pluto_mars_aspects,
    'Jupiter':   pluto_jupiter_aspects,
    'Saturn':    pluto_saturn_aspects,
    'Neptune':   pluto_neptune_aspects,
    'Ascendant': pluto_ascendant_aspects,
    'Uranus':    pluto_uranus_aspects
}

# Map incoming aspect titles to the exact key used in the dicts
_ASPECT_ALIASES = {
    'conjunction': ['Conjunct', 'Conjunction'],
    'sextile':     ['Sextile', 'Sext'],
    'trine':       ['Trine'],
    'square':      ['Square'],
    'opposition':  ['Opposition', 'Opp']
}


def get_pluto_aspect_interpretation(
    planet: str,
    aspect: str,
    gender_expression: str = 'other'
) -> dict:
    """
    Unified return for Pluto–planet aspects.

    Always returns a dict with exactly:
      - hook               : str
      - core_description   : str
      - gender_description : str
    """
    # 1) Normalize aspect key via alias map
    raw_key = aspect.strip().capitalize()
    asp_key = _ASPECT_ALIASES.get(raw_key, raw_key)

    # 2) Lookup the aspects dict for this planet
    planet_aspects = PLANET_ASPECTS.get(planet)
    if not planet_aspects:
        raise ValueError(f"No interpretations for Pluto–{planet}")

    # 3) Find the specific aspect object
    interp = planet_aspects.get(asp_key)
    if not interp:
        raise ValueError(f"No {asp_key} for Pluto–{planet}")

    # 4) Choose gendered phrasing
    expr_attr = f"{gender_expression.lower()}_expression"
    if not hasattr(interp, expr_attr):
        expr_attr = 'other_expression'
    expression = getattr(interp, expr_attr)

    # 5) Return only the three standardized fields
    return {
        'hook': interp.hook,
        'core_description': interp.core_interpretation,
        'gender_description': expression
    }


# Example usage
# if __name__ == "__main__":
#     # Demo interpretation
#     print("PLUTO ASPECT INTERPRETER")
#     print("=" * 50)
    
#     # Get and display interpretation
#     interpretation = get_pluto_aspect_interpretation("Uranus", "Trine", "Male")
#     print_interpretation(interpretation)