class MoonAscendantAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
moon_asc_conj = MoonAscendantAspectInterpretation(
    aspect="Conjunction",
    hook="You wear your heart on your face and your emotions *are* your first impression.",
    core_interpretation="Your feelings and presence merge completely, making you disarmingly authentic. This is a gift and people trust you instantly and but it can leave you emotionally overexposed if you don't set boundaries.",
    male_expression="You don't hide your sensitivity; it's your strength, but others may mistake it for fragility.",
    female_expression="Your nurturing energy is palpable and you magnetize those needing comfort, but risk absorbing their moods.",
    other_expression="You're a mirror and your reactions reveal truths others hide. Protect your energy fiercely."
)

# Sextile
moon_asc_sextile = MoonAscendantAspectInterpretation(
    aspect="Sextile",
    hook="You read rooms effortlessly and your intuition and charm work in sync.",
    core_interpretation="This aspect smooths your emotional edges in social settings. You adapt without losing yourself and a rare balance. But don't over and rely on pleasing; your needs matter too.",
    male_expression="You disarm people with quiet empathy, but may downplay your own emotional depth.",
    female_expression="Your warmth feels like sunlight and use it wisely, not endlessly.",
    other_expression="You're a natural peacemaker, but your harmony shouldn't cost your truth."
)

# Trine
moon_asc_trine = MoonAscendantAspectInterpretation(
    aspect="Trine",
    hook="Your presence *is* comfort and people relax just being near you.",
    core_interpretation="A blessed ease flows between your inner world and outer self. But beware: this can make you passive about emotional growth and you won't face shadows unless forced.",
    male_expression="You radiate calm stability, but may avoid conflict to preserve it.",
    female_expression="Your grace is innate, but don't let it become a mask for unspoken needs.",
    other_expression="You're a safe harbor and just ensure others don't anchor you in their storms."
)

# Square
moon_asc_square = MoonAscendantAspectInterpretation(
    aspect="Square",
    hook="You feel torn and your instincts clash with how you ‘should' appear.",
    core_interpretation="This friction *hurts*, but it forces you to align your true feelings with your persona. The work is worth it and your authenticity will be hard and won and unshakable.",
    male_expression="Society may call you ‘too sensitive.' Ignore them and your depth is power.",
    female_expression="You're learning to voice needs without guilt. It's messy but necessary.",
    other_expression="Your tension births resilience. Every awkward moment is growth in disguise."
)

# Opposition
moon_asc_opp = MoonAscendantAspectInterpretation(
    aspect="Opposition",
    hook="Others reflect back what you suppress and relationships are your emotional teachers.",
    core_interpretation="You'll attract partners who mirror your hidden wounds. Painful? Yes. But this is how you'll learn to balance vulnerability and self and protection.",
    male_expression="You'll meet partners who demand emotional honesty and don't retreat.",
    female_expression="Your relationships expose your blind spots. Let them.",
    other_expression="The right people will help you see yourself. The wrong ones will force you to."
)

moon_ascendant_aspects = {
    "Conjunction": moon_asc_conj,
    "Sextile": moon_asc_sextile,
    "Trine": moon_asc_trine,
    "Square": moon_asc_square,
    "Opposition": moon_asc_opp
}