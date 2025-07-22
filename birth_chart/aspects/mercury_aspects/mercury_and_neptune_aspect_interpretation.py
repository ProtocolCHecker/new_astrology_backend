class MercuryNeptuneAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunct
mercury_conjunct_neptune = MercuryNeptuneAspectInterpretation(
    aspect="Conjunct",
    hook="Your thoughts drift like mist. Poetic, mysterious, and full of magic.",
    core_interpretation="You blend intuition with imagination in your mind. Grounding ideas in reality helps turn vision into value.",
    male_expression="You speak in symbols. Adding structure to your insights ensures they shine.",
    female_expression="Your words feel like dreams. Clarifying boundaries brings focus to your creativity.",
    other_expression="You channel ethereal ideas. Anchoring them gives your magic form."
)

# Trine
mercury_trine_neptune = MercuryNeptuneAspectInterpretation(
    aspect="Trine",
    hook="Your mind paints what words can't hold. Graceful, deep, and attuned to subtle truths.",
    core_interpretation="You are granted as a natural flow between clarity and compassion. Trusting your hunches while verifying facts brings elegance to your intuition.",
    male_expression="Your voice inspires. Mixing insight with evidence elevates your wisdom.",
    female_expression="You feel through language. Pairing emotion with logic amplifies your impact.",
    other_expression="You are a soulful guide. Grounding your visions empowers others."
)

# Sextile
mercury_sextile_neptune = MercuryNeptuneAspectInterpretation(
    aspect="Sextile",
    hook="Your thoughts shimmer with insight. Gentle, inspired, and full of creative spark.",
    core_interpretation="You infuse your speech with poetic resonance. Channeling that spark with clear intent makes your message unforgettable.",
    male_expression="Your tone comforts. Linking dreams to purpose gives them power.",
    female_expression="Your insights soothe. Balancing fantasy with function sustains your vision.",
    other_expression="You bridge imagination and reality. Solidifying ideas brings them to life."
)

# Square
mercury_square_neptune = MercuryNeptuneAspectInterpretation(
    aspect="Square",
    hook="Your mind wanders strange paths. Sometimes magical, sometimes misleading.",
    core_interpretation="You challenge yourself to distinguish fantasy from fact. Developing discernment lets your creativity become your greatest gift.",
    male_expression="You dream vividly. Practicing clarity stops illusions from misguiding you.",
    female_expression="Your empathy runs deep. Grounding emotions prevents misunderstanding.",
    other_expression="You transform confusion into art. Focus channels your muse."
)

# Opposition
mercury_opposite_neptune = MercuryNeptuneAspectInterpretation(
    aspect="Opposition",
    hook="You listen for truths between the lines. But sometimes you echo dreams, not facts.",
    core_interpretation="You are pulled between reason and revelation. Integrating both disciplines sharpens your insight and steadies your voice.",
    male_expression="Your mystic flair intrigues. Pairing it with precision ensures your vision lands.",
    female_expression="Your intuition guides. You thrive when you balance faith with fact.",
    other_expression="You are a dream weaver. Rooting your words in truth makes them resonate."
)

mercury_neptune_aspects = {
    "Conjunct": mercury_conjunct_neptune,
    "Trine": mercury_trine_neptune,
    "Sextile": mercury_sextile_neptune,
    "Square": mercury_square_neptune,
    "Opposition": mercury_opposite_neptune
}