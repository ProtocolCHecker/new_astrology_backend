class NeptuneAscendantAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
neptune_asc_conj = NeptuneAscendantAspectInterpretation(
    aspect="Conjunction",
    hook="You wear fog and light together  and  your presence feels spiritual and shifting.",
    core_interpretation="With Neptune conjunct your Ascendant, your identity is elusive and highly intuitive. You often blend dreams with reality in how you present yourself, making you a chameleon in social situations.",
    male_expression="You have a mystic presence, feeling others' vibes deeply. Remember to set boundaries to stay grounded.",
    female_expression="Your ethereal aura is soft and compassionate, though your identity may feel fluid. Embrace this aspect of yourself.",
    other_expression="You are a spiritual reflector, mirroring others and the atmosphere through an open soul. Cherish this gift."
)

# Sextile
neptune_asc_sextile = NeptuneAscendantAspectInterpretation(
    aspect="Sextile",
    hook="You flow gently between self and spirit  and  creativity accompanies your calm presence.",
    core_interpretation="With Neptune sextile your Ascendant, you possess artistic sensitivity and intuitive charm. Your compassionate persona adapts gracefully to different energies.",
    male_expression="You are a supportive empath, easily connecting with others. Ensure you take solitude to recharge.",
    female_expression="As a dreamy nurturer, creative expression and care come naturally to you. Embrace these talents.",
    other_expression="You are a balanced empath, bringing peaceful inspiration into any room. Your presence is a gift to others."
)

# Trine
neptune_asc_trine = NeptuneAscendantAspectInterpretation(
    aspect="Trine",
    hook="You align with the unseen  and  your expression is intuitive and gentle.",
    core_interpretation="With Neptune trine your Ascendant, you are granted harmonious spiritual grace. You are instinctively attuned to others' energies and express yourself with artistic or mystical ease.",
    male_expression="You are emotionally tuned, with a presence that is soothing and perceptive. Use this to connect deeply with others.",
    female_expression="As a subtle visionary, you embody spiritual elegance with ease. Your intuition guides you well.",
    other_expression="You are a synchronistic soul, radiating empathetic flow effortlessly. This is a beautiful aspect of your nature."
)

# Square
neptune_asc_square = NeptuneAscendantAspectInterpretation(
    aspect="Square",
    hook="Your identity collides with illusion  and  tension teaches you grounding.",
    core_interpretation="With Neptune square your Ascendant, you may experience tension between self and image and perception, often causing confusion or instability. Developing boundaries will help you distinguish fantasy from reality.",
    male_expression="As a vulnerable idealist, you must learn to anchor your dreams in clarity. This will bring you strength.",
    female_expression="You are sensitive yet resistant; growth comes through concrete self and definition. Embrace this journey.",
    other_expression="Your presence may feel fogged, but clarity will emerge through boundary work. Stay committed to this process."
)

# Opposition
neptune_asc_opp = NeptuneAscendantAspectInterpretation(
    aspect="Opposition",
    hook="You meet yourself through others  and  relationships reflect your misty edges.",
    core_interpretation="With Neptune opposite your Ascendant, you learn about relational mirroring and idealization. It's important to distinguish between projection and reality in your partnerships.",
    male_expression="As a reflective partner, you learn about your identity through relational clarity. Cherish these insights.",
    female_expression="You are a romantic mirror, balancing empathy with grounded boundaries. This balance is key to your growth.",
    other_expression="You are a relational sponge; clarity emerges through mutual revelation. Embrace these moments of understanding."
)

neptune_ascendant_aspects = {
    "Conjunction": neptune_asc_conj,
    "Sextile": neptune_asc_sextile,
    "Trine": neptune_asc_trine,
    "Square": neptune_asc_square,
    "Opposition": neptune_asc_opp
}
