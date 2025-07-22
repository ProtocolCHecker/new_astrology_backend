# import pandas as pd
# import importlib
# from .transit_calculation import (
#     generate_all_transits,
#     summarize_category_counts,
# )

# # === 🌍 Load interpretation modules ===
# planet_modules = {
#     "Sun": "sun_transit_interpretation",
#     "Moon": "moon_transit_interpretation",
#     "Mercury": "mercury_transit_interpretation",
#     "Venus": "venus_transit_interpretation",
#     "Mars": "mars_transit_interpretation",
#     "Jupiter": "jupiter_transit_interpretation",
#     "Saturn": "saturn_transit_interpretation",
#     "Uranus": "uranus_transit_interpretation",
#     "Neptune": "neptune_transit_interpretation",
#     "Pluto": "pluto_transit_interpretation"
# }

# # ✅ Aspects we support
# supported_aspects = {"square", "sextile", "opposition", "conjunction", "trine"}

# user_details = {
#     "name": "Your Name",
#     "birth_year": 1990,
#     "birth_month": 5,
#     "birth_day": 15,
#     "birth_hour": 14,
#     "birth_minute": 30,
#     "birth_city": "Paris",
#     "latitude": 48.8566,
#     "longitude": 2.3522,
#     "timezone_str": "Europe/Paris"
# }

# def get_interpretation_or_none(transit_row):
#     """Returns interpretation if known, otherwise None."""
#     p1 = transit_row["transiting_planet"]
#     p2 = transit_row["natal_planet"]
#     aspect = transit_row["aspect_type"].lower()

#     if aspect not in supported_aspects:
#         return None

#     module_name = planet_modules.get(p1)
#     if not module_name:
#         return None

#     try:
#         module = importlib.import_module(module_name)
#         class_name = f"{p1}{p2}Transits"
#         transit_class = getattr(module, class_name, None)
#         if not transit_class:
#             return None

#         aspect_method = getattr(transit_class, aspect, None)
#         if not aspect_method:
#             return None

#         result = aspect_method()
#         return [result["hook"], result["interpretation"]]
#     except Exception:
#         return None

# def interpret_dataframe(df: pd.DataFrame) -> pd.DataFrame:
#     """Add interpretations and filter out unknowns."""
#     if df.empty:
#         return df

#     df["interpretation"] = df.apply(get_interpretation_or_none, axis=1)
#     return df[df["interpretation"].notnull()].reset_index(drop=True)


#!/usr/bin/env python3
import pandas as pd
import importlib

# absolute import from your package
from .transit_calculation import (
    generate_all_transits,
    summarize_category_counts,
)

# === 🌍 Load interpretation modules ===
planet_modules = {
    "Sun": "sun_transit_interpretation",
    "Moon": "moon_transit_interpretation",
    "Mercury": "mercury_transit_interpretation",
    "Venus": "venus_transit_interpretation",
    "Mars": "mars_transit_interpretation",
    "Jupiter": "jupiter_transit_interpretation",
    "Saturn": "saturn_transit_interpretation",
    "Uranus": "uranus_transit_interpretation",
    "Neptune": "neptune_transit_interpretation",
    "Pluto": "pluto_transit_interpretation"
}

# ✅ Aspects we support
supported_aspects = {"square", "sextile", "opposition", "conjunction", "trine"}

def get_interpretation_or_none(transit_row):
    """Returns interpretation if known, otherwise None."""
    p1 = transit_row["transiting_planet"]
    p2 = transit_row["natal_planet"]
    aspect = transit_row["aspect_type"].lower()

    if aspect not in supported_aspects:
        return None

    module_name = planet_modules.get(p1)
    if not module_name:
        return None

    try:
        module = importlib.import_module(f"prediction.{module_name}")
        cls = getattr(module, f"{p1}{p2}Transits", None)
        method = getattr(cls, aspect, None) if cls else None
        if not method:
            return None
        res = method()
        return [res["hook"], res["interpretation"]]
    except Exception:
        return None

def interpret_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Add interpretations and filter out unknowns."""
    if df.empty:
        return df
    df["interpretation"] = df.apply(get_interpretation_or_none, axis=1)
    return df[df["interpretation"].notnull()].reset_index(drop=True)

# def run_transits(user_details: dict, periods: list[str] = None):
#     """
#     user_details should be:
#       {
#         "name": str,
#         "birth_year": int,
#         "birth_month": int,
#         "birth_day": int,
#         "birth_hour": int,
#         "birth_minute": int,
#         "birth_city": str,
#         "latitude": float,
#         "longitude": float,
#         "timezone_str": str
#       }
#     periods is a list from ["today","tomorrow","week-end","month-end","year-end"].
#     """
#     valid = ["today", "tomorrow", "week-end", "month-end", "year-end"]
#     if periods is None:
#         periods = valid

#     # generate transit dataframes
#     df_today, df_tomorrow, df_week_end, df_month_end, df_year_end = \
#         generate_all_transits(user_details)

#     mapping = {
#         "today":     ("Today", df_today),
#         "tomorrow":  ("Tomorrow", df_tomorrow),
#         "week-end":  ("Week End", df_week_end),
#         "month-end": ("Month End", df_month_end),
#         "year-end":  ("Year End", df_year_end),
#     }

#     for key in valid:
#         if key in periods:
#             label, df = mapping[key]
#             print(f"\n🔭 Transits for {label}:\n")
#             interp = interpret_dataframe(df)
#             if not interp.empty:
#                 print(interp[[
#                     "transiting_planet",
#                     "natal_planet",
#                     "aspect_type",
#                     "category",
#                     "interpretation"
#                 ]])
#                 summarize_category_counts(interp, label)
#             else:
#                 print("No significant transits.\n")

def run_transits(user_details:dict, periods: list[str]) -> dict:
    df_today, df_tomorrow, df_week_end, df_month_end, df_year_end = \
        generate_all_transits(user_details)

    mapping = {
      "today":     ("Today",   df_today),
      "tomorrow":  ("Tomorrow",df_tomorrow),
      "week-end":  ("Week End",df_week_end),
      "month-end": ("Month End",df_month_end),
      "year-end":  ("Year End", df_year_end),
    }

    result: dict[str, list[dict]] = {}
    for key,label in mapping.items():
        if key in periods:
            df = mapping[key][1]
            interp = interpret_dataframe(df)
            # convert dataframe rows to list of dicts
            result[key] = interp.to_dict(orient="records")

    return result

# if __name__ == "__main__":
#     df_today, df_tomorrow, df_week_end, df_month_end, df_year_end = generate_all_transits(user_details)

#     print("\n🔭 Transits for Today:\n")
#     today_interp = interpret_dataframe(df_today)
#     print(today_interp[["transiting_planet", "natal_planet", "aspect_type", "category", "interpretation"]])
#     summarize_category_counts(today_interp, "Today")

#     print("\n🔭 Transits for Tomorrow:\n")
#     tomorrow_interp = interpret_dataframe(df_tomorrow)
#     print(tomorrow_interp[["transiting_planet", "natal_planet", "aspect_type", "category", "interpretation"]])
#     summarize_category_counts(tomorrow_interp, "Tomorrow")

#     print("\n🔭 Transits for Week-End:\n")
#     week_interp = interpret_dataframe(df_week_end)
#     print(week_interp[["transiting_planet", "natal_planet", "aspect_type", "category", "interpretation"]])
#     summarize_category_counts(week_interp, "Week End")

#     print("\n🔭 Transits for Month-End:\n")
#     month_interp = interpret_dataframe(df_month_end)
#     print(month_interp[["transiting_planet", "natal_planet", "aspect_type", "category", "interpretation"]])
#     summarize_category_counts(month_interp, "Month End")

#     print("\n🔭 Transits for Year-End:\n")
#     year_interp = interpret_dataframe(df_year_end)
#     print(year_interp[["transiting_planet", "natal_planet", "aspect_type", "category", "interpretation"]])
#     summarize_category_counts(year_interp, "Year End")
