# # main_saturn_aspect_interpreter.py
# from .saturn_and_sun_aspect_interpretation import saturn_sun_aspects
# from .saturn_and_moon_aspect_interpretation import saturn_moon_aspects
# from .saturn_and_mercury_aspect_interpretation import saturn_mercury_aspects
# from .saturn_and_venus_aspect_interpretation import saturn_venus_aspects
# from .saturn_and_mars_aspect_interpretation import saturn_mars_aspects
# from .saturn_and_jupiter_aspect_interpretation import saturn_jupiter_aspects
# from .saturn_and_uranus_aspect_interpretation import saturn_uranus_aspects
# from .saturn_and_neptune_aspect_interpretation import saturn_neptune_aspects
# from .saturn_and_pluto_aspect_interpretation import saturn_pluto_aspects
# from .saturn_and_ascendant_aspect_interpretation import saturn_ascendant_aspects

# class SaturnAspectInterpreter:
#     def __init__(self):
#         self.aspect_libraries = {
#             'sun': saturn_sun_aspects,
#             'moon': saturn_moon_aspects,
#             'mercury': saturn_mercury_aspects,
#             'venus': saturn_venus_aspects,
#             'mars': saturn_mars_aspects,
#             'jupiter': saturn_jupiter_aspects,
#             'uranus': saturn_uranus_aspects,
#             'neptune': saturn_neptune_aspects,
#             'pluto': saturn_pluto_aspects,
#             'ascendant': saturn_ascendant_aspects
#         }
        
#         self.valid_aspects = {
#             'conjunction', 'sextile', 'trine', 'square', 'opposition',
#             'conj', 'sex', 'tri', 'squ', 'opp'  # Allow abbreviations
#         }
        
#         self.aspect_mapping = {
#             'conj': 'Conjunction',
#             'sex': 'Sextile',
#             'tri': 'Trine',
#             'squ': 'Square',
#             'opp': 'Opposition'
#         }

#     # def get_interpretation(self, planet, aspect, gender='other'):
#     #     """
#     #     Get Saturn aspect interpretation for a specific planet and aspect type
        
#     #     Parameters:
#     #     - planet (str): The other planet (e.g., 'sun', 'moon', 'venus')
#     #     - aspect (str): Aspect type (e.g., 'conjunction', 'square', 'trine')
#     #     - gender (str): 'male', 'female', or 'other' (default)
        
#     #     Returns: Dictionary containing all interpretation components
#     #     """
#     #     # Normalize inputs
#     #     planet = planet.lower()
#     #     aspect = aspect.lower()
#     #     gender = gender.lower()
        
#     #     # Validate planet
#     #     if planet not in self.aspect_libraries:
#     #         raise ValueError(f"Invalid planet. Available options: {', '.join(self.aspect_libraries.keys())}")
        
#     #     # Validate and normalize aspect
#     #     if aspect not in self.valid_aspects:
#     #         raise ValueError(f"Invalid aspect. Available options: {', '.join(self.valid_aspects)}")
        
#     #     # Map abbreviations to full aspect names
#     #     if aspect in self.aspect_mapping:
#     #         aspect = self.aspect_mapping[aspect]
#     #     else:
#     #         # Capitalize first letter if not already
#     #         aspect = aspect.capitalize()
        
#     #     # Get the aspect interpretation
#     #     try:
#     #         interpretation = self.aspect_libraries[planet][aspect]
#     #     except KeyError:
#     #         raise ValueError(f"No interpretation found for {planet} {aspect}")
        
#     #     # Select gender-specific expression
#     #     gender_expressions = {
#     #         'male': interpretation.male_expression,
#     #         'female': interpretation.female_expression,
#     #         'other': interpretation.other_expression
#     #     }
        
#     #     gender = gender if gender in gender_expressions else 'other'
        
#     #     return {
#     #         'hook': interpretation.hook,
#     #         'core_interpretation': interpretation.core_interpretation,
#     #         'gender_expression': gender_expressions[gender],
#     #         'aspect': interpretation.aspect,
#     #         'planet': planet
#     #     }

#     def get_saturn_aspect_interpretation(
#         self,
#         planet: str,
#         aspect: str,
#         gender_expression: str = "other"
#     ) -> dict:
#         """
#         Unified return for Saturn–planet aspects.

#         Always returns a dict with exactly:
#         - hook               : str
#         - core_description   : str
#         - gender_description : str
#         """
#         # 1) Lookup the aspects dict for this planet
#         planet_aspects = PLANET_ASPECTS.get(planet)
#         if not planet_aspects:
#             raise ValueError(f"No interpretations for Saturn–{planet}")

#         # 2) Find the specific aspect object
#         interp = planet_aspects.get(aspect)
#         if not interp:
#             raise ValueError(f"No {aspect} for Saturn–{planet}")

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


#     def print_interpretation(self, planet, aspect, gender='other'):
#         """Print formatted interpretation to console"""
#         interpretation = self.get_interpretation(planet, aspect, gender)
        
#         print(f"\nSATURN-{interpretation['planet'].upper()} {interpretation['aspect'].upper()} INTERPRETATION")
#         print("=" * 50)
#         print(f"\n{interpretation['hook']}\n")
#         print(f"CORE MEANING:")
#         print(f"{interpretation['core_interpretation']}\n")
#         print(f"GENDER EXPRESSION ({gender}):")
#         print(f"{interpretation['gender_expression']}\n")
#         print("=" * 50)

# main_saturn_aspects.py

# Import all aspect interpretation dictionaries
from .saturn_and_ascendant_aspect_interpretation import saturn_ascendant_aspects
from .saturn_and_sun_aspect_interpretation         import saturn_sun_aspects
from .saturn_and_moon_aspect_interpretation        import saturn_moon_aspects
from .saturn_and_mercury_aspect_interpretation     import saturn_mercury_aspects
from .saturn_and_venus_aspect_interpretation       import saturn_venus_aspects
from .saturn_and_mars_aspect_interpretation        import saturn_mars_aspects
from .saturn_and_jupiter_aspect_interpretation     import saturn_jupiter_aspects
from .saturn_and_uranus_aspect_interpretation      import saturn_uranus_aspects
from .saturn_and_neptune_aspect_interpretation     import saturn_neptune_aspects
from .saturn_and_pluto_aspect_interpretation       import saturn_pluto_aspects

class SaturnAspectInterpreter:
    def __init__(self):
        # Map lowercase planet keys to their respective aspect dictionaries
        self.aspect_libraries = {
            'ascendant': saturn_ascendant_aspects,
            'sun':        saturn_sun_aspects,
            'moon':       saturn_moon_aspects,
            'mercury':    saturn_mercury_aspects,
            'venus':      saturn_venus_aspects,
            'mars':       saturn_mars_aspects,
            'jupiter':    saturn_jupiter_aspects,
            'uranus':     saturn_uranus_aspects,
            'neptune':    saturn_neptune_aspects,
            'pluto':      saturn_pluto_aspects
        }
        # Aliases for aspect naming inconsistencies
        self.aspect_aliases = {
            'conjunction': ['Conjunction', 'Conjunct'],
            'sextile':     ['Sextile'],
            'trine':       ['Trine'],
            'square':      ['Square'],
            'opposition':  ['Opposition']
        }

    def get_saturn_aspect_interpretation(
        self,
        planet: str,
        aspect: str,
        gender_expression: str = 'other'
    ) -> dict:
        """
        Unified return for Saturn–planet aspects.

        Always returns a dict with exactly:
          - hook               : str
          - core_description   : str
          - gender_description : str
        """
        # Normalize planet key
        key = planet.strip().lower()
        planet_aspects = self.aspect_libraries.get(key)
        if not planet_aspects:
            raise ValueError(f"No interpretations for Saturn–{planet}")

        # Normalize aspect and resolve alias
        asp_norm = aspect.strip().lower()
        candidates = self.aspect_aliases.get(asp_norm, [aspect.capitalize()])
        # Pick first matching alias in the dict
        aspect_key = next((alias for alias in candidates if alias in planet_aspects), None)
        if not aspect_key:
            raise ValueError(
                f"Aspect '{aspect}' not found for Saturn–{planet}. "
                f"Available: {', '.join(planet_aspects.keys())}"
            )

        # Get interpretation object
        interp = planet_aspects[aspect_key]

        # Choose gendered phrasing
        attr = f"{gender_expression.lower()}_expression"
        if not hasattr(interp, attr):
            attr = 'other_expression'
        expr = getattr(interp, attr)

        # Return only standardized fields
        return {
            'hook': interp.hook,
            'core_description': interp.core_interpretation,
            'gender_description': expr
        }

# Singleton instance for module-level function
_saturn_interpreter = SaturnAspectInterpreter()


def get_saturn_aspect_interpretation(
    planet: str,
    aspect: str,
    gender_expression: str = 'other'
) -> dict:
    """
    Module-level function for easy import and uniform signature.
    """
    return _saturn_interpreter.get_saturn_aspect_interpretation(
        planet=planet,
        aspect=aspect,
        gender_expression=gender_expression
    )


# # Example usage
# if __name__ == "__main__":
#     interpreter = SaturnAspectInterpreter()
    
#     # Sample queries
#     interpreter.print_interpretation('venus', 'conjunction', 'female')
#     interpreter.print_interpretation('mars', 'square')
#     interpreter.print_interpretation('moon', 'opp', 'male')
    
#     # Get interpretation as dictionary for programmatic use
#     jupiter_trine = interpreter.get_interpretation('jupiter', 'trine')
#     print(f"\nJupiter Trine Hook: {jupiter_trine['hook']}")