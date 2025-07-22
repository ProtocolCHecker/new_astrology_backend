import swisseph as swe
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import datetime
import pytz

class AstrologyCalculator:
    def __init__(self):
        # Initialize Swiss Ephemeris
        swe.set_ephe_path()  # Uses default ephemeris path

        # Define planets
        self.planets = {
            swe.SUN: "Sun",
            swe.MOON: "Moon",
            swe.MERCURY: "Mercury",
            swe.VENUS: "Venus",
            swe.MARS: "Mars",
            swe.JUPITER: "Jupiter",
            swe.SATURN: "Saturn",
            swe.URANUS: "Uranus",
            swe.NEPTUNE: "Neptune",
            swe.PLUTO: "Pluto"
        }

        # Define zodiac signs
        self.signs = [
            "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
            "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
        ]

    def get_coordinates(self, location):
        """Convert location name to latitude and longitude."""
        geolocator = Nominatim(user_agent="astrology_calculator")
        location_data = geolocator.geocode(location)
        if location_data:
            return location_data.latitude, location_data.longitude
        else:
            raise ValueError(f"Could not find coordinates for location: {location}")

    def get_timezone(self, latitude, longitude):
        """Get timezone for given coordinates using TimeZoneDB API."""
        import requests
        
        params = {
            'key': 'CPA8DG44IP5Z',
            'format': 'json',
            'by': 'position',
            'lat': latitude,
            'lng': longitude
        }
        
        response = requests.get("http://api.timezonedb.com/v2.1/get-time-zone", params=params)
        data = response.json()
        
        if data.get('status') == 'OK':
            return data['zoneName']
        else:
            raise ValueError("Could not determine timezone for the provided coordinates")

    def calculate_julian_day(self, birth_date, birth_time, latitude, longitude):
        """Calculate Julian day for the birth date and time."""
        timezone_str = self.get_timezone(latitude, longitude)
        timezone = pytz.timezone(timezone_str)
        year, month, day = birth_date
        hour, minute, second = birth_time
        local_datetime = datetime.datetime(year, month, day, hour, minute, second)
        local_datetime = timezone.localize(local_datetime)
        utc_datetime = local_datetime.astimezone(pytz.UTC)
        jd = swe.julday(
            utc_datetime.year, utc_datetime.month, utc_datetime.day,
            utc_datetime.hour + utc_datetime.minute / 60.0 + utc_datetime.second / 3600.0
        )
        return jd, timezone_str

    def calculate_houses(self, jd, latitude, longitude):
        """Calculate the house cusps using the Placidus system."""
        geolat, geolon = latitude, longitude
        houses = swe.houses(jd, geolat, geolon)[0]
        ascendant = houses[0]
        midheaven = houses[9]
        return houses, ascendant, midheaven

    def calculate_planet_positions(self, jd):
        """Calculate positions of planets at a given Julian day."""
        planet_positions = {}
        for planet_id, planet_name in self.planets.items():
            result, _ = swe.calc_ut(jd, planet_id)
            if isinstance(result, tuple) and len(result) > 0:
                longitude = result[0]
                sign_num = int(longitude / 30)
                sign_deg = longitude % 30
                planet_positions[planet_name] = {
                    "longitude": longitude,
                    "sign": self.signs[sign_num],
                    "degree": sign_deg
                }
        return planet_positions

    def calculate_retrograde_status(self, jd):
        """Calculate retrograde status of planets at a given Julian day."""
        retrograde_status = {}
        for planet_id, planet_name in self.planets.items():
            pos_data, _ = swe.calc_ut(jd, planet_id)
            speed = pos_data[3]
            retrograde = speed < 0
            retrograde_status[planet_name] = "Retrograde" if retrograde else "Direct"
        return retrograde_status

    def calculate_aspects(self, planet_positions):
        """Calculate aspects between planets."""
        aspects_list = []
        planets = list(planet_positions.keys())
        for i in range(len(planets)):
            for j in range(i + 1, len(planets)):
                planet1 = planets[i]
                planet2 = planets[j]
                long1 = planet_positions[planet1]["longitude"]
                long2 = planet_positions[planet2]["longitude"]
                angle = abs(long1 - long2)
                if angle > 180:
                    angle = 360 - angle

                # Define aspects and their orbs
                aspects = {
                    "Conjunction": {"angle": 0, "orb": 8},
                    "Opposition": {"angle": 180, "orb": 8},
                    "Trine": {"angle": 120, "orb": 8},
                    "Square": {"angle": 90, "orb": 7},
                    "Sextile": {"angle": 60, "orb": 6}
                }

                for aspect_name, aspect_info in aspects.items():
                    aspect_angle = aspect_info["angle"]
                    orb = aspect_info["orb"]
                    if abs(angle - aspect_angle) <= orb:
                        aspects_list.append({
                            "planet1": planet1,
                            "planet2": planet2,
                            "aspect": aspect_name,
                            "orb": round(abs(angle - aspect_angle), 2)
                        })
        return aspects_list

    def assign_planets_to_houses(self, planet_positions, houses):
        """Assign planets to houses."""
        planets_in_houses = {}
        for house_num in range(1, 13):
            planets_in_houses[house_num] = []
            house_start = houses[house_num - 1]
            house_end = houses[house_num % 12]
            if house_end < house_start:
                house_end += 360
            for planet, data in planet_positions.items():
                planet_long = data["longitude"]
                if house_end > 360 and planet_long < house_end - 360:
                    adjusted_long = planet_long + 360
                else:
                    adjusted_long = planet_long
                if house_start <= adjusted_long < house_end:
                    planets_in_houses[house_num].append(planet)
        return planets_in_houses

    def calculate_birth_chart(self, birth_date, birth_time, birth_place):
        """Calculate a birth chart from the provided information."""
        latitude, longitude = self.get_coordinates(birth_place)
        jd, timezone = self.calculate_julian_day(birth_date, birth_time, latitude, longitude)
        houses, ascendant, midheaven = self.calculate_houses(jd, latitude, longitude)
        planet_positions = self.calculate_planet_positions(jd)
        retrograde_status = self.calculate_retrograde_status(jd)
        aspects = self.calculate_aspects(planet_positions)
        planets_in_houses = self.assign_planets_to_houses(planet_positions, houses)

        asc_sign_num = int(ascendant / 30)
        ascendant_sign = self.signs[asc_sign_num]

        result = {
            "birth_info": {
                "date": f"{birth_date[2]}/{birth_date[1]}/{birth_date[0]}",
                "time": f"{birth_time[0]:02d}:{birth_time[1]:02d}:{birth_time[2]:02d}",
                "place": birth_place,
                "coordinates": f"{latitude:.4f}, {longitude:.4f}",
                "timezone": timezone
            },
            "chart_data": {
                "julian_day": jd,
                "ascendant": {
                    "degree": ascendant,
                    "sign": ascendant_sign
                },
                "midheaven": {
                    "degree": midheaven,
                    "sign": self.signs[int(midheaven / 30)]
                },
                "houses": {i+1: houses[i] for i in range(12)},
                "planets": planet_positions,
                "retrograde_status": retrograde_status,
                "aspects": aspects
            }
        }
        return result

