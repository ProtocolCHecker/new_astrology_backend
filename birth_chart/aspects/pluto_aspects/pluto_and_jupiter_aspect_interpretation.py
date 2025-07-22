class PlutoJupiterAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
pluto_jupiter_conj = PlutoJupiterAspectInterpretation(
    aspect="Conjunction",
    hook="Your power and vision unite.",
    core_interpretation="You possess a deep drive for growth and meaning, fueled by relentless ambition and the need to rebuild your worldview through intense experiences. This compels you to transform your beliefs and expand your horizons.",
    male_expression="You are a visionary powerhouse, driven to reshape your life through faith and determination. Your journey involves harnessing your intensity to achieve your goals.",
    female_expression="You are a relentless seeker, transforming through belief and conviction. Your path requires balancing your zeal to avoid excess and maintain focus.",
    other_expression="You are an alchemical leader, where your beliefs become the crucible for profound change. Your power lies in your ability to inspire and transform."
)

# Sextile
pluto_jupiter_sextile = PlutoJupiterAspectInterpretation(
    aspect="Sextile",
    hook="You evolve with grace.",
    core_interpretation="You experience steady transformation through opportunities and inner growth, blending ambition with insight. This aspect supports your journey of personal evolution and philosophical understanding.",
    male_expression="You are a subtle architect, channeling your drive into meaningful expansion. Your transformations are strategic and purposeful.",
    female_expression="You are a purposeful transformer, growing through thoughtful empowerment. Your path involves using your insights to guide your evolution.",
    other_expression="You are a calm catalyst, with your evolution emerging through quiet, grounded momentum. Your journey is marked by steady and meaningful progress."
)

# Trine
pluto_jupiter_trine = PlutoJupiterAspectInterpretation(
    aspect="Trine",
    hook="Your impact resonates deeply.",
    core_interpretation="You have effortless access to transformative influence, amplifying your leadership, insight, and capacity to inspire collective evolution. This aspect grants you the ability to effect change with natural authority.",
    male_expression="You are a magnetic guide, inspiring change with your natural authority. Your presence and vision drive your ability to lead and transform.",
    female_expression="You are a graceful reformer, leading with depth and wisdom. Your journey involves using your insights to guide and inspire others.",
    other_expression="You are a fluid visionary, with transformation flowing through your purposeful vision. Your path is marked by continuous growth and renewal."
)

# Square
pluto_jupiter_square = PlutoJupiterAspectInterpretation(
    aspect="Square",
    hook="Your beliefs challenge your power.",
    core_interpretation="You experience friction between ambition and transformation, often facing power struggles or challenges that test your beliefs. This aspect pushes you to rebuild your convictions through resilience and intensity.",
    male_expression="You are a driven challenger, learning growth through tests of your beliefs. Your journey involves overcoming obstacles to emerge stronger and more determined.",
    female_expression="You are a tension tempered leader, redefining your purpose under pressure. Your path requires resilience and adaptability to navigate challenges.",
    other_expression="You are a conflict born philosopher, evolving your beliefs through resilience. Your power comes from facing and overcoming your struggles."
)

# Opposition
pluto_jupiter_opp = PlutoJupiterAspectInterpretation(
    aspect="Opposition",
    hook="Your mirror reflects your purpose.",
    core_interpretation="You experience relational tension between personal power and shared beliefs, prompting growth by reconciling your transformation with external ideals. This aspect highlights the need to balance self mastery with collective values.",
    male_expression="You are a reflective leader, evolving through balancing self power and external philosophies. Your journey involves integrating personal depth with collective ideals.",
    female_expression="You are a relational reformer, learning integration by honoring both personal depth and shared beliefs. Your path is marked by continuous evolution through interactions.",
    other_expression="You are a mirror of purpose, with transformation finding balance through interaction. Your journey involves reconciling personal power with external influences."
)

pluto_jupiter_aspects = {
    "Conjunction": pluto_jupiter_conj,
    "Sextile": pluto_jupiter_sextile,
    "Trine": pluto_jupiter_trine,
    "Square": pluto_jupiter_square,
    "Opposition": pluto_jupiter_opp
}
