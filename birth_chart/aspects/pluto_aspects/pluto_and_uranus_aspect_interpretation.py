class PlutoUranusAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
pluto_uranus_conj = PlutoUranusAspectInterpretation(
    aspect="Conjunction",
    hook="You transform through bold rebellion.",
    core_interpretation="You ignite intense and radical transformation, driving revolutionary energy that breaks old patterns in favor of groundbreaking evolution. This aspect empowers you to lead and inspire change.",
    male_expression="You are a revolutionary catalyst, with a presence that sparks significant change. Your journey involves using your insights to challenge and transform established norms.",
    female_expression="You are a trailblazing transformer, where power meets freedom at a profound level. Your path requires balancing your intensity with visionary leadership.",
    other_expression="You are a collective iconoclast, with personal evolution mirroring cultural revolution. Your strength lies in your ability to inspire and lead transformative change."
)

# Sextile
pluto_uranus_sextile = PlutoUranusAspectInterpretation(
    aspect="Sextile",
    hook="You shift through insightful depth.",
    core_interpretation="You harmonize power and progress, offering subtle activist energy and smooth pathways to innovate deep seated transformation. This aspect supports your journey of personal growth and societal change.",
    male_expression="You are a quiet revolutionist, seeking change through empowered insight. Your journey involves using your vision to guide and transform.",
    female_expression="You are a gentle reformer, transforming structures with creative ease. Your path is marked by continuous evolution and understanding.",
    other_expression="You are a strategic innovator, with depth and change aligning fluidly. Your strength lies in your ability to inspire and lead transformative progress."
)

# Trine
pluto_uranus_trine = PlutoUranusAspectInterpretation(
    aspect="Trine",
    hook="Your evolution resonates with depth.",
    core_interpretation="You experience graceful revolutionary transformation, allowing instinct, authenticity, and collective awakening to unfold with ease. This aspect grants you the ability to integrate change naturally.",
    male_expression="You are an effortless reformer, with authority blending with originality. Your journey involves using your insights to inspire and lead with authenticity.",
    female_expression="You are a harmonious disruptor, transforming through visionary flow. Your path is marked by continuous growth and renewal.",
    other_expression="You are a fluid catalyst, with personal growth aligning with wider evolution. Your strength lies in your ability to transform and lead with ease."
)

# Square
pluto_uranus_square = PlutoUranusAspectInterpretation(
    aspect="Square",
    hook="Your power challenges change.",
    core_interpretation="You experience intense clashes between authority and freedom, often triggering profound crises or rebellion that demand personal or cultural metamorphosis. This aspect pushes you to evolve and lead with resilience.",
    male_expression="You are a conflicted innovator, with adversity fueling creativity and reform. Your journey involves overcoming internal struggles to emerge stronger.",
    female_expression="You are a bold transformer, with tension giving birth to catalytic insight. Your path requires facing and resolving your challenges.",
    other_expression="You are a pressure driven rebel, with evolution forged through confrontation. Your strength comes from facing and overcoming your struggles."
)

# Opposition
pluto_uranus_opp = PlutoUranusAspectInterpretation(
    aspect="Opposition",
    hook="Your reflection reveals transformative power.",
    core_interpretation="You experience mirrored power dynamics and change catalyzed through relationships, calling for balance between personal transformation and collective freedom. This aspect highlights the need to integrate your vision with external influences.",
    male_expression="You are a reflective insurgent, learning transformation through confrontation. Your journey involves understanding and managing your dynamics with others.",
    female_expression="You are a relational reformer, with growth driven through interactions. Your path is marked by continuous evolution through relationships.",
    other_expression="You are an interdependent catalyst, with evolution unfolding through polarity. Your strength lies in your ability to integrate your insights with external influences."
)

pluto_uranus_aspects = {
    "Conjunction": pluto_uranus_conj,
    "Sextile": pluto_uranus_sextile,
    "Trine": pluto_uranus_trine,
    "Square": pluto_uranus_square,
    "Opposition": pluto_uranus_opp
}
