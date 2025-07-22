class MoonAscendantAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
moon_asc_conj = MoonAscendantAspectInterpretation(
    aspect="Conjunction",
    hook="Your feelings are your face, what you carry inside shows up in every glance.",
    core_interpretation="You share your emotions freely, drawing people in with genuine warmth. At times you might wish for more solitude, but your openness gives others real comfort.",
    male_expression="You emit a steady, caring presence that instantly soothes. Don't forget to give yourself a moment's peace and you deserve the same kindness you give.",
    female_expression="Your gentle warmth feels like a safe harbor to everyone around you. Remember to tuck away some of that tenderness for your own heart.",
    other_expression="You mirror people's feelings in a way that feels deeply healing, but guarding your own energy ensures you stay balanced."
)

# Sextile
moon_asc_sextile = MoonAscendantAspectInterpretation(
    aspect="Sextile",
    hook="Your heart guides your presence and care flows naturally in how you show up.",
    core_interpretation="You sense what others need before they say it and offer kindness with ease. Sometimes you rush to support, and it's okay to pause and check in with yourself.",
    male_expression="Your instinctive understanding makes people feel truly seen. Be sure to lean on trusted friends when you need the same care.",
    female_expression="Your soft empathy creates harmony wherever you go. Take moments to reflect on your own feelings, too.",
    other_expression="You make others comfortable with your calm attention—just ensure you keep that same compassion for you."
)

# Trine
moon_asc_trine = MoonAscendantAspectInterpretation(
    aspect="Trine",
    hook="Your inner calm flows outward and your presence feels like a warm embrace.",
    core_interpretation="People relax around you because your emotions and actions match so smoothly. If life ever feels too easy, challenge yourself gently to grow.",
    male_expression="Your natural grace inspires trust and ease in others. Remember to step into new situations to keep that inner light shining bright.",
    female_expression="Your soothing energy feels like home to everyone you meet. Embracing a little novelty can refresh that comforting glow.",
    other_expression="You radiate authenticity in every gesture—occasionally seeking fresh experiences keeps your spirit vibrant."
)

# Square
moon_asc_square = MoonAscendantAspectInterpretation(
    aspect="Square",
    hook="Your inside and outside tug at each other and tension shapes your strength.",
    core_interpretation="Sometimes what you feel doesn't match how you act, and that friction helps you learn who you really are. Embracing both sides of yourself brings genuine confidence.",
    male_expression="You wrestle with showing emotion and staying composed, and that struggle teaches resilience. Let small moments of vulnerability remind you of your own strength.",
    female_expression="You feel deeply yet mask it outwardly, which pushes you to integrate heart and image. Celebrating when they align fuels your authenticity.",
    other_expression="Your contradictions forge a unique presence—honoring both your light and your shade makes you truly whole."
)

# Opposition
moon_asc_opp = MoonAscendantAspectInterpretation(
    aspect="Opposition",
    hook="Your self meets your mirror and relationships reflect your heart.",
    core_interpretation="You learn about your own needs by how others respond to you, turning every partnership into a lesson in self awareness. Finding balance in giving and receiving leads to deeper connections.",
    male_expression="You grow through the emotional feedback of those closest to you, building clearer boundaries. Trusting your own instincts strengthens your bonds.",
    female_expression="You see your own sensitivity reflected in relationships, guiding you to honor your needs. Embracing mutual support helps you stand strong.",
    other_expression="You deepen your self knowledge through interaction—opening and protecting your heart in equal measure brings real intimacy."
)

moon_ascendant_aspects = {
    "Conjunction": moon_asc_conj,
    "Sextile": moon_asc_sextile,
    "Trine": moon_asc_trine,
    "Square": moon_asc_square,
    "Opposition": moon_asc_opp
}
