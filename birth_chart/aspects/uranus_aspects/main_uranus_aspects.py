# # main_uranus_aspect_interpreter.py
# from .uranus_and_sun_aspect_interpretation import uranus_sun_aspects
# from .uranus_and_moon_aspect_interpretation import uranus_moon_aspects
# from .uranus_and_mercury_aspect_interpretation import uranus_mercury_aspects
# from .uranus_and_venus_aspect_interpretation import uranus_venus_aspects
# from .uranus_and_mars_aspect_interpretation import uranus_mars_aspects
# from .uranus_and_jupiter_aspect_interpretation import uranus_jupiter_aspects
# from .uranus_and_saturn_aspect_interpretation import uranus_saturn_aspects
# from .uranus_and_neptune_aspect_interpretation import uranus_neptune_aspects
# from .uranus_and_pluto_aspect_interpretation import uranus_pluto_aspects
# from .uranus_and_ascendant_aspect_interpretation import uranus_ascendant_aspects

# class UranusAspectInterpreter:
#     def __init__(self):
#         self.aspect_libraries = {
#             "sun": uranus_sun_aspects,
#             "moon": uranus_moon_aspects,
#             "mercury": uranus_mercury_aspects,
#             "venus": uranus_venus_aspects,
#             "mars": uranus_mars_aspects,
#             "jupiter": uranus_jupiter_aspects,
#             "saturn": uranus_saturn_aspects,
#             "neptune": uranus_neptune_aspects,
#             "pluto": uranus_pluto_aspects,
#             "ascendant": uranus_ascendant_aspects
#         }
        
#         self.valid_aspects = {
#             "conjunction", "sextile", "trine", 
#             "square", "opposition"
#         }
    
#     # def get_interpretation(self, planet, aspect, component="core"):
#     #     """
#     #     Get Uranus aspect interpretation components
        
#     #     Parameters:
#     #     - planet (str): lowercase planet name (e.g., "sun", "moon")
#     #     - aspect (str): aspect type (e.g., "conjunction", "sextile")
#     #     - component (str): which part to return. Options:
#     #         - "full" : returns complete interpretation object
#     #         - "hook" : just the hook phrase
#     #         - "core" : core interpretation (default)
#     #         - "male" : male expression
#     #         - "female" : female expression
#     #         - "other" : other/non-binary expression
#     #         - "all_expressions" : returns all gender expressions as dict
        
#     #     Returns: Requested component(s) or error message
#     #     """
#     #     # Normalize inputs
#     #     planet = planet.lower()
#     #     aspect = aspect.lower()
#     #     component = component.lower()
        
#     #     # Validate inputs
#     #     if planet not in self.aspect_libraries:
#     #         return f"Error: Unknown planet '{planet}'. Valid options: {list(self.aspect_libraries.keys())}"
        
#     #     if aspect not in self.valid_aspects:
#     #         return f"Error: Unknown aspect '{aspect}'. Valid options: {list(self.valid_aspects)}"
        
#     #     # Get interpretation object
#     #     aspect_title = aspect.capitalize()
#     #     interpretation = self.aspect_libraries[planet].get(aspect_title)
        
#     #     if not interpretation:
#     #         return f"Error: No interpretation found for {planet} {aspect}"
        
#     #     # Return requested component
#     #     if component == "full":
#     #         return interpretation
#     #     elif component == "hook":
#     #         return interpretation.hook
#     #     elif component == "core":
#     #         return interpretation.core_interpretation
#     #     elif component in ("male", "female", "other"):
#     #         return getattr(interpretation, f"{component}_expression")
#     #     elif component == "all_expressions":
#     #         return {
#     #             "male": interpretation.male_expression,
#     #             "female": interpretation.female_expression,
#     #             "other": interpretation.other_expression
#     #         }
#     #     else:
#     #         return f"Error: Unknown component '{component}'. Valid options: full, hook, core, male, female, other, all_expressions"
    
#     def get_uranus_aspect_interpretation(
#         self,
#         planet: str,
#         aspect: str,
#         gender_expression: str = "other"
#     ) -> dict:
#         """
#         Unified return for Uranus–planet aspects.

#         Always returns a dict with exactly:
#         - hook               : str
#         - core_description   : str
#         - gender_description : str
#         """
#         # 1) Lookup the aspects dict for this planet
#         planet_aspects = PLANET_ASPECTS.get(planet)
#         if not planet_aspects:
#             raise ValueError(f"No interpretations for Uranus–{planet}")

#         # 2) Find the specific aspect object
#         interp = planet_aspects.get(aspect)
#         if not interp:
#             raise ValueError(f"No {aspect} for Uranus–{planet}")

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

#     def list_available_combinations(self):
#         """Return all available planet-aspect combinations"""
#         combinations = []
#         for planet, aspects_dict in self.aspect_libraries.items():
#             for aspect in aspects_dict.keys():
#                 combinations.append(f"{planet} {aspect.lower()}")
#         return combinations

# main_uranus_aspects.py

# Import all aspect interpretation dictionaries
from .uranus_and_ascendant_aspect_interpretation import uranus_ascendant_aspects
from .uranus_and_sun_aspect_interpretation        import uranus_sun_aspects
from .uranus_and_moon_aspect_interpretation       import uranus_moon_aspects
from .uranus_and_mercury_aspect_interpretation    import uranus_mercury_aspects
from .uranus_and_venus_aspect_interpretation      import uranus_venus_aspects
from .uranus_and_mars_aspect_interpretation       import uranus_mars_aspects
from .uranus_and_jupiter_aspect_interpretation    import uranus_jupiter_aspects
from .uranus_and_saturn_aspect_interpretation     import uranus_saturn_aspects
from .uranus_and_neptune_aspect_interpretation    import uranus_neptune_aspects
from .uranus_and_pluto_aspect_interpretation      import uranus_pluto_aspects

class UranusAspectInterpreter:
    def __init__(self):
        # Map lowercase planet keys to their respective aspect dictionaries
        self.aspect_libraries = {
            'ascendant': uranus_ascendant_aspects,
            'sun':        uranus_sun_aspects,
            'moon':       uranus_moon_aspects,
            'mercury':    uranus_mercury_aspects,
            'venus':      uranus_venus_aspects,
            'mars':       uranus_mars_aspects,
            'jupiter':    uranus_jupiter_aspects,
            'saturn':     uranus_saturn_aspects,
            'neptune':    uranus_neptune_aspects,
            'pluto':      uranus_pluto_aspects
        }
        # Aliases for aspect naming inconsistencies
        self.aspect_aliases = {
            'conjunction': ['Conjunction', 'Conjunct'],
            'sextile':     ['Sextile'],
            'trine':       ['Trine'],
            'square':      ['Square'],
            'opposition':  ['Opposition']
        }

    def get_uranus_aspect_interpretation(
        self,
        planet: str,
        aspect: str,
        gender_expression: str = 'other'
    ) -> dict:
        """
        Unified return for Uranus–planet aspects.

        Always returns a dict with exactly:
          - hook               : str
          - core_description   : str
          - gender_description : str
        """
        # Normalize planet key
        key = planet.strip().lower()
        planet_aspects = self.aspect_libraries.get(key)
        if not planet_aspects:
            raise ValueError(f"No interpretations for Uranus–{planet}")

        # Normalize aspect and resolve alias
        asp_norm = aspect.strip().lower()
        candidates = self.aspect_aliases.get(asp_norm, [aspect.capitalize()])
        aspect_key = next((alias for alias in candidates if alias in planet_aspects), None)
        if not aspect_key:
            raise ValueError(
                f"Aspect '{aspect}' not found for Uranus–{planet}. "
                f"Available: {', '.join(planet_aspects.keys())}"
            )

        # Retrieve interpretation object
        interp = planet_aspects[aspect_key]

        # Choose gendered phrasing
        expr_attr = f"{gender_expression.lower()}_expression"
        if not hasattr(interp, expr_attr):
            expr_attr = 'other_expression'
        expr = getattr(interp, expr_attr)

        # Return only the three standardized fields
        return {
            'hook': interp.hook,
            'core_description': interp.core_interpretation,
            'gender_description': expr
        }

# Singleton instance for module-level function
_uranus_interpreter = UranusAspectInterpreter()


def get_uranus_aspect_interpretation(
    planet: str,
    aspect: str,
    gender_expression: str = 'other'
) -> dict:
    """
    Module-level function mirroring class method, for easy import.
    """
    return _uranus_interpreter.get_uranus_aspect_interpretation(
        planet=planet,
        aspect=aspect,
        gender_expression=gender_expression
    )


# # Example usage
# if __name__ == "__main__":
#     interpreter = UranusAspectInterpreter()
    
#     # Get an interpretation
#     print("--- Example Interpretation ---")
#     print(interpreter.get_interpretation("ascendant", "conjunction","full").core_interpretation)
    