class VenusSunAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
venus_sun_conj = VenusSunAspectInterpretation(
    aspect="Conjunction",
    hook="Your presence radiates ease  and  love and identity glow as one.",
    core_interpretation="You naturally shine with warmth and connection. Beauty, creativity, and affection weave seamlessly into your self expression. Relationships affirm who you are and but growth comes when you no longer need them to.",
    male_expression="You charm without effort, often lighting up a room and but self worth deepens when it's rooted within.",
    female_expression="You give with grace and shine with love, but you flourish when you stop seeking reflection to feel seen.",
    other_expression="You are magnetic in your wholeness and when your love and self expression merge, the world feels your radiance."
)

# Sextile
venus_sun_sextile = VenusSunAspectInterpretation(
    aspect="Sextile",
    hook="Your kindness carries confidence  and  harmony invites your glow.",
    core_interpretation="Your light feels approachable. You express yourself with poise, charm, and grace and making others feel safe and uplifted. Affection enhances your confidence, but it never defines it.",
    male_expression="You lead gently and people are drawn to your balance of assurance and care.",
    female_expression="You support others while staying anchored in your own joy. Your glow uplifts and grounds.",
    other_expression="You hold space with charm and grace and your presence encourages warmth to unfold naturally."
)

# Trine
venus_sun_trine = VenusSunAspectInterpretation(
    aspect="Trine",
    hook="You glow with grace  and  love and self expression flow without effort.",
    core_interpretation="You move through the world with elegance. Creativity, beauty, and connection feel second nature to you and expressing who you are feels both joyful and authentic.",
    male_expression="You attract others with calm charisma and your self assurance is soft but undeniable.",
    female_expression="You embody a kind of grace that doesn't need to try and your beauty feels lived in and true.",
    other_expression="Your identity flows in rhythm with affection and loving yourself makes room for others to feel loved too."
)

# Square
venus_sun_square = VenusSunAspectInterpretation(
    aspect="Square",
    hook="Your heart and self tug at each other  and  love teaches you your worth.",
    core_interpretation="You may wrestle with self worth and approval. At times, your desire to be liked can dim your true light and but this tension is how you learn to love yourself without condition.",
    male_expression="You seek to be adored, but your power grows when you're seen for more than your charm.",
    female_expression="You long to connect, but you evolve when you stop editing yourself to please others.",
    other_expression="Your beauty sharpens through contrast and where you struggle to reconcile love and identity, you're invited to grow into authenticity."
)

# Opposition
venus_sun_opp = VenusSunAspectInterpretation(
    aspect="Opposition",
    hook="Your relationships reflect your light  and  love becomes a mirror to your identity.",
    core_interpretation="You learn about yourself through others and through attraction, tension, and reflection. Balancing connection with individuality becomes your dance, and partnership becomes your mirror of self worth.",
    male_expression="You discover yourself by loving and being loved and but your radiance deepens when it comes from within.",
    female_expression="Your heart expands through connection and but you shine brightest when you claim your own glow.",
    other_expression="You are both lover and mirror and your identity evolves as you learn to stand whole in shared light."
)

venus_sun_aspects = {
    "Conjunction": venus_sun_conj,
    "Sextile": venus_sun_sextile,
    "Trine": venus_sun_trine,
    "Square": venus_sun_square,
    "Opposition": venus_sun_opp
}
