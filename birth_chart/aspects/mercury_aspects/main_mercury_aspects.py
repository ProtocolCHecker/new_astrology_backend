# # Static imports of Mercury aspect interpretation modules
# from .mercury_and_ascendant_aspect_interpretation import MercuryAscendantAspectInterpretation, mercury_ascendant_aspects
# from .mercury_and_sun_aspect_interpretation        import MercurySunAspectInterpretation, mercury_sun_aspects
# from .mercury_and_moon_aspect_interpretation       import MercuryMoonAspectInterpretation, mercury_moon_aspects
# from .mercury_and_venus_aspect_interpretation      import MercuryVenusAspectInterpretation, mercury_venus_aspects
# from .mercury_and_mars_aspect_interpretation       import MercuryMarsAspectInterpretation, mercury_mars_aspects
# from .mercury_and_jupiter_aspect_interpretation    import MercuryJupiterAspectInterpretation, mercury_jupiter_aspects
# from .mercury_and_saturn_aspect_interpretation     import MercurySaturnAspectInterpretation, mercury_saturn_aspects
# from .mercury_and_uranus_aspect_interpretation     import MercuryUranusAspectInterpretation, mercury_uranus_aspects
# from .mercury_and_neptune_aspect_interpretation    import MercuryNeptuneAspectInterpretation, mercury_neptune_aspects
# from .mercury_and_pluto_aspect_interpretation      import MercuryPlutoAspectInterpretation, mercury_pluto_aspects


# class MercuryAspectInterpreter:
#     def __init__(self):
#         # Map planet names to their respective aspect dictionaries
#         self.aspect_libraries = {
#             'ascendant': mercury_ascendant_aspects,
#             'sun':        mercury_sun_aspects,
#             'moon':       mercury_moon_aspects,
#             'venus':      mercury_venus_aspects,
#             'mars':       mercury_mars_aspects,
#             'jupiter':    mercury_jupiter_aspects,
#             'saturn':     mercury_saturn_aspects,
#             'uranus':     mercury_uranus_aspects,
#             'neptune':    mercury_neptune_aspects,
#             'pluto':      mercury_pluto_aspects
#         }

#         # Standardize aspect names across different files
#         self.aspect_name_mapping = {
#             'conjunction': ['Conjunct', 'Conjunction'],
#             'sextile':     ['Sextile'],
#             'trine':       ['Trine'],
#             'square':      ['Square'],
#             'opposition':  ['Opposition']
#         }

#     # def get_interpretation(self, planet: str, aspect: str, gender_expression: str = 'other') -> dict:
#     #     """
#     #     Get the Mercury aspect interpretation for a given planet and aspect type.

#     #     Parameters:
#     #         planet (str): The planet Mercury is in aspect with (e.g., 'sun', 'moon', 'venus')
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
#     #             for alias in aliases:
#     #                 if alias in self.aspect_libraries[planet]:
#     #                     aspect_key = alias
#     #                     break
#     #             break

#     #     if not aspect_key:
#     #         available_aspects = {alias for aliases in self.aspect_name_mapping.values() for alias in aliases}
#     #         raise ValueError(f"Invalid aspect. Available options: {', '.join(sorted(available_aspects))}")

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

#     def get_mercury_aspect_interpretation(
#         self,
#         planet: str,
#         aspect: str,
#         gender_expression: str = "other"
#     ) -> dict:
#         """
#         Unified return for Mercury–planet aspects.

#         Always returns a dict with exactly:
#         - hook               : str
#         - core_description   : str
#         - gender_description : str
#         """
#         # 1) Lookup the aspects dict for this planet
#         planet_aspects = PLANET_ASPECTS.get(planet)
#         if not planet_aspects:
#             raise ValueError(f"No interpretations for Mercury–{planet}")

#         # 2) Find the specific aspect object
#         interp = planet_aspects.get(aspect)
#         if not interp:
#             raise ValueError(f"No {aspect} for Mercury–{planet}")

#         # 3) Choose gendered phrasing
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

# main_mercury_aspects.py

# Static imports of Mercury aspect interpretation modules
from .mercury_and_ascendant_aspect_interpretation import mercury_ascendant_aspects
from .mercury_and_sun_aspect_interpretation        import mercury_sun_aspects
from .mercury_and_moon_aspect_interpretation       import mercury_moon_aspects
from .mercury_and_venus_aspect_interpretation      import mercury_venus_aspects
from .mercury_and_mars_aspect_interpretation       import mercury_mars_aspects
from .mercury_and_jupiter_aspect_interpretation    import mercury_jupiter_aspects
from .mercury_and_saturn_aspect_interpretation     import mercury_saturn_aspects
from .mercury_and_uranus_aspect_interpretation     import mercury_uranus_aspects
from .mercury_and_neptune_aspect_interpretation    import mercury_neptune_aspects
from .mercury_and_pluto_aspect_interpretation      import mercury_pluto_aspects

class MercuryAspectInterpreter:
    def __init__(self):
        # Map planet names to their respective aspect dictionaries
        # keys are lowercase counterparts of the planetary bodies
        self.aspect_libraries = {
            'ascendant': mercury_ascendant_aspects,
            'sun':        mercury_sun_aspects,
            'moon':       mercury_moon_aspects,
            'venus':      mercury_venus_aspects,
            'mars':       mercury_mars_aspects,
            'jupiter':    mercury_jupiter_aspects,
            'saturn':     mercury_saturn_aspects,
            'uranus':     mercury_uranus_aspects,
            'neptune':    mercury_neptune_aspects,
            'pluto':      mercury_pluto_aspects
        }
        # Map normalized aspect names to possible keys in the dicts
        self.aspect_aliases = {
            'conjunction': ['Conjunction', 'Conjunct'],
            'sextile':     ['Sextile'],
            'trine':       ['Trine'],
            'square':      ['Square'],
            'opposition':  ['Opposition']
        }

    def get_mercury_aspect_interpretation(
        self,
        planet: str,
        aspect: str,
        gender_expression: str = 'other'
    ) -> dict:
        """
        Unified return for Mercury–planet aspects.

        Always returns a dict with exactly:
          - hook               : str
          - core_description   : str
          - gender_description : str
        """
        # Normalize planet key
        key = planet.strip().lower()
        aspects = self.aspect_libraries.get(key)
        if not aspects:
            raise ValueError(f"No interpretations for Mercury–{planet}")

        # Normalize aspect and resolve alias
        asp_norm = aspect.strip().lower()
        candidates = self.aspect_aliases.get(asp_norm, [aspect])
        aspect_key = None
        for alias in candidates:
            if alias in aspects:
                aspect_key = alias
                break
        if not aspect_key:
            raise ValueError(
                f"Aspect '{aspect}' not found for Mercury–{planet}. "
                f"Available: {', '.join(aspects.keys())}"
            )

        # Retrieve interpretation object
        interp = aspects[aspect_key]

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
_mercury_interpreter = MercuryAspectInterpreter()


def get_mercury_aspect_interpretation(
    planet: str,
    aspect: str,
    gender_expression: str = 'other'
) -> dict:
    """
    Module-level function for easy import and uniform signature.
    """
    return _mercury_interpreter.get_mercury_aspect_interpretation(
        planet=planet,
        aspect=aspect,
        gender_expression=gender_expression
    )


# # Example usage
# if __name__ == "__main__":
#     interpreter = MercuryAspectInterpreter()

#     # Test with Mercury square Venus (female expression)
#     try:
#         interpretation = interpreter.get_interpretation('ascendant', 'square', 'female')
#         print("\nMercury Square Venus Interpretation (Female):")
#         print(f"Hook: {interpretation['hook']}")
#         print(f"Core Interpretation: {interpretation['core_interpretation']}")
#         print(f"Expression: {interpretation['expression']}")
#     except ValueError as e:
#         print(f"Error: {e}")
