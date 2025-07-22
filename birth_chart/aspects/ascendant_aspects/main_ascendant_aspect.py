# # main_ascendant_aspect_interpreter.py

# # Import all the ascendant aspect interpretation modules
# from .ascendant_and_moon_aspect_interpretation import moon_ascendant_aspects
# from .jupiter_and_ascendant_aspect_interpretation import jupiter_ascendant_aspects
# from .mars_and_ascendant_aspect_interpretation import mars_ascendant_aspects
# from .mercury_and_ascendant_aspect_interpretation import mercury_ascendant_aspects
# from .neptune_and_ascendant_aspect_interpretation import neptune_ascendant_aspects
# from .pluto_and_ascendant_aspect_interpretation import pluto_ascendant_aspects
# from .saturn_and_ascendant_aspect_interpretation import saturn_ascendant_aspects
# from .sun_and_ascendant_aspect_interpretation import sun_ascendant_aspects
# from .uranus_and_ascendant_aspect_interpretation import uranus_ascendant_aspects
# from .venus_and_ascendant_aspect_interpretation import venus_ascendant_aspects

# # Dictionary mapping planets to their aspect dictionaries
# PLANET_ASPECTS = {
#     "Moon": moon_ascendant_aspects,
#     "Jupiter": jupiter_ascendant_aspects,
#     "Mars": mars_ascendant_aspects,
#     "Mercury": mercury_ascendant_aspects,
#     "Neptune": neptune_ascendant_aspects,
#     "Pluto": pluto_ascendant_aspects,
#     "Saturn": saturn_ascendant_aspects,
#     "Sun": sun_ascendant_aspects,
#     "Uranus": uranus_ascendant_aspects,
#     "Venus": venus_ascendant_aspects
# }

# # def get_ascendant_aspect_interpretation(planet, aspect, gender_expression="other"):
# #     """
# #     Get the interpretation for an Ascendant planet aspect based on the aspect type and gender expression.
    
# #     Args:
# #         planet (str): The planet aspecting the Ascendant (e.g., "Moon", "Venus")
# #         aspect (str): The type of aspect (e.g., "Conjunction", "Sextile")
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

# def get_ascendant_aspect_interpretation(
#     planet: str,
#     aspect: str,
#     gender_expression: str = "other"
# )  -> dict:
#     """
#     Unified return for Ascendant planet aspects.

#     Returns a dict with exactly:
#         hook               : str
#         core_description   : str
#         gender_description : str
#     """
#     # 1) Lookup the aspects dict for this planet
#     planet_aspects = PLANET_ASPECTS.get(planet)
#     if not planet_aspects:
#         raise ValueError(f"No interpretations for Ascendant–{planet}")

#     # 2) Find the specific aspect object
#     interp = planet_aspects.get(aspect)
#     if not interp:
#         raise ValueError(f"No {aspect} for Ascendant–{planet}")

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
#     print(f"Ascendant {interpretation['aspect']} {interpretation['planet']} Interpretation")
#     print("="*50)
#     print(f"\nHOOK: {interpretation['hook']}\n")
#     print("CORE INTERPRETATION:")
#     print(interpretation['core_interpretation'] + "\n")
#     print(f"{interpretation['gender_expression'].upper()} EXPRESSION:")
#     print(interpretation['expression'] + "\n")


# main_ascendant_aspect_interpreter.py

# # Import all the ascendant aspect interpretation modules
# from .ascendant_and_moon_aspect_interpretation      import moon_ascendant_aspects
# from .jupiter_and_ascendant_aspect_interpretation   import jupiter_ascendant_aspects
# from .mars_and_ascendant_aspect_interpretation      import mars_ascendant_aspects
# from .mercury_and_ascendant_aspect_interpretation   import mercury_ascendant_aspects
# from .neptune_and_ascendant_aspect_interpretation   import neptune_ascendant_aspects
# from .pluto_and_ascendant_aspect_interpretation     import pluto_ascendant_aspects
# from .saturn_and_ascendant_aspect_interpretation    import saturn_ascendant_aspects
# from .sun_and_ascendant_aspect_interpretation       import sun_ascendant_aspects
# from .uranus_and_ascendant_aspect_interpretation    import uranus_ascendant_aspects
# from .venus_and_ascendant_aspect_interpretation     import venus_ascendant_aspects

# # Map canonical aspect names to possible keys in the aspect dicts
# _ASPECT_ALIASES = {
#     'conjunction': ['Conjunct',   'Conjunction'],
#     'sextile':     ['Sextile'],
#     'trine':       ['Trine'],
#     'square':      ['Square'],
#     'opposition':  ['Opposition']
# }

# # Dictionary mapping planets to their aspect dictionaries
# PLANET_ASPECTS = {
#     'Moon':      moon_ascendant_aspects,
#     'Jupiter':   jupiter_ascendant_aspects,
#     'Mars':      mars_ascendant_aspects,
#     'Mercury':   mercury_ascendant_aspects,
#     'Neptune':   neptune_ascendant_aspects,
#     'Pluto':     pluto_ascendant_aspects,
#     'Saturn':    saturn_ascendant_aspects,
#     'Sun':       sun_ascendant_aspects,
#     'Uranus':    uranus_ascendant_aspects,
#     'Venus':     venus_ascendant_aspects
# }


# def get_ascendant_aspect_interpretation(
#     planet: str,
#     aspect: str,
#     gender_expression: str = 'other'
# ) -> dict:
#     """
#     Unified return for Ascendant–planet aspects.

#     Returns a dict with exactly:
#       - hook               : str
#       - core_description   : str
#       - gender_description : str
#     """
#     # 1) Normalize & resolve the aspect key
#     asp_norm   = aspect.strip().lower()
#     candidates = _ASPECT_ALIASES.get(asp_norm, [aspect.strip().capitalize()])

#     # 2) Lookup the aspects dict for this planet
#     planet_aspects = PLANET_ASPECTS.get(planet)
#     if not planet_aspects:
#         raise ValueError(f"No interpretations for Ascendant–{planet}")

#     # 3) Pick the first alias that exists
#     for asp_key in candidates:
#         if asp_key in planet_aspects:
#             break
#     else:
#         raise ValueError(f"No '{aspect}' (tried {candidates}) for Ascendant–{planet}")

#     interp = planet_aspects[asp_key]

#     # 4) Choose gendered phrasing
#     attr = f"{gender_expression.lower()}_expression"
#     if not hasattr(interp, attr):
#         attr = 'other_expression'
#     expr = getattr(interp, attr)

#     # 5) Return only the three standardized fields
#     return {
#         'hook': interp.hook,
#         'core_description': interp.core_interpretation,
#         'gender_description': expr
#     }


# def display_interpretation(interpretation):
#     """Display the interpretation in a user friendly format"""
#     if 'hook' not in interpretation:
#         print(f"Error: {interpretation.get('error', 'Invalid interpretation')}" )
#         return
#     print("\n" + "="*50)
#     print(f"Ascendant {interpretation['aspect']} {interpretation['other']} Interpretation")
#     print("="*50)
#     print(f"\nHOOK: {interpretation['hook']}\n")
#     print("CORE INTERPRETATION:")
#     print(interpretation['core_description'] + "\n")
#     print(f"{interpretation['gender_description'].upper()} EXPRESSION:")
#     print(interpretation['gender_description'] + "\n")


# main_ascendant_aspect_interpreter.py

# main_ascendant_aspect_interpreter.py

# Import all the ascendant aspect interpretation modules
from .ascendant_and_moon_aspect_interpretation      import moon_ascendant_aspects
from .jupiter_and_ascendant_aspect_interpretation   import jupiter_ascendant_aspects
from .mars_and_ascendant_aspect_interpretation      import mars_ascendant_aspects
from .mercury_and_ascendant_aspect_interpretation   import mercury_ascendant_aspects
from .neptune_and_ascendant_aspect_interpretation   import neptune_ascendant_aspects
from .pluto_and_ascendant_aspect_interpretation     import pluto_ascendant_aspects
from .saturn_and_ascendant_aspect_interpretation    import saturn_ascendant_aspects
from .sun_and_ascendant_aspect_interpretation       import sun_ascendant_aspects
from .uranus_and_ascendant_aspect_interpretation    import uranus_ascendant_aspects
from .venus_and_ascendant_aspect_interpretation     import venus_ascendant_aspects

# Map canonical aspect names to lists of possible dict keys
_ASPECT_ALIASES = {
    'conjunction': ['Conjunct', 'Conjunction'],
    'sextile':     ['Sextile'],
    'trine':       ['Trine'],
    'square':      ['Square'],
    'opposition':  ['Opposition']
}

# Dictionary mapping planets to their aspect dictionaries
PLANET_ASPECTS = {
    'Moon':      moon_ascendant_aspects,
    'Jupiter':   jupiter_ascendant_aspects,
    'Mars':      mars_ascendant_aspects,
    'Mercury':   mercury_ascendant_aspects,
    'Neptune':   neptune_ascendant_aspects,
    'Pluto':     pluto_ascendant_aspects,
    'Saturn':    saturn_ascendant_aspects,
    'Sun':       sun_ascendant_aspects,
    'Uranus':    uranus_ascendant_aspects,
    'Venus':     venus_ascendant_aspects
}


def get_ascendant_aspect_interpretation(
    planet: str,
    aspect: str,
    gender_expression: str = 'other'
) -> dict:
    """
    Unified return for Ascendant–planet aspects.

    Always returns a dict with exactly:
      - hook               : str
      - core_description   : str
      - gender_description : str
    """
    # 1) Normalize canonical key
    asp_norm   = aspect.strip().lower()
    candidates = _ASPECT_ALIASES.get(asp_norm, [aspect.strip().capitalize()])

    # 2) Lookup the aspect dict for this planet
    planet_aspects = PLANET_ASPECTS.get(planet)
    if not planet_aspects:
        raise ValueError(f"No interpretations for Ascendant–{planet}")

    # 3) Find the first matching alias in the dict
    asp_key = next((key for key in candidates if key in planet_aspects), None)
    if not asp_key:
        raise ValueError(f"No '{aspect}' (tried {candidates}) for Ascendant–{planet}")

    interp = planet_aspects[asp_key]

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


def display_interpretation(interpretation):
    """Display the interpretation in a user friendly format"""
    if 'hook' not in interpretation:
        print(f"Error: {interpretation.get('error', 'Invalid interpretation')}" )
        return

    print("\n" + "="*50)
    print(f"Ascendant {interpretation['aspect']} {interpretation['other']} Interpretation")
    print("="*50)
    print(f"\nHOOK: {interpretation['hook']}\n")
    print("CORE INTERPRETATION:")
    print(interpretation['core_description'] + "\n")
    print(f"{interpretation['gender_description'].upper()} EXPRESSION:")
    print(interpretation['gender_description'] + "\n")


# # Example usage
# if __name__ == "__main__":
#     # Test with Ascendant Conjunct Moon (female expression)
#     interpretation = get_ascendant_aspect_interpretation(
#         planet="Moon",
#         aspect="Conjunction",
#         gender_expression="female"
#     )
    
#     display_interpretation(interpretation)