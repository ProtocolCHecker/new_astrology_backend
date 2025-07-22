# # main_script.py
# from .jupiter_and_ascendant_aspect_interpretation import jupiter_ascendant_aspects
# from .jupiter_and_mars_aspect_interpretation import jupiter_mars_aspects
# from .jupiter_and_mercury_aspect_interpretation import jupiter_mercury_aspects
# from .jupiter_and_moon_aspect_interpretation import jupiter_moon_aspects
# from .jupiter_and_neptune_aspect_interpretation import jupiter_neptune_aspects
# from .jupiter_and_pluto_aspect_interpretation import jupiter_pluto_aspects
# from .jupiter_and_saturn_aspect_interpretation import jupiter_saturn_aspects
# from .jupiter_and_sun_aspect_interpretation import jupiter_sun_aspects
# from .jupiter_and_uranus_aspect_interpretation import jupiter_uranus_aspects
# from .jupiter_and_venus_aspect_interpretation import jupiter_venus_aspects

# # Dictionary mapping planets to their respective aspect dictionaries
# planet_aspects = {
#     "Ascendant": jupiter_ascendant_aspects,
#     "Mars": jupiter_mars_aspects,
#     "Mercury": jupiter_mercury_aspects,
#     "Moon": jupiter_moon_aspects,
#     "Neptune": jupiter_neptune_aspects,
#     "Pluto": jupiter_pluto_aspects,
#     "Saturn": jupiter_saturn_aspects,
#     "Sun": jupiter_sun_aspects,
#     "Uranus": jupiter_uranus_aspects,
#     "Venus": jupiter_venus_aspects
# }

# # def get_jupiter_aspect_interpretation(planet, aspect, gender_expression="other"):
# #     """
# #     Retrieve Jupiter aspect interpretation for a given planet and aspect.
    
# #     Parameters:
# #     - planet (str): The planet Jupiter is aspecting (e.g., "Sun", "Moon", "Mars")
# #     - aspect (str): The type of aspect (e.g., "Conjunct", "Sextile", "Trine")
# #     - gender_expression (str): The gender expression to use ("male", "female", or "other")
    
# #     Returns:
# #     - dict: A dictionary containing the interpretation components
# #     """
# #     # Get the aspect dictionary for the specified planet
# #     planet_dict = planet_aspects.get(planet)
# #     if not planet_dict:
# #         return {"error": f"No interpretations available for Jupiter-{planet} aspects"}
    
# #     # Get the specific aspect interpretation
# #     aspect_interpretation = planet_dict.get(aspect)
# #     if not aspect_interpretation:
# #         return {"error": f"No {aspect} interpretation available for Jupiter-{planet}"}
    
# #     # Determine which expression to use based on gender_expression
# #     if gender_expression.lower() == "male":
# #         expression = aspect_interpretation.male_expression
# #     elif gender_expression.lower() == "female":
# #         expression = aspect_interpretation.female_expression
# #     else:
# #         expression = aspect_interpretation.other_expression
    
# #     # Return all relevant information
# #     return {
# #         "planet": planet,
# #         "aspect": aspect,
# #         "hook": aspect_interpretation.hook,
# #         "core_interpretation": aspect_interpretation.core_interpretation,
# #         "gender_expression": gender_expression,
# #         "expression": expression
# #     }

# def get_jupiter_aspect_interpretation(
#     planet: str,
#     aspect: str,
#     gender_expression: str = "other"
# ) -> dict:
#     """
#     Unified return for Jupiter–planet aspects.

#     Always returns a dict with exactly:
#       - hook               : str
#       - core_description   : str
#       - gender_description : str
#     """
#     # 1) Lookup the aspects dict for this planet
#     planet_aspects = PLANET_ASPECTS.get(planet)
#     if not planet_aspects:
#         raise ValueError(f"No interpretations for Jupiter–{planet}")

#     # 2) Find the specific aspect object
#     interp = planet_aspects.get(aspect)
#     if not interp:
#         raise ValueError(f"No {aspect} for Jupiter–{planet}")

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
#     """Helper function to print the interpretation in a readable format"""
#     if "error" in interpretation:
#         print(interpretation["error"])
#         return
    
#     print(f"\nJupiter {interpretation['aspect']} {interpretation['planet']} Interpretation")
#     print("=" * 50)
#     print(f"\nHook: {interpretation['hook']}")
#     print(f"\nCore Interpretation:\n{interpretation['core_interpretation']}")
#     print(f"\n{interpretation['gender_expression'].title()} Expression:\n{interpretation['expression']}")
#     print("\n" + "=" * 50)

# main_jupiter_aspects.py

# main_jupiter_aspects.py

# Import all aspect interpretation dictionaries
from .jupiter_and_ascendant_aspect_interpretation import jupiter_ascendant_aspects
from .jupiter_and_sun_aspect_interpretation        import jupiter_sun_aspects
from .jupiter_and_moon_aspect_interpretation      import jupiter_moon_aspects
from .jupiter_and_mercury_aspect_interpretation   import jupiter_mercury_aspects
from .jupiter_and_venus_aspect_interpretation     import jupiter_venus_aspects
from .jupiter_and_mars_aspect_interpretation      import jupiter_mars_aspects
from .jupiter_and_saturn_aspect_interpretation    import jupiter_saturn_aspects
from .jupiter_and_uranus_aspect_interpretation    import jupiter_uranus_aspects
from .jupiter_and_neptune_aspect_interpretation  import jupiter_neptune_aspects
from .jupiter_and_pluto_aspect_interpretation     import jupiter_pluto_aspects

# Map incoming aspect titles to the exact key your dict uses
_ASPECT_ALIASES = {
    'conjunction': ['Conjunct', 'Conjunction'],
    'sextile':     ['Sextile', 'Sext'],
    'trine':       ['Trine'],
    'square':      ['Square'],
    'opposition':  ['Opposition', 'Opp']
}

# Dictionary mapping planets to their aspect dictionaries
PLANET_ASPECTS = {
    'Ascendant': jupiter_ascendant_aspects,
    'Sun':       jupiter_sun_aspects,
    'Moon':      jupiter_moon_aspects,
    'Mercury':   jupiter_mercury_aspects,
    'Venus':     jupiter_venus_aspects,
    'Mars':      jupiter_mars_aspects,
    'Saturn':    jupiter_saturn_aspects,
    'Uranus':    jupiter_uranus_aspects,
    'Neptune':   jupiter_neptune_aspects,
    'Pluto':     jupiter_pluto_aspects
}


def get_jupiter_aspect_interpretation(
    planet: str,
    aspect: str,
    gender_expression: str = 'other'
) -> dict:
    """
    Unified return for Jupiter–planet aspects.

    Returns a dict with exactly:
      - hook               : str
      - core_description   : str
      - gender_description : str
    """
    # 1) Normalize canonical key and find candidates
    asp_norm   = aspect.strip().lower()
    candidates = _ASPECT_ALIASES.get(asp_norm, [aspect.strip().capitalize()])

    # 2) Lookup the aspect dict for this planet
    planet_aspects = PLANET_ASPECTS.get(planet)
    if not planet_aspects:
        raise ValueError(f"No interpretations for Jupiter–{planet}")

    # 3) Resolve the actual dict key
    asp_key = next((alias for alias in candidates if alias in planet_aspects), None)
    if not asp_key:
        raise ValueError(f"No '{aspect}' (tried {candidates}) for Jupiter–{planet}")

    # 4) Retrieve interpretation object
    interp = planet_aspects[asp_key]

    # 5) Choose gendered phrasing
    expr_attr = f"{gender_expression.lower()}_expression"
    if not hasattr(interp, expr_attr):
        expr_attr = 'other_expression'
    expression = getattr(interp, expr_attr)

    # 6) Return only the three standardized fields
    return {
        'hook': interp.hook,
        'core_description': interp.core_interpretation,
        'gender_description': expression
    }


# # Example usage
# if __name__ == "__main__":
#     # Test with Jupiter conjunct Sun for female expression
#     interpretation = get_jupiter_aspect_interpretation("Venus", "Conjunction", "female")
#     print_interpretation(interpretation)