class MarsNeptuneAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
mars_neptune_conj = MarsNeptuneAspectInterpretation(
    aspect="Conjunction",
    hook="You move on dreams, instinct guides your hand, and inspiration sets your pace.",
    core_interpretation="You act from deep intuition, and your motivation is fueled by inspiration, not just logic. You're at your best when your actions serve a creative or spiritual vision, but if you lose touch with reality, it's easy to drift or become passive. If you lean into escapism or self deception, you risk wasting your drive, but when you channel your instincts, you become truly magnetic.",
    male_expression="You have an elusive charisma and might be drawn to fantasy or spiritual paths, but staying grounded is essential for you.",
    female_expression="Your empathy and subtlety make you mysterious, yet you need clarity to avoid being misled by illusions.",
    other_expression="You combine mysticism with action, but you thrive when your passion serves a purpose greater than yourself."
)

# Sextile
mars_neptune_sextile = MarsNeptuneAspectInterpretation(
    aspect="Sextile",
    hook="You create with subtle fire and your strength shines through acts of healing and creative expression.",
    core_interpretation="You have the ability to act on your ideals with grace. You inspire others with quiet motivation and a gentle, soulful approach. When you follow your artistic or compassionate urges, you become a source of healing, but you might struggle if you hide behind the scenes too much.",
    male_expression="You're quietly powerful, leading with subtle influence instead of confrontation.",
    female_expression="You move with intuition, blending emotion with purpose, but you need to honor your own needs as well.",
    other_expression="You're a spiritual catalyst, bringing dreams into reality through gentle yet persistent action."
)

# Trine
mars_neptune_trine = MarsNeptuneAspectInterpretation(
    aspect="Trine",
    hook="You swim through life's rhythms and you always tuned to inspiration and inner guidance.",
    core_interpretation="You have an effortless connection between drive and intuition. You move through life like a dancer: inspired, artistic, and often drawn to help or uplift others. Your energy is gentle yet steady, but if you lack focus, you might miss opportunities to bring your dreams to life.",
    male_expression="You create from the heart, using intuition as your compass, but grounding your vision keeps you growing.",
    female_expression="You radiate compassion and move with spiritual strength, but you shine brightest when you pursue your passions openly.",
    other_expression="You take soulful action, living between the tangible and the invisible with genuine purpose."
)

# Square
mars_neptune_square = MarsNeptuneAspectInterpretation(
    aspect="Square",
    hook="You chase shadows, learning to tell dreams from illusions is your test.",
    core_interpretation="Mars square Neptune challenges you with inner conflict, you often want something, but doubt or confusion gets in the way. At your worst, you can act impulsively for reasons you don't understand or fall into escapism. But if you confront your fears honestly, you unlock real creativity and compassion that's anchored in reality.",
    male_expression="You battle between ideals and what's real, discipline and honest self reflection will keep you from sabotaging yourself.",
    female_expression="You search for meaning and need to trust your instincts without being swept away by fantasy.",
    other_expression="You're an elusive warrior, finding your power when you steer through life with your own inner compass."
)

# Opposition
mars_neptune_opp = MarsNeptuneAspectInterpretation(
    aspect="Opposition",
    hook="Your true strength is in surrender but you must choose which dreams to pursue with care.",
    core_interpretation="Mars opposite Neptune pulls you between assertiveness and surrender, making it hard to act clearly or stand up for yourself. You're deeply imaginative and alluring, but can get lost in projection or lose energy if you're not careful. When you learn to balance action with spiritual intention, you find your real power and become a force for inspiration.",
    male_expression="You have a magnetic presence, but you grow by learning to claim your goals and not give your power away.",
    female_expression="You give deeply, but it's vital to protect your boundaries so you aren't drained or idealized.",
    other_expression="You're a soul driven explorer, discovering your power through the dance between effort and surrender."
)

# Dictionary of all aspects
mars_neptune_aspects = {
    "Conjunction": mars_neptune_conj,
    "Sextile": mars_neptune_sextile,
    "Trine": mars_neptune_trine,
    "Square": mars_neptune_square,
    "Opposition": mars_neptune_opp
}
