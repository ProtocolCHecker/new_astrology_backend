class MercuryMarsAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Mercury Conjunct Mars
mercury_conjunct_mars = MercuryMarsAspectInterpretation(
    aspect="Conjunct",
    hook="Your words are weapons. Sharp, fast, and forged in conviction.",
    core_interpretation="Your mind is fueled with fierce clarity and bold assertion. Tempering impulse with reflection ensures your sharp insights land with care.",
    male_expression="You speak with fiery confidence. Pausing to listen transforms debate into dialogue.",
    female_expression="Your directness commands attention. Softening your edge amplifies connection.",
    other_expression="You are a verbal warrior. Harnessing that energy into focused inquiry refines your power."
)

# Mercury Sextile Mars
mercury_sextile_mars = MercuryMarsAspectInterpretation(
    aspect="Sextile",
    hook="Your mind strikes with precision. Articulate, focused, and ready for action.",
    core_interpretation="Your thinking is blended by assertive delivery. Channeling that synergy turns conversation into creative strategy.",
    male_expression="You lead with logical clarity. Pair determination with empathy to heighten your influence.",
    female_expression="Your focused speech drives results. Balancing ambition with warmth deepens impact.",
    other_expression="You are a tactful dynamo. Aligning purpose with persuasion elevates every exchange."
)

# Mercury Trine Mars
mercury_trine_mars = MercuryMarsAspectInterpretation(
    aspect="Trine",
    hook="Your thoughts flow into action. Smooth, strong, and timely.",
    core_interpretation="You are granted seamless integration of thought and movement. Your decisive clarity empowers others when you remain open to new angles.",
    male_expression="You speak and act in harmony. Welcoming feedback sharpens your edge.",
    female_expression="Your responses feel instinctive. Inviting challenge expands your growth.",
    other_expression="You are a composed powerhouse. Balancing initiative with reflection sustains your momentum."
)

# Mercury Square Mars
mercury_square_mars = MercuryMarsAspectInterpretation(
    aspect="Square",
    hook="Your tongue is sharp. Fierce in thought, fiery in response.",
    core_interpretation="You create intense mental energy and quick reactions. Learning to pause refines your passion into persuasive dialogue.",
    male_expression="You challenge with bold ideas. Tempering heat with empathy builds bridges.",
    female_expression="Your outspoken nature cuts through noise. Softening tone strengthens your message.",
    other_expression="You are a mental combatant. Harnessing that fire through mindful speech unlocks true influence."
)

# Mercury Opposite Mars
mercury_opposite_mars = MercuryMarsAspectInterpretation(
    aspect="Opposition",
    hook="Your mind wrestles with will. Torn between speaking up and holding back.",
    core_interpretation="You highlight inner debate between impulse and restraint. Mastering that tension lets your voice become both bold and balanced.",
    male_expression="You stand firm in your beliefs. Choosing when to speak elevates your leadership.",
    female_expression="Your courage to speak is fierce. Knowing when to pause empowers your advocacy.",
    other_expression="You are an inner debater. Harmonizing assertion with reflection creates your strongest arguments."
)

mercury_mars_aspects = {
    "Conjunct": mercury_conjunct_mars,
    "Sextile": mercury_sextile_mars,
    "Trine": mercury_trine_mars,
    "Square": mercury_square_mars,
    "Opposition": mercury_opposite_mars
}