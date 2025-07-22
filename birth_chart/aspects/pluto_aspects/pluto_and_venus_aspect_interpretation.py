class PlutoVenusAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
pluto_venus_conj = PlutoVenusAspectInterpretation(
    aspect="Conjunction",
    hook="Your love transforms deeply.",
    core_interpretation="You experience a fusion of deep transformation with affection, giving you magnetic charm and intense relational power. This aspect empowers you to heal and evolve through your relationships, though it demands balance to avoid obsession.",
    male_expression="You are a magnetic lover, with transformational depth in relationships. Your journey involves guarding against obsession and using your insights to foster growth.",
    female_expression="You are a deep romantic, healing through love yet challenged by emotional extremes. Your path requires balancing your intensity with self awareness and compassion.",
    other_expression="You are a catalytic heart, where love becomes a transformative force. Your strength lies in balancing passion with care and using your insights to guide your relationships."
)

# Sextile
pluto_venus_sextile = PlutoVenusAspectInterpretation(
    aspect="Sextile",
    hook="Your love is a subtle power.",
    core_interpretation="You have a potent yet gentle emotional transformation, fostering healing relationships and evolving self worth through relational insight. This aspect supports your journey of personal growth and deep connections.",
    male_expression="You are an insightful partner, with relationships deepening your compassion and strength. Your journey involves using your insights to foster healing and transformation.",
    female_expression="You are an empathic transformer, with love refining your personal power with grace. Your path is marked by continuous growth and understanding.",
    other_expression="You are a quiet alchemist, with bonds cultivating transformation subtly. Your strength lies in your ability to heal and transform through your relationships."
)

# Trine
pluto_venus_trine = PlutoVenusAspectInterpretation(
    aspect="Trine",
    hook="Your love flows with purpose.",
    core_interpretation="You experience harmonious emotional depth, allowing profound yet graceful relational power and resilient intimacy to evolve effortlessly. This aspect grants you the ability to integrate your emotions with ease.",
    male_expression="You are a composed healer, with deep bonds forming with ease and authority. Your journey involves using your insights to inspire and lead with authenticity.",
    female_expression="You are a fluid transformer, with love nurturing soul level renewal naturally. Your path is marked by continuous growth and renewal.",
    other_expression="You are a harmonious alchemist, with relational power flowing elegantly. Your strength lies in your ability to transform and heal through your emotional depth."
)

# Square
pluto_venus_square = PlutoVenusAspectInterpretation(
    aspect="Square",
    hook="Your passion challenges your power.",
    core_interpretation="You experience tension between desire and control, unleashing intense emotions and growth through relational challenges. This aspect pushes you to evolve and lead with resilience.",
    male_expression="You are a passionate lover, learning self worth through handling intensity. Your journey involves overcoming internal struggles to emerge stronger.",
    female_expression="You are an intense romantic, with boundary challenges catalyzing transformation. Your path requires facing and resolving your challenges.",
    other_expression="You are a pressure tempered heart, with clarity arising from relational friction. Your strength comes from facing and overcoming your struggles."
)

# Opposition
pluto_venus_opp = PlutoVenusAspectInterpretation(
    aspect="Opposition",
    hook="Your reflection reveals transformative desire.",
    core_interpretation="You experience relational projection and power imbalances, urging integration of deeper dynamics through mirrored intimacy and emotional understanding. This aspect highlights the need to balance your inner depth with external connections.",
    male_expression="You are a reflective lover, learning balance through relational power dynamics. Your journey involves understanding and managing your emotional dynamics with others.",
    female_expression="You are a mirror of depth, growing by facing your partner's reflections. Your path is marked by continuous evolution through interactions.",
    other_expression="You are a relational alchemist, with transformation unfolding in mirrored bonds. Your strength lies in your ability to integrate your emotional insights with external influences."
)

pluto_venus_aspects = {
    "Conjunction": pluto_venus_conj,
    "Sextile": pluto_venus_sextile,
    "Trine": pluto_venus_trine,
    "Square": pluto_venus_square,
    "Opposition": pluto_venus_opp
}
