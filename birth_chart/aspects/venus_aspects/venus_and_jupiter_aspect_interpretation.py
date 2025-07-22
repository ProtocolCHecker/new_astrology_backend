class VenusJupiterAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
venus_jupiter_conj = VenusJupiterAspectInterpretation(
    aspect="Conjunction",
    hook="You attract blessings without even trying.",
    core_interpretation="You carry a joyful, open hearted presence that draws people and good fortune into your life. You love to share beauty, affection, and pleasure and but your challenge is learning when enough is truly enough.",
    male_expression="You're generous with love, time, and attention, often spreading warmth wherever you go. Just watch that your giving doesn't turn into overextending.",
    female_expression="You radiate charm and kindness, with a heart that wants everyone to feel good. But you thrive most when your joy is rooted in intention, not just impulse.",
    other_expression="You shine in the art of connection and fun, loving, and generous. Your journey is about knowing that saying yes to everything can sometimes mean losing touch with yourself."
)

# Sextile
venus_jupiter_sextile = VenusJupiterAspectInterpretation(
    aspect="Sextile",
    hook="Your charm opens doors and hearts.",
    core_interpretation="You bring people together with ease, offering a warm, optimistic energy that feels both supportive and uplifting. You see the good in others and help them see it too, often through shared joy or creativity.",
    male_expression="You're naturally encouraging and socially smooth, helping others feel accepted and welcomed. Your generosity feels light and genuine.",
    female_expression="You move through the world with a soft strength that blends kindness and confidence. People feel better just by being around you.",
    other_expression="You offer good energy without needing to take the spotlight. Your presence reminds others how good it can feel to just enjoy each other."
)

# Trine
venus_jupiter_trine = VenusJupiterAspectInterpretation(
    aspect="Trine",
    hook="You make life feel sweeter and just by being you.",
    core_interpretation="You carry a natural flow of affection, beauty, and goodwill that makes relationships smooth and enjoyable. Your sense of harmony isn't just personal and it lifts the energy around you effortlessly.",
    male_expression="You live with an ease that draws people in, often combining culture, kindness, and fun in a way that makes everyone feel included.",
    female_expression="You shine with graceful abundance and your warmth, taste, and emotional intelligence make you someone people want in their corner.",
    other_expression="You exude a gentle confidence that doesn't need to impress. Love, beauty, and connection follow you because you bring them with you."
)

# Square
venus_jupiter_square = VenusJupiterAspectInterpretation(
    aspect="Square",
    hook="You give big and but sometimes too much.",
    core_interpretation="You love deeply and often say yes too quickly and to people, experiences, or pleasures. The challenge is finding where generosity ends and overindulgence begins, especially when you're trying to prove your worth through what you offer.",
    male_expression="You often want to be everything for everyone, which can drain your joy if not kept in check. Real love doesn't need to be earned through excess.",
    female_expression="You can overextend in relationships, thinking love means giving more than you actually feel. Your power comes when you learn to give with clarity, not obligation.",
    other_expression="You're learning that more isn't always better. Your heart is huge and but balance is what keeps it open without getting lost in the overflow."
)

# Opposition
venus_jupiter_opp = VenusJupiterAspectInterpretation(
    aspect="Opposition",
    hook="Others show you where your heart overreaches.",
    core_interpretation="Relationships often reveal how much you give and and where you might be giving too much. Your path is about balancing your desire to please with the wisdom to know when giving becomes self sacrifice.",
    male_expression="You're generous in love, sometimes to the point of forgetting your own needs. True growth comes when you realize that real connection doesn't require overcompensating.",
    female_expression="You're learning that saying no can be as loving as saying yes. Through relationships, you discover the line between support and self neglect.",
    other_expression="You often meet people who mirror your own patterns around giving and receiving. These moments are chances to redefine love with more honesty and self respect."
)

# Store all Venus–Jupiter aspect interpretations
venus_jupiter_aspects = {
    "Conjunction": venus_jupiter_conj,
    "Sextile": venus_jupiter_sextile,
    "Trine": venus_jupiter_trine,
    "Square": venus_jupiter_square,
    "Opposition": venus_jupiter_opp
}
