import json

# 1) Bring in every planet's interpreter function
from .ascendant_aspects.main_ascendant_aspect import get_ascendant_aspect_interpretation
from .sun_aspects.main_sun_aspects import get_sun_aspect_interpretation
from .moon_aspects.main_moon_aspects import get_moon_aspect_interpretation
from .mercury_aspects.main_mercury_aspects import get_mercury_aspect_interpretation
from .venus_aspects.main_venus_aspects import get_venus_aspect_interpretation
from .mars_aspects.main_mars_aspects import get_mars_aspect_interpretation
from .jupiter_aspects.main_jupiter_aspects import get_jupiter_aspect_interpretation
from .saturn_aspects.main_saturn_aspects import get_saturn_aspect_interpretation
from .uranus_aspects.main_uranus_aspects import get_uranus_aspect_interpretation
from .neptune_aspects.main_neptune_aspects import get_neptune_aspect_interpretation
from .pluto_aspects.main_pluto_aspects import get_pluto_aspect_interpretation


# 2) Normalize common aspect labels to canonical lowercase
def normalize_aspect(a: str) -> str:
    key = a.strip().lower()
    mapping = {
        **dict.fromkeys(['conj','conjunct','conjunction'], 'conjunction'),
        **dict.fromkeys(['sex','sext','sextile'],     'sextile'),
        **dict.fromkeys(['tri','trine'],              'trine'),
        **dict.fromkeys(['squ','square'],             'square'),
        **dict.fromkeys(['opp','op','opposition'],    'opposition')
    }
    return mapping.get(key, key)

# 3) Mercury uses a slightly different key set in its data
_MERCURY_TITLE = {
    'conjunction': 'Conjunct',
    'sextile':     'Sextile',
    'trine':       'Trine',
    'square':      'Square',
    'opposition':  'Opposition'
}

# 4) Dispatch table: main → (other, aspect, gender) → unified dict
_INTERPRETERS = {
    'ascendant': lambda other, asp, gen:
        get_ascendant_aspect_interpretation(planet=other, aspect=asp.capitalize(), gender_expression=gen),

    'sun': lambda other, asp, gen:
        get_sun_aspect_interpretation(planet=other, aspect=asp.capitalize(), gender_expression=gen),

    'moon': lambda other, asp, gen:
        get_moon_aspect_interpretation(planet=other, aspect=asp.capitalize(), gender_expression=gen),

    'mercury': lambda other, asp, gen:
        get_mercury_aspect_interpretation(planet=other, aspect=_MERCURY_TITLE[asp], gender_expression=gen),

    'venus': lambda other, asp, gen:
        get_venus_aspect_interpretation(planet=other, aspect=asp.capitalize(), gender_expression=gen),

    'mars': lambda other, asp, gen:
        get_mars_aspect_interpretation(planet=other, aspect=asp.capitalize(), gender_expression=gen),

    'jupiter': lambda other, asp, gen:
        get_jupiter_aspect_interpretation(planet=other, aspect=asp.capitalize(), gender_expression=gen),

    'saturn': lambda other, asp, gen:
        get_saturn_aspect_interpretation(planet=other, aspect=asp.capitalize(), gender_expression=gen),

    'uranus': lambda other, asp, gen:
        get_uranus_aspect_interpretation(planet=other, aspect=asp.capitalize(), gender_expression=gen),

    'neptune': lambda other, asp, gen:
        get_neptune_aspect_interpretation(planet=other, aspect=asp.capitalize(), gender_expression=gen),

    'pluto': lambda other, asp, gen:
        get_pluto_aspect_interpretation(planet=other, aspect=asp.capitalize(), gender_expression=gen),
}


def get_aspect_json(
    main_planet: str,
    other_planet: str,
    aspect: str,
    gender: str = 'other'
) -> dict | None:
    """
    Return a unified dict for any main–other aspect.
    Returns None for invalid inputs or same-planet.
    """
    mp = main_planet.strip().lower()
    op = other_planet.strip().capitalize()
    if mp == op.lower() or mp not in _INTERPRETERS:
        return None

    asp = normalize_aspect(aspect)
    if asp not in ('conjunction', 'sextile', 'trine', 'square', 'opposition'):
        return None

    gen = gender.strip().lower()
    try:
        raw = _INTERPRETERS[mp](op, asp, gen)
    except Exception:
        return None

    if not isinstance(raw, dict):
        return None

    return {
        'main': main_planet,
        'other': other_planet,
        'aspect': asp,
        'hook': raw.get('hook'),
        'core_description': raw.get('core_description'),
        'gender_description': raw.get('gender_description')
    }


# 5) Demo
if __name__ == "__main__":
    sample = [
        ("Sun",       "Venus",      "Conjunct"),
        ("Mars",      "Saturn",     "squ"),
        ("Mercury",   "Jupiter",    "sext"),
        ("Venus",     "Neptune",    "opp"),
        ("Moon",      "Pluto",      "trine"),
        ("Uranus",    "Ascendant",  "Conjunct"),
        ("Saturn",    "Mercury",    "square"),
        ("Neptune",   "Sun",        "sex"),
        ("Pluto",     "Moon",       "Opposition"),
        ("Jupiter",   "Sun",        "Opposition"),
        ("Ascendant", "Moon",       "Opposition")
    ]
    results = [get_aspect_json(*t, gender=('male' if t[2] in ('squ','square') else 'other'))
               for t in sample]
    print(json.dumps([r for r in results if r], indent=2))
