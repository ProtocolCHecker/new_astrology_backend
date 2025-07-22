class NeptuneMoonAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
neptune_moon_conj = NeptuneMoonAspectInterpretation(
    aspect="Conjunction",
    hook="Your feelings drift like mist and empathy and imagination entwine.",
    core_interpretation="You experience emotions on a deep, intuitive level; grounding in simple self care keeps you balanced.",
    male_expression="Your compassionate heart feels vast and anchoring in routine shields your energy.",
    female_expression="Your intuitive sensitivity touches others and setting clear boundaries preserves your calm.",
    other_expression="Your dreamy empathy uplifts and practical pauses sustain your flow."
)

# Sextile
neptune_moon_sextile = NeptuneMoonAspectInterpretation(
    aspect="Sextile",
    hook="Your heart hears every whisper and care and insight blend.",
    core_interpretation="You comfort others with gentle understanding; pairing that with personal reflection keeps your spirit strong.",
    male_expression="Your soothing presence heals and journaling refines your clarity.",
    female_expression="Your tender insight guides and quiet rituals anchor your care.",
    other_expression="Your inner listening connects and mindful breaks sharpen your gift."
)

# Trine
neptune_moon_trine = NeptuneMoonAspectInterpretation(
    aspect="Trine",
    hook="Your soul flows in compassion and depth feels effortless.",
    core_interpretation="You nurture with poetic grace; interweaving simple structure lets that compassion endure.",
    male_expression="Your gentle strength inspires and small routines sustain your kindness.",
    female_expression="Your empathetic flow soothes and practical anchors bolster your warmth.",
    other_expression="Your harmonized heart uplifts and grounded habits fuel your gift."
)

# Square
neptune_moon_square = NeptuneMoonAspectInterpretation(
    aspect="Square",
    hook="Your emotions blur and tension calls you to find clarity.",
    core_interpretation="You move between feeling and fantasy, and carving out quiet focus transforms confusion into purpose.",
    male_expression="Your sensitive waves overwhelm and brief meditations sharpen your insight.",
    female_expression="Your dreamy heart wanders and anchoring yourself in small tasks refines your vision.",
    other_expression="Your emotional dance enriches and periodic pauses reveal your path."
)

# Opposition
neptune_moon_opp = NeptuneMoonAspectInterpretation(
    aspect="Opposition",
    hook="Your heart sees itself in others and relationships reflect your depth.",
    core_interpretation="You learn about your own boundaries through connection; balancing giving and receiving fosters mutual healing.",
    male_expression="Your mirrored empathy guides growth and practicing self compassion anchors your care.",
    female_expression="Your reflective kindness teaches balance and inviting support sustains you.",
    other_expression="Your shared sensitivity enlightens and grounded self care secures your gift."
)

neptune_moon_aspects = {
    "Conjunction": neptune_moon_conj,
    "Sextile": neptune_moon_sextile,
    "Trine": neptune_moon_trine,
    "Square": neptune_moon_square,
    "Opposition": neptune_moon_opp
}
