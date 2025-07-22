# main_mercury_aspect_interpreter.py

# # Import all aspect interpretation dictionaries
# from .mercury_and_moon_aspect_interpretation import mercury_moon_aspects
# from .sun_and_moon_aspect_interpretation import sun_moon_aspects
# from .venus_and_moon_aspect_interpretation import venus_moon_aspects
# from .mars_and_moon_aspect_interpretation import moon_mars_aspects
# from .jupiter_and_moon_aspect_interpretation import jupiter_moon_aspects
# from .saturn_and_moon_aspect_interpretation import saturn_moon_aspects
# from .uranus_and_moon_aspect_interpretation import uranus_moon_aspects
# from .neptune_and_moon_aspect_interpretation import moon_neptune_aspects
# from .pluto_and_moon_aspect_interpretation import pluto_moon_aspects
# from .ascendant_and_moon_aspect_interpretation import moon_ascendant_aspects

# class MoonAspectInterpreter:
#     def __init__(self):
#         # Map planet names to their respective aspect dictionaries
#         self.aspect_libraries = {
#             "Sun": sun_moon_aspects,
#             "Moon": mercury_moon_aspects,  # Mercury Moon is already in mercury_moon_aspects
#             "Mercury": mercury_moon_aspects,  # Self aspect would be handled differently
#             "Venus": venus_moon_aspects,
#             "Mars": moon_mars_aspects,
#             "Jupiter": jupiter_moon_aspects,
#             "Saturn": saturn_moon_aspects,
#             "Uranus": uranus_moon_aspects,
#             "Neptune": moon_neptune_aspects,
#             "Pluto": pluto_moon_aspects,
#             "Ascendant": moon_ascendant_aspects
#         }
    
#     # def get_interpretation(self, planet, aspect, expression_type="core"):
#     #     """
#     #     Get the interpretation for a Mercury Planet aspect
        
#     #     Parameters:
#     #       planet: The planet Mercury is aspecting (e.g., "Sun", "Moon", "Venus")
#     #       aspect: The aspect type (e.g., "Conjunction", "Sextile", "Square")
#     #       expression_type: Which interpretation to return 
#     #            ("core", "male", "female", or "other")
        
#     #     Returns: The requested interpretation as a string
#     #     """
#     #     # Get the correct aspect dictionary
#     #     aspects = self.aspect_libraries.get(planet)
        
#     #     if not aspects:
#     #         return f"No interpretations available for Mercury {planet} aspects"
        
#     #     # Get the specific aspect interpretation
#     #     aspect_interp = aspects.get(aspect)
        
#     #     if not aspect_interp:
#     #         return f"No interpretation available for {aspect} aspect between Mercury and {planet}"
        
#     #     # Return the requested expression type
#     #     if expression_type == "male":
#     #         return aspect_interp.male_expression
#     #     elif expression_type == "female":
#     #         return aspect_interp.female_expression
#     #     elif expression_type == "other":
#     #         return aspect_interp.other_expression
#     #     else:  # Default to core interpretation
#     #         return aspect_interp.core_interpretation
    
#     # def get_all_interpretations(self, planet, aspect):
#     #     """
#     #     Get all interpretations for a Mercury Planet aspect
        
#     #     Parameters:
#     #       planet: The planet Mercury is aspecting
#     #       aspect: The aspect type
        
#     #     Returns: Dictionary with all interpretation types
#     #     """
#     #     aspects = self.aspect_libraries.get(planet)
#     #     if not aspects:
#     #         return None
        
#     #     aspect_interp = aspects.get(aspect)
#     #     if not aspect_interp:
#     #         return None
        
#     #     return {
#     #         "hook": aspect_interp.hook,
#     #         "core": aspect_interp.core_interpretation,
#     #         "male": aspect_interp.male_expression,
#     #         "female": aspect_interp.female_expression,
#     #         "other": aspect_interp.other_expression
#     #     }

#     def get_moon_aspect_interpretation(
#         self,
#         planet: str,
#         aspect: str,
#         gender_expression: str = "other"
#     )  -> dict:
#         """
#         Unified return for Moon planet aspects.

#         Always returns a dict with exactly:
#           hook               : str
#           core_description   : str
#           gender_description : str
#         """
#         # 1) Lookup the aspects dict for this planet
#         planet_aspects = PLANET_ASPECTS.get(planet)
#         if not planet_aspects:
#             raise ValueError(f"No interpretations for Moon {planet}")

#         # 2) Find the specific aspect object
#         interp = planet_aspects.get(aspect)
#         if not interp:
#             raise ValueError(f"No {aspect} for Moon {planet}")

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


# main_moon_aspects.py

# Import all aspect interpretation dictionaries
from .sun_and_moon_aspect_interpretation import sun_moon_aspects
from .mercury_and_moon_aspect_interpretation import mercury_moon_aspects
from .venus_and_moon_aspect_interpretation import venus_moon_aspects
from .mars_and_moon_aspect_interpretation import moon_mars_aspects
from .jupiter_and_moon_aspect_interpretation import jupiter_moon_aspects
from .saturn_and_moon_aspect_interpretation import saturn_moon_aspects
from .uranus_and_moon_aspect_interpretation import uranus_moon_aspects
from .neptune_and_moon_aspect_interpretation import moon_neptune_aspects
from .pluto_and_moon_aspect_interpretation import pluto_moon_aspects
from .ascendant_and_moon_aspect_interpretation import moon_ascendant_aspects

class MoonAspectInterpreter:
    def __init__(self):
        # Map planet names to their respective aspect dictionaries
        self.aspect_libraries = {
            "Sun":        sun_moon_aspects,
            "Mercury":    mercury_moon_aspects,
            "Venus":      venus_moon_aspects,
            "Mars":       moon_mars_aspects,
            "Jupiter":    jupiter_moon_aspects,
            "Saturn":     saturn_moon_aspects,
            "Uranus":     uranus_moon_aspects,
            "Neptune":    moon_neptune_aspects,
            "Pluto":      pluto_moon_aspects,
            "Ascendant":  moon_ascendant_aspects
        }

    def get_moon_aspect_interpretation(
        self,
        planet: str,
        aspect: str,
        gender_expression: str = "other"
    ) -> dict:
        """
        Unified return for Moon–planet aspects.

        Always returns a dict with exactly:
          - hook               : str
          - core_description   : str
          - gender_description : str
        """
        # 1) Lookup the aspects dict for this planet
        planet_aspects = self.aspect_libraries.get(planet)
        if not planet_aspects:
            raise ValueError(f"No interpretations for Moon–{planet}")

        # 2) Find the specific aspect object
        interp = planet_aspects.get(aspect)
        if not interp:
            raise ValueError(f"No {aspect} for Moon–{planet}")

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
_moon_interpreter = MoonAspectInterpreter()


def get_moon_aspect_interpretation(
    planet: str,
    aspect: str,
    gender_expression: str = "other"
) -> dict:
    """
    Module-level function mirroring class method, for easy import.
    """
    return _moon_interpreter.get_moon_aspect_interpretation(
        planet=planet,
        aspect=aspect,
        gender_expression=gender_expression
    )


# # Example usage
# if __name__ == "__main__":
#     interpreter = MoonAspectInterpreter()
    
#     # Get a single interpretation
#     print("    Mercury Sun Conjunction (Core)    ")
#     print(interpreter.get_interpretation("Ascendant", "Conjunction"))
    # print("\n    Mercury Moon Square (Male)    ")
    # print(interpreter.get_interpretation("Moon", "Square", "male"))
    
    # # Get all interpretations for an aspect
    # print("\n    Mercury Venus Trine (All)    ")
    # all_interps = interpreter.get_all_interpretations("Venus", "Trine")
    # for key, value in all_interps.items():
    #     print(f"\n{key.capitalize()}:")
    #     print(value)