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
    hook="You transform from within  and  your presence reshapes reality.",
    core_interpretation="With Pluto conjunct Ascendant, you possess intense personal power and charisma. This aspect often brings early and life challenges that compel you to reinvent your identity and take deep control over your self and image. You have the potential to rise like a phoenix from your past.",
    male_expression="You have a formidable presence and evolve by breaking and rebuilding your self and image. Embrace this journey as it leads to profound personal growth.",
    female_expression="You are a magnetic transformer, learning to balance your intensity with self and acceptance. This balance will bring you inner peace and strength.",
    other_expression="You are a catalytic self; your transformation arises through owning your power. This ownership is your path to empowerment."
)

# Sextile
pluto_asc_sextile = PlutoAscendantAspectInterpretation(
    aspect="Sextile",
    hook="Your influence is quiet but profound  and  power flows in subtle ways.",
    core_interpretation="Pluto sextile Ascendant grants you a discreet yet magnetic presence. You have intuitive insights into others, offering opportunities to grow through gradual transformation. Your subtle power is your strength.",
    male_expression="You are a stealth catalyst, shifting your identity with purpose and subtle impact. Your quiet influence can lead to significant changes.",
    female_expression="You are an understated transformer, guiding yourself and others with calm depth. Your calmness is a source of power.",
    other_expression="You are an empowered catalyst; your transformation flows in measured steps. Each step is a building block to your evolution."
)

# Trine
pluto_asc_trine = PlutoAscendantAspectInterpretation(
    aspect="Trine",
    hook="Power flows effortlessly through your spirit  and  you change with grace.",
    core_interpretation="With Pluto trine Ascendant, you have natural charisma and a regenerative presence. This aspect enables graceful personal evolution, allowing you to reshape yourself without alienating others. Your transformations are smooth and impactful.",
    male_expression="You are a composed transformer; your presence inspires change with ease. Your ease is a gift that can inspire others.",
    female_expression="You are a graceful regenerator; your identity evolves through steady metamorphosis. This steady evolution is your strength.",
    other_expression="You are a fluid force; your transformation blends smoothly into self and expression. Your fluidity is a source of creativity and growth."
)

# Square
pluto_asc_square = PlutoAscendantAspectInterpretation(
    aspect="Square",
    hook="Your emerging self clashes with inherited power  and  tension births your truth.",
    core_interpretation="Pluto square Ascendant creates inner friction between your self and image and deep transformation. This aspect pushes you through internal power struggles and conflicts as you claim your authenticity. Embrace these challenges as they lead to profound self and discovery.",
    male_expression="You are a challenged leader, fighting inner control to discover your true identity. This fight is your path to self and mastery.",
    female_expression="You are a tension and charged self, growing by confronting personal power and adopting it consciously. This conscious adoption is your key to empowerment.",
    other_expression="You are a dynamic reinvention; your identity is forged through internal conflict. This conflict is your crucible of transformation."
)

# Opposition
pluto_asc_opp = PlutoAscendantAspectInterpretation(
    aspect="Opposition",
    hook="Your persona mirrors transformation  and  others are the stage for your self and power.",
    core_interpretation="With Pluto opposite Ascendant, your transformation is emphasized through relationships. This aspect spotlights power dynamics and projection, necessitating a balance between self and mastery and relational authenticity. Your relationships are your mirrors.",
    male_expression="You are a reflective sovereign, learning power through mirrored partnerships. These partnerships are your teachers.",
    female_expression="You are an electric mirror, evolving by navigating power with others. This navigation is your path to growth.",
    other_expression="You are a relational alchemist; your transformation unfolds through mirrored depth. This depth is your source of wisdom."
)

pluto_ascendant_aspects = {
    "Conjunction": pluto_asc_conj,
    "Sextile": pluto_asc_sextile,
    "Trine": pluto_asc_trine,
    "Square": pluto_asc_square,
    "Opposition": pluto_asc_opp
}
