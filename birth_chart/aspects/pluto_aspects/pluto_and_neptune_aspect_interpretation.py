class PlutoNeptuneAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
neptune_pluto_conj = PlutoNeptuneAspectInterpretation(
    aspect="Conjunction",
    hook="You embody transformative visions.",
    core_interpretation="You merge idealism with transformative power, igniting shifts in consciousness and spiritual regeneration. This aspect empowers you to guide and inspire collective evolution.",
    male_expression="You are a visionary catalyst, channeling societal change through deep ideals. Your journey involves using your insights to transform and lead.",
    female_expression="You are a mystical transformer, guiding transformation by merging soul and depth. Your path requires balancing your intensity with compassion.",
    other_expression="You are a collective alchemist, with evolution arising from profound awakening. Your strength lies in your ability to inspire and transform through your vision."
)

# Sextile
neptune_pluto_sextile = PlutoNeptuneAspectInterpretation(
    aspect="Sextile",
    hook="You evolve through spiritual depth.",
    core_interpretation="You have subtle pathways to spiritual regeneration and collective healing, enabling gentle yet profound transformation over time. This aspect supports your journey of personal and societal growth.",
    male_expression="You are a supportive reformer, nurturing societal growth through conscious depth. Your journey involves using your insights to guide and transform.",
    female_expression="You are a subtle visionary, with changes unfolding through intuitive resonance. Your path is marked by continuous growth and understanding.",
    other_expression="You are a patient alchemist, with transformation arising from soulful purpose. Your strength lies in your ability to heal and transform through your spiritual insights."
)

# Trine
neptune_pluto_trine = PlutoNeptuneAspectInterpretation(
    aspect="Trine",
    hook="You flow with collective change.",
    core_interpretation="You have a harmonious link between spiritual imagination and transformative energy, empowering graceful cultural and personal evolution. This aspect grants you the ability to integrate your vision with ease.",
    male_expression="You are an effortless guide, leading change with intuitive clarity. Your journey involves using your insights to inspire and transform.",
    female_expression="You are a fluid reformer, with transformation blossoming through compassion. Your path is marked by continuous growth and renewal.",
    other_expression="You are a harmonious changer, with unity of soul and power unfolding gently. Your strength lies in your ability to transform and heal through your spiritual depth."
)

# Square
neptune_pluto_square = PlutoNeptuneAspectInterpretation(
    aspect="Square",
    hook="You wrestle with unseen forces.",
    core_interpretation="You experience friction between collective ideals and structural power, triggering tension that demands the dismantling of illusions for authentic transformation. This aspect pushes you to confront and overcome societal challenges.",
    male_expression="You are a turbulent visionary, learning to channel tension into cultural evolution. Your journey involves overcoming internal struggles to emerge stronger.",
    female_expression="You are an intense catalyst, growing through confronting societal shadows. Your path requires facing and resolving your challenges.",
    other_expression="You are a pressure driven changer, with transformation forged through conflict. Your strength comes from facing and overcoming your struggles."
)

# Opposition
neptune_pluto_opp = PlutoNeptuneAspectInterpretation(
    aspect="Opposition",
    hook="Your reflection reveals collective dreams.",
    core_interpretation="You experience polarized collective energies, requiring reconciliation of spiritual ideals with power structures and prompting societal awakening through contrast. This aspect highlights the need to balance your vision with external influences.",
    male_expression="You are a reflective architect, balancing authority with shared vision. Your journey involves understanding and managing your power dynamics with others.",
    female_expression="You are a relational mystic, evolving by merging deep empathy and power. Your path is marked by continuous evolution through interactions.",
    other_expression="You are a mirror of change, with transformation arising through relational polarity. Your strength lies in your ability to integrate your spiritual insights with external influences."
)

pluto_neptune_aspects = {
    "Conjunction": neptune_pluto_conj,
    "Sextile": neptune_pluto_sextile,
    "Trine": neptune_pluto_trine,
    "Square": neptune_pluto_square,
    "Opposition": neptune_pluto_opp
}
