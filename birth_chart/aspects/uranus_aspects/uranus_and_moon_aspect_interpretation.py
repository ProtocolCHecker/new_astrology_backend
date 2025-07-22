class UranusMoonAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
uranus_moon_conj = UranusMoonAspectInterpretation(
    aspect="Conjunction",
    hook="Your feelings shift without warning.",
    core_interpretation="You experience emotions in sudden waves and intuitive, intense, and often unpredictable. You need freedom to feel without limits, but that same need can make it hard for others to truly reach you.",
    male_expression="You sense emotional change before it happens, but your reactions may feel hard to follow. Learning to pause before you act helps you connect without losing your independence.",
    female_expression="You're deeply sensitive but need space to feel on your own terms. When you honor both your need for closeness and your craving for freedom, you thrive.",
    other_expression="You feel like a live wire and emotionally charged, deeply aware, and hard to box in. Your journey is about trusting your emotional flow while grounding in safety."
)

# Sextile
uranus_moon_sextile = UranusMoonAspectInterpretation(
    aspect="Sextile",
    hook="Your emotions breathe with freedom.",
    core_interpretation="You feel things deeply, but you also give yourself the space to stay flexible and open. You have a refreshing emotional presence that often helps others loosen up and be more authentic around you.",
    male_expression="You show care in ways that are original and uplifting. Your emotional world is both deep and surprisingly light and people find comfort in your presence.",
    female_expression="You blend intuition with emotional freedom, creating space for others to be themselves. You're nurturing without clinging, and it makes you magnetic.",
    other_expression="You offer warmth and spontaneity in equal measure, making emotional connection feel like a breath of fresh air. You teach others that care doesn't have to feel heavy."
)

# Trine
uranus_moon_trine = UranusMoonAspectInterpretation(
    aspect="Trine",
    hook="Your emotional flow is intuitive and free.",
    core_interpretation="You move through emotions with grace and inner knowing, allowing change without resistance. You're someone who brings emotional renewal simply by being present and open.",
    male_expression="You connect to your feelings with ease and clarity, offering others a sense of calm even in chaos. Your ability to adapt emotionally makes you deeply wise.",
    female_expression="You intuit what's needed before it's said, and you offer it without losing your own balance. Your care is effortless, creative, and healing.",
    other_expression="You feel deeply but lightly, able to move through change without losing your emotional center. Your intuition leads you toward the kind of freedom that soothes rather than disrupts."
)

# Square
uranus_moon_square = UranusMoonAspectInterpretation(
    aspect="Square",
    hook="Your heart wants freedom and but not without conflict.",
    core_interpretation="You often feel torn between needing emotional closeness and craving space to breathe. This tension can stir restlessness or emotional outbursts, but it's also what pushes you to grow beyond outdated emotional habits.",
    male_expression="You love fiercely but pull away just as fast. Your challenge is learning how to stay emotionally present without feeling trapped.",
    female_expression="Your emotions can feel like a storm and sudden, intense, and hard to contain. But each wave teaches you something vital about what you really need to feel safe and free.",
    other_expression="You're wired for emotional truth, even when it disrupts the peace. Your evolution lies in making space for both connection and independence without needing to choose one over the other."
)

# Opposition
uranus_moon_opp = UranusMoonAspectInterpretation(
    aspect="Opposition",
    hook="Others stir emotions you didn't know you had.",
    core_interpretation="You often meet people who awaken your emotional needs in unexpected ways. Relationships can feel unstable or liberating, but they always teach you something about how you handle closeness and freedom.",
    male_expression="You feel deeply, but not always in sync with others. Through relationships, you're learning how to balance emotional connection with the need for space.",
    female_expression="You're drawn to people who shake up your emotional world and sometimes by choice, sometimes not. In those moments, your deepest emotional truths begin to emerge.",
    other_expression="You grow through the tension between needing people and needing freedom. Your emotions don't exist in a vacuum and they evolve through the mirrors others provide."
)

# Store all Uranus–Moon aspect interpretations
uranus_moon_aspects = {
    "Conjunction": uranus_moon_conj,
    "Sextile": uranus_moon_sextile,
    "Trine": uranus_moon_trine,
    "Square": uranus_moon_square,
    "Opposition": uranus_moon_opp
}
