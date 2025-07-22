class MercuryMoonAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunct
moon_conjunct_mercury = MercuryMoonAspectInterpretation(
    aspect="Conjunct",
    hook="Your heart and mind speak the same language. Curious, caring, and ready to connect.",
    core_interpretation="With the Moon conjunct Mercury, you express emotions through ideas, weaving feeling into every word. Watch for overanalysis and remember to simply feel sometimes.",
    male_expression="You verbalize feelings easily. Creating a safe space to share softens any edge.",
    female_expression="Your words flow from intuition. Balancing thought with stillness deepens your insight.",
    other_expression="You tell emotional stories that resonate. Pausing to listen restores harmony."
)

# Sextile
moon_sextile_mercury = MercuryMoonAspectInterpretation(
    aspect="Sextile",
    hook="Your thoughts have heart. Empathetic, articulate, and inviting.",
    core_interpretation="Moon sextile Mercury gifts you gentle clarity in communication, making you a natural confidant. Be mindful to ground feelings in facts when needed.",
    male_expression="You calm and translate emotions. Your listening is as powerful as your words.",
    female_expression="You blend care and clarity. Your advice heals when you trust your inner voice.",
    other_expression="You nurture through speech. Recognizing boundaries strengthens your empathy."
)

# Trine
moon_trine_mercury = MercuryMoonAspectInterpretation(
    aspect="Trine",
    hook="Your voice flows from the heart. Sincere, sensitive, and in sync.",
    core_interpretation="Moon trine Mercury endows you with seamless emotional intelligence and eloquence. Sharing vulnerability invites deeper connection.",
    male_expression="You soothe with your words. Your tone carries both comfort and wisdom.",
    female_expression="You inspire trust through warmth. Letting others speak lifts every conversation.",
    other_expression="You balance thought and feeling. Honoring both enriches your presence."
)

# Square
moon_square_mercury = MercuryMoonAspectInterpretation(
    aspect="Square",
    hook="Your mind and emotions wrestle. Expressive, anxious, and deeply human.",
    core_interpretation="Moon square Mercury stirs inner debate between feeling and thinking. Learning to honor both sides brings clarity without sacrificing authenticity.",
    male_expression="Your insight can sting. Softening delivery nurtures understanding.",
    female_expression="Your depth may overwhelm. Steady breathing helps align heart and head.",
    other_expression="You grow through honest reflection. Acknowledging both voices calms the storm."
)

# Opposition
moon_opposite_mercury = MercuryMoonAspectInterpretation(
    aspect="Opposition",
    hook="Your mind questions what your heart knows. Always translating, rarely at rest.",
    core_interpretation="Moon opposite Mercury highlights the push pull between emotion and intellect. Integrating impulses with reason lets your voice become both compassionate and clear.",
    male_expression="Your logic may mute feeling. Inviting vulnerability enriches your words.",
    female_expression="Your depth could silence you. Trusting emotion empowers your expression.",
    other_expression="You learn through dialogue. Balancing give and take refines your truth."
)

mercury_moon_aspects = {
    "Conjunct": moon_conjunct_mercury,
    "Sextile": moon_sextile_mercury,
    "Trine": moon_trine_mercury,
    "Square": moon_square_mercury,
    "Opposition": moon_opposite_mercury
}