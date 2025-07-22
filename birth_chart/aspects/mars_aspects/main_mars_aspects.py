# # main.py
# from .mars_and_ascendant_aspect_interpretation import MarsAscendantAspectInterpretation, mars_ascendant_aspects
# from .mars_and_jupiter_aspect_interpretation import MarsJupiterAspectInterpretation, mars_jupiter_aspects
# from .mars_and_mercury_aspect_interpretation import MercuryMarsAspectInterpretation, mercury_mars_aspects
# from .mars_and_moon_aspect_interpretation import MoonMarsAspectInterpretation, moon_mars_aspects
# from .mars_and_neptune_aspect_interpretation import MarsNeptuneAspectInterpretation, mars_neptune_aspects
# from .mars_and_pluto_aspect_interpretation import MarsPlutoAspectInterpretation, mars_pluto_aspects
# from .mars_and_saturn_aspect_interpretation import MarsSaturnAspectInterpretation, mars_saturn_aspects
# from .mars_and_sun_aspect_interpretation import SunMarsAspectInterpretation, sun_mars_aspects
# from .mars_and_uranus_aspect_interpretation import MarsUranusAspectInterpretation, mars_uranus_aspects
# from .mars_and_venus_aspect_interpretation import VenusMarsAspectInterpretation, venus_mars_aspects

# class MarsAspectInterpreter:
#     def __init__(self):
#         # Map planet names to their respective aspect dictionaries
#         self.aspect_libraries = {
#             'ascendant': mars_ascendant_aspects,
#             'jupiter': mars_jupiter_aspects,
#             'mercury': mercury_mars_aspects,
#             'moon': moon_mars_aspects,
#             'neptune': mars_neptune_aspects,
#             'pluto': mars_pluto_aspects,
#             'saturn': mars_saturn_aspects,
#             'sun': sun_mars_aspects,
#             'uranus': mars_uranus_aspects,
#             'venus': venus_mars_aspects
#         }
        
#         # Standardize aspect names across different files
#         self.aspect_name_mapping = {
#             'conjunction': ['Conjunct', 'Conjunction'],
#             'sextile': ['Sextile'],
#             'trine': ['Trine'],
#             'square': ['Square'],
#             'opposition': ['Opposition']
#         }
    
#     # def get_interpretation(self, planet, aspect, gender_expression='other'):
#     #     """
#     #     Get the Mars aspect interpretation for a given planet and aspect type.
        
#     #     Parameters:
#     #         planet (str): The planet Mars is in aspect with (e.g., 'sun', 'moon', 'venus')
#     #         aspect (str): The type of aspect (e.g., 'conjunction', 'sextile', 'square')
#     #         gender_expression (str): Which gender expression to return ('male', 'female', or 'other')
        
#     #     Returns:
#     #         dict: A dictionary containing the hook and interpretation for the requested aspect
#     #     """
#     #     # Normalize input
#     #     planet = planet.lower()
#     #     aspect = aspect.lower()
#     #     gender_expression = gender_expression.lower()
        
#     #     # Check if planet is valid
#     #     if planet not in self.aspect_libraries:
#     #         raise ValueError(f"Invalid planet. Available options: {', '.join(self.aspect_libraries.keys())}")
        
#     #     # Check if aspect is valid and find the correct key in the aspect dictionary
#     #     aspect_key = None
#     #     for asp, aliases in self.aspect_name_mapping.items():
#     #         if aspect == asp:
#     #             # Try each possible alias for this aspect
#     #             for alias in aliases:
#     #                 if alias in self.aspect_libraries[planet]:
#     #                     aspect_key = alias
#     #                     break
#     #             break
        
#     #     if not aspect_key:
#     #         available_aspects = set()
#     #         for aliases in self.aspect_name_mapping.values():
#     #             available_aspects.update(aliases)
#     #         raise ValueError(f"Invalid aspect. Available options: {', '.join(available_aspects)}")
        
#     #     # Get the aspect interpretation object
#     #     aspect_obj = self.aspect_libraries[planet].get(aspect_key)
#     #     if not aspect_obj:
#     #         raise ValueError(f"Aspect '{aspect_key}' not found for planet {planet}")
        
#     #     # Get the requested gender expression
#     #     if gender_expression == 'male':
#     #         expression = aspect_obj.male_expression
#     #     elif gender_expression == 'female':
#     #         expression = aspect_obj.female_expression
#     #     else:
#     #         expression = aspect_obj.other_expression
        
#     #     # Return the interpretation data
#     #     return {
#     #         'planet': planet,
#     #         'aspect': aspect_key,
#     #         'hook': aspect_obj.hook,
#     #         'core_interpretation': aspect_obj.core_interpretation,
#     #         'gender_expression': gender_expression,
#     #         'expression': expression
#     #     }

#     def get_mars_aspect_interpretation(
#         self,
#         planet: str,
#         aspect: str,
#         gender_expression: str = "other"
#     ) -> dict:
#         """
#         Unified return for Mars–planet aspects.

#         Always returns a dict with exactly:
#         - hook               : str
#         - core_description   : str
#         - gender_description : str
#         """
#         # 1) Lookup the aspects dict for this planet
#         planet_aspects = PLANET_ASPECTS.get(planet)
#         if not planet_aspects:
#             raise ValueError(f"No interpretations for Mars–{planet}")

#         # 2) Find the specific aspect object
#         interp = planet_aspects.get(aspect)
#         if not interp:
#             raise ValueError(f"No {aspect} for Mars–{planet}")

#         # 3) Choose gendered phrasing (male/female → specific, otherwise other)
#         attr = f"{gender_expression.lower()}_expression"
#         if not hasattr(interp, attr):
#             attr = "other_expression"
#         expr = getattr(interp, attr)

#         # 4) Return only the three standardized fields
#         return {
#             "hook": interp.hook,
#             "core_description": interp.core_interpretation,
#             "gender_description": expr
#         }


# main_mars_aspects.py

# Import all aspect interpretation dictionaries
from .mars_and_ascendant_aspect_interpretation import mars_ascendant_aspects
from .mars_and_sun_aspect_interpretation import sun_mars_aspects
from .mars_and_moon_aspect_interpretation import moon_mars_aspects
from .mars_and_mercury_aspect_interpretation import mercury_mars_aspects
from .mars_and_venus_aspect_interpretation import venus_mars_aspects
from .mars_and_jupiter_aspect_interpretation import mars_jupiter_aspects
from .mars_and_saturn_aspect_interpretation import mars_saturn_aspects
from .mars_and_uranus_aspect_interpretation import mars_uranus_aspects
from .mars_and_neptune_aspect_interpretation import mars_neptune_aspects
from .mars_and_pluto_aspect_interpretation import mars_pluto_aspects

class MarsAspectInterpreter:
    def __init__(self):
        # Map planet keys (lowercase) to their respective aspect dictionaries
        self.aspect_libraries = {
            'ascendant': mars_ascendant_aspects,
            'sun':       sun_mars_aspects,
            'moon':      moon_mars_aspects,
            'mercury':   mercury_mars_aspects,
            'venus':     venus_mars_aspects,
            'jupiter':   mars_jupiter_aspects,
            'saturn':    mars_saturn_aspects,
            'uranus':    mars_uranus_aspects,
            'neptune':   mars_neptune_aspects,
            'pluto':     mars_pluto_aspects
        }
        # Standardize possible aspect names (aliases)
        self.aspect_aliases = {
            'conjunction': ['Conjunct', 'Conjunction'],
            'sextile':     ['Sextile'],
            'trine':       ['Trine'],
            'square':      ['Square'],
            'opposition':  ['Opposition']
        }

    def get_mars_aspect_interpretation(
        self,
        planet: str,
        aspect: str,
        gender_expression: str = 'other'
    ) -> dict:
        """
        Unified return for Mars–planet aspects.

        Always returns a dict with exactly:
          - hook               : str
          - core_description   : str
          - gender_description : str
        """
        # Normalize planet key
        key = planet.strip().lower()
        planet_aspects = self.aspect_libraries.get(key)
        if not planet_aspects:
            raise ValueError(f"No interpretations for Mars–{planet}")

        # Normalize aspect and resolve alias
        asp_norm = aspect.strip().lower()
        candidates = self.aspect_aliases.get(asp_norm, [aspect])
        aspect_key = None
        for alias in candidates:
            if alias in planet_aspects:
                aspect_key = alias
                break
        if not aspect_key:
            raise ValueError(
                f"Aspect '{aspect}' not found for Mars–{planet}. "
                f"Available: {', '.join(planet_aspects.keys())}"
            )

        # Retrieve interpretation object
        interp = planet_aspects[aspect_key]

        # Choose gendered phrasing
        attr = f"{gender_expression.lower()}_expression"
        if not hasattr(interp, attr):
            attr = 'other_expression'
        expr = getattr(interp, attr)

        # Return only the three standardized fields
        return {
            'hook': interp.hook,
            'core_description': interp.core_interpretation,
            'gender_description': expr
        }

# Instantiate a single interpreter for module-level function
_mars_interpreter = MarsAspectInterpreter()


def get_mars_aspect_interpretation(
    planet: str,
    aspect: str,
    gender_expression: str = 'other'
) -> dict:
    """
    Module-level function for easy import and uniform signature.
    """
    return _mars_interpreter.get_mars_aspect_interpretation(
        planet=planet,
        aspect=aspect,
        gender_expression=gender_expression
    )


# Example usage
# if __name__ == "__main__":
#     interpreter = MarsAspectInterpreter()
    
#     # Test with Mars square Venus
#     try:
#         interpretation = interpreter.get_interpretation('Pluto', 'square', 'female')
#         print("\nMars Square Venus Interpretation (Female Expression):")
#         print(f"Hook: {interpretation['hook']}")
#         print(f"\nCore Interpretation: {interpretation['core_interpretation']}")
#         print(f"\nExpression: {interpretation['expression']}")
        
#         # Print separator
#         print("\n" + "="*80 + "\n")
        
#         # Test with Mars conjunct Sun
#         interpretation = interpreter.get_interpretation('Uranus', 'conjunction', 'male')
#         print("Mars Conjunct Sun Interpretation (Male Expression):")
#         print(f"Hook: {interpretation['hook']}")
#         print(f"\nCore Interpretation: {interpretation['core_interpretation']}")
#         print(f"\nExpression: {interpretation['expression']}")
        
#     except ValueError as e:
#         print(f"Error: {e}")