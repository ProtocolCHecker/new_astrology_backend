from typing import List
from datetime import datetime, timedelta
import pytz
from dateutil.relativedelta import relativedelta
import pandas as pd
from kerykeion import AstrologicalSubject, SynastryAspects
from kerykeion.ephemeris_data import EphemerisDataFactory
from kerykeion.kr_types.kr_literals import AxialCusps, Planet
from kerykeion.kr_types.kr_models import ActiveAspect, TransitMomentModel, TransitsTimeRangeModel
from kerykeion.settings.config_constants import DEFAULT_ACTIVE_POINTS, DEFAULT_ACTIVE_ASPECTS

# === 🚰 LIFE CATEGORIES & PLANETS ===
life_categories = {
    "Identity":     ["Sun", "Mars", "Uranus"],
    "Emotion":      ["Moon", "Neptune", "Pluto"],
    "Relationships":["Venus", "Moon", "Pluto", "Saturn"],
    "Communication":["Mercury", "Jupiter", "Uranus"],
    "Career":       ["Saturn", "Sun", "Pluto"],
    "Finances":     ["Venus", "Jupiter", "Saturn", "Pluto"],
    "Health":       ["Mars", "Moon", "Saturn", "Mercury"],
    "Growth":       ["Jupiter", "Neptune", "Pluto", "Uranus"],
}

# ✅ Only consider these interpretable planets
interpretable_planets = [
    "Sun", "Moon", "Mercury", "Venus", "Mars",
    "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"
]

def get_life_category(row):
    """Determine life category based on the natal planet only."""
    natal_p = row["natal_planet"]
    for category, planets in life_categories.items():
        if natal_p in planets:
            return category
    return "Uncategorized"

def summarize_category_counts(df, label=""):
    """Summarize and interpret the frequency of life categories in a transit dataframe."""
    if df.empty:
        print(f"No data found for {label}.\n")
        return None

    counts = df["category"].value_counts()
    total = counts.sum()
    percentages = (counts / total * 100).round(2)

    summary_df = pd.DataFrame({
        "count": counts,
        "percentage": percentages
    })

    dominant = summary_df.index[0]
    strength = summary_df.iloc[0]["percentage"]

    print(f"\n🔮 Summary for {label}:")
    print(summary_df, "\n")
    print(f"👉 Dominant theme: **{dominant}** ({strength}% of transits)\n")
    return summary_df

class TransitsTimeRangeFactory:
    def __init__(
        self,
        natal_chart: AstrologicalSubject,
        ephemeris_data_points: List[AstrologicalSubject],
        active_points: List = DEFAULT_ACTIVE_POINTS,
        active_aspects: List = DEFAULT_ACTIVE_ASPECTS,
        settings_file: str = None
    ):
        self.natal_chart = natal_chart
        self.ephemeris_data_points = ephemeris_data_points
        self.active_points = active_points
        self.active_aspects = active_aspects
        self.settings_file = settings_file

    def get_transit_moments(self) -> TransitsTimeRangeModel:
        transit_moments = []
        for ephemeris_point in self.ephemeris_data_points:
            aspects = SynastryAspects(
                ephemeris_point,
                self.natal_chart,
                active_points=self.active_points,
                active_aspects=self.active_aspects,
                new_settings_file=self.settings_file,
            ).relevant_aspects
            transit_moments.append(
                TransitMomentModel(
                    date=ephemeris_point.iso_formatted_utc_datetime,
                    aspects=aspects,
                )
            )
        return TransitsTimeRangeModel(
            dates=[pt.iso_formatted_utc_datetime for pt in self.ephemeris_data_points],
            subject=self.natal_chart.model(),
            transits=transit_moments
        )

def get_transit_data(natal_chart, latitude, longitude, timezone_str, start_date, end_date):
    print(f"Getting transit data from {start_date} to {end_date}")

    ephemeris_factory = EphemerisDataFactory(
        start_datetime=start_date,
        end_datetime=end_date,
        step_type="days",
        step=1,
        lat=latitude,
        lng=longitude,
        tz_str=timezone_str,
    )
    ephemeris_data_points = ephemeris_factory.get_ephemeris_data_as_astrological_subjects()
    raw = TransitsTimeRangeFactory(natal_chart, ephemeris_data_points).get_transit_moments().model_dump()

    all_aspects = []
    for day in raw["transits"]:
        for asp in day["aspects"]:
            all_aspects.append({
                "date": day["date"],
                "transiting_planet": asp["p1_name"],
                "natal_planet":     asp["p2_name"],
                "aspect_type":      asp["aspect"],
                "orb":              asp["orbit"],
                "aspect_degrees":   asp["aspect_degrees"],
                "diff":             asp["diff"],
            })

    df = pd.DataFrame(all_aspects)
    df["date"] = (
        pd.to_datetime(df["date"])
          .dt.tz_convert("UTC")
          .dt.tz_convert(timezone_str)
          .dt.date
    )

    df = df[
        df["transiting_planet"].isin(interpretable_planets) &
        df["natal_planet"].isin(interpretable_planets)
    ]

    df["category"] = df.apply(get_life_category, axis=1)

    return df


def generate_all_transits(user_details):
    natal_chart = AstrologicalSubject(
        name=user_details["name"],
        year=user_details["birth_year"],
        month=user_details["birth_month"],
        day=user_details["birth_day"],
        hour=user_details["birth_hour"],
        minute=user_details["birth_minute"],
        lat=user_details["latitude"],
        lng=user_details["longitude"],
        city=user_details["birth_city"],
        tz_str=user_details["timezone_str"],
    )

    tz = pytz.timezone(user_details["timezone_str"])
    now = datetime.now(tz)
    today = now.replace(hour=0, minute=0, second=0, microsecond=0)

    start_today = today
    end_today = today + timedelta(days=1)
    start_tomorrow = today + timedelta(days=1)
    end_tomorrow = start_tomorrow + timedelta(days=1)
    week_end = today + timedelta(days=(6 - today.weekday()) % 7)
    month_end = (today + relativedelta(months=1, day=1)) - timedelta(days=1)
    year_end = (today + relativedelta(years=1, month=1, day=1)) - timedelta(days=1)

    df_today = get_transit_data(natal_chart, user_details["latitude"], user_details["longitude"], user_details["timezone_str"], start_today, end_today)
    df_tomorrow = get_transit_data(natal_chart, user_details["latitude"], user_details["longitude"], user_details["timezone_str"], start_tomorrow, end_tomorrow)
    df_week_end = get_transit_data(natal_chart, user_details["latitude"], user_details["longitude"], user_details["timezone_str"], week_end, week_end + timedelta(days=1))
    df_month_end = get_transit_data(natal_chart, user_details["latitude"], user_details["longitude"], user_details["timezone_str"], month_end, month_end + timedelta(days=1))
    df_year_end = get_transit_data(natal_chart, user_details["latitude"], user_details["longitude"], user_details["timezone_str"], year_end, year_end + timedelta(days=1))

    df_today = df_today[df_today["date"] == today.date()]
    df_tomorrow = df_tomorrow[df_tomorrow["date"] == start_tomorrow.date()]
    df_week_end = df_week_end[df_week_end["date"] == week_end.date()]
    df_month_end = df_month_end[df_month_end["date"] == month_end.date()]
    df_year_end = df_year_end[df_year_end["date"] == year_end.date()]

    return df_today, df_tomorrow, df_week_end, df_month_end, df_year_end
