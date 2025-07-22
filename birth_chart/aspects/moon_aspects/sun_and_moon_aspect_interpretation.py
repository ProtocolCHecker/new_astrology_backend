class SunMoonAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
sun_conjunct_moon = SunMoonAspectInterpretation(
    aspect="Conjunction",
    hook="Your inner world and outer will unite and purpose and feeling blend seamlessly.",
    core_interpretation="You know what you want and feel it deeply, giving you strong self awareness; balancing that focus with flexibility brings harmony.",
    male_expression="Your confidence feels genuine and staying open to change enhances your leadership.",
    female_expression="Your instincts align with intention and embracing others' perspectives enriches your path.",
    other_expression="You radiate authenticity and mixing determination with adaptability fuels growth."
)

# Sextile
sun_sextile_moon = SunMoonAspectInterpretation(
    aspect="Sextile",
    hook="Your will and feelings dance together and graceful and cooperative.",
    core_interpretation="You flow through life with inner ease, making others feel supported; nudging yourself toward challenge brings new strength.",
    male_expression="Your balanced approach attracts respect and welcoming discomfort expands your potential.",
    female_expression="Your steady harmony comforts those around you and trying bold steps sparks fresh energy.",
    other_expression="You unite drive and care and pushing gently beyond comfort deepens your confidence."
)

# Trine
sun_trine_moon = SunMoonAspectInterpretation(
    aspect="Trine",
    hook="You flow with yourself and emotionally whole and purposefully at peace.",
    core_interpretation="Your sense of self and your heart align so naturally that you inspire calm; inviting a little challenge prevents complacency.",
    male_expression="Your serenity comforts others and seeking novelty keeps your spirit engaged.",
    female_expression="Your inner peace feels magnetic and embracing growth keeps your warmth alive.",
    other_expression="Your centered grace uplifts all and pursuing new horizons renews your calm."
)

# Square
sun_square_moon = SunMoonAspectInterpretation(
    aspect="Square",
    hook="Your heart and will conflict and a dance of craving and control.",
    core_interpretation="You experience inner push pull, which fuels growth and self discovery when you embrace both sides of yourself.",
    male_expression="Your drive and sensitivity clash, yet each tension brings clarity. Embracing your feelings alongside ambition deepens your insight.",
    female_expression="Your passion and need for peace compete, guiding you toward balance. Nurturing both strength and softness makes you whole.",
    other_expression="Your inner conflict forges resilience and honoring every part of you transforms tension into power."
)

# Opposition
sun_opposition_moon = SunMoonAspectInterpretation(
    aspect="Opposition",
    hook="You see yourself in contrast and growth emerges through reflection.",
    core_interpretation="You learn self understanding through your relationships, turning external mirrors into pathways for inner harmony.",
    male_expression="Your identity shines in connection and embracing reciprocity strengthens your sense of self.",
    female_expression="Your emotional depth surfaces through others and balancing autonomy and intimacy empowers you.",
    other_expression="Your mirrored interactions guide your journey and each dialogue opens a new layer of self awareness."
)

sun_moon_aspects = {
    "Conjunction": sun_conjunct_moon,
    "Sextile": sun_sextile_moon,
    "Trine": sun_trine_moon,
    "Square": sun_square_moon,
    "Opposition": sun_opposition_moon
}
