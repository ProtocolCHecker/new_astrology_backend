class NeptunePlutoAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
neptune_pluto_conj = NeptunePlutoAspectInterpretation(
    aspect="Conjunction",
    hook="Your empathy and change merge and healing flows through you.",
    core_interpretation="You help others transform old wounds with your gentle understanding. Reflecting on your own needs keeps your caring spirit strong.",
    male_expression="Your deep insight into pain brings comfort to those who suffer. Taking time to rest restores your own energy.",
    female_expression="Your soulful presence encourages growth in everyone. Scheduling quiet moments refills your capacity to heal.",
    other_expression="Your caring touch sparks renewal far and wide. Balancing giving and rest protects your warmth."
)

# Sextile
neptune_pluto_sextile = NeptunePlutoAspectInterpretation(
    aspect="Sextile",
    hook="You heal through quiet strength and depth flows with ease.",
    core_interpretation="You notice what needs fixing and offer calm support that lasts. Pairing that with personal boundaries keeps you from wearing thin.",
    male_expression="Your steady calm encourages others to open up. Saying “no” when you need time off restores your balance.",
    female_expression="Your gentle guidance feels like a safe shelter. Setting small limits protects your own peace.",
    other_expression="Your quiet power fosters real change in others. Remembering self care keeps your kindness lasting."
)

# Trine
neptune_pluto_trine = NeptunePlutoAspectInterpretation(
    aspect="Trine",
    hook="Your heart evolves in harmony and growth feels natural.",
    core_interpretation="You navigate emotional shifts with calm confidence, inspiring trust in others. Sharing your journey openly reminds you that self care matters, too.",
    male_expression="Your smooth courage encourages people to grow. Celebrating your own steps forward fuels more healing.",
    female_expression="Your balanced support transforms hearts gently. Reflecting on your wins keeps your spirit light.",
    other_expression="Your steady strength lifts everyone around you. A quick self check reinforces your growth."
)

# Square
neptune_pluto_square = NeptunePlutoAspectInterpretation(
    aspect="Square",
    hook="Your compassion and power collide and tension reveals your truth.",
    core_interpretation="You face emotional battles head on, and each challenge makes you wiser. Pausing to breathe helps turn struggle into clarity.",
    male_expression="Your fierce caring can feel overwhelming for you or others. Taking short breaks recovers your calm.",
    female_expression="Your intense empathy drives deep healing, yet it can exhaust you. A moment of quiet resets your strength.",
    other_expression="Your confronting grace forges real change. Mindful rest shapes that power into purpose."
)

# Opposition
neptune_pluto_opp = NeptunePlutoAspectInterpretation(
    aspect="Opposition",
    hook="Your depth mirrors in others and shared change guides you.",
    core_interpretation="You grow through the transformation you witness in loved ones, and balancing give and take deepens every bond. Letting others support you makes that growth more joyful.",
    male_expression="Your heartfelt care invites others to heal alongside you. Welcoming their help protects your own heart.",
    female_expression="Your shared vulnerability brings real closeness. Accepting support builds your strength.",
    other_expression="Your mirrored journey teaches mutual renewal. Embracing reciprocity fuels lasting change."
)

neptune_pluto_aspects = {
    "Conjunction": neptune_pluto_conj,
    "Sextile": neptune_pluto_sextile,
    "Trine": neptune_pluto_trine,
    "Square": neptune_pluto_square,
    "Opposition": neptune_pluto_opp
}
