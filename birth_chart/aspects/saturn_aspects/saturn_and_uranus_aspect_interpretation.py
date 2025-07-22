class SaturnUranusAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
saturn_uranus_conj = SaturnUranusAspectInterpretation(
    aspect="Conjunction",
    hook="Revolution meets discipline in your soul.",
    core_interpretation="You possess a rare gift for turning wild ideas into concrete reality, blending your rebellious spirit with methodical precision. Your innovative mind works best when you create structure around your breakthrough moments, allowing you to build lasting change from the ground up.",
    male_expression="You're the strategic rebel who builds tomorrow's world with today's tools. Your revolution comes through calculated risks and patient transformation.",
    female_expression="You architect change with both vision and wisdom, creating new pathways while honoring what truly works. Your strength lies in structured innovation that serves the greater good.",
    other_expression="You bridge the gap between dreamer and builder, transforming radical concepts into practical solutions. Your methodical approach to change creates lasting impact in everything you touch."
)

# Sextile
saturn_uranus_sextile = SaturnUranusAspectInterpretation(
    aspect="Sextile",
    hook="Opportunity flows between order and innovation.",
    core_interpretation="You have a natural talent for spotting where tradition needs updating and knowing exactly how to make it happen. Your ability to work within existing systems while introducing fresh perspectives makes you invaluable as a change agent.",
    male_expression="You excel at progressive planning, seeing three steps ahead while keeping your feet firmly planted. Your innovations feel natural and well timed to those around you.",
    female_expression="You blend wisdom with creativity, knowing when to push boundaries and when to work within them. Your gentle approach to reform wins hearts and minds effortlessly.",
    other_expression="You navigate between stability and change like a skilled diplomat, finding the sweet spot where progress feels comfortable. Your timing for introducing new ideas is impeccable."
)

# Trine
saturn_uranus_trine = SaturnUranusAspectInterpretation(
    aspect="Trine",
    hook="Change flows through you like water finding its path.",
    core_interpretation="You embody the perfect marriage of stability and innovation, where your most creative ideas emerge from solid foundations. Your ability to evolve systems gradually while maintaining their core strength makes you a trusted leader in transformation.",
    male_expression="You transform situations with quiet confidence, making radical changes feel like natural evolution. Your steady approach to innovation inspires trust and long term success.",
    female_expression="You guide change with grace and intuition, helping others embrace new possibilities without fear. Your elegant approach to reform creates harmony rather than conflict.",
    other_expression="You channel revolutionary energy through stable structures, making breakthrough moments feel inevitable rather than disruptive. Your balanced approach to change creates sustainable transformation."
)

# Square
saturn_uranus_square = SaturnUranusAspectInterpretation(
    aspect="Square",
    hook="Tension ignites your creative fire.",
    core_interpretation="You thrive on the friction between wanting security and craving freedom, using this internal conflict as fuel for your most innovative breakthroughs. Your greatest achievements come when you refuse to choose between stability and change, instead forging a third path that honors both.",
    male_expression="You're the restless innovator who learns through productive rebellion, turning frustration into breakthrough moments. Your unconventional approach to problems creates solutions others never imagined.",
    female_expression="You transform resistance into creative energy, using tension as your teacher and guide. Your ability to work with conflict rather than against it makes you incredibly resourceful.",
    other_expression="You thrive in the space between order and chaos, using creative tension to fuel your most important work. Your breakthroughs emerge from embracing rather than resolving internal contradictions."
)

# Opposition
saturn_uranus_opp = SaturnUranusAspectInterpretation(
    aspect="Opposition",
    hook="Balance teaches you mastery through contrast.",
    core_interpretation="You learn your greatest lessons through experiencing the extremes of structure and freedom, developing wisdom about when to hold steady and when to embrace change. Your ability to see both sides of any situation makes you an exceptional mediator and visionary leader.",
    male_expression="You master the art of measured response, learning to temper your reactions with wisdom gained through experience. Your perspective on change becomes more refined through encountering resistance.",
    female_expression="You excel at finding harmony between opposing forces, creating bridges where others see only conflict. Your diplomatic approach to transformation brings out the best in challenging situations.",
    other_expression="You develop deep understanding through experiencing life's polarities, becoming a master of synthesis and integration. Your ability to hold paradox makes you a powerful agent of conscious evolution."
)

saturn_uranus_aspects = {
    "Conjunction": saturn_uranus_conj,
    "Sextile": saturn_uranus_sextile,
    "Trine": saturn_uranus_trine,
    "Square": saturn_uranus_square,
    "Opposition": saturn_uranus_opp
}