class MercurySunAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
mercury_sun_conj = MercurySunAspectInterpretation(
    aspect="Conjunct",
    hook="You think and will move as one. Your mind is the heart of your identity.",
    core_interpretation="This close mental alignment blends your expression with your core self. You're articulate and speak with confidence. Staying open to feedback helps your strong voice uplift rather than overshadow.",
    male_expression="You lead conversations with bold clarity. Pausing to truly listen deepens your impact.",
    female_expression="Your words carry the force of self. Making space for others enriches every exchange.",
    other_expression="You fuse thought and being. Balancing assertion with receptivity refines your message."
)

# Sextile
mercury_sun_sext = MercurySunAspectInterpretation(
    aspect="Sextile",
    hook="You chat with sunny ease. Your ideas feel both warm and sharp.",
    core_interpretation="This harmonious connection gives you natural eloquence and confidence. Your friendly tone wins trust, while humility keeps you relatable.",
    male_expression="You express with charm and clarity. Grounding your vision in others' needs amplifies your appeal.",
    female_expression="Your speech feels genuine. Embracing vulnerability makes your insights more compelling.",
    other_expression="You balance wit and warmth. Pairing optimism with precision enhances every conversation."
)

# Trine
mercury_sun_trine = MercurySunAspectInterpretation(
    aspect="Trine",
    hook="Your words flow in harmony with your spirit. Everything you say rings true.",
    core_interpretation="This flowing aspect brings effortless self-expression and creative insight. You inspire with authenticity. Remember not everyone sees things exactly as you do.",
    male_expression="You speak with natural authority. Inviting diverse views keeps your ideas fresh.",
    female_expression="Your voice feels luminous. Welcoming challenge fuels your growth.",
    other_expression="You blend identity and intellect. Remaining curious ensures your clarity endures."
)

# Square
mercury_sun_square = MercurySunAspectInterpretation(
    aspect="Square",
    hook="Your mind and ego can clash. Words sometimes feel like a battleground.",
    core_interpretation="This challenging aspect creates tension between self and thought. You may take feedback personally or speak before thinking. Developing self-awareness transforms friction into strength.",
    male_expression="You assert with fire. Tempering intensity with patience prevents regrets.",
    female_expression="Your convictions burn bright. Softening delivery nurtures understanding.",
    other_expression="You grow through mindful speech. Balancing strength with softness refines your voice."
)

# Opposition
mercury_sun_opp = MercurySunAspectInterpretation(
    aspect="Opposition",
    hook="Your voice dances with counterpoint. You learn self through every dialogue.",
    core_interpretation="This polar aspect highlights the balance between speaking and being heard. Your identity evolves through meaningful exchange when you balance assertion with listening.",
    male_expression="You shine in debate. Honoring others' truths strengthens your own.",
    female_expression="Your words mirror your self. Inviting feedback empowers both sides of conversation.",
    other_expression="You become whole through dialogue. Harmonizing self-expression and receptivity brings clarity."
)

mercury_sun_aspects = {
    "Conjunct": mercury_sun_conj,
    "Sextile": mercury_sun_sext,
    "Trine": mercury_sun_trine,
    "Square": mercury_sun_square,
    "Opposition": mercury_sun_opp
}