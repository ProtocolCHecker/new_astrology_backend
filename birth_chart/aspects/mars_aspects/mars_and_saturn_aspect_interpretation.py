class MarsSaturnAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
mars_saturn_conj = MarsSaturnAspectInterpretation(
    aspect="Conjunction",
    hook="You build under pressure and slow fire forges your strongest steel.",
    core_interpretation="With Mars conjunct Saturn, you have relentless grit and measure every step with care; over time, you turn every setback into strategic strength.",
    male_expression="You power through limits like a steadfast architect and learn to honor your pacing to avoid burnout.",
    female_expression="You endure and construct your destiny with quiet resolve and embrace moments of rest as part of your journey.",
    other_expression="You shape your will with discipline and true mastery comes from patience and precision."
)

# Sextile
mars_saturn_sextile = MarsSaturnAspectInterpretation(
    aspect="Sextile",
    hook="Your strength is sustainable and you move forward with grounded intent.",
    core_interpretation="Mars sextile Saturn grants you a mature, steady drive and the wisdom to pace yourself through challenges.",
    male_expression="You act with reliable consistency and your calm determination inspires trust over the long haul.",
    female_expression="You blend drive with discretion and your thoughtful momentum builds lasting success.",
    other_expression="You channel energy where it counts and your strategic patience is your greatest asset."
)

# Trine
mars_saturn_trine = MarsSaturnAspectInterpretation(
    aspect="Trine",
    hook="You thrive with structure—patience fuels your momentum.",
    core_interpretation="Mars trine Saturn gives you a seamless flow between ambition and discipline, letting you achieve steadily without strain.",
    male_expression="You move with confident order and your quiet ambition achieves more than you realize.",
    female_expression="You balance effort and ease and your consistent grace builds enduring foundations.",
    other_expression="You integrate action and restraint and your progress feels natural and lasting."
)

# Square
mars_saturn_square = MarsSaturnAspectInterpretation(
    aspect="Square",
    hook="Your will meets walls you learn strength through resistance.",
    core_interpretation="Mars square Saturn creates tension between impulse and limits, driving you to forge resilience from every obstacle.",
    male_expression="You confront barriers head on your fierce determination grows stronger when you practice self compassion.",
    female_expression="You push through challenges softening and self criticism will free more of your power.",
    other_expression="You build inner fortitude in adversity and mastery comes as you transform resistance into resolve."
)

# Opposition
mars_saturn_opp = MarsSaturnAspectInterpretation(
    aspect="Opposition",
    hook="Your fire is tested by boundaries and pressure reveals your true power.",
    core_interpretation="Mars opposite Saturn highlights a dance between your ambition and external constraints, teaching you to assert wisely and with purpose.",
    male_expression="You clash with limits and learn to earn your confidence and each challenge refines your authority.",
    female_expression="You balance drive and caution and trusting your timing empowers your voice.",
    other_expression="You grow through tension and reclaiming your power from outside pressures brings true self mastery."
)

# Store all in dictionary
mars_saturn_aspects = {
    "Conjunction": mars_saturn_conj,
    "Sextile": mars_saturn_sextile,
    "Trine": mars_saturn_trine,
    "Square": mars_saturn_square,
    "Opposition": mars_saturn_opp
}
