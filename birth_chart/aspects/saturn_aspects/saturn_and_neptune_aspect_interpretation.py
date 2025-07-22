class SaturnNeptuneAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
saturn_neptune_conj = SaturnNeptuneAspectInterpretation(
    aspect="Conjunction",
    hook="You balance dreams with discipline, tempering vision with reality.",
    core_interpretation="You merge structure with imagination, creating a tension between practical limits and idealistic longing. You learn to bring your dreams down to earth without losing their essence, finding a way to make your visions tangible and meaningful.",
    male_expression="You are a grounded visionary, with ideals that gain clarity when tested by reality. This journey helps you refine your dreams and make them achievable, leading to personal growth and fulfillment.",
    female_expression="You are a serious dreamer, learning to build while imagining with heart. This process of integrating practicality with vision helps you create a life that is both meaningful and inspired.",
    other_expression="You are a spiritual realist, bridging illusion and order through disciplined compassion. This balance allows you to pursue your dreams with a sense of purpose and responsibility, making them a reality."
)

# Sextile
saturn_neptune_sextile = SaturnNeptuneAspectInterpretation(
    aspect="Sextile",
    hook="Your structure serves wonder, building ideals with integrity.",
    core_interpretation="You have practical compassion, where dreams are thoughtfully realized step by step. You combine patience with faith to create results that feel both meaningful and enduring, making your visions a reality.",
    male_expression="You are a strategic nurturer, constructing with purpose and heart. This trait makes you a dependable and inspiring figure, capable of turning dreams into tangible achievements.",
    female_expression="You are a steady idealist, manifesting beauty with responsibility. This balance of traits makes you a respected and admired figure, capable of creating a life that is both inspired and grounded.",
    other_expression="You are a visionary builder, weaving structure into your spiritual life. This ability allows you to pursue your dreams with a sense of purpose and responsibility, making them a reality."
)

# Trine
saturn_neptune_trine = SaturnNeptuneAspectInterpretation(
    aspect="Trine",
    hook="You flow between heaven and earth, aligning purpose with divine form.",
    core_interpretation="You have a seamless blend of discipline and imagination, where inner sensitivity is guided by structure. This enables inspired creativity rooted in stability, making your dreams both achievable and meaningful.",
    male_expression="You are a creative stabilizer, with insight that is grounded and profound. This trait makes you a respected and influential figure, capable of turning visions into reality with grace and determination.",
    female_expression="You are an inspired craftsman, channeling intuition into graceful form. This ability allows you to create a life that is both beautiful and meaningful, admired for your sense of purpose and responsibility.",
    other_expression="You are a sacred architect, building dream realities with soulful precision. This balance of traits makes you a visionary and respected figure, capable of turning visions into tangible achievements."
)

# Square
saturn_neptune_square = SaturnNeptuneAspectInterpretation(
    aspect="Square",
    hook="Your dreams clash with duty, teaching reconciliation of illusion and order.",
    core_interpretation="You experience friction between desire and responsibility, often triggering disillusionment or confusion. Learning to discern fantasy from purpose and bring structure to inspiration helps you grow and achieve your dreams.",
    male_expression="You are a challenged idealist, with a path that grows through building out of doubt. This journey of overcoming obstacles helps you refine your dreams and make them a reality, leading to personal growth and fulfillment.",
    female_expression="You are a struggling mystic, refining faith with practical tests. This process of facing and overcoming challenges helps you integrate your dreams with reality, creating a life that is both inspired and grounded.",
    other_expression="You have tension born clarity, learning shape through spirit and structure. This dynamic of facing and resolving tensions helps you develop a more robust and resilient character, capable of pursuing your dreams with a sense of purpose and responsibility."
)

# Opposition
saturn_neptune_opp = SaturnNeptuneAspectInterpretation(
    aspect="Opposition",
    hook="Your boundaries face the mist, holding form against uncertainty.",
    core_interpretation="You balance control with openness, where relationships mirror the need to define structure around compassion and dream without dissolving boundaries. This dynamic teaches you to integrate your dreams with reality, creating a life that is both inspired and grounded.",
    male_expression="You are a reflective boundary keeper, learning empathy with firm presence. This balance of traits makes you a respected and trusted figure, capable of providing both emotional and practical support.",
    female_expression="You are a sensitive stabilizer, integrating responsibility and care in relation. This ability allows you to create a life that is both meaningful and inspired, admired for your sense of purpose and compassion.",
    other_expression="You are a mirror mediator, building emotional clarity through relational wisdom. This process of understanding and integrating different aspects of yourself helps you grow into a well rounded and successful individual, capable of pursuing your dreams with a sense of purpose and responsibility."
)

saturn_neptune_aspects = {
    "Conjunction": saturn_neptune_conj,
    "Sextile": saturn_neptune_sextile,
    "Trine": saturn_neptune_trine,
    "Square": saturn_neptune_square,
    "Opposition": saturn_neptune_opp
}
