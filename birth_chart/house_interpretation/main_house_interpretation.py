# main_astrology_interpretation.py
from .ascendant_in_houses_interpretation import ascendant_houses
from .jupiter_in_houses_interpretation import jupiter_houses
from .mars_in_houses_interpretation import mars_houses
from .mercury_in_houses_interpretation import mercury_houses
from .moon_in_houses_interpretation import moon_houses
from .neptune_in_houses_interpretation import neptune_houses
from .pluto_in_houses_interpretation import pluto_houses
from .saturn_in_houses_interpretation import saturn_houses
from .sun_in_houses_interpretation import sun_houses
from .uranus_in_houses_interpretation import uranus_houses
from .venus_in_houses_interpretation import venus_houses

# Dictionary mapping planet names to their house interpretation dictionaries
PLANET_INTERPRETATIONS = {
    "jupiter": jupiter_houses,
    "mars": mars_houses,
    "mercury": mercury_houses,
    "moon": moon_houses,
    "neptune": neptune_houses,
    "pluto": pluto_houses,
    "saturn": saturn_houses,
    "sun": sun_houses,
    "uranus": uranus_houses,
    "venus": venus_houses,
    "ascendant": ascendant_houses
}

def get_interpretation(planet, house, gender="other"):
    """
    Get the interpretation for a planet in a specific house with gender specific expression.
    
    Args:
        planet (str): Name of the planet (e.g., "sun", "moon", "venus")
        house (str): House number (e.g., "1st", "2nd", "3rd")
        gender (str): Gender expression ("male", "female", or "other")
    
    Returns:
        dict: Dictionary containing all interpretation components
    """
    planet = planet.lower()
    house = house.lower()
    
    # Get the planet's house interpretations
    planet_data = PLANET_INTERPRETATIONS.get(planet)
    if not planet_data:
        raise ValueError(f"Invalid planet: {planet}. Available planets are: {list(PLANET_INTERPRETATIONS.keys())}")
    
    # Get the specific house interpretation
    house_interpretation = planet_data.get(house)
    if not house_interpretation:
        raise ValueError(f"Invalid house: {house}. Available houses are: {list(planet_data.keys())}")
    
    # Prepare the interpretation based on gender
    interpretation = {
        "planet": planet.capitalize(),
        "house": house,
        "hook": house_interpretation.hook,
        "core_interpretation": house_interpretation.core_interpretation,
        "interpretation": getattr(house_interpretation, f"{gender}_expression")
    }
    
    return interpretation

def print_interpretation(interpretation):
    """Print the interpretation in a readable format"""
    print(f"\n{interpretation['planet']} in {interpretation['house']} House")
    print("━" * 50)
    print(f"⚡ {interpretation['hook']}")
    print(f"\n{interpretation['core_interpretation']}")
    print(f"\n✨ {interpretation['interpretation']}\n")

# Example usage
if __name__ == "__main__":
    # Test with Sun in 5th House for female expression
    interpretation = get_interpretation("ascendant", "5th", "female")
    print_interpretation(interpretation)