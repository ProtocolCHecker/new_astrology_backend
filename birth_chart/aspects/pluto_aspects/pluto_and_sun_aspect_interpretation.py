class PlutoSunAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
pluto_sun_conj = PlutoSunAspectInterpretation(
    aspect="Conjunction",
    hook="Your identity is shaped by profound depth.",
    core_interpretation="You possess a magnetic presence and relentless self exploration, with the capacity to reinvent yourself through significant trials. This aspect empowers you to transform and lead with intensity.",
    male_expression="You are an intense force, with a presence that demands depth and transformation. Your journey involves using your insights to inspire and evolve.",
    female_expression="You are a magnetic agent of change, with your identity emerging through inner rebirth. Your path requires balancing your intensity with self awareness.",
    other_expression="You are a powerful force, evolving your identity through courageous depth. Your strength lies in your ability to transform and lead with authenticity."
)

# Sextile
pluto_sun_sextile = PlutoSunAspectInterpretation(
    aspect="Sextile",
    hook="You influence with grace and purpose.",
    core_interpretation="You have deep self awareness and willpower aligned with your goals, enabling you to harness transformative energy with insight and subtle authority. This aspect supports your journey of personal growth and leadership.",
    male_expression="You are a strategic leader, guiding change with measured potency. Your journey involves using your insights to transform and inspire.",
    female_expression="You are a transformative presence, nurturing growth through refined power. Your path is marked by continuous evolution and understanding.",
    other_expression="You are a quiet catalyst, with power and purpose integrating smoothly. Your strength lies in your ability to influence and transform with ease."
)

# Trine
pluto_sun_trine = PlutoSunAspectInterpretation(
    aspect="Trine",
    hook="Your purpose resonates with depth and power.",
    core_interpretation="You experience a harmonious blend of identity and transformation, empowering authentic self expression through natural resilience and regenerative charisma. This aspect grants you the ability to evolve and lead with grace.",
    male_expression="You are an effortless force, with self renewal flowing naturally. Your journey involves using your insights to inspire and transform with ease.",
    female_expression="You are a graceful transformer, with your identity blossoming through quiet power. Your path is marked by continuous growth and renewal.",
    other_expression="You are a fluid force, with personal evolution feeling organic and natural. Your strength lies in your ability to transform and lead with authenticity."
)

# Square
pluto_sun_square = PlutoSunAspectInterpretation(
    aspect="Square",
    hook="Your self grapples with intense power.",
    core_interpretation="You experience inner friction between your identity and transformation, leading to significant self growth through confronting challenges and control issues. This aspect pushes you to evolve and lead with resilience.",
    male_expression="You are a resilient force, learning authenticity through struggle. Your journey involves overcoming internal battles to emerge stronger.",
    female_expression="You are a fierce force, growing by mastering internal power dynamics. Your path requires facing and resolving your challenges.",
    other_expression="You are a conflict forged presence, with your identity emerging stronger through challenges. Your strength comes from facing and overcoming your struggles."
)

# Opposition
pluto_sun_opp = PlutoSunAspectInterpretation(
    aspect="Opposition",
    hook="Your reflection reveals transformative power.",
    core_interpretation="You experience relational dynamics that mirror your identity, urging balance between self assertion and surrender through interactions. This aspect highlights the need to integrate your power with external influences.",
    male_expression="You are a relational force, integrating power through mirrored encounters. Your journey involves understanding and managing your dynamics with others.",
    female_expression="You are a reflective transformer, with your self worth refining through relational depth. Your path is marked by continuous evolution through interactions.",
    other_expression="You are a mirror powered identity, evolving authenticity through contrast. Your strength lies in your ability to integrate your power with external influences."
)

pluto_sun_aspects = {
    "Conjunction": pluto_sun_conj,
    "Sextile": pluto_sun_sextile,
    "Trine": pluto_sun_trine,
    "Square": pluto_sun_square,
    "Opposition": pluto_sun_opp
}
