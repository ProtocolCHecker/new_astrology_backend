from compatibility.birth_chart_calculator import calculate_birth_chart

def get_sun_sign(birth_chart: dict) -> str:
    """
    Extracts and returns the Sun sign from a birth-chart dict.
    """
    return birth_chart['chart_data']['planets']['Sun']['sign']



