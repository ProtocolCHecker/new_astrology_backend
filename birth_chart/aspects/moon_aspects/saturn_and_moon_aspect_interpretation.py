class SaturnMoonAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
saturn_moon_conj = SaturnMoonAspectInterpretation(
    aspect="Conjunction",
    hook="Your heart carries weight and strength grows through restraint.",
    core_interpretation="You build emotional resilience through discipline, and embracing moments of softness heals the hardest places.",
    male_expression="Your quiet strength comforts others and opening to vulnerability enriches your connections.",
    female_expression="Your composed care feels grounding and allowing compassion for yourself brings freedom.",
    other_expression="Your disciplined heart guides many and mixing tenderness with structure solidifies your support."
)

# Sextile
saturn_moon_sextile = SaturnMoonAspectInterpretation(
    aspect="Sextile",
    hook="Your feelings dance with discipline and steady care flows sincerely.",
    core_interpretation="You offer reliable comfort through thoughtful support; balancing seriousness with playfulness lifts spirits.",
    male_expression="Your consistent kindness feels like a rock and inviting joy keeps your care vibrant.",
    female_expression="Your nurturing steadiness sustains others and embracing spontaneity sparks warmth.",
    other_expression="Your dependability nurtures trust and mixing lighthearted moments brightens your presence."
)

# Trine
saturn_moon_trine = SaturnMoonAspectInterpretation(
    aspect="Trine",
    hook="Your heart and habits align and integrity feels effortless.",
    core_interpretation="You express care with natural grace, making others feel safe; stretching your comfort zone brings new vitality.",
    male_expression="Your steady empathy inspires trust and trying fresh experiences energizes your warmth.",
    female_expression="Your calm nurture feels healing and welcoming novelty keeps your heart open.",
    other_expression="Your balanced care uplifts all and occasionally shaking up routine renews your spirit."
)

# Square
saturn_moon_square = SaturnMoonAspectInterpretation(
    aspect="Square",
    hook="Your feelings bump into your fears and tension shapes your courage.",
    core_interpretation="You confront emotional challenges head on, and each breakthrough deepens your self compassion.",
    male_expression="Your guarded kindness teaches resilience and letting walls down invites connection.",
    female_expression="Your careful heart builds strength and embracing softness shows true power.",
    other_expression="Your struggle builds empathy and opening fully completes your growth."
)

# Opposition
saturn_moon_opp = SaturnMoonAspectInterpretation(
    aspect="Opposition",
    hook="You seek comfort in others and balance grows through shared support.",
    core_interpretation="You learn to care for yourself by caring with others, and healthy give and take brings real security.",
    male_expression="Your reliability draws people in and inviting others to support you fortifies your spirit.",
    female_expression="Your reflective nurture blossoms through partnership and trusting closeness frees your heart.",
    other_expression="Your mirrored care teaches mutual strength and embracing interdependence enriches your path."
)

saturn_moon_aspects = {
    "Conjunction": saturn_moon_conj,
    "Sextile": saturn_moon_sextile,
    "Trine": saturn_moon_trine,
    "Square": saturn_moon_square,
    "Opposition": saturn_moon_opp
}
