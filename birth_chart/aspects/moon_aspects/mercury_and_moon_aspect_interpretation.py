class MercuryMoonAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
moon_conjunct_mercury = MercuryMoonAspectInterpretation(
    aspect="Conjunction",
    hook="Your heart and mind speak as one and empathy meets wit.",
    core_interpretation="You weave feelings into every thought, making your words resonate; sometimes stepping back into silence refreshes your insight.",
    male_expression="Your natural warmth sharpens your ideas and pausing to listen deepens your wisdom.",
    female_expression="Your intuitive voice feels sincere and taking quiet moments balances your flow.",
    other_expression="Your heartfelt insights comfort and enlighten and stillness enriches that gift."
)

# Sextile
moon_sextile_mercury = MercuryMoonAspectInterpretation(
    aspect="Sextile",
    hook="Your thoughts have heart and empathy gives your words weight.",
    core_interpretation="You express feelings with gentle clarity, which others find reassuring; grounding emotion in facts helps you stay balanced.",
    male_expression="Your compassionate words guide others and pairing that with practical detail builds trust.",
    female_expression="Your caring tone soothes and adding structure helps your message land.",
    other_expression="Your blend of kindness and clarity charms everyone and anchoring feeling in logic sharpens your edge."
)

# Trine
moon_trine_mercury = MercuryMoonAspectInterpretation(
    aspect="Trine",
    hook="Your voice flows from the heart and sincere, sensitive, and smooth.",
    core_interpretation="Your ease in blending thought and feeling inspires trust; inviting challenge keeps your perspective fresh.",
    male_expression="Your calm insight uplifts and welcoming different views enriches your depth.",
    female_expression="Your gentle eloquence resonates and curiosity expands your reach.",
    other_expression="Your balanced speech connects deeply and remaining open fuels your growth."
)

# Square
moon_square_mercury = MercuryMoonAspectInterpretation(
    aspect="Square",
    hook="Your mind and heart spar and honesty grows through tension.",
    core_interpretation="You wrestle with emotion and logic, forging clear understanding; honoring both sides brings true clarity.",
    male_expression="Your candid reflections can sting, yet each moment teaches compassion.",
    female_expression="Your insightful honesty challenges comfort, guiding you to deeper empathy.",
    other_expression="Your internal dialogue strengthens your voice and integrating both sides refines your truth."
)

# Opposition
moon_opposite_mercury = MercuryMoonAspectInterpretation(
    aspect="Opposition",
    hook="Your heart questions your head and balance is your art.",
    core_interpretation="You translate feelings into thought and vice versa, gaining depth in every exchange; practicing patience allows your message to settle.",
    male_expression="Your thoughtful empathy shines when you let silence and words share the stage.",
    female_expression="Your insightful caring blooms when you trust both head and heart equally.",
    other_expression="Your dual awareness guides others and harmonizing emotion and reason reveals your wisdom."
)

mercury_moon_aspects = {
    "Conjunction": moon_conjunct_mercury,
    "Sextile": moon_sextile_mercury,
    "Trine": moon_trine_mercury,
    "Square": moon_square_mercury,
    "Opposition": moon_opposite_mercury
}
