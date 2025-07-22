class MercuryPlutoAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunct
mercury_conjunct_pluto = MercuryPlutoAspectInterpretation(
    aspect="Conjunct",
    hook="Your mind is a scalpel. Cutting deep, questioning everything, fearing nothing.",
    core_interpretation="This intense mental alignment gives you penetrating insight and fearless curiosity. Channeling your intensity with tact transforms discoveries into empowerment.",
    male_expression="You speak with precision and power. Balancing force with empathy prevents overwhelm.",
    female_expression="Your words probe beneath surfaces. Pausing to nurture keeps your depth sustainable.",
    other_expression="You uncover hidden truths. Tempering zeal with care sharpens your impact."
)

# Sextile
mercury_sextile_pluto = MercuryPlutoAspectInterpretation(
    aspect="Sextile",
    hook="Your words carry weight. Measured, thoughtful, and quietly transformative.",
    core_interpretation="This harmonious connection grants subtle power in speech and thought. Using your clarity to support others amplifies your influence.",
    male_expression="You strategize in silence. Speaking at the right moment magnifies your message.",
    female_expression="Your insight heals. Choosing your words makes every phrase count.",
    other_expression="You connect depth and dialogue. Timing your revelations sustains trust."
)

# Trine
mercury_trine_pluto = MercuryPlutoAspectInterpretation(
    aspect="Trine",
    hook="Your insight flows like shadow and light. Smooth, deep, and compelling.",
    core_interpretation="This flowing aspect merges perception and expression seamlessly. Sharing your wisdom with compassion ensures your words resonate long after they're spoken.",
    male_expression="You speak with calm authority. Inviting dialogue enriches your presence.",
    female_expression="Your depth illuminates. Balancing intensity with gentleness engages hearts.",
    other_expression="You are a mental alchemist. Blending truth with subtlety transforms minds."
)

# Square
mercury_square_pluto = MercuryPlutoAspectInterpretation(
    aspect="Square",
    hook="Your mind challenges reality. You question, confront, and compel truth open.",
    core_interpretation="This dynamic tension fuels relentless inquiry and fierce debate. Learning to listen as sharply as you speak refines your transformative gift.",
    male_expression="You confront with boldness. Softening tone deepens your reach.",
    female_expression="Your curiosity can intimidate. Mixing patience with passion eases tension.",
    other_expression="You spark powerful change. Grounding intensity nourishes connection."
)

# Opposition
mercury_opposite_pluto = MercuryPlutoAspectInterpretation(
    aspect="Opposition",
    hook="Your mind mirrors shadows. Drawn to secrets, shaped by confrontation.",
    core_interpretation="This polar aspect highlights tension between your insight and others' defenses. Choosing collaboration over conflict magnifies your transformational potential.",
    male_expression="You debate with intensity. Embracing shared truth expands your power.",
    female_expression="Your penetrating gaze can wound. Gentle openness heals.",
    other_expression="You reflect hidden depths. Uniting curiosity with compassion awakens growth."
)

mercury_pluto_aspects = {
    "Conjunct": mercury_conjunct_pluto,
    "Sextile": mercury_sextile_pluto,
    "Trine": mercury_trine_pluto,
    "Square": mercury_square_pluto,
    "Opposition": mercury_opposite_pluto
}