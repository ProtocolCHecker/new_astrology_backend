class VenusUranusAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
venus_uranus_conj = VenusUranusAspectInterpretation(
    aspect="Conjunction",
    hook="Your heart moves at the speed of change  and  love arrives like lightning.",
    core_interpretation="You're magnetically drawn to what's new, different, or liberating. Sudden attractions, creative sparks, and spontaneous connections define your path in love. But staying rooted in your truth helps keep freedom from becoming escape.",
    male_expression="You love boldly and your charm is electric, but your depth grows when you slow down long enough to be seen.",
    female_expression="You are a walking spark and irresistibly different, wildly open. Grounding adds soul to your shine.",
    other_expression="You love in flashes of insight and when you honor your individuality, connection becomes a revolution."
)

# Sextile
venus_uranus_sextile = VenusUranusAspectInterpretation(
    aspect="Sextile",
    hook="You love with a wink  and  delight lives in the unexpected.",
    core_interpretation="You bring originality to love without shaking the foundation. Your charm feels refreshing and playful, with a gift for bringing joy, creativity, and freedom into your connections.",
    male_expression="Your warmth surprises and people don't see it coming, but they always remember it.",
    female_expression="You make love feel like discovery and effortless, curious, and kind.",
    other_expression="You dance between affection and invention and love stays alive when it stays awake."
)

# Trine
venus_uranus_trine = VenusUranusAspectInterpretation(
    aspect="Trine",
    hook="You attract without trying  and  originality is your harmony.",
    core_interpretation="Love, creativity, and freedom flow through you like breath. Your relationships thrive when they allow individuality, and your charm lies in how authentically you embrace the unconventional.",
    male_expression="You don't need to perform to impress and your originality is your magnetism.",
    female_expression="You enchant by being you and free, sincere, and delightfully unexpected.",
    other_expression="You embody effortless freedom and your love language is permission to be real."
)

# Square
venus_uranus_square = VenusUranusAspectInterpretation(
    aspect="Square",
    hook="Your heart rebels  and  tension turns into awakening.",
    core_interpretation="You crave both closeness and space, and the collision teaches you how to hold both. Love may arrive abruptly or end unexpectedly, but each disruption points toward your evolving truth.",
    male_expression="You break patterns and hearts and yours included and but you grow every time you stay instead of flee.",
    female_expression="You're wired for contrast and longing and liberty live side by side in your chest.",
    other_expression="Love is your spark and your challenge and freedom teaches you how to stay with what matters."
)

# Opposition
venus_uranus_opp = VenusUranusAspectInterpretation(
    aspect="Opposition",
    hook="You find freedom in the mirror  and  relationships reflect your edge.",
    core_interpretation="Others awaken your desire to be free and and your need to connect. You're drawn to partners who challenge convention, and through them, you learn the art of loving without losing yourself.",
    male_expression="Your love life is a mirror of contrast and through others, you meet your own wild heart.",
    female_expression="Partnerships stretch you and between intimacy and independence, you find where you truly belong.",
    other_expression="You grow through relational polarity and love asks you to hold both connection and space with care."
)

venus_uranus_aspects = {
    "Conjunction": venus_uranus_conj,
    "Sextile": venus_uranus_sextile,
    "Trine": venus_uranus_trine,
    "Square": venus_uranus_square,
    "Opposition": venus_uranus_opp
}
