# from astrology_calculator import AstrologyCalculator

# def calculate_birth_chart(birth_date, birth_time, birth_place):
#     """
#     Calculate a birth chart from the provided information.

#     Args:
#         birth_date (tuple): Birth date as a tuple (year, month, day).
#         birth_time (tuple): Birth time as a tuple (hour, minute, second).
#         birth_place (str): Birth place as a string.

#     Returns:
#         dict: A dictionary containing birth chart information and chart data.
#     """
#     calculator = AstrologyCalculator()
#     return calculator.calculate_birth_chart(birth_date, birth_time, birth_place)


from .astrology_calculator import AstrologyCalculator

def calculate_birth_chart(
    birth_date,
    birth_time,
    birth_place,
    *,
    tz_str: str = None,
    lat: float = None,
    lng: float = None
):
    """
    Calculate a birth chart. You can pass explicit tz_str/lat/lng to skip lookup.

    Args:
        birth_date: tuple (year, month, day)
        birth_time: tuple (hour, minute, second)
        birth_place: str
        tz_str: optional IANA timezone name
        lat:  optional latitude
        lng:  optional longitude

    Returns:
        dict with chart info.
    """
    calculator = AstrologyCalculator()
    return calculator.calculate_birth_chart(
        birth_date=birth_date,
        birth_time=birth_time,
        birth_place=birth_place,
        tz_str=tz_str,
        lat=lat,
        lng=lng
    )
