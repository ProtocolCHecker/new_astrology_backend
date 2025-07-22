class NeptuneVenusAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
neptune_venus_conj = NeptuneVenusAspectInterpretation(
    aspect="Conjunction",
    hook="Your love feels like a gentle dream and affection flows from your soul.",
    core_interpretation="You give and receive love in a beautifully soft way that comforts others. Remembering to care for yourself keeps your heart open and strong.",
    male_expression="Your tender devotion warms those around you. Taking time for your own needs keeps you giving happily.",
    female_expression="Your loving nature brings peace and joy. Letting others care for you fills your well.",
    other_expression="Your compassionate charm lights up every relationship. Welcoming self care makes your warmth last."
)

# Sextile
neptune_venus_sextile = NeptuneVenusAspectInterpretation(
    aspect="Sextile",
    hook="Your affection carries a soft glow and harmony is your signature.",
    core_interpretation="You bring beauty and kindness effortlessly to every bond. Balancing that with clear personal boundaries keeps your relationships healthy.",
    male_expression="Your gentle charm uplifts people quickly. Saying “I need a moment” protects your own energy.",
    female_expression="Your poetic care feels natural and true. Setting small limits helps you give from a full heart.",
    other_expression="Your soft love inspires trust and comfort. Remembering self respect makes your care sustainable."
)

# Trine
neptune_venus_trine = NeptuneVenusAspectInterpretation(
    aspect="Trine",
    hook="Your feelings and desires harmonize and love feels like second nature.",
    core_interpretation="You connect through warmth and ease, making intimacy flow naturally. Carving out “me time” ensures your love never runs dry.",
    male_expression="Your caring confidence draws people close. Scheduling personal breaks keeps your love vibrant.",
    female_expression="Your affectionate flow feels abundant and true. Taking time for solitude refills your heart.",
    other_expression="Your seamless love brightens every life. Pairing giving with receiving makes it last."
)

# Square
neptune_venus_square = NeptuneVenusAspectInterpretation(
    aspect="Square",
    hook="Your heart wavers between giving and needing and tension invites growth.",
    core_interpretation="You learn to balance generosity with self care, and that tension teaches you healthy limits. Saying “no” sometimes keeps your kindness from burning out.",
    male_expression="Your big heart can give too much without rest. Setting clear boundaries protects your spirit.",
    female_expression="Your nurturing side sometimes forgets to recharge. Taking regular breaks lets you sustain that care.",
    other_expression="Your evolving love shapes you deeply. Honoring your own needs refines your generosity."
)

# Opposition
neptune_venus_opp = NeptuneVenusAspectInterpretation(
    aspect="Opposition",
    hook="Love mirrors your feelings and relationships reflect your depth.",
    core_interpretation="You learn what you need most through your closest bonds. Balancing giving and receiving makes every connection stronger.",
    male_expression="Your empathy deepens through partnership and feedback. Letting others support you keeps your heart from tiring.",
    female_expression="Your caring naturally reflects back, teaching you your own worth. Welcoming affection ensures your love stays bright.",
    other_expression="Your mirrored intimacy guides your growth. Mutual care strengthens every bond."
)

neptune_venus_aspects = {
    "Conjunction": neptune_venus_conj,
    "Sextile": neptune_venus_sextile,
    "Trine": neptune_venus_trine,
    "Square": neptune_venus_square,
    "Opposition": neptune_venus_opp
}
