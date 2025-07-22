class MarsPlutoAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
mars_pluto_conj = MarsPlutoAspectInterpretation(
    aspect="Conjunction",
    hook="You throw yourself into every pursuit with all consuming intensity.",
    core_interpretation="You possess unstoppable stamina and a laser focus that turns challenges into triumphs. When you balance this power, you become a force for transformation; unchecked, you risk slipping into obsession or control battles.",
    male_expression="You charge ahead like a warrior, unstoppable, but learn to temper your drive with patience.",
    female_expression="Your magnetism reshapes everything around you and embrace tenderness to soften that powerful edge.",
    other_expression="You wield your energy to create deep change knowing when to let go is your true mastery."
)

# Sextile
mars_pluto_sextile = MarsPlutoAspectInterpretation(
    aspect="Sextile",
    hook="You blend passion and precision—your actions always have depth and purpose.",
    core_interpretation="You a quiet yet formidable resolve, so you get to the heart of issues with grace. Your emotional intelligence helps you steer transformation without force; avoid becoming too detached or manipulative.",
    male_expression="You work strategically behind the scenes, your subtle power moves projects forward, but stay warm in your dealings.",
    female_expression="You heal and rebuild with insight and just guard against using strategy as a shield from real connection.",
    other_expression="You're a disciplined catalyst for change and remember to stay present, not just efficient."
)

# Trine
mars_pluto_trine = MarsPlutoAspectInterpretation(
    aspect="Trine",
    hook="Power flows effortlessly through you and channel it with elegant clarity.",
    core_interpretation="You are with natural confidence and an innate ability to drive positive change. Your calm courage attracts respect, yet be mindful not to let ease turn into complacency.",
    male_expression="You lead with quiet authority, your composed strength inspires, but don't hold back your warmth.",
    female_expression="You move with graceful conviction and your presence transforms, so share your light freely.",
    other_expression="You model empowered action and balance your drive with moments of stillness."
)

# Square
mars_pluto_square = MarsPlutoAspectInterpretation(
    aspect="Square",
    hook="You wrestle with inner volcanoes—your power demands healthy outlets.",
    core_interpretation="You bring intense drive and the urge to control situations, often sparking internal or external clashes. Channel that fierce energy into disciplined practice to turn conflict into personal growth.",
    male_expression="You face challenges head on and your fierceness builds strength, but practice patience to avoid burnout.",
    female_expression="You push through barriers and your determination is fierce, yet soften your approach to reduce friction.",
    other_expression="You forge resilience in the fire of struggle—learn self control to master your power."
)

# Opposition
mars_pluto_opp = MarsPlutoAspectInterpretation(
    aspect="Opposition",
    hook="Your strength shines brightest against opposition.",
    core_interpretation="You highlight tensions between your will and outside forces, often in relationships or power dynamics. Use these clashes as mirrors to integrate your true power without overpowering others.",
    male_expression="You mirror power struggles, own your influence to transform conflict into self awareness.",
    female_expression="You meet passion with passion, and balance giving and receiving to avoid losing yourself.",
    other_expression="You learn through tension, and reclaim displaced power to emerge whole."
)

# Store all in dictionary
mars_pluto_aspects = {
    "Conjunction": mars_pluto_conj,
    "Sextile": mars_pluto_sextile,
    "Trine": mars_pluto_trine,
    "Square": mars_pluto_square,
    "Opposition": mars_pluto_opp
}
