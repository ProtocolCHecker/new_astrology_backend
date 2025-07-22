class UranusSaturnAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
uranus_saturn_conj = UranusSaturnAspectInterpretation(
    aspect="Conjunction",
    hook="You disrupt to rebuild.",
    core_interpretation="You carry both the spark of innovation and the weight of responsibility. You're wired to reshape what no longer serves, even when it's uncomfortable. Structure doesn't hold you back and it becomes your canvas.",
    male_expression="You're the rebel with a blueprint. Discipline and innovation collide in you, and you're constantly reshaping systems from the inside out. You don't just want freedom and you want to make it sustainable.",
    female_expression="You hold chaos and order in each hand. You've had to grow through boundaries and break them too. When you trust your vision, you don't just change things and you revolutionize them with grace and strength.",
    other_expression="You're wired to reprogram the old code. You don't fear disruption and you guide it. With your vision and steadiness, you bring change that actually lasts."
)

# Sextile
uranus_saturn_sextile = UranusSaturnAspectInterpretation(
    aspect="Sextile",
    hook="You make the strange practical.",
    core_interpretation="You blend originality with grounded vision. Change doesn't scare you and you engineer it with care. Your ideas are unconventional, but your methods make them real.",
    male_expression="You take bold ideas and build them step by step. Your strength is your follow through and you make room for new systems without losing the value of what works.",
    female_expression="You bring intuition into order. Your creativity flows within the structures you design. What others call wild, you call possible and and you prove it with quiet power.",
    other_expression="You move between the old and the new with purpose. Your path isn't loud, but it leads to transformation that's both inspired and enduring."
)

# Trine
uranus_saturn_trine = UranusSaturnAspectInterpretation(
    aspect="Trine",
    hook="You balance risk with wisdom.",
    core_interpretation="You naturally blend tradition and revolution. Change flows through you without chaos and what you build is visionary but stable. You carry a deep ease with reform.",
    male_expression="You innovate without shaking the ground too hard. People trust your changes because they're anchored. You show that freedom doesn't have to abandon structure.",
    female_expression="You hold a visionary calm. New ideas arrive easily and land with impact because you've learned how to root them. You move the world by shifting its rhythm, not its foundation.",
    other_expression="You bring reform with rhythm. What you touch becomes a new standard and one that honors both freedom and form."
)

# Square
uranus_saturn_square = UranusSaturnAspectInterpretation(
    aspect="Square",
    hook="You grow by breaking your own rules.",
    core_interpretation="You live with inner conflict between safety and disruption. You crave structure and but also need to smash it. The tension isn't a flaw and it's where your true brilliance lives.",
    male_expression="You've been torn between control and release. That pressure has shaped you into someone who knows how to rebuild from your own resistance. The more you confront it, the more powerful you become.",
    female_expression="You've felt trapped by your own limits and but breaking them has taught you to trust yourself. You don't follow the rules. You refine them until they reflect your truth.",
    other_expression="You've lived in systems you longed to change. And now, your growth is shaped by the sparks that fly when you push back. You don't evolve in peace and you evolve in fire."
)

# Opposition
uranus_saturn_opp = UranusSaturnAspectInterpretation(
    aspect="Opposition",
    hook="You hold stillness in the storm.",
    core_interpretation="Your life teaches you to walk the line between tradition and rebellion. Others reflect your need to free yourself from the very walls you've helped build. Balance is your greatest teacher.",
    male_expression="You're a builder with a wild heart. You attract people who challenge your systems, and through them, you learn to soften your grip and expand your vision.",
    female_expression="You hold the paradox of order and upheaval. In relationship, you've faced control and chaos and and you've grown by learning not to reject either. They've shaped you in equal measure.",
    other_expression="You walk the boundary between preservation and reinvention. In others, you meet your own dual nature. Your evolution begins when you accept the pull of both sides."
)

uranus_saturn_aspects = {
    "Conjunction": uranus_saturn_conj,
    "Sextile": uranus_saturn_sextile,
    "Trine": uranus_saturn_trine,
    "Square": uranus_saturn_square,
    "Opposition": uranus_saturn_opp
}
