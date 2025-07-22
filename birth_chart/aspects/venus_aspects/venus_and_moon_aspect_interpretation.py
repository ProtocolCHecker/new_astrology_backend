class VenusMoonAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
venus_moon_conj = VenusMoonAspectInterpretation(
    aspect="Conjunction",
    hook="You love with your whole heart.",
    core_interpretation="You're emotionally warm and naturally affectionate and someone who expresses love through care and presence. Your need for connection runs deep, and your greatest fulfillment comes when you're able to both give and receive tenderness.",
    male_expression="You're a kind soul with a natural gift for comforting others. Your emotional sensitivity is part of your charm and just don't forget to tend to your own heart too.",
    female_expression="You nurture through affection, making others feel safe and loved. But you thrive most when you also let your own needs be seen and met.",
    other_expression="You have a soft and loving presence that makes others feel emotionally held. Your challenge is learning how to balance your giving with receiving love fully."
)

# Sextile
venus_moon_sextile = VenusMoonAspectInterpretation(
    aspect="Sextile",
    hook="Your care feels easy and sincere.",
    core_interpretation="You express affection with warmth and thoughtfulness, creating emotional connections that feel stable and kind. You make space for people to feel accepted, often through simple acts of love and presence.",
    male_expression="You offer quiet emotional support that doesn't ask for attention but leaves a lasting impact. Your love feels steady, not showy.",
    female_expression="You're someone others trust with their feelings. Your nurturing feels genuine, and your ability to create harmony is a quiet superpower.",
    other_expression="You give care naturally and from the heart. Your emotional expression is smooth and gentle, allowing for peaceful and loving connections."
)

# Trine
venus_moon_trine = VenusMoonAspectInterpretation(
    aspect="Trine",
    hook="You make love feel like home.",
    core_interpretation="Your emotional and romantic instincts work in perfect sync, allowing you to build relationships that feel safe, affectionate, and deeply fulfilling. You offer warmth without fear, and your love flows with ease.",
    male_expression="You bring a calming, nurturing energy to your connections. People feel emotionally grounded around you, often without knowing why.",
    female_expression="You radiate comfort and grace in relationships, making people feel both cherished and at ease. Your softness is your strength.",
    other_expression="You offer emotional harmony to those around you, creating space where love feels natural, safe, and nourishing. You embody comfort in connection."
)

# Square
venus_moon_square = VenusMoonAspectInterpretation(
    aspect="Square",
    hook="You feel more than you show.",
    core_interpretation="You may feel caught between what you want emotionally and how you express love. This tension pushes you to grow through learning how to care for others without abandoning your own emotional clarity.",
    male_expression="You often want to give more than you have and or expect others to meet needs you haven't expressed. Finding your emotional voice is key to building stronger relationships.",
    female_expression="You may feel like your emotions and desires pull in different directions. But that friction is exactly what helps you build deeper self trust.",
    other_expression="You wrestle with being nurturing while honoring your own emotional truth. But your growth lies in learning how to stay loving without losing yourself."
)

# Opposition
venus_moon_opp = VenusMoonAspectInterpretation(
    aspect="Opposition",
    hook="You find your heart in the eyes of another.",
    core_interpretation="Relationships show you where your emotional needs live and and where they haven't been fully understood yet. Through love and connection, you learn how to balance giving with receiving, and how to stay emotionally true to yourself.",
    male_expression="You often give too much or pull away too fast. Balance comes when you learn that real connection includes your needs, too.",
    female_expression="You grow through relationship dynamics that challenge how you express care. Over time, you learn that harmony doesn't mean self sacrifice.",
    other_expression="Your relationships teach you how to navigate emotional give and take. With time, love becomes less about adapting and and more about being fully seen."
)

# Store all Venus–Moon aspect interpretations
venus_moon_aspects = {
    "Conjunction": venus_moon_conj,
    "Sextile": venus_moon_sextile,
    "Trine": venus_moon_trine,
    "Square": venus_moon_square,
    "Opposition": venus_moon_opp
}
