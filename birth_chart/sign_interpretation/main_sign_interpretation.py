# main_interpretation.py

from .sun_sign_interpretation import sun_signs           
from .moon_sign_interpretation import moon_signs         
from .mercury_in_signs_interpretation import mercury_signs  
from .venus_in_signs_interpretation import venus_signs     
from .mars_in_signs_interpretation import mars_signs       
from .jupiter_in_signs_interpretation import jupiter_signs 
from .saturn_in_signs_interpretation import saturn_signs   
from .uranus_in_signs_interpretation import uranus_signs   
from .neptune_in_signs_interpretation import neptune_signs 
from .ascendant_in_signs_interpretation import ascendant_signs 
from .pluto_in_signs_interpretation import pluto_signs 

# Map each planet to its sign interpretation dict
planet_interpretations = {
    "Sun": sun_signs,
    "Moon": moon_signs,
    "Mercury": mercury_signs,
    "Venus": venus_signs,
    "Mars": mars_signs,
    "Jupiter": jupiter_signs,
    "Saturn": saturn_signs,
    "Uranus": uranus_signs,
    "Neptune": neptune_signs,
    "Ascendant": ascendant_signs,
    "Pluto": pluto_signs
}

def interpret(planet: str, sign: str, gender: str = "male")  -> str:
    """
    Return a formatted interpretation for the given planet in the given sign,
    using the specified gender expression ("male", "female", or "other"/"nonbinary").
    """
    planet = planet.capitalize()
    sign = sign.capitalize()
    if planet not in planet_interpretations:
        raise ValueError(f"Unknown planet: {planet}")
    if sign not in planet_interpretations[planet]:
        raise ValueError(f"{planet} has no interpretation for sign '{sign}'")
    obj = planet_interpretations[planet][sign]

    # pick the gender specific field, falling back to 'other_expression' if needed
    expr_attr = {
        "male": "male_expression",
        "female": "female_expression",
        "nonbinary": "nonbinary_expression",
        "other": "other_expression"
    }.get(gender.lower(), "other_expression")

    gender_text = getattr(obj, expr_attr, obj.other_expression)

    return (
        f"{planet} in {sign}\n"
        f"Hook: {obj.hook}\n\n"
        f"Core: {obj.core_interpretation}\n\n"
        f"Specially for you: {gender_text}"
    )

if __name__ == "__main__":
    # Example test: Sun in Aries, nonbinary
    print( interpret("Sun", "Aries", gender="nonbinary") )
