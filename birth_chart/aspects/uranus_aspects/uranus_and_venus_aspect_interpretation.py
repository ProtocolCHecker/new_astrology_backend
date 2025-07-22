class UranusVenusAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
uranus_venus_conj = UranusVenusAspectInterpretation(
    aspect="Conjunction",
    hook="You love in flashes and intensely and unexpectedly.",
    core_interpretation="You're drawn to connection that feels electric and alive, not conventional or predictable. Relationships need to breathe for you to stay engaged, but your challenge is learning how to stay open without disappearing.",
    male_expression="You captivate quickly, and love feels like a spark and but staying power grows when you learn to pace the fire. Freedom doesn't have to mean distance.",
    female_expression="You fall for energy, not appearances. What draws you is soul deep difference, but love matures when excitement makes room for real connection.",
    other_expression="You're magnetic in your own way and quirky, bold, and hard to forget. Your heart wakes up when love feels like an adventure, not a script."
)

# Sextile
uranus_venus_sextile = UranusVenusAspectInterpretation(
    aspect="Sextile",
    hook="You blend freedom and affection with charm.",
    core_interpretation="You bring an easy freshness to your relationships and open minded, creative, and naturally flexible. Love doesn't trap you; it evolves with you, making space for joy and surprise.",
    male_expression="You're the kind of partner who keeps things interesting without drama. You offer connection that feels light but real.",
    female_expression="You love playfully and with presence. People feel safe with you to be their weirdest, truest selves and and that's where the magic lives.",
    other_expression="You don't need a perfect romance and you need one that can grow. Your way of loving makes space for spontaneity, change, and joy."
)

# Trine
uranus_venus_trine = UranusVenusAspectInterpretation(
    aspect="Trine",
    hook="Your love flows with natural originality.",
    core_interpretation="You express affection in a way that's unique but never forced. People feel both surprised and at ease around you and your relationships evolve smoothly, with freedom built into the bond.",
    male_expression="You radiate charm that doesn't try too hard. Your ability to love freely makes you both easy to be with and deeply inspiring.",
    female_expression="You offer love that feels refreshing and unforced, open, and honest. Others are drawn to your ability to mix closeness with independence so effortlessly.",
    other_expression="You naturally mix warmth with innovation, creating relationships that feel alive and unstuck. Your love language is freedom wrapped in care."
)

# Square
uranus_venus_square = UranusVenusAspectInterpretation(
    aspect="Square",
    hook="You crave love and but resist being tied down.",
    core_interpretation="You feel a constant push and pull between wanting closeness and needing space. That tension can lead to breakups, breakthroughs, or both and but it always pushes you to redefine what love really means for you.",
    male_expression="You may chase excitement and pull away once it feels routine. Your challenge is learning how to stay curious without always needing to escape.",
    female_expression="You love fiercely but need to breathe on your own terms. Relationships will challenge you to own both your desire for connection and your right to freedom.",
    other_expression="You're not here to follow anyone's rules about love. But to grow, you'll need to learn when freedom is real and and when it's just fear in disguise."
)

# Opposition
uranus_venus_opp = UranusVenusAspectInterpretation(
    aspect="Opposition",
    hook="Love reflects your need for space.",
    core_interpretation="You often attract relationships that challenge your sense of freedom, showing you where your patterns play out through others. It's not about choosing between closeness and independence and it's about creating a version of love that honors both.",
    male_expression="You may fall for people who feel just out of reach and or too close for comfort. Your growth comes when you stop running and start relating.",
    female_expression="You're drawn to contrasts in love and stable one day, distant the next. But in those mirrors, you begin to understand what you truly need to feel seen and free.",
    other_expression="Your love life may feel like a dance between yes and no, close and far. But every connection is an opportunity to learn how to love without losing yourself."
)

# Store all Uranus–Venus aspect interpretations
uranus_venus_aspects = {
    "Conjunction": uranus_venus_conj,
    "Sextile": uranus_venus_sextile,
    "Trine": uranus_venus_trine,
    "Square": uranus_venus_square,
    "Opposition": uranus_venus_opp
}
