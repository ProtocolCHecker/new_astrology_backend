class PlutoAscendantAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
pluto_asc_conj = PlutoAscendantAspectInterpretation(
    aspect="Conjunction",
    hook="Your presence transforms reality.",
    core_interpretation="You possess an intense personal power and charisma that often stems from early life experiences, compelling you to reinvent your identity and take deep control over your self image. This suggests a journey of self discovery through transformation and rebirth.",
    male_expression="You have a formidable presence that evolves by breaking down and rebuilding your self image. This process can be challenging but ultimately leads to a stronger sense of self.",
    female_expression="You are a magnetic transformer, learning to balance your intensity with self acceptance. Your journey involves understanding and harnessing your inner power.",
    other_expression="You are a catalyst for change, with transformation arising through owning your power. This drives you to continually evolve and grow."
)

# Sextile
pluto_asc_sextile = PlutoAscendantAspectInterpretation(
    aspect="Sextile",
    hook="Your influence is subtle yet profound.",
    core_interpretation="You have a discreet yet magnetic presence, providing intuitive insights into others and opportunities for growth through gradual transformation. You have the ability to subtly influence and transform your surroundings.",
    male_expression="You are a catalyst for change, shifting your identity with purpose and subtle impact. Your transformations are often internal but deeply significant.",
    female_expression="You are an understated transformer, guiding yourself and others with calm depth. Your power lies in your ability to influence quietly but effectively.",
    other_expression="You are an empowered catalyst, with transformation flowing in measured steps. Your journey is one of steady and meaningful change."
)

# Trine
pluto_asc_trine = PlutoAscendantAspectInterpretation(
    aspect="Trine",
    hook="Power flows effortlessly through you.",
    core_interpretation="You have a natural charisma and a regenerative presence, enabling graceful personal evolution. You have the ability to reshape yourself without alienating others, making your transformations smooth and impactful.",
    male_expression="You are a composed transformer, whose presence inspires change with ease. Your ability to evolve gracefully is one of your greatest strengths.",
    female_expression="You are a graceful regenerator, with your identity evolving through steady metamorphosis. Your transformations are a source of inspiration for others.",
    other_expression="You are a fluid force, with transformation blending smoothly into your self expression. Your journey is marked by continuous growth and renewal."
)

# Square
pluto_asc_square = PlutoAscendantAspectInterpretation(
    aspect="Square",
    hook="Your truth emerges from inner clashes.",
    core_interpretation="You experience inner friction between your self image and deep transformation, pushing you through internal struggles and conflict as you claim your authenticity. This challenges you to confront and overcome your inner demons.",
    male_expression="You are a challenged leader, fighting inner control to discover your true identity. Your journey involves overcoming internal battles to emerge stronger.",
    female_expression="You are a dynamic self, growing by confronting personal power and adopting it consciously. Your transformations are driven by internal conflicts and resolutions.",
    other_expression="You are a dynamic reinvention, with your identity forged through internal conflict. Your power comes from facing and overcoming your challenges."
)

# Opposition
pluto_asc_opp = PlutoAscendantAspectInterpretation(
    aspect="Opposition",
    hook="Your persona mirrors transformation.",
    core_interpretation="You experience transformation through relationships, spotlighting power dynamics and the necessity to balance self mastery with relational authenticity. Your journey involves understanding and navigating power dynamics in your relationships.",
    male_expression="You are a reflective individual, learning power through mirrored partnerships. Your growth comes from understanding and managing these dynamics.",
    female_expression="You are an insightful mirror, evolving by navigating power with others. Your transformations are deeply tied to your interactions and relationships.",
    other_expression="You are a relational alchemist, with transformation unfolding through mirrored depth. Your journey is one of continuous evolution through your connections with others."
)

pluto_ascendant_aspects = {
    "Conjunction": pluto_asc_conj,
    "Sextile": pluto_asc_sextile,
    "Trine": pluto_asc_trine,
    "Square": pluto_asc_square,
    "Opposition": pluto_asc_opp
}
