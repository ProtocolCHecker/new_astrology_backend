# # main_sun_aspect_interpreter.py

# # Import all the aspect interpretation modules
# from .sun_and_ascendant_aspect_interpretation import sun_ascendant_aspects
# from .sun_and_jupiter_aspect_interpretation import sun_jupiter_aspects
# from .sun_and_mars_aspect_interpretation import sun_mars_aspects
# from .sun_and_mercury_aspect_interpretation import sun_mercury_aspects
# from .sun_and_moon_aspect_interpretation import sunn_moon_aspects
# from .sun_and_neptune_aspect_interpretation import sun_neptune_aspects
# from .sun_and_pluto_aspect_interpretation import sun_pluto_aspects
# from .sun_and_saturn_aspect_interpretation import sun_saturn_aspects
# from .sun_and_uranus_aspect_interpretation import sun_uranus_aspects
# from .sun_and_venus_aspect_interpretation import sun_venus_aspects

# # Dictionary mapping planets to their aspect dictionaries
# PLANET_ASPECTS = {
#     "Ascendant": sun_ascendant_aspects,
#     "Jupiter": sun_jupiter_aspects,
#     "Mars": sun_mars_aspects,
#     "Mercury": sun_mercury_aspects,
#     "Moon": sunn_moon_aspects,
#     "Neptune": sun_neptune_aspects,
#     "Pluto": sun_pluto_aspects,
#     "Saturn": sun_saturn_aspects,
#     "Uranus": sun_uranus_aspects,
#     "Venus": sun_venus_aspects
# }

# # def get_sun_aspect_interpretation(planet, aspect, gender_expression="other"):
# #     """
# #     Get the interpretation for a Sun planet aspect based on the aspect type and gender expression.
    
# #     Args:
# #         planet (str): The planet the Sun is aspecting (e.g., "Moon", "Venus")
# #         aspect (str): The type of aspect (e.g., "Conjunct", "Sextile")
# #         gender_expression (str): The gender expression to use ("male", "female", or "other")
    
# #     Returns:
# #         dict: A dictionary containing all interpretation components
# #     """
# #     # Get the correct planet's aspect dictionary
# #     planet_aspects = PLANET_ASPECTS.get(planet)
    
# #     if not planet_aspects:
# #         return {"error": f"Planet {planet} not found in interpretations"}
    
# #     # Get the specific aspect interpretation
# #     aspect_interpretation = planet_aspects.get(aspect)
    
# #     if not aspect_interpretation:
# #         return {"error": f"Aspect {aspect} not found for planet {planet}"}
    
# #     # Get the appropriate gender expression
# #     if gender_expression.lower() == "male":
# #         expression = aspect_interpretation.male_expression
# #     elif gender_expression.lower() == "female":
# #         expression = aspect_interpretation.female_expression
# #     else:
# #         expression = aspect_interpretation.other_expression
    
# #     # Return all components in a dictionary
# #     return {
# #         "planet": planet,
# #         "aspect": aspect,
# #         "hook": aspect_interpretation.hook,
# #         "core_interpretation": aspect_interpretation.core_interpretation,
# #         "gender_expression": gender_expression,
# #         "expression": expression
# #     }

# def get_sun_aspect_interpretation(
#     planet: str,
#     aspect: str,
#     gender_expression: str = "other"
# )  -> dict:
#     """
#     Unified return for Sun–planet aspects.

#     Always returns a dict with exactly:
#         hook               : str
#         core_description   : str
#         gender_description : str
#     """
#     # 1) Lookup the aspects dict for this planet
#     planet_aspects = PLANET_ASPECTS.get(planet)
#     if not planet_aspects:
#         raise ValueError(f"No interpretations for Sun–{planet}")

#     # 2) Find the specific aspect object
#     interp = planet_aspects.get(aspect)
#     if not interp:
#         raise ValueError(f"No {aspect} for Sun–{planet}")

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


# def display_interpretation(interpretation):
#     """Display the interpretation in a user friendly format"""
#     if "error" in interpretation:
#         print(f"Error: {interpretation['error']}")
#         return
    
#     print("\n" + "="*50)
#     print(f"Sun {interpretation['aspect']} {interpretation['planet']} Interpretation")
#     print("="*50)
#     print(f"\nHOOK: {interpretation['hook']}\n")
#     print("CORE INTERPRETATION:")
#     print(interpretation['core_interpretation'] + "\n")
#     print(f"{interpretation['gender_expression'].upper()} EXPRESSION:")
#     print(interpretation['expression'] + "\n")


# main_sun_aspects.py

# Import all aspect interpretation dictionaries
from .sun_and_ascendant_aspect_interpretation import sun_ascendant_aspects
from .sun_and_jupiter_aspect_interpretation    import sun_jupiter_aspects
from .sun_and_mars_aspect_interpretation       import sun_mars_aspects
from .sun_and_mercury_aspect_interpretation    import sun_mercury_aspects
from .sun_and_moon_aspect_interpretation       import sun_moon_aspects
from .sun_and_neptune_aspect_interpretation    import sun_neptune_aspects
from .sun_and_pluto_aspect_interpretation      import sun_pluto_aspects
from .sun_and_saturn_aspect_interpretation     import sun_saturn_aspects
from .sun_and_uranus_aspect_interpretation     import sun_uranus_aspects
from .sun_and_venus_aspect_interpretation      import sun_venus_aspects

# Map incoming aspect titles to the exact key your dict uses
_ASPECT_ALIASES = {
    'Conjunction': 'Conjunct',
    'Conjunct':   'Conjunct',
    'Sextile':    'Sextile',
    'Sext':       'Sextile',
    'Trine':      'Trine',
    'Square':     'Square',
    'Opposition': 'Opposition',
    'Opp':        'Opposition'
}


# Map each body to its aspect dictionary
PLANET_ASPECTS = {
    'Ascendant': sun_ascendant_aspects,
    'Jupiter':   sun_jupiter_aspects,
    'Mars':      sun_mars_aspects,
    'Mercury':   sun_mercury_aspects,
    'Moon':      sun_moon_aspects,
    'Neptune':   sun_neptune_aspects,
    'Pluto':     sun_pluto_aspects,
    'Saturn':    sun_saturn_aspects,
    'Uranus':    sun_uranus_aspects,
    'Venus':     sun_venus_aspects
}


def get_sun_aspect_interpretation(
    planet: str,
    aspect: str,
    gender_expression: str = 'other'
) -> dict:
    """
    Unified return for Sun–planet aspects.

    Always returns a dict with exactly:
      - hook               : str
      - core_description   : str
      - gender_description : str
    """
    # Normalize aspect key
    #asp_key = aspect.strip().capitalize()
    raw_key = aspect.strip().capitalize()
    asp_key = _ASPECT_ALIASES.get(raw_key, raw_key)


    # 1) Lookup the aspects dict for this planet
    planet_aspects = PLANET_ASPECTS.get(planet)
    if not planet_aspects:
        raise ValueError(f"No interpretations for Sun–{planet}")

    # 2) Find the specific aspect object
    interp = planet_aspects.get(asp_key)
    if not interp:
        raise ValueError(f"No {asp_key} for Sun–{planet}")

    # 3) Choose gendered phrasing
    expr_attr = f"{gender_expression.lower()}_expression"
    if not hasattr(interp, expr_attr):
        expr_attr = 'other_expression'
    expression = getattr(interp, expr_attr)

    # 4) Return only the three standardized fields
    return {
        'hook': interp.hook,
        'core_description': interp.core_interpretation,
        'gender_description': expression
    }



# # Example usage
# if __name__ == "__main__":
#     # Test with Sun Conjunct Moon
#     interpretation = get_sun_aspect_interpretation(
#         planet="Moon",
#         aspect="Conjunct",
#         gender_expression="other"
#     )
    
#     display_interpretation(interpretation)