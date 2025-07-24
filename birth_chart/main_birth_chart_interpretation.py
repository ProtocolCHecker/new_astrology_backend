# import json
# import inspect

# # Correct import from the local module
# from birth_chart import calculate_birth_chart

# from .house_interpretation.main_house_interpretation import (
#     get_interpretation as get_house_interp,
#     print_interpretation as print_house_interp
# )

# # Debug: Check the function signature
# print("=== DEBUG: calculate_birth_chart signature ===")
# sig = inspect.signature(calculate_birth_chart)
# print(f"Function: {calculate_birth_chart}")
# print(f"Signature: {sig}")
# print(f"Parameters: {list(sig.parameters.keys())}")
# print("=" * 50)

# # Use existing main interpretation modules
# from .sign_interpretation.main_sign_interpretation import interpret as interpret_sign
# from .aspects.main_aspects_interpreter import get_aspect_json


# def ordinal(n: int) -> str:
#     """Convert an integer to its ordinal representation, e.g. 1->'1st'."""
#     if 10 <= n % 100 <= 20:
#         suffix = 'th'
#     else:
#         suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
#     return f"{n}{suffix}"


# def planet_house(planet_deg: float, houses: dict[int, float]) -> str:
#     """
#     Given a planet's degree and the chart's house cusps (1->deg, ... 12->deg),
#     return the ordinal house label (e.g. '5th').
#     """
#     cusps = {int(k): v for k, v in houses.items()}
#     for i in range(1, 13):
#         start = cusps[i]
#         end = cusps[i % 12 + 1]
#         if start <= end:
#             if start <= planet_deg < end:
#                 return ordinal(i)
#         else:
#             if planet_deg >= start or planet_deg < end:
#                 return ordinal(i)
#     return ordinal(1)


# def compute_birth_chart(
#     birth_date: tuple[int,int,int],
#     birth_time: tuple[int,int,int],
#     birth_place: str,
#     tz_str: str = None,
#     lat: float = None,
#     lng: float = None,
#     gender: str = "other"
# ) -> dict:
#     """
#     Debugging version - prints input params and function signature
#     """
#     # ===== DEBUG PRINT 1: Show incoming parameters =====
#     print("\n[DEBUG] Input parameters received:")
#     print(f"birth_date: {birth_date} (type: {type(birth_date)})")
#     print(f"birth_time: {birth_time} (type: {type(birth_time)})")
#     print(f"birth_place: {birth_place} (type: {type(birth_place)})")
#     print(f"tz_str: {tz_str} (type: {type(tz_str)})")
#     print(f"lat: {lat} (type: {type(lat)})")
#     print(f"lng: {lng} (type: {type(lng)})")

#     # ===== DEBUG PRINT 2: Show calculate_birth_chart's signature =====
#     from inspect import signature
#     sig = signature(calculate_birth_chart)
#     print("\n[DEBUG] calculate_birth_chart function signature:")
#     print(sig)
#     print("Parameter names:", list(sig.parameters.keys()))

#     # ===== FIXED: Remove the problematic import and debug print =====
#     # The calculate_birth_chart function is already imported at the top
#     # No need to import birth_chart_calculator separately

#     # Pass parameters to calculator - USE THE IMPORTED FUNCTION DIRECTLY
#     chart = calculate_birth_chart(
#         birth_date=birth_date,
#         birth_time=birth_time,
#         birth_place=birth_place,
#         tz_str=tz_str,
#         lat=lat,
#         lng=lng
#     )
    
#     data = chart.get("chart_data", {})
#     planets = data.get("planets", {})
#     houses  = data.get("houses", {})
#     asc     = data.get("ascendant")

#     # 1) Signs
#     sign_list: list[str] = []
#     if asc:
#         try:
#             sign_list.append(interpret_sign("Ascendant", asc["sign"], gender))
#         except Exception as e:
#             sign_list.append(f"<Error Ascendant {asc['sign']}: {e}>")

#     for planet, info in planets.items():
#         try:
#             sign_list.append(interpret_sign(planet, info["sign"], gender))
#         except Exception as e:
#             sign_list.append(f"<Error {planet} {info.get('sign')}: {e}>")

#     # 2) Houses
#     house_list: list[str] = []
#     if asc:
#         try:
#             h = get_house_interp("ascendant","1st",gender)
#             house_list.append(json.dumps(h))
#         except Exception as e:
#             house_list.append(f"<Error ascendant 1st: {e}>")

#     for planet,info in planets.items():
#         deg = info.get("degree")
#         if deg is not None:
#             label = planet_house(deg, houses)
#             try:
#                 h = get_house_interp(planet,label,gender)
#                 house_list.append(json.dumps(h))
#             except Exception as e:
#                 house_list.append(f"<Error {planet} {label}: {e}>")

#     # 3) Aspects
#     aspect_list: list[str] = []
#     for asp in data.get("aspects", []):
#         j = get_aspect_json(
#             main_planet = asp["planet1"],
#             other_planet= asp["planet2"],
#             aspect      = asp["aspect"],
#             gender      = gender
#         )
#         if j:
#             aspect_list.append(json.dumps(j))

#     return {
#         "sign_interpretations":   sign_list,
#         "house_interpretations":  house_list,
#         "aspect_interpretations": aspect_list
#     }


# def main(birth_date, birth_time, birth_place, gender: str = 'other'):
#     # 1) Calculate raw chart (now passing tz/coords)
#     chart = calculate_birth_chart(
#         birth_date=birth_date,
#         birth_time=birth_time,
#         birth_place=birth_place,
#         tz_str=None,
#         lat=None,
#         lng=None
#     )
#     data = chart.get('chart_data', {})
#     planets = data.get('planets', {})
#     houses_cusps = data.get('houses', {})

#     print("=== SIGN INTERPRETATIONS ===\n")
#     asc = data.get('ascendant')
#     if asc:
#         sign = asc.get('sign')
#         try:
#             print(interpret_sign('Ascendant', sign, gender))
#         except Exception as e:
#             print(f"<Error interpreting Ascendant in {sign}: {e}>")
#         print("\n" + "="*60 + "\n")

#     for planet, info in planets.items():
#         sign = info.get('sign')
#         try:
#             print(interpret_sign(planet, sign, gender))
#         except Exception as e:
#             print(f"<Error interpreting {planet} in {sign}: {e}>")
#         print("\n" + "="*60 + "\n")

#     print("=== HOUSE INTERPRETATIONS ===\n")
#     if asc:
#         try:
#             interp = get_house_interp('ascendant', '1st', gender)
#             print_house_interp(interp)
#         except Exception as e:
#             print(f"<Error interpreting ascendant in 1st: {e}>")
#         print("\n" + "="*60 + "\n")

#     for planet, info in planets.items():
#         deg = info.get('degree')
#         if deg is None:
#             continue
#         house_label = planet_house(deg, houses_cusps)
#         try:
#             interp = get_house_interp(planet, house_label, gender)
#             print_house_interp(interp)
#         except Exception as e:
#             print(f"<Error interpreting {planet} in {house_label}: {e}>")
#         print("\n" + "="*60 + "\n")

#     print("=== ASPECT INTERPRETATIONS ===\n")
#     for asp in data.get('aspects', []):
#         j = get_aspect_json(
#             main_planet=asp.get('planet1'),
#             other_planet=asp.get('planet2'),
#             aspect=asp.get('aspect'),
#             gender=gender
#         )
#         if not j:
#             continue
#         print(f"{j['main']} {j['aspect']} {j['other']}")
#         print("━"*40)
#         print(f"⚡ {j['hook']}\n")
#         print(f"{j['core_description']}\n")
#         print(f"✨ {j['gender_description']}\n")
#         print("\n" + "="*60 + "\n")


import json
import inspect

# Correct import from the local module
from birth_chart import calculate_birth_chart

from .house_interpretation.main_house_interpretation import (
    get_interpretation as get_house_interp,
    print_interpretation as print_house_interp
)

# Debug: Check the function signature
print("=== DEBUG: calculate_birth_chart signature ===")
sig = inspect.signature(calculate_birth_chart)
print(f"Function: {calculate_birth_chart}")
print(f"Signature: {sig}")
print(f"Parameters: {list(sig.parameters.keys())}")
print("=" * 50)

# Use existing main interpretation modules
from .sign_interpretation.main_sign_interpretation import interpret as interpret_sign
from .aspects.main_aspects_interpreter import get_aspect_json


def ordinal(n: int) -> str:
    """Convert an integer to its ordinal representation, e.g. 1->'1st'."""
    if 10 <= n % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return f"{n}{suffix}"


def planet_house(planet_deg: float, houses: dict[int, float]) -> str:
    """
    Given a planet's degree and the chart's house cusps (1->deg, ... 12->deg),
    return the ordinal house label (e.g. '5th').
    """
    cusps = {int(k): v for k, v in houses.items()}
    for i in range(1, 13):
        start = cusps[i]
        end = cusps[i % 12 + 1]
        if start <= end:
            if start <= planet_deg < end:
                return ordinal(i)
        else:
            if planet_deg >= start or planet_deg < end:
                return ordinal(i)
    return ordinal(1)


def get_planet_symbol(planet_name: str) -> str:
    """Return the Unicode symbol for a planet."""
    symbols = {
        'Sun': '☉',
        'Moon': '☽',
        'Mercury': '☿',
        'Venus': '♀',
        'Mars': '♂',
        'Jupiter': '♃',
        'Saturn': '♄',
        'Uranus': '♅',
        'Neptune': '♆',
        'Pluto': '♇',
        'Ascendant': '↗'
    }
    return symbols.get(planet_name, '●')


def get_house_meaning(house_number: int) -> str:
    """Return the meaning/theme of each house."""
    meanings = {
        1: "Self and Identity",
        2: "Money and Possessions",
        3: "Communication and Siblings",
        4: "Home and Family",
        5: "Creativity and Romance",
        6: "Health and Service",
        7: "Partnerships and Marriage", 
        8: "Transformation and Shared Resources",
        9: "Philosophy and Higher Learning",
        10: "Career and Public Image",
        11: "Friends and Social Groups",
        12: "Spirituality and Subconscious"
    }
    return meanings.get(house_number, "Unknown")


def compute_birth_chart(
    birth_date: tuple[int,int,int],
    birth_time: tuple[int,int,int],
    birth_place: str,
    tz_str: str = None,
    lat: float = None,
    lng: float = None,
    gender: str = "other"
) -> dict:
    """
    Enhanced version that returns complete birth chart data including basic chart info
    """
    # Calculate the raw birth chart
    chart = calculate_birth_chart(
        birth_date=birth_date,
        birth_time=birth_time,
        birth_place=birth_place,
        tz_str=tz_str,
        lat=lat,
        lng=lng
    )
    
    # Extract data from the chart
    data = chart.get("chart_data", {})
    birth_info = chart.get("birth_info", {})
    planets = data.get("planets", {})
    houses = data.get("houses", {})
    asc = data.get("ascendant")
    aspects_data = data.get("aspects", [])

    # 1) Build basic chart information that frontend expects
    
    # Extract big three signs
    sun_sign = planets.get("Sun", {}).get("sign", "Unknown")
    moon_sign = planets.get("Moon", {}).get("sign", "Unknown")
    rising_sign = asc.get("sign", "Unknown") if asc else "Unknown"
    
    # 2) Build planets array for frontend
    planets_array = []
    if asc:  # Add Ascendant as first "planet"
        planets_array.append({
            "name": "Ascendant",
            "sign": asc["sign"],
            "degree": asc["degree"] % 30,  # Degree within sign
            "house": 1,  # Ascendant is always in 1st house
            "symbol": get_planet_symbol("Ascendant")
        })
    
    # Add all planets with their house assignments
    for planet_name, planet_info in planets.items():
        # Find which house this planet is in
        planet_degree = planet_info["degree"]
        house_number = int(planet_house(planet_info["longitude"], houses).replace('st', '').replace('nd', '').replace('rd', '').replace('th', ''))
        
        planets_array.append({
            "name": planet_name,
            "sign": planet_info["sign"],
            "degree": planet_degree,
            "house": house_number,
            "symbol": get_planet_symbol(planet_name)
        })
    
    # 3) Build houses array for frontend
    houses_array = []
    for house_num in range(1, 13):
        house_cusp_degree = houses.get(house_num, 0)
        house_sign = data.get("signs", {}).get(house_num) 
        
        # If sign not directly available, calculate from cusp degree
        if not house_sign:
            sign_index = int(house_cusp_degree / 30) % 12
            signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
                    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
            house_sign = signs[sign_index]
        
        houses_array.append({
            "number": house_num,
            "sign": house_sign,
            "degree": house_cusp_degree,
            "meaning": get_house_meaning(house_num)
        })

    # 4) Generate interpretations (existing code)
    
    # Sign interpretations
    sign_list: list[str] = []
    if asc:
        try:
            sign_list.append(interpret_sign("Ascendant", asc["sign"], gender))
        except Exception as e:
            sign_list.append(f"<Error Ascendant {asc['sign']}: {e}>")

    for planet, info in planets.items():
        try:
            sign_list.append(interpret_sign(planet, info["sign"], gender))
        except Exception as e:
            sign_list.append(f"<Error {planet} {info.get('sign')}: {e}>")

    # House interpretations
    house_list: list[str] = []
    if asc:
        try:
            h = get_house_interp("ascendant","1st",gender)
            house_list.append(json.dumps(h))
        except Exception as e:
            house_list.append(f"<Error ascendant 1st: {e}>")

    for planet,info in planets.items():
        deg = info.get("degree")
        if deg is not None:
            label = planet_house(info["longitude"], houses)
            try:
                h = get_house_interp(planet,label,gender)
                house_list.append(json.dumps(h))
            except Exception as e:
                house_list.append(f"<Error {planet} {label}: {e}>")

    # Aspect interpretations
    aspect_list: list[str] = []
    for asp in aspects_data:
        j = get_aspect_json(
            main_planet = asp["planet1"],
            other_planet= asp["planet2"],
            aspect      = asp["aspect"],
            gender      = gender
        )
        if j:
            aspect_list.append(json.dumps(j))

    # 5) Build complete response that matches frontend expectations
    return {
        # Basic chart data that frontend expects
        "sunSign": sun_sign,
        "moonSign": moon_sign,
        "risingSign": rising_sign,
        
        # Detailed arrays
        "planets": planets_array,
        "houses": houses_array,
        
        # Birth information
        "birthInfo": {
            "date": birth_info.get("date", "Unknown"),
            "time": birth_info.get("time", "Unknown"),
            "place": birth_info.get("place", birth_place),
            "coordinates": birth_info.get("coordinates", "Unknown"),
            "timezone": birth_info.get("timezone", "Unknown")
        },
        
        # Interpretations (your existing functionality)
        "signInterpretations": sign_list,
        "houseInterpretations": house_list,
        "aspectInterpretations": aspect_list,
        
    }