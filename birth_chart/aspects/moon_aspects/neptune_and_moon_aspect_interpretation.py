class MoonNeptuneAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
moon_neptune_conj = MoonNeptuneAspectInterpretation(
    aspect="Conjunction",
    hook="You drift in tides of feeling and empathy flows like waves.",
    core_interpretation="Your sensitivity and imagination paint life in vivid hues; learning clear boundaries helps you stay grounded.",
    male_expression="Your compassionate insight feels magical and anchoring yourself with routine keeps you steady.",
    female_expression="Your intuitive warmth soothes others and grounding practices add clarity to your vision.",
    other_expression="Your creative empathy inspires many and balancing dream with reality empowers your gifts."
)

# Sextile
moon_neptune_sextile = MoonNeptuneAspectInterpretation(
    aspect="Sextile",
    hook="You feel with gentle grace and your compassion knows no bounds.",
    core_interpretation="Your caring presence comforts like a healing touch; pairing it with simple structure sustains your spirit.",
    male_expression="Your warm intuition guides people softly and setting small goals channels your insight.",
    female_expression="Your nurturing vision uplifts and integrating a bit of routine brings focus.",
    other_expression="Your soulful empathy bridges worlds and roots give your beauty strength."
)

# Trine
moon_neptune_trine = MoonNeptuneAspectInterpretation(
    aspect="Trine",
    hook="Your heart whispers in dreams and insight floats free.",
    core_interpretation="Your blend of feeling and vision feels effortless; adding a dash of practicality makes your compassion truly transformative.",
    male_expression="Your poetic care feels timeless and coupling it with clear steps brings impact.",
    female_expression="Your soulful kindness resonates and pairing it with gentle plans makes dreams real.",
    other_expression="Your intuitive grace guides many and grounding your flow amplifies your reach."
)

# Square
moon_neptune_square = MoonNeptuneAspectInterpretation(
    aspect="Square",
    hook="Your emotions blur and tension calls you to find clarity.",
    core_interpretation="You swim between reality and dream, and honing discernment transforms confusion into art.",
    male_expression="Your visionary heart drifts and practicing focus sculpts your ideas.",
    female_expression="Your empathic waves wash over others and discernment gives shape to your flow.",
    other_expression="Your creative struggle refines your vision and balance births brilliance."
)

# Opposition
moon_neptune_opp = MoonNeptuneAspectInterpretation(
    aspect="Opposition",
    hook="Your mirror is mist and relationships reflect your depth.",
    core_interpretation="You project your empathy onto others, learning healthy boundaries brings true connection.",
    male_expression="Your caring nature reaches out and knowing when to step back protects your heart.",
    female_expression="Your intuitive bonds deepen and balancing giving and receiving keeps love bright.",
    other_expression="Your mirrored empathy enlightens and grounded self care sustains your gift."
)

moon_neptune_aspects = {
    "Conjunction": moon_neptune_conj,
    "Sextile": moon_neptune_sextile,
    "Trine": moon_neptune_trine,
    "Square": moon_neptune_square,
    "Opposition": moon_neptune_opp
}
