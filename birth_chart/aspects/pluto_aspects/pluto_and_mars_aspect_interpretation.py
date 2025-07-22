class PlutoMarsAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
pluto_mars_conj = PlutoMarsAspectInterpretation(
    aspect="Conjunction",
    hook="Your drive is unstoppable.",
    core_interpretation="You possess an intense will and transformative energy that must be channeled consciously to avoid being overwhelmed by impulses. This aspect fuels your actions with a powerful drive for transformation.",
    male_expression="You are a relentless force, fueled by instinct and driven by purpose. Your journey involves learning to temper your drive with conscious direction.",
    female_expression="You are a powerful initiator, with a strong will that needs to be guided with intention. Your path requires balancing your intensity with clear goals.",
    other_expression="You are a catalytic force, where your actions become transformative when grounded. Your power lies in your ability to channel your energy effectively."
)

# Sextile
pluto_mars_sextile = PlutoMarsAspectInterpretation(
    aspect="Sextile",
    hook="You move with purpose.",
    core_interpretation="You have a subtle but potent power that enables you to act with transformative intent and quiet strength. This aspect supports your ability to effect change with composed conviction.",
    male_expression="You are a strategic doer, with power flowing through mindful action. Your transformations are guided by steady and deliberate efforts.",
    female_expression="You are an empowered agent, effecting change with composed conviction. Your journey involves using your inner strength to drive your actions.",
    other_expression="You are a forceful catalyst, with transformation guided by steady will. Your path is marked by purposeful and impactful actions."
)

# Trine
pluto_mars_trine = PlutoMarsAspectInterpretation(
    aspect="Trine",
    hook="Your energy is transformative.",
    core_interpretation="You experience a harmonious integration of drive and depth, providing regenerative resilience and focused personal evolution. This aspect fuels your actions with a natural alignment of passion and power.",
    male_expression="You are a composed powerhouse, turning challenges into growth with grace. Your journey involves using your inner strength to overcome obstacles.",
    female_expression="You are a fluid transformer, with passion and power aligning naturally. Your path is marked by continuous and effortless evolution.",
    other_expression="You are an energetic catalyst, with your internal will fueling transformation effortlessly. Your power lies in your ability to drive change with ease."
)

# Square
pluto_mars_square = PlutoMarsAspectInterpretation(
    aspect="Square",
    hook="Your passion tests your strength.",
    core_interpretation="You experience tension between instinct and power, leading to intense conflict that, when mastered, yields resilience and self mastery. This aspect challenges you to harness your energy effectively.",
    male_expression="You are a restless force, with tension teaching self mastery through challenge. Your journey involves learning to manage your intensity and drive.",
    female_expression="You are a fierce catalyst, with conflict prompting deep self honesty. Your path requires facing and overcoming internal struggles.",
    other_expression="You are a tension led catalyst, with pressure polishing your transformational will. Your power comes from facing and resolving your challenges."
)

# Opposition
pluto_mars_opp = PlutoMarsAspectInterpretation(
    aspect="Opposition",
    hook="Your fire meets your depth.",
    core_interpretation="You experience power dynamics mirrored in others, urging integration of aggression and transformation through relational tension. This aspect highlights the need to balance your inner strength with external interactions.",
    male_expression="You are a reflective warrior, learning balance through mirrored intensity. Your journey involves understanding and managing your power dynamics with others.",
    female_expression="You are a relational transformer, with strength deepening through mirrored conflict. Your path is marked by continuous evolution through interactions.",
    other_expression="You are a mirror of power, evolving by reconciling self with reflected force. Your journey involves integrating your inner strength with external influences."
)

pluto_mars_aspects = {
    "Conjunction": pluto_mars_conj,
    "Sextile": pluto_mars_sextile,
    "Trine": pluto_mars_trine,
    "Square": pluto_mars_square,
    "Opposition": pluto_mars_opp
}
