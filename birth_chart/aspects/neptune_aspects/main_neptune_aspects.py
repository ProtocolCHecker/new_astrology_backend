# # Import all Neptune aspect interpretation files
# from .neptune_and_sun_aspect_interpretation import neptune_sun_aspects
# from .neptune_and_moon_aspect_interpretation import neptune_moon_aspects
# from .neptune_and_mercury_aspect_interpretation import neptune_mercury_aspects
# from .neptune_and_venus_aspect_interpretation import neptune_venus_aspects
# from .neptune_and_mars_aspect_interpretation import neptune_mars_aspects
# from .neptune_and_jupiter_aspect_interpretation import neptune_jupiter_aspects
# from .neptune_and_saturn_aspect_interpretation import neptune_saturn_aspects
# from .neptune_and_uranus_aspect_interpretation import neptune_uranus_aspects
# from .neptune_and_pluto_aspect_interpretation import neptune_pluto_aspects
# from .neptune_and_ascendant_aspect_interpretation import neptune_asc_aspects  # Updated import for Ascendant

# # Master dictionary mapping planets to their aspect interpretations
# neptune_aspects = {
#     "Sun": neptune_sun_aspects,
#     "Moon": neptune_moon_aspects,
#     "Mercury": neptune_mercury_aspects,
#     "Venus": neptune_venus_aspects,
#     "Mars": neptune_mars_aspects,
#     "Jupiter": neptune_jupiter_aspects,
#     "Saturn": neptune_saturn_aspects,
#     "Uranus": neptune_uranus_aspects,
#     "Pluto": neptune_pluto_aspects,
#     "Ascendant": neptune_asc_aspects  # Updated key to match the imported dictionary
# }

# # def get_neptune_aspect_interpretation(planet, aspect):
# #     """
# #     Retrieve the interpretation for a Neptune-Planet aspect.
    
# #     Args:
# #         planet (str): The planet (e.g., "Sun", "Moon", "Ascendant").
# #         aspect (str): The aspect (e.g., "Conjunction", "Sextile").
    
# #     Returns:
# #         Neptune[Planet]AspectInterpretation: The interpretation object.
# #     Raises:
# #         ValueError: If planet/aspect is invalid.
# #     """
# #     planet_aspects = neptune_aspects.get(planet)
# #     if not planet_aspects:
# #         raise ValueError(f"Planet '{planet}' not found. Valid options: {list(neptune_aspects.keys())}")
    
# #     interpretation = planet_aspects.get(aspect)
# #     if not interpretation:
# #         raise ValueError(f"Aspect '{aspect}' not found for Neptune-{planet}. Valid options: {list(planet_aspects.keys())}")
    
# #     return interpretation

# def get_neptune_aspect_interpretation(
#     planet: str,
#     aspect: str,
#     gender_expression: str = "other"
# ) -> dict:
#     """
#     Unified return for Neptune–planet aspects.

#     Always returns a dict with exactly:
#       - hook               : str
#       - core_description   : str
#       - gender_description : str
#     """
#     # 1) Lookup the aspects dict for this planet
#     planet_aspects = PLANET_ASPECTS.get(planet)
#     if not planet_aspects:
#         raise ValueError(f"No interpretations for Neptune–{planet}")

#     # 2) Find the specific aspect object
#     interp = planet_aspects.get(aspect)
#     if not interp:
#         raise ValueError(f"No {aspect} for Neptune–{planet}")

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

# main_neptune_aspects.py

# Import all aspect interpretation dictionaries
from .neptune_and_sun_aspect_interpretation      import neptune_sun_aspects
from .neptune_and_moon_aspect_interpretation     import neptune_moon_aspects
from .neptune_and_mercury_aspect_interpretation import neptune_mercury_aspects
from .neptune_and_venus_aspect_interpretation   import neptune_venus_aspects
from .neptune_and_mars_aspect_interpretation    import neptune_mars_aspects
from .neptune_and_jupiter_aspect_interpretation import neptune_jupiter_aspects
from .neptune_and_saturn_aspect_interpretation  import neptune_saturn_aspects
from .neptune_and_uranus_aspect_interpretation  import neptune_uranus_aspects
from .neptune_and_pluto_aspect_interpretation   import neptune_pluto_aspects
from .neptune_and_ascendant_aspect_interpretation import neptune_asc_aspects

# Map each body to its aspect dictionary
PLANET_ASPECTS = {
    'Sun':       neptune_sun_aspects,
    'Moon':      neptune_moon_aspects,
    'Mercury':   neptune_mercury_aspects,
    'Venus':     neptune_venus_aspects,
    'Mars':      neptune_mars_aspects,
    'Jupiter':   neptune_jupiter_aspects,
    'Saturn':    neptune_saturn_aspects,
    'Uranus':    neptune_uranus_aspects,
    'Pluto':     neptune_pluto_aspects,
    'Ascendant': neptune_asc_aspects
}

# Map incoming aspect titles to the exact key used in the dicts
aSpect_aliases = {
    'conjunction': ['Conjunct', 'Conjunction'],
    'sextile':     ['Sextile', 'Sext'],
    'trine':       ['Trine'],
    'square':      ['Square'],
    'opposition':  ['Opposition', 'Opp']
}

def get_neptune_aspect_interpretation(
    planet: str,
    aspect: str,
    gender_expression: str = 'other'
) -> dict:
    """
    Unified return for Neptune–planet aspects.

    Always returns a dict with exactly:
      - hook               : str
      - core_description   : str
      - gender_description : str
    """
    # 1) Normalize the aspect key via alias map
    raw_key = aspect.strip().capitalize()
    asp_key = aSpect_aliases.get(raw_key, raw_key)

    # 2) Lookup the aspects dict for this planet
    planet_aspects = PLANET_ASPECTS.get(planet)
    if not planet_aspects:
        raise ValueError(f"No interpretations for Neptune–{planet}")

    # 3) Find the specific aspect object
    interp = planet_aspects.get(asp_key)
    if not interp:
        raise ValueError(f"No {asp_key} for Neptune–{planet}")

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


# # Example usage
# if __name__ == "__main__":
#     # Example 1: Neptune-Ascendant Conjunction
#     asc_conj = get_neptune_aspect_interpretation("Mercury", "Conjunction")
#     print("=== Neptune-Ascendant Conjunction ===")
#     print("Hook:", asc_conj.hook)
#     print("Core Interpretation:", asc_conj.core_interpretation)
#     print("Female Expression:", asc_conj.female_expression)

#     # Example 2: Neptune-Mars Square
#     mars_square = get_neptune_aspect_interpretation("Moon", "Square")
#     print("\n=== Neptune-Mars Square ===")
#     print("Hook:", mars_square.hook)
#     print("Other Expression:", mars_square.other_expression)