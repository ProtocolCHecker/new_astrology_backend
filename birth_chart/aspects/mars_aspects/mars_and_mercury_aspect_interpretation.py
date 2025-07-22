class MercuryMarsAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
mercury_mars_conj = MercuryMarsAspectInterpretation(
    aspect="Conjunction",
    hook="You think fast, speak hard, and rarely hold back.",
    core_interpretation="Your mind is sharp, fast, and full of fire. You express yourself with urgency and conviction and sometimes too sharply. You're quick to defend your ideas and don't shy away from confrontation, but your power deepens when you learn to temper intensity with listening. Your words can cut and the choice is yours.",
    male_expression="You speak with force and clarity, but growth means learning when silence is stronger than argument.",
    female_expression="You're bright, bold, and brutally honest, which empowers or overwhelms, depending on delivery. Tact refines your edge.",
    other_expression="You're wired for mental action and a fierce debater or verbal warrior. Power grows when passion aligns with intention."
)

# Sextile
mercury_mars_sextile = MercuryMarsAspectInterpretation(
    aspect="Sextile",
    hook="You speak with spark, direct, clear, and compelling.",
    core_interpretation="Your thoughts move with momentum and your voice carries confidence. You know how to make a point without starting a war. You're persuasive, lively, and often take initiative in communication. Your sharp mind opens doors, especially when you pair it with emotional awareness.",
    male_expression="You're a confident speaker who backs words with action. Success comes when you act on your ideas.",
    female_expression="You combine intelligence with initiative, assertive but grounded. Your words motivate.",
    other_expression="You communicate with drive and grace. Your mind's fire moves others, especially when focused with care."
)

# Trine
mercury_mars_trine = MercuryMarsAspectInterpretation(
    aspect="Trine",
    hook="You move and speak as one, smooth, swift, and self assured.",
    core_interpretation="Your thoughts, words, and actions align effortlessly. You're confident in your ideas and express them with ease and charm. You rarely hesitate, but you also don't bulldoze your natural eloquence draws others in. When you trust your instincts, your communication becomes a powerful tool for leadership and influence.",
    male_expression="You're smooth and strategic with a clear minded speaker others trust. Your energy calms as much as it drives.",
    female_expression="You express yourself with clarity and strength, but never lose warmth. You know how to lead a room without raising your voice.",
    other_expression="You're a harmonizer of will and word. Success comes easily when you stay true to your natural rhythm."
)

# Square
mercury_mars_square = MercuryMarsAspectInterpretation(
    aspect="Square",
    hook="You speak before thinking and sometimes think like you're in a fight.",
    core_interpretation="Your mind is bright and bold, but tension often builds between impulse and communication. You may speak too soon or too sharply, especially when emotions are high. Arguments come easily, but so does progress once you learn to pause and ground your responses. With awareness, your mental energy becomes a focused flame instead of a wildfire.",
    male_expression="You're clever but reactive, quick to speak, quicker to regret. Patience turns your fire into fuel.",
    female_expression="You defend your truth with passion, but growth means learning how to channel frustration into clarity.",
    other_expression="You have a fighter's mind, fierce and focused when centered, chaotic when scattered. Self regulation unlocks your potential."
)

# Opposition
mercury_mars_opp = MercuryMarsAspectInterpretation(
    aspect="Opposition",
    hook="You argue with others and often with yourself.",
    core_interpretation="You're caught between impulse and logic, often feeling torn between what you want to say and how it's received. You may project mental tension onto others, leading to debates, power struggles, or verbal misunderstandings. But when you integrate that inner friction, you develop razor sharp communication and a powerful ability to stand your ground without creating unnecessary war.",
    male_expression="You push hard in conversation and attract opposition. Balance comes when you listen as fiercely as you speak.",
    female_expression="You're mentally alive and always engaged, but your strength sharpens when you stop needing to win every exchange.",
    other_expression="You're forged in verbal fire, a challenger and truth seeker. Peace comes when you speak with both clarity and care."
)

# Store all interpretations
mercury_mars_aspects = {
    "Conjunction": mercury_mars_conj,
    "Sextile": mercury_mars_sextile,
    "Trine": mercury_mars_trine,
    "Square": mercury_mars_square,
    "Opposition": mercury_mars_opp
}
