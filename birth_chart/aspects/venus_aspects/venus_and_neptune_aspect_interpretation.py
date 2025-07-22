class VenusNeptuneAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
venus_neptune_conj = VenusNeptuneAspectInterpretation(
    aspect="Conjunction",
    hook="You fall in love with what could be.",
    core_interpretation="You love deeply and dream beautifully. Your heart longs for soul connection and creative transcendence and  but to stay whole, you'll need to balance your hopes with clear vision.",
    male_expression="You're a romantic idealist, moved by beauty and emotion. But your path is learning how to love fully without losing yourself in the dream.",
    female_expression="You love with your whole soul and  tenderly, intuitively, and with devotion. Your strength lies in learning to see clearly while still feeling deeply.",
    other_expression="You offer love as art and prayer. Clarity becomes your anchor, guiding your compassion toward the real and the lasting."
)

# Sextile
venus_neptune_sextile = VenusNeptuneAspectInterpretation(
    aspect="Sextile",
    hook="You offer love as a quiet gift.",
    core_interpretation="You express love with grace and intuition, bringing beauty and kindness into your relationships. Creative expression and emotional attunement come naturally to you.",
    male_expression="You're emotionally perceptive and artistically inclined, giving affection with subtlety and depth.",
    female_expression="Your love feels soft and healing. You make others feel cherished just by being fully present.",
    other_expression="You carry an aura of warmth and inspiration and  your affection comes through in small, meaningful gestures that open hearts."
)

# Trine
venus_neptune_trine = VenusNeptuneAspectInterpretation(
    aspect="Trine",
    hook="You love like music and  fluid, intuitive, and serene.",
    core_interpretation="You blend emotion and imagination with natural ease. Your romantic life is colored by compassion, creativity, and a quiet kind of spiritual magic that draws others in.",
    male_expression="You're gentle and imaginative in love and  someone who brings harmony without needing to be loud about it.",
    female_expression="Your heart is open and graceful. You offer affection that feels timeless and true.",
    other_expression="Your presence soothes and inspires. You know how to love with softness, wisdom, and a quiet creative power."
)

# Square
venus_neptune_square = VenusNeptuneAspectInterpretation(
    aspect="Square",
    hook="You reach for love and sometimes miss the mark and  but you grow every time.",
    core_interpretation="You feel deeply, often sensing more than is spoken and  but this sensitivity can blur boundaries. Love, for you, is a journey of learning when to hold on, and when to see more clearly.",
    male_expression="You long to be seen through idealized eyes and  but real connection comes when you stop hiding behind charm or fantasy.",
    female_expression="You seek soulful romance, but may overlook red flags. Over time, you learn that grounded love can be just as magical.",
    other_expression="You're moved by beauty and longing and  but your power lies in choosing love that reflects the truth of who you are."
)

# Opposition
venus_neptune_opp = VenusNeptuneAspectInterpretation(
    aspect="Opposition",
    hook="Your love reflects what you most long to see.",
    core_interpretation="Relationships often feel dreamlike or confusing. You learn through others what's real, what's illusion, and how to love without losing sight of yourself in the mirror.",
    male_expression="You seek deep emotional resonance but may mistake fantasy for connection. Growth comes when you love with both heart and clear eyes.",
    female_expression="You're drawn to soulful bonds, yet your healing begins when you stop pouring into what cannot hold you.",
    other_expression="You love through projection and  but also through deep grace. As you reclaim your heart, love becomes clearer, more compassionate, and truly reciprocal."
)

# Store all Venus–Neptune aspects
venus_neptune_aspects = {
    "Conjunction": venus_neptune_conj,
    "Sextile": venus_neptune_sextile,
    "Trine": venus_neptune_trine,
    "Square": venus_neptune_square,
    "Opposition": venus_neptune_opp
}
