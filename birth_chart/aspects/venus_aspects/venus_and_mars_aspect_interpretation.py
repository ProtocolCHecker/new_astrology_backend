class VenusMarsAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
venus_mars_conj = VenusMarsAspectInterpretation(
    aspect="Conjunction",
    hook="You love with fire and intention.",
    core_interpretation="You bring together desire and affection in a way that's magnetic and bold. Your charm is instinctive and your energy intense, but learning to pace your passion helps you build lasting connections.",
    male_expression="You go after what you want with confidence, especially in love. Just make sure you're not mistaking spark for substance.",
    female_expression="You lead with both heart and heat, drawing people in effortlessly. When you slow down, you find who's truly ready for your kind of passion.",
    other_expression="You radiate a powerful mix of charm and drive and people feel your presence. With balance, your relationships become both exciting and real."
)

# Sextile
venus_mars_sextile = VenusMarsAspectInterpretation(
    aspect="Sextile",
    hook="You make passion look easy.",
    core_interpretation="You blend confidence with care, creating warm and playful connections. Your creative energy is inviting, and your relationships tend to grow through shared joy and natural chemistry.",
    male_expression="You pursue love with charm and lightness, rarely forcing anything. People feel safe around your mix of warmth and self assurance.",
    female_expression="You flirt with ease, offering affection that feels genuine and fun. Your presence is sweet but never dull.",
    other_expression="You move through love and life with flow and spark. It's your balance of energy and empathy that brings others closer."
)

# Trine
venus_mars_trine = VenusMarsAspectInterpretation(
    aspect="Trine",
    hook="You're in sync with your passion.",
    core_interpretation="You carry an effortless blend of affection and desire, making your relationships and creative pursuits flow naturally. You don't chase love and it tends to meet you right where you are.",
    male_expression="You exude calm confidence and know how to connect without pushing. People are drawn to how grounded your charm feels.",
    female_expression="Your elegance and magnetism work hand in hand and you attract love through ease, not effort. Others admire how true you stay to yourself.",
    other_expression="You express affection with grace and strength. Your energy feels whole, balanced, and undeniably attractive."
)

# Square
venus_mars_square = VenusMarsAspectInterpretation(
    aspect="Square",
    hook="You burn hot and sometimes too hot.",
    core_interpretation="You often feel torn between wanting closeness and needing space to assert yourself. This tension can lead to passion and frustration and but it's also what helps you grow in love and creativity.",
    male_expression="You love intensely, but the push pull between tenderness and desire can confuse things. Your strength comes from learning how to slow down before you explode.",
    female_expression="You attract strong energy, but it's not always stable. Conflict shows up to teach you how to express yourself without losing your center.",
    other_expression="You love with force and feeling, and it can get messy. But it's in that mess that you learn how to love more consciously and clearly."
)

# Opposition
venus_mars_opp = VenusMarsAspectInterpretation(
    aspect="Opposition",
    hook="You attract what you're still learning to balance.",
    core_interpretation="Your relationships reflect a dance between desire and connection, often showing up through intense attraction or clashing needs. Growth comes when you stop pulling between the two and and start integrating them within yourself.",
    male_expression="You often meet partners who show you where you overdo or hold back. Love deepens when you stop seeing tension as conflict and start seeing it as growth.",
    female_expression="You're drawn to contrasts and softness meets strength, love meets fire. These mirrors help you learn how to stand in both without choosing sides.",
    other_expression="You evolve through relational tension. Your energy is magnetic, and when you learn to hold both passion and patience, you create powerful, lasting bonds."
)

# Store all Venus–Mars aspect interpretations
venus_mars_aspects = {
    "Conjunction": venus_mars_conj,
    "Sextile": venus_mars_sextile,
    "Trine": venus_mars_trine,
    "Square": venus_mars_square,
    "Opposition": venus_mars_opp
}
