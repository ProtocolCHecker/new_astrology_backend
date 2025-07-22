# #!/usr/bin/env python3
# import json
# from birth_chart_calculator import calculate_birth_chart
# from get_sun_sign import get_sun_sign
# from score_compatibility_calculation import calculate_compatibility
# from compatibility_interpretation import get_synastry_json, categorize_synastry
# from kerykeion import AstrologicalSubject

# def get_person_details(label):
#     print(f"--- Enter details for {label} ---")
#     name = input("Name: ")
#     year = int(input("Year of birth (e.g., 1990): "))
#     month = int(input("Month of birth (1-12): "))
#     day = int(input("Day of birth (1-31): "))
#     hour = int(input("Hour of birth (0-23): "))
#     minute = int(input("Minute of birth (0-59): "))
#     birth_place = input("Birth place (e.g., City, Country): ")
#     lat = float(input("Latitude of birthplace (e.g., 48.8566): "))
#     lng = float(input("Longitude of birthplace (e.g., 2.3522): "))
#     tz_str = input("Time zone (e.g., Europe/Paris): ")
#     birth_date = (year, month, day)
#     birth_time = (hour, minute, 0)
#     return {
#         "name": name,
#         "birth_date": birth_date,
#         "birth_time": birth_time,
#         "birth_place": birth_place,
#         "lat": lat,
#         "lng": lng,
#         "tz_str": tz_str
#     }

# def main():
#     # Gather details for both people
#     p1 = get_person_details("first person")
#     p2 = get_person_details("second person")

#     # Calculate Sun signs
#     chart1 = calculate_birth_chart(p1["birth_date"], p1["birth_time"], p1["birth_place"])
#     sun1 = get_sun_sign(chart1)
#     chart2 = calculate_birth_chart(p2["birth_date"], p2["birth_time"], p2["birth_place"])
#     sun2 = get_sun_sign(chart2)

#     # Compute compatibility score
#     compat = calculate_compatibility(sun1, sun2)
#     print(f"\n{p1['name']}\'s Sun sign: {sun1}")
#     print(f"{p2['name']}\'s Sun sign: {sun2}\n")

#     if 'error' in compat:
#         print(f"Error: {compat['error']}")
#     else:
#         print("Compatibility Scores:")
#         print(f"  Overall: {compat['overall_score']} – {compat['overall_explanation']}")
#         print(f"  Communication: {compat['communication_score']} – {compat['communication_explanation']}")
#         print(f"  Emotional: {compat['emotional_score']} – {compat['emotional_explanation']}")
#         print(f"  Intimacy: {compat['intimacy_score']} – {compat['intimacy_explanation']}")

#     # Prepare subjects for synastry
#     subj1 = AstrologicalSubject(
#         name=p1['name'],
#         year=p1['birth_date'][0], month=p1['birth_date'][1], day=p1['birth_date'][2],
#         hour=p1['birth_time'][0], minute=p1['birth_time'][1],
#         lat=p1['lat'], lng=p1['lng'],
#         city=p1['birth_place'], tz_str=p1['tz_str']
#     )
#     subj2 = AstrologicalSubject(
#         name=p2['name'],
#         year=p2['birth_date'][0], month=p2['birth_date'][1], day=p2['birth_date'][2],
#         hour=p2['birth_time'][0], minute=p2['birth_time'][1],
#         lat=p2['lat'], lng=p2['lng'],
#         city=p2['birth_place'], tz_str=p2['tz_str']
#     )

#     # Compute and display synastry interpretation
#     synastry = get_synastry_json(subj1, subj2)
#     grouped = categorize_synastry(synastry)
#     print(json.dumps(grouped, indent=2, ensure_ascii=False))


# if __name__ == "__main__":
#     main()

#!/usr/bin/env python3
import json
from birth_chart_calculator import calculate_birth_chart
from .get_sun_sign import get_sun_sign
from .score_compatibility_calculation import calculate_compatibility
from .compatibility_interpretation import get_synastry_json, categorize_synastry
from kerykeion import AstrologicalSubject

def run_compatibility(p1: dict, p2: dict) -> dict:
    """
    Compute compatibility and synastry given two person dictionaries:
      {
        "name": str,
        "birth_date": (year, month, day),
        "birth_time": (hour, minute, second),
        "birth_place": str,
        "lat": float,
        "lng": float,
        "tz_str": str
      }
    Returns:
      {
        "sun1": str,
        "sun2": str,
        "compatibility": dict,
        "synastry": dict
      }
    """
    # Calculate natal charts and sun signs
    chart1 = calculate_birth_chart(p1["birth_date"], p1["birth_time"], p1["birth_place"])
    sun1 = get_sun_sign(chart1)
    chart2 = calculate_birth_chart(p2["birth_date"], p2["birth_time"], p2["birth_place"])
    sun2 = get_sun_sign(chart2)

    # Compute compatibility scores
    compat = calculate_compatibility(sun1, sun2)

    # Prepare AstrologicalSubject instances for synastry
    subj1 = AstrologicalSubject(
        name=p1['name'],
        year=p1['birth_date'][0], month=p1['birth_date'][1], day=p1['birth_date'][2],
        hour=p1['birth_time'][0], minute=p1['birth_time'][1],
        lat=p1['lat'], lng=p1['lng'],
        city=p1['birth_place'], tz_str=p1['tz_str']
    )
    subj2 = AstrologicalSubject(
        name=p2['name'],
        year=p2['birth_date'][0], month=p2['birth_date'][1], day=p2['birth_date'][2],
        hour=p2['birth_time'][0], minute=p2['birth_time'][1],
        lat=p2['lat'], lng=p2['lng'],
        city=p2['birth_place'], tz_str=p2['tz_str']
    )

    # Compute and categorize synastry
    synastry = get_synastry_json(subj1, subj2)
    grouped = categorize_synastry(synastry)

    return {
        "sun1": sun1,
        "sun2": sun2,
        "compatibility": compat,
        "synastry": grouped
    }
