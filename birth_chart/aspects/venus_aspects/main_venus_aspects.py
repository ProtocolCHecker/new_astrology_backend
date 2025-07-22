# # venus_aspects_interpreter.py
# from .venus_and_sun_aspect_interpretation import venus_sun_aspects
# from .venus_and_moon_aspect_interpretation import venus_moon_aspects
# from .venus_and_mercury_aspect_interpretation import venus_mercury_aspects
# from .venus_and_mars_aspect_interpretation import venus_mars_aspects
# from .venus_and_jupiter_aspect_interpretation import venus_jupiter_aspects
# from .venus_and_saturn_aspect_interpretation import venus_saturn_aspects
# from .venus_and_uranus_aspect_interpretation import venus_uranus_aspects
# from .venus_and_neptune_aspect_interpretation import venus_neptune_aspects
# from .venus_and_pluto_aspect_interpretation import venus_pluto_aspects
# from .venus_and_ascendant_aspect_interpretation import venus_ascendant_aspects

# class VenusAspectInterpreter:
#     def __init__(self):
#         self.aspect_libraries = {
#             'sun': venus_sun_aspects,
#             'moon': venus_moon_aspects,
#             'mercury': venus_mercury_aspects,
#             'mars': venus_mars_aspects,
#             'jupiter': venus_jupiter_aspects,
#             'saturn': venus_saturn_aspects,
#             'uranus': venus_uranus_aspects,
#             'neptune': venus_neptune_aspects,
#             'pluto': venus_pluto_aspects,
#             'ascendant': venus_ascendant_aspects
#         }
        
#         self.valid_aspects = {
#             'conjunction', 'sextile', 'trine', 'square', 'opposition'
#         }
    
#     # def get_interpretation(self, planet, aspect, gender='other'):
#     #     """
#     #     Get Venus aspect interpretation for a planet and aspect
        
#     #     Parameters:
#     #     - planet: str (sun, moon, mercury, etc.)
#     #     - aspect: str (conjunction, sextile, trine, square, opposition)
#     #     - gender: str (male, female, other) - defaults to 'other'
        
#     #     Returns: dict with interpretation data or error message
#     #     """
#     #     planet = planet.lower()
#     #     aspect = aspect.lower()
#     #     gender = gender.lower()
        
#     #     # Validate inputs
#     #     if planet not in self.aspect_libraries:
#     #         return {'error': f"Invalid planet. Valid options are: {', '.join(self.aspect_libraries.keys())}"}
        
#     #     if aspect not in self.valid_aspects:
#     #         return {'error': f"Invalid aspect. Valid options are: {', '.join(self.valid_aspects)}"}
        
#     #     if gender not in {'male', 'female', 'other'}:
#     #         return {'error': "Invalid gender. Use 'male', 'female', or 'other'"}
        
#     #     # Get the aspect interpretation
#     #     try:
#     #         aspect_obj = self.aspect_libraries[planet][aspect.capitalize()]
            
#     #         return {
#     #             'planet': planet,
#     #             'aspect': aspect,
#     #             'hook': aspect_obj.hook,
#     #             'core_interpretation': aspect_obj.core_interpretation,
#     #             'interpretation': getattr(aspect_obj, f"{gender}_expression")
#     #         }
#     #     except KeyError:
#     #         return {'error': f"Aspect '{aspect}' not found for {planet}"}
#     #     except AttributeError:
#     #         return {'error': f"Could not retrieve interpretation for {planet} {aspect}"}
    
#     # def get_available_planets(self):
#     #     """Return list of available planets"""
#     #     return list(self.aspect_libraries.keys())
    
#     # def get_available_aspects(self):
#     #     """Return list of available aspects"""
#     #     return list(self.valid_aspects)

#     def get_venus_aspect_interpretation(
#         self,
#         planet: str,
#         aspect: str,
#         gender_expression: str = "other"
#     ) -> dict:
#         """
#         Unified return for Venus–planet aspects.

#         Always returns a dict with exactly:
#         - hook               : str
#         - core_description   : str
#         - gender_description : str
#         """
#         # 1) Lookup the aspects dict for this planet
#         planet_aspects = PLANET_ASPECTS.get(planet)
#         if not planet_aspects:
#             raise ValueError(f"No interpretations for Venus–{planet}")

#         # 2) Find the specific aspect object
#         interp = planet_aspects.get(aspect)
#         if not interp:
#             raise ValueError(f"No {aspect} for Venus–{planet}")

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


# main_venus_aspects.py

# Import all aspect interpretation dictionaries
from .venus_and_sun_aspect_interpretation import venus_sun_aspects
from .venus_and_moon_aspect_interpretation import venus_moon_aspects
from .venus_and_mercury_aspect_interpretation import venus_mercury_aspects
from .venus_and_mars_aspect_interpretation import venus_mars_aspects
from .venus_and_jupiter_aspect_interpretation import venus_jupiter_aspects
from .venus_and_saturn_aspect_interpretation import venus_saturn_aspects
from .venus_and_uranus_aspect_interpretation import venus_uranus_aspects
from .venus_and_neptune_aspect_interpretation import venus_neptune_aspects
from .venus_and_pluto_aspect_interpretation import venus_pluto_aspects
from .venus_and_ascendant_aspect_interpretation import venus_ascendant_aspects

class VenusAspectInterpreter:
    def __init__(self):
        # Map planet names to their respective aspect dictionaries
        self.aspect_libraries = {
            'Sun':        venus_sun_aspects,
            'Moon':       venus_moon_aspects,
            'Mercury':    venus_mercury_aspects,
            'Mars':       venus_mars_aspects,
            'Jupiter':    venus_jupiter_aspects,
            'Saturn':     venus_saturn_aspects,
            'Uranus':     venus_uranus_aspects,
            'Neptune':    venus_neptune_aspects,
            'Pluto':      venus_pluto_aspects,
            'Ascendant':  venus_ascendant_aspects
        }

    def get_venus_aspect_interpretation(
        self,
        planet: str,
        aspect: str,
        gender_expression: str = "other"
    ) -> dict:
        """
        Unified return for Venus–planet aspects.

        Always returns a dict with exactly:
          - hook               : str
          - core_description   : str
          - gender_description : str
        """
        # 1) Lookup the aspects dict for this planet
        planet_aspects = self.aspect_libraries.get(planet)
        if not planet_aspects:
            raise ValueError(f"No interpretations for Venus–{planet}")

        # 2) Find the specific aspect object
        interp = planet_aspects.get(aspect)
        if not interp:
            raise ValueError(f"No {aspect} for Venus–{planet}")

        # 3) Choose gendered phrasing
        attr = f"{gender_expression.lower()}_expression"
        if not hasattr(interp, attr):
            attr = "other_expression"
        expr = getattr(interp, attr)

        # 4) Return only the three standardized fields
        return {
            "hook": interp.hook,
            "core_description": interp.core_interpretation,
            "gender_description": expr
        }

# Instantiate a single interpreter for module-level function
_venus_interpreter = VenusAspectInterpreter()


def get_venus_aspect_interpretation(
    planet: str,
    aspect: str,
    gender_expression: str = "other"
) -> dict:
    """
    Module-level function for easy import and uniform signature.
    """
    return _venus_interpreter.get_venus_aspect_interpretation(
        planet=planet,
        aspect=aspect,
        gender_expression=gender_expression
    )


# # Example usage
# if __name__ == "__main__":
#     interpreter = VenusAspectInterpreter()
    
#     # Get an interpretation
#     result = interpreter.get_interpretation('mercury', 'square', 'female')
    
#     print(f"hook: {result["hook"]}")
#     print(f"Core interpretation: {result["core_interpretation"]}")
#     print(f"gender interpretation: {result["interpretation"]}")