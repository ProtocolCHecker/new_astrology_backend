class PlutoMercuryAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
pluto_mercury_conj = PlutoMercuryAspectInterpretation(
    aspect="Conjunction",
    hook="Your words carry profound depth.",
    core_interpretation="You possess a powerful mind with penetrating thoughts and psychological insights, granting you the ability to communicate with intensity. This aspect demands balance to avoid becoming overly obsessive or paranoid.",
    male_expression="You are an intense communicator, delving into truths and learning to temper your depth with compassion. Your journey involves using your insights to inspire and transform.",
    female_expression="You are a psychological speaker, exploring hidden meanings and grounding your insights in empathy. Your path requires balancing your intensity with understanding.",
    other_expression="You are a mental alchemist, discovering power through the conscious transformation of ideas. Your strength lies in your ability to communicate profound truths."
)

# Sextile
pluto_mercury_sextile = PlutoMercuryAspectInterpretation(
    aspect="Sextile",
    hook="Your insight flows with grace.",
    core_interpretation="You have a strategic mind with deep analytical power, blending clear communication and mental resilience. This aspect supports your ability to influence subtly and think profoundly.",
    male_expression="You are a stealth thinker, discerning hidden truths and speaking with measured influence. Your journey involves using your insights to guide and transform.",
    female_expression="You are an insightful strategist, balancing depth and diplomacy in your thoughts. Your path is marked by continuous growth and understanding.",
    other_expression="You are a quiet investigator, with your mind and transformations weaving smoothly. Your strength lies in your ability to communicate and influence effectively."
)

# Trine
pluto_mercury_trine = PlutoMercuryAspectInterpretation(
    aspect="Trine",
    hook="Your thoughts reveal deep insights.",
    core_interpretation="You possess effortless psychological insight and transformative intellect, enabling you to communicate with depth and intuitive clarity. This aspect allows your insights to emerge naturally and powerfully.",
    male_expression="You are a natural psychologist, with truths emerging from your voice with ease. Your journey involves using your insights to inspire and lead.",
    female_expression="You are a serene truth seeker, with intellectual transformations feeling fluid and natural. Your path is marked by continuous growth and renewal.",
    other_expression="You are a flowing detective, with transformation through inspired thought. Your strength lies in your ability to communicate profound insights."
)

# Square
pluto_mercury_square = PlutoMercuryAspectInterpretation(
    aspect="Square",
    hook="Your mind grapples with intensity.",
    core_interpretation="You experience friction between your intellect and transformation, prompting deep thought patterns and communicative challenges that forge mental strength. This aspect pushes you to refine your thinking and expression.",
    male_expression="You are a restless thinker, with tension teaching clarity and self mastery. Your journey involves overcoming mental challenges to emerge stronger.",
    female_expression="You are a bold mental explorer, with conflict driving the refinement of your expression. Your path requires facing and resolving internal struggles.",
    other_expression="You are fueled by tension led insight, with growth emerging through mental challenges. Your strength comes from facing and overcoming your struggles."
)

# Opposition
pluto_mercury_opp = PlutoMercuryAspectInterpretation(
    aspect="Opposition",
    hook="Your voice reflects hidden depths.",
    core_interpretation="You experience psychological projection in communication, challenging you to balance inner intensity with relationship awareness and honest expression. This aspect highlights the need to integrate your insights with external interactions.",
    male_expression="You are a reflective speaker, learning to temper depth with relational sensitivity. Your journey involves understanding and managing your power dynamics with others.",
    female_expression="You are a dialogic psychologist, with growth arising through mirrored conversations. Your path is marked by continuous evolution through interactions.",
    other_expression="You are a mirror minded alchemist, with clarity growing through mental reflection. Your strength lies in your ability to integrate your insights with external influences."
)

pluto_mercury_aspects = {
    "Conjunction": pluto_mercury_conj,
    "Sextile": pluto_mercury_sextile,
    "Trine": pluto_mercury_trine,
    "Square": pluto_mercury_square,
    "Opposition": pluto_mercury_opp
}
