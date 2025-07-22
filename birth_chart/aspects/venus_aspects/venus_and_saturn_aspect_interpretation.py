class VenusSaturnAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
venus_saturn_conj = VenusSaturnAspectInterpretation(
    aspect="Conjunction",
    hook="You love with gravity.",
    core_interpretation="You don't love lightly. Your affections carry depth, caution, and devotion. Trust must be earned, but when you give your heart, it's solid, enduring, and fiercely loyal.",
    male_expression="You approach love like architecture and carefully, purposefully, with lasting intent. You may guard your heart, but once open, you become a deeply committed and steady partner.",
    female_expression="You've learned love through tests. You give your affection carefully, and behind your reserved grace lies a depth that anchors those you let close. You're a safe harbor once trust is earned.",
    other_expression="You're built for soulful commitment. Love isn't just a feeling and it's a responsibility. But when it's real, you offer stability that few can match."
)

# Sextile
venus_saturn_sextile = VenusSaturnAspectInterpretation(
    aspect="Sextile",
    hook="You give with quiet strength.",
    core_interpretation="You know how to show love in tangible ways. You're generous with presence, patient with growth, and skilled at building trust through action, not just words.",
    male_expression="You show care by showing up and consistently, without drama. Love, for you, is built on time, effort, and earned respect. You value what you commit to.",
    female_expression="You embody graceful loyalty. You're drawn to those who value patience and maturity. Your affection may be quiet, but it's felt deeply and trusted completely.",
    other_expression="You offer love that feels safe and steady. You don't chase sparks and you nurture embers into warmth that lasts."
)

# Trine
venus_saturn_trine = VenusSaturnAspectInterpretation(
    aspect="Trine",
    hook="You love with elegant trust.",
    core_interpretation="You create stable, graceful connections. You understand boundaries without losing warmth, and you offer devotion with a calm, unwavering heart.",
    male_expression="Your affection feels timeless. You bring calm reassurance into relationships, and people feel grounded around you. You don't push and you support and endure.",
    female_expression="Your love flows with wisdom. You know your worth and give steadily, drawing in those who appreciate your strength and gentleness in equal measure.",
    other_expression="You balance self respect and devotion effortlessly. Your love feels reliable without being rigid and offering quiet strength to those around you."
)

# Square
venus_saturn_square = VenusSaturnAspectInterpretation(
    aspect="Square",
    hook="You carry armor around your heart.",
    core_interpretation="You've learned to protect yourself in love. Maybe you've felt rejected, unseen, or unworthy and but you're here to transform that story into strength, not isolation.",
    male_expression="You've wrestled with vulnerability. You want love, but fear loss or inadequacy. Still, every scar has sharpened your integrity and deepened your emotional resilience.",
    female_expression="You've felt the tension between desire and self protection. You crave closeness but fear the cost. Love, for you, becomes a sacred challenge and one that teaches healing through honesty.",
    other_expression="You long for deep connection, but trust doesn't come easy. The friction you feel in love is your invitation to build bridges where there were once walls."
)

# Opposition
venus_saturn_opp = VenusSaturnAspectInterpretation(
    aspect="Opposition",
    hook="You seek what you fear to give.",
    core_interpretation="You're drawn to relationships that reflect your inner conflict and between longing and restraint, intimacy and independence. You evolve by bridging that gap with honesty and self worth.",
    male_expression="You often meet people who challenge your ideas of value and connection. Through them, you're learning that true affection doesn't demand perfection and it asks for presence.",
    female_expression="You've danced between self denial and longing. Love shows up through contrast, calling you to soften, trust, and hold your ground with an open heart.",
    other_expression="You meet yourself in others through love's tension. What feels like distance is really a mirror and showing you how worthy you are of closeness and care."
)

venus_saturn_aspects = {
    "Conjunction": venus_saturn_conj,
    "Sextile": venus_saturn_sextile,
    "Trine": venus_saturn_trine,
    "Square": venus_saturn_square,
    "Opposition": venus_saturn_opp
}
