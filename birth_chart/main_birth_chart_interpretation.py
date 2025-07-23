# import json

# from birth_chart_calculator import calculate_birth_chart
# from .house_interpretation.main_house_interpretation import (
#     get_interpretation as get_house_interp,
#     print_interpretation as print_house_interp
# )
# # Use existing main interpretation modules
# from .sign_interpretation.main_sign_interpretation import interpret as interpret_sign
# from .aspects.main_aspects_interpreter import get_aspect_json


# def ordinal(n: int) -> str:
#     """Convert an integer to its ordinal representation, e.g. 1->'1st', 2->'2nd'."""
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
#     # Ensure integer keys
#     cusps = {int(k): v for k, v in houses.items()}
#     for i in range(1, 13):
#         start = cusps[i]
#         end = cusps[i % 12 + 1]
#         if start <= end:
#             if start <= planet_deg < end:
#                 return ordinal(i)
#         else:
#             # wrap past 360°
#             if planet_deg >= start or planet_deg < end:
#                 return ordinal(i)
#     return ordinal(1)


# def compute_birth_chart(
#     birth_date: tuple[int,int,int],
#     birth_time: tuple[int,int,int],
#     birth_place: str,
#     gender: str = "other"
# ) -> dict:
#     """
#     Returns a JSON-friendly dict with:
#       - sign_interpretations: list of strings
#       - house_interpretations: list of strings
#       - aspect_interpretations: list of strings
#     """
#     chart = calculate_birth_chart(birth_date, birth_time, birth_place)
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
#     def ordinal(n:int) -> str:
#         if 10 <= n % 100 <= 20: return f"{n}th"
#         return f"{n}{ {1:'st',2:'nd',3:'rd'}.get(n%10,'th') }"
#     def planet_house(deg, cusps):
#         cusps_i = {int(k):v for k,v in cusps.items()}
#         for i in range(1,13):
#             start, end = cusps_i[i], cusps_i[i%12+1]
#             if start<=end and start<=deg<end or (start> end and (deg>=start or deg<end)):
#                 return ordinal(i)
#         return ordinal(1)

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
#     # 1) Calculate raw chart
#     chart = calculate_birth_chart(birth_date, birth_time, birth_place)
#     data = chart.get('chart_data', {})
#     planets = data.get('planets', {})
#     houses_cusps = data.get('houses', {})

#     print("=== SIGN INTERPRETATIONS ===\n")
#     # Ascendant sign if available
#     asc = data.get('ascendant')
#     if asc:
#         sign = asc.get('sign')
#         try:
#             print(interpret_sign('Ascendant', sign, gender))
#         except Exception as e:
#             print(f"<Error interpreting Ascendant in {sign}: {e}>")
#         print("\n" + "="*60 + "\n")

#     # Each planet's sign
#     for planet, info in planets.items():
#         sign = info.get('sign')
#         try:
#             print(interpret_sign(planet, sign, gender))
#         except Exception as e:
#             print(f"<Error interpreting {planet} in {sign}: {e}>")
#         print("\n" + "="*60 + "\n")

#     print("=== HOUSE INTERPRETATIONS ===\n")
#     # Ascendant house (always 1st)
#     if asc:
#         try:
#             interp = get_house_interp('ascendant', '1st', gender)
#             print_house_interp(interp)
#         except Exception as e:
#             print(f"<Error interpreting ascendant in 1st: {e}>")
#         print("\n" + "="*60 + "\n")

#     # Each planet's house
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
#         # Format aspect output
#         print(f"{j['main']} {j['aspect']} {j['other']}")
#         print("━"*40)
#         print(f"⚡ {j['hook']}\n")
#         print(f"{j['core_description']}\n")
#         print(f"✨ {j['gender_description']}\n")
#         print("\n" + "="*60 + "\n")

# # if __name__ == '__main__':
# #     # Example invocation; replace with dynamic input as needed
# #     birth_date = (1999, 12, 3)
# #     birth_time = (22, 59, 0)
# #     birth_place = 'Paris, France'
# #     main(birth_date, birth_time, birth_place, gender='other')


import json
import inspect

#from birth_chart_calculator import calculate_birth_chart
from birth_chart.birth_chart_calculator import calculate_birth_chart

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
    Debugging version - prints input params and function signature
    """
    # ===== DEBUG PRINT 1: Show incoming parameters =====
    print("\n[DEBUG] Input parameters received:")
    print(f"birth_date: {birth_date} (type: {type(birth_date)})")
    print(f"birth_time: {birth_time} (type: {type(birth_time)})")
    print(f"birth_place: {birth_place} (type: {type(birth_place)})")
    print(f"tz_str: {tz_str} (type: {type(tz_str)})")
    print(f"lat: {lat} (type: {type(lat)})")
    print(f"lng: {lng} (type: {type(lng)})")

    # ===== DEBUG PRINT 2: Show calculate_birth_chart's signature =====
    from inspect import signature
    sig = signature(calculate_birth_chart)
    print("\n[DEBUG] calculate_birth_chart function signature:")
    print(sig)
    print("Parameter names:", list(sig.parameters.keys()))

    # ===== DEBUG PRINT 3: Verify module path =====
    import birth_chart_calculator
    print("\n[DEBUG] birth_chart_calculator module path:")
    print(birth_chart_calculator.__file__)

    # Pass parameters to calculator (original code continues)
    chart = calculate_birth_chart(
        birth_date=birth_date,
        birth_time=birth_time,
        birth_place=birth_place,
        tz_str=tz_str,
        lat=lat,
        lng=lng
    )
    
    data = chart.get("chart_data", {})
    planets = data.get("planets", {})
    houses  = data.get("houses", {})
    asc     = data.get("ascendant")

    # 1) Signs
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

    # 2) Houses
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
            label = planet_house(deg, houses)
            try:
                h = get_house_interp(planet,label,gender)
                house_list.append(json.dumps(h))
            except Exception as e:
                house_list.append(f"<Error {planet} {label}: {e}>")

    # 3) Aspects
    aspect_list: list[str] = []
    for asp in data.get("aspects", []):
        j = get_aspect_json(
            main_planet = asp["planet1"],
            other_planet= asp["planet2"],
            aspect      = asp["aspect"],
            gender      = gender
        )
        if j:
            aspect_list.append(json.dumps(j))

    return {
        "sign_interpretations":   sign_list,
        "house_interpretations":  house_list,
        "aspect_interpretations": aspect_list
    }


def main(birth_date, birth_time, birth_place, gender: str = 'other'):
    # 1) Calculate raw chart (now passing tz/coords)
    chart = calculate_birth_chart(
        birth_date=birth_date,
        birth_time=birth_time,
        birth_place=birth_place,
        tz_str=None,
        lat=None,
        lng=None
    )
    data = chart.get('chart_data', {})
    planets = data.get('planets', {})
    houses_cusps = data.get('houses', {})

    print("=== SIGN INTERPRETATIONS ===\n")
    asc = data.get('ascendant')
    if asc:
        sign = asc.get('sign')
        try:
            print(interpret_sign('Ascendant', sign, gender))
        except Exception as e:
            print(f"<Error interpreting Ascendant in {sign}: {e}>")
        print("\n" + "="*60 + "\n")

    for planet, info in planets.items():
        sign = info.get('sign')
        try:
            print(interpret_sign(planet, sign, gender))
        except Exception as e:
            print(f"<Error interpreting {planet} in {sign}: {e}>")
        print("\n" + "="*60 + "\n")

    print("=== HOUSE INTERPRETATIONS ===\n")
    if asc:
        try:
            interp = get_house_interp('ascendant', '1st', gender)
            print_house_interp(interp)
        except Exception as e:
            print(f"<Error interpreting ascendant in 1st: {e}>")
        print("\n" + "="*60 + "\n")

    for planet, info in planets.items():
        deg = info.get('degree')
        if deg is None:
            continue
        house_label = planet_house(deg, houses_cusps)
        try:
            interp = get_house_interp(planet, house_label, gender)
            print_house_interp(interp)
        except Exception as e:
            print(f"<Error interpreting {planet} in {house_label}: {e}>")
        print("\n" + "="*60 + "\n")

    print("=== ASPECT INTERPRETATIONS ===\n")
    for asp in data.get('aspects', []):
        j = get_aspect_json(
            main_planet=asp.get('planet1'),
            other_planet=asp.get('planet2'),
            aspect=asp.get('aspect'),
            gender=gender
        )
        if not j:
            continue
        print(f"{j['main']} {j['aspect']} {j['other']}")
        print("━"*40)
        print(f"⚡ {j['hook']}\n")
        print(f"{j['core_description']}\n")
        print(f"✨ {j['gender_description']}\n")
        print("\n" + "="*60 + "\n")

