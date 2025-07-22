class VenusAscendantAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
venus_asc_conj = VenusAscendantAspectInterpretation(
    aspect="Conjunction",
    hook="You charm the world by simply being  and  beauty is woven into your presence.",
    core_interpretation="With Venus conjunct Ascendant, you possess a natural charm and style that resonates aesthetically in your appearance and demeanor. You are attractive, gracious, and socially magnetic. Embrace your charm as it opens doors for you.",
    male_expression="You are an effortless charmer, drawing others with warmth and style. However, strive to ground your superficial appeal in deeper connections.",
    female_expression="You are graceful and attractive, naturally sociable. Remember to seek depth beyond your looks to find true fulfillment.",
    other_expression="You have a magnetic aura; your presence delights others. Focus on developing the beauty beneath the surface to enrich your relationships."
)

# Sextile
venus_asc_sext = VenusAscendantAspectInterpretation(
    aspect="Sextile",
    hook="You flow with harmony  and  charm meets opportunity in your aura.",
    core_interpretation="Venus sextile Ascendant gives you a pleasant and approachable presence, making social interactions feel easy and enjoyable. You blend grace with subtle magnetism effortlessly. Your social grace is a gift.",
    male_expression="You are a polished socializer, connecting smoothly with others through gentle warmth. Your warmth is your strength.",
    female_expression="You are a friendly nurturer, balancing charm with empathetic engagement. Your empathy enriches your connections.",
    other_expression="You have a harmonious presence; your charisma feels both genuine and welcoming. Your authenticity draws people to you."
)

# Trine
venus_asc_trine = VenusAscendantAspectInterpretation(
    aspect="Trine",
    hook="Your presence whispers beauty  and  compatibility flows naturally.",
    core_interpretation="With Venus trine Ascendant, you exude effortless social grace and refined style. Your interactions are smooth and aesthetically pleasing, making you naturally appealing. Your grace is effortless and inspiring.",
    male_expression="You are cultured and confident, naturally elegant in appearance and manner. Your elegance is a reflection of your inner poise.",
    female_expression="You are an elegant influencer, embodying beauty and kindness without effort. Your influence is a natural extension of who you are.",
    other_expression="You have a poised presence; your charm and authenticity resonate in harmony. Your authenticity is your power."
)

# Square
venus_asc_square = VenusAscendantAspectInterpretation(
    aspect="Square",
    hook="Your beauty is challenged  and  tension invites self and definition.",
    core_interpretation="Venus square Ascendant creates inner conflict between your self and image and values. This tension prompts growth through reconciling your desires for approval with authentic self and presentation. Embrace this challenge as it leads to self and discovery.",
    male_expression="You are fashion and conscious yet restless, maturing through self and acceptance beyond appearance. Your journey is about finding inner confidence.",
    female_expression="You are sensitive yet striving, learning emotional clarity through self and expression. Your sensitivity is your guide to inner strength.",
    other_expression="You have a tension and tempered aura; your personal style evolves through conflict and driven insight. Your conflicts are your stepping stones."
)

# Opposition
venus_asc_opp = VenusAscendantAspectInterpretation(
    aspect="Opposition",
    hook="You mirror affection  and  relationships show you your appeal.",
    core_interpretation="With Venus opposite Ascendant, your relational dynamics are highlighted in your self and presentation. You learn about your own values through how others respond to your charm and presence. Your relationships are your mirrors.",
    male_expression="You are a relational mirror, learning about self and worth through partnerships. These partnerships are your teachers.",
    female_expression="You have reflective charm, growing in identity through relational feedback. This feedback is your guide to self and awareness.",
    other_expression="You are a mirror of beauty, evolving through interpersonal resonance. This resonance is your path to understanding yourself."
)

venus_ascendant_aspects = {
    "Conjunction": venus_asc_conj,
    "Sextile": venus_asc_sext,
    "Trine": venus_asc_trine,
    "Square": venus_asc_square,
    "Opposition": venus_asc_opp
}
