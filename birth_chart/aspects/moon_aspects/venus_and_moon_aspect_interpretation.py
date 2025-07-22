class VenusMoonAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
venus_moon_conj = VenusMoonAspectInterpretation(
    aspect="Conjunction",
    hook="You nurture through love and your warmth feels like home.",
    core_interpretation="You blend caring and affection so naturally that relationships thrive; remembering to welcome love back to yourself keeps your heart full.",
    male_expression="Your tender devotion heals others and allowing yourself to be cared for renews your soul.",
    female_expression="Your affectionate presence comforts deep and receiving kindness fuels your own joy.",
    other_expression="Your loving nature binds hearts and self compassion completes the circle."
)

# Sextile
venus_moon_sextile = VenusMoonAspectInterpretation(
    aspect="Sextile",
    hook="Your heart and values flow together and compassion meets harmony.",
    core_interpretation="You give and receive affection gracefully, weaving beauty into every bond; balancing self care with generosity keeps your spirit bright.",
    male_expression="Your generous care feels effortless and checking in with your own needs sustains your giving.",
    female_expression="Your nurturing touch uplifts and honoring your well being enriches your love.",
    other_expression="Your balanced affection inspires and tending to yourself nourishes your connections."
)

# Trine
venus_moon_trine = VenusMoonAspectInterpretation(
    aspect="Trine",
    hook="Your feelings and desires harmonize and love feels like second nature.",
    core_interpretation="You create warmth and joy wherever you go, and sharing that ease with yourself deepens every bond.",
    male_expression="Your caring spirit comforts and making space for your own wants keeps that spirit alive.",
    female_expression="Your affectionate flow feels abundant and pausing for self love replenishes your well.",
    other_expression="Your seamless love uplifts all and self kindness ignites lasting harmony."
)

# Square
venus_moon_square = VenusMoonAspectInterpretation(
    aspect="Square",
    hook="Your heart wavers between giving and needing and tension invites growth.",
    core_interpretation="You learn healthy balance by honoring both your generosity and your own needs, turning friction into self discovery.",
    male_expression="Your caring drive can overwhelm and you grow by setting clear boundaries that protect your heart.",
    female_expression="Your nurturing impulse needs reflection and claiming space for yourself empowers your care.",
    other_expression="Your tension breeds wisdom and balancing self and others refines your love."
)

# Opposition
venus_moon_opp = VenusMoonAspectInterpretation(
    aspect="Opposition",
    hook="Love mirrors your feelings and intimacy reflects your heart.",
    core_interpretation="Your relationships reveal what you need most, guiding you to find harmony between closeness and independence.",
    male_expression="Your heartfelt devotion learns from partnership and sharing needs nurtures true connection.",
    female_expression="Your emotional bonds teach you boundaries and mutual understanding fosters lasting affection.",
    other_expression="Your mirrored intimacy illuminates growth and balancing give and take enriches your soul."
)

venus_moon_aspects = {
    "Conjunction": venus_moon_conj,
    "Sextile": venus_moon_sextile,
    "Trine": venus_moon_trine,
    "Square": venus_moon_square,
    "Opposition": venus_moon_opp
}
