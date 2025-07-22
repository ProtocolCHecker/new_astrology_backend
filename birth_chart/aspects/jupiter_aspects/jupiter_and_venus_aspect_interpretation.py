class JupiterVenusAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Jupiter Conjunct Venus
jupiter_conjunction_venus = JupiterVenusAspectInterpretation(
    aspect="Conjunction",
    hook="You love in bold strokes  and  more joy, more beauty, more heart.",
    core_interpretation="With Venus conjunct Jupiter, you're wired for big hearted joy. You love deeply, give generously, and often find meaning in celebrating life and love. But to stay balanced, you'll need to watch your tendency to idealize others or overdo what feels good in the moment.",
    male_expression="You're charming and giving  and  a romantic who wants to make people feel seen and adored. Just be careful not to give more than you truly have.",
    female_expression="You radiate love, warmth, and sensual joy. But stay grounded  and  your big heart doesn't need to save everyone to be valuable.",
    other_expression="You're a joyful amplifier of connection. When you pair generosity with self awareness, your love becomes a blessing for all involved."
)

# Jupiter Sextile Venus
jupiter_sextile_venus = JupiterVenusAspectInterpretation(
    aspect="Sextile",
    hook="You live with an open heart  and  and love tends to meet you halfway.",
    core_interpretation="This aspect brings warmth, grace, and ease in relationships. You attract affection through kindness and authenticity, often creating harmony without trying too hard. Your natural optimism helps others feel safe and seen  and  and love, for you, is about mutual upliftment.",
    male_expression="You're gracious and genuine  and  someone people trust and enjoy being around. You give love with simplicity and warmth.",
    female_expression="You connect through shared values and heartfelt presence. Your love feels natural, never forced.",
    other_expression="You make space for others to feel appreciated and safe. Your presence soothes, and your heart knows how to welcome joy."
)

# Jupiter Trine Venus
jupiter_trine_venus = JupiterVenusAspectInterpretation(
    aspect="Trine",
    hook="You were born to love  and  and to be loved, effortlessly and fully.",
    core_interpretation="With Venus trine Jupiter, love, beauty, and abundance tend to flow to you with ease. You carry a peaceful charm and sincere generosity that make you naturally magnetic. Relationships often expand your life, and your ability to find joy in connection is a gift  and  just remember to stay engaged, even when things come easily.",
    male_expression="You're a source of comfort and celebration  and  steady, affectionate, and admired for your gentle strength.",
    female_expression="You bring light, love, and balance wherever you go. Others are drawn to your sense of harmony and soul deep joy.",
    other_expression="You uplift with grace  and  offering joy, safety, and emotional beauty in every space you enter. Love flows from you, not just to you."
)

# Jupiter Square Venus
jupiter_square_venus = JupiterVenusAspectInterpretation(
    aspect="Square",
    hook="You love with your whole heart  and  but sometimes it spills over too far.",
    core_interpretation="This aspect fills you with enthusiasm, generosity, and hunger for connection  and  but it also challenges you to find balance. You may love hard and fast, spend easily, or expect a lot without always checking in with reality. Still, when you learn to give from fullness rather than longing, your love becomes expansive and true.",
    male_expression="You're magnetic and giving  and  but need to learn when enough is enough. Boundaries protect both your heart and your energy.",
    female_expression="You love richly and want to lift others up  and  but don't let that become self sacrifice. Your joy matters too.",
    other_expression="You're a passionate giver, sometimes to a fault. Learning to receive and rest helps your love shine even brighter."
)

# Jupiter Opposite Venus
jupiter_opposition_venus = JupiterVenusAspectInterpretation(
    aspect="Opposition",
    hook="You stretch for something bigger in love  and  sometimes beyond what's truly there.",
    core_interpretation="With this opposition, your heart longs for deep, expansive love  and  but may chase idealized versions of it. You give easily and want meaning in every connection, but must learn not to lose yourself in the dream. When your love is rooted in self honesty, your warmth becomes truly magnetic.",
    male_expression="You're charming and expansive in love, but must learn to choose with clarity. Romance is richer when it's real.",
    female_expression="You offer so much of your heart  and  but part of your growth is learning to give from self love, not just hope.",
    other_expression="You're a seeker of soulful love, often ahead of what others can offer. When you meet yourself with that same devotion, love becomes real and lasting."
)

# Create a dictionary to store all Jupiter Venus aspect interpretations
jupiter_venus_aspects = {
    "Conjunction": jupiter_conjunction_venus,
    "Sextile": jupiter_sextile_venus,
    "Trine": jupiter_trine_venus,
    "Square": jupiter_square_venus,
    "Opposition": jupiter_opposition_venus
}