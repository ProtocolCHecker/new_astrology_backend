class PlutoMoonAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
pluto_moon_conj = PlutoMoonAspectInterpretation(
    aspect="Conjunction",
    hook="Your emotions delve into profound depths.",
    core_interpretation="You experience a powerful fusion of emotional instincts and transformation, empowering you to confront deep feelings and heal significant wounds. This aspect demands balance to avoid emotional overwhelm.",
    male_expression="You are an emotional alchemist, diving into the depths of your feelings to reclaim your power. Your journey involves using your emotional insights to transform and heal.",
    female_expression="You are a nurturing healer, transforming through emotional truth and understanding. Your path requires balancing your intensity with self care.",
    other_expression="You are a seeker of emotional depth, where your feelings become a catalyst for change. Your strength lies in setting clear boundaries and using your insights to guide your transformation."
)

# Sextile
pluto_moon_sextile = PlutoMoonAspectInterpretation(
    aspect="Sextile",
    hook="You heal through gentle intensity.",
    core_interpretation="You have opportunities to transform emotional patterns with insight, allowing steady healing through awareness of your deeper needs. This aspect supports your journey of emotional growth and resilience.",
    male_expression="You are a supportive transformer, nurturing growth through calm understanding. Your journey involves using your emotional insights to foster healing.",
    female_expression="You are an insightful healer, using emotional depth to foster resilience. Your path is marked by continuous growth and understanding.",
    other_expression="You are a guided empath, with emotional alchemy unfolding with gentle purpose. Your strength lies in your ability to heal and transform through your emotional insights."
)

# Trine
pluto_moon_trine = PlutoMoonAspectInterpretation(
    aspect="Trine",
    hook="Your emotions evolve in harmony.",
    core_interpretation="You experience smooth emotional regeneration and intuitive depth, enabling compassionate insight and resilience as your feelings transform naturally. This aspect grants you the ability to integrate your emotions with ease.",
    male_expression="You are a fluid catalyst, with emotional strength guiding your transformation. Your journey involves using your insights to inspire and lead.",
    female_expression="You are a gracious transformer, nurturing with soulful understanding. Your path is marked by continuous growth and renewal.",
    other_expression="You are a harmonious alchemist, with emotional depth integrating smoothly. Your strength lies in your ability to transform and heal through your emotional insights."
)

# Square
pluto_moon_square = PlutoMoonAspectInterpretation(
    aspect="Square",
    hook="Your emotions and power challenge each other.",
    core_interpretation="You experience friction between your instincts and transformation, triggering emotional intensity that forces you to build resilience and conscious response patterns. This aspect pushes you to master your emotional depth.",
    male_expression="You are a tension forged empath, learning emotional control through challenge. Your journey involves overcoming internal struggles to emerge stronger.",
    female_expression="You are a fierce nurturer, with strength emerging by mastering emotional triggers. Your path requires facing and resolving your challenges.",
    other_expression="You are a pressure driven alchemist, with emotional growth demanding conscious effort. Your strength comes from facing and overcoming your struggles."
)

# Opposition
pluto_moon_opp = PlutoMoonAspectInterpretation(
    aspect="Opposition",
    hook="Your reflection reveals emotional transformation.",
    core_interpretation="You experience emotional projection and relational dynamics, urging you to reclaim your feelings through interactions and deepen emotional awareness. This aspect highlights the need to balance your inner depth with external connections.",
    male_expression="You are a reflective healer, learning self power through the emotional dance of relationships. Your journey involves understanding and managing your emotional dynamics with others.",
    female_expression="You are a relational transformer, with emotional clarity growing through connection. Your path is marked by continuous evolution through interactions.",
    other_expression="You are a mirror of emotional depth, with insight emerging through relational context. Your strength lies in your ability to integrate your emotional insights with external influences."
)

pluto_moon_aspects = {
    "Conjunction": pluto_moon_conj,
    "Sextile": pluto_moon_sextile,
    "Trine": pluto_moon_trine,
    "Square": pluto_moon_square,
    "Opposition": pluto_moon_opp
}
