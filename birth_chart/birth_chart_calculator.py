from astrology_calculator import AstrologyCalculator

def calculate_birth_chart(birth_date, birth_time, birth_place):
    """
    Calculate a birth chart from the provided information.

    Args:
        birth_date (tuple): Birth date as a tuple (year, month, day).
        birth_time (tuple): Birth time as a tuple (hour, minute, second).
        birth_place (str): Birth place as a string.

    Returns:
        dict: A dictionary containing birth chart information and chart data.
    """
    calculator = AstrologyCalculator()
    return calculator.calculate_birth_chart(birth_date, birth_time, birth_place)
