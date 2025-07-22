class JupiterMoonAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
moon_conjunct_jupiter = JupiterMoonAspectInterpretation(
    aspect="Conjunction",
    hook="Your heart expands with generosity and joy comes naturally to you.",
    core_interpretation="You give comfort and laughter in equal measure, making people feel hopeful. Learning to say no sometimes keeps your kindness from stretching you too thin.",
    male_expression="Your warmth feels like a beacon, drawing others in with ease. Remember to create space for your own needs; generosity flows best when it's balanced.",
    female_expression="Your bright spirit uplifts everyone you meet, and your optimism is contagious. Don't forget that restfulness fuels your joy just as much as giving does.",
    other_expression="You share abundance as freely as air grounding yourself ensures your kindness never empties your own reserve."
)

# Sextile
moon_sextile_jupiter = JupiterMoonAspectInterpretation(
    aspect="Sextile",
    hook="Your feelings shine with steady optimism and people lean on your calm faith.",
    core_interpretation="You handle life's ups and downs with gentle humor and perspective, making you a soothing companion. Balancing your big heart with practical realism helps you stay centered.",
    male_expression="Your quiet confidence comforts others in tough times. Grounding your hopes in small, daily wins keeps that confidence strong.",
    female_expression="Your steady kindness and insight feel like a guiding light. Remember that even optimists need moments of pause to stay clear eyed.",
    other_expression="Your balanced outlook lifts spirits wherever you go and anchoring your dreams in action makes them flourish."
)

# Trine
moon_trine_jupiter = JupiterMoonAspectInterpretation(
    aspect="Trine",
    hook="Your feelings flow with faith and joy is a philosophy you live by.",
    core_interpretation="You inspire others simply by believing in good outcomes, and that belief circles right back to you. Keeping your ideals grounded in reality ensures they stand the test of time.",
    male_expression="Your trusting nature teaches people to hope again. Checking in with small details ensures your faith stays well placed.",
    female_expression="Your inclusive warmth makes everyone feel like family. Combining that with careful planning brings your vision to life.",
    other_expression="Your hopefulness guides others pairing it with mindful steps turns dreams into reality."
)

# Square
moon_square_jupiter = JupiterMoonAspectInterpretation(
    aspect="Square",
    hook="Your heart stretches wide and sometimes it pulls you off balance.",
    core_interpretation="Your generosity and enthusiasm can overwhelm if you don't set boundaries, but learning to pace yourself brings you deeper fulfillment.",
    male_expression="Your big hearted nature risks burnout without time to recharge. Honoring your limits brings lasting joy.",
    female_expression="Your caring spirit soars, yet you may give more than you have. Practicing self care ensures you can continue to uplift others.",
    other_expression="Your expansive emotions teach you to blend kindness with self restraint, creating a sustainable flow of warmth."
)

# Opposition
moon_opposite_jupiter = JupiterMoonAspectInterpretation(
    aspect="Opposition",
    hook="Your emotions mirror the horizon and searching balance between comfort and growth.",
    core_interpretation="You're torn between nurturing others and pursuing your own adventure, and learning to honor both parts of yourself brings true harmony.",
    male_expression="Your generosity needs a partner who understands your need for freedom. Balancing support with self exploration fuels your spirit.",
    female_expression="You give deeply but crave new horizons and finding a rhythm between caring and curiosity nurtures your soul.",
    other_expression="Your journey blends compassion with discovery and embracing both brings you home to yourself."
)

jupiter_moon_aspects = {
    "Conjunction": moon_conjunct_jupiter,
    "Sextile": moon_sextile_jupiter,
    "Trine": moon_trine_jupiter,
    "Square": moon_square_jupiter,
    "Opposition": moon_opposite_jupiter
}
