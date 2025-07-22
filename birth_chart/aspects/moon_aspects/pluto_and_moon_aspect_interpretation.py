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
    hook="Your feelings run deep into shadow and intensity births renewal.",
    core_interpretation="You dive fearlessly into emotional depths, and balancing that power with gentle care brings true healing.",
    male_expression="Your fierce sensitivity uncovers truth and softening your approach invites trust.",
    female_expression="Your soulful depth transforms pain into strength and allowing softness anchors your power.",
    other_expression="Your emotional alchemy inspires change and tempering intensity protects your heart."
)

# Sextile
pluto_moon_sextile = PlutoMoonAspectInterpretation(
    aspect="Sextile",
    hook="You heal through quiet intensity and depth flows with ease.",
    core_interpretation="You sense hidden needs and guide others to renewal; blending that with patient kindness makes your wisdom shine.",
    male_expression="Your calm insight supports others boldly and remember to refill your own well.",
    female_expression="Your nurturing depth feels profound and pair it with gentle moments to stay refreshed.",
    other_expression="Your steady strength empowers transformation and balancing force with rest keeps you whole."
)

# Trine
pluto_moon_trine = PlutoMoonAspectInterpretation(
    aspect="Trine",
    hook="Your heart evolves in harmony and depth becomes comfort.",
    core_interpretation="You regenerate emotionally with natural grace, and sharing that resilience inspires those around you.",
    male_expression="Your steady courage brings others peace and celebrating small joys fuels your renewal.",
    female_expression="Your inner strength feels like sanctuary and embracing playfulness keeps your spirit light.",
    other_expression="Your balanced power uplifts many and mixing intensity with laughter sparks joy."
)

# Square
pluto_moon_square = PlutoMoonAspectInterpretation(
    aspect="Square",
    hook="Your emotions and power clash and pressure forges your truth.",
    core_interpretation="You face emotional battles head on, and each struggle builds a wiser, more compassionate self.",
    male_expression="Your intensity shapes your strength and allowing vulnerability deepens your bonds.",
    female_expression="Your fierce resilience shines and softening defenses reveals your true heart.",
    other_expression="Your confrontation with self births growth and embracing gentleness completes the cycle."
)

# Opposition
pluto_moon_opp = PlutoMoonAspectInterpretation(
    aspect="Opposition",
    hook="Your reflection reveals depth and others mirror your transformation.",
    core_interpretation="You reclaim your feelings through relationships, and balancing giving and receiving deepens your self awareness.",
    male_expression="Your mirrored intensity teaches you balance and practicing reciprocity nurtures your soul.",
    female_expression="Your relational depth invites growth and honoring both connection and independence sustains your heart.",
    other_expression="Your shared alchemy heals and grounded self care ensures lasting renewal."
)

pluto_moon_aspects = {
    "Conjunction": pluto_moon_conj,
    "Sextile": pluto_moon_sextile,
    "Trine": pluto_moon_trine,
    "Square": pluto_moon_square,
    "Opposition": pluto_moon_opp
}
