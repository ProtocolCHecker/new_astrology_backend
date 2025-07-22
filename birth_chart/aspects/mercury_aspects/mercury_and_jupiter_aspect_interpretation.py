class MercuryJupiterAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Mercury Conjunct Jupiter
mercury_conjunct_jupiter = MercuryJupiterAspectInterpretation(
    aspect="Conjunct",
    hook="Your thoughts arrive in full color. Big ideas pour out without restraint.",
    core_interpretation="You speak with infectious optimism and breadth. Focus on details to turn your visionary flair into tangible progress.",
    male_expression="You inspire through grand storytelling. Balancing scope with specifics strengthens your credibility.",
    female_expression="Your insights uplift and expand minds. Rooting dreams in data grounds your wisdom.",
    other_expression="You're a motivational thinker. Bridging ideals with praxis unlocks your greatest impact."
)

# Mercury Sextile Jupiter
mercury_sextile_jupiter = MercuryJupiterAspectInterpretation(
    aspect="Sextile",
    hook="Your ideas find wings. Eloquent, warm, and broadly received.",
    core_interpretation="You are granted polish perspective and generous speech. Pairing your open mind with focused intent turns conversation into connection.",
    male_expression="You bridge cultures through dialogue. Adding depth to your optimism cements your message.",
    female_expression="Your teaching spirit shines. Grounding philosophy in practice enhances your influence.",
    other_expression="You connect dots with ease. Channeling curiosity into expertise refines your gift."
)

# Mercury Trine Jupiter
mercury_trine_jupiter = MercuryJupiterAspectInterpretation(
    aspect="Trine",
    hook="Your words light paths. Effortlessly wise, gently guiding.",
    core_interpretation="You are blessed with natural mentorship and eloquence. Weaving nuance into your broad view deepens every lesson you share.",
    male_expression="You enlighten with humor and heart. Stretching empathy amplifies your reach.",
    female_expression="Your wisdom comforts and inspires. Inviting questions sustains your growth.",
    other_expression="You are an intellectual bridge. Fusing idealism with discernment empowers your voice."
)

# Mercury Square Jupiter
mercury_square_jupiter = MercuryJupiterAspectInterpretation(
    aspect="Square",
    hook="Your mind races ahead. Sometimes faster than facts can follow.",
    core_interpretation="You are facing your boundless zeal. Slowing to verify details turns enthusiasm into lasting authority.",
    male_expression="You spark curiosity with bold claims. Pair passion with precision to build trust.",
    female_expression="Your expansive vision excites. Anchoring ideas in reality tempers overreach.",
    other_expression="You're a big picture thinker. Marrying ambition with accuracy elevates your voice."
)

# Mercury Opposite Jupiter
mercury_opposite_jupiter = MercuryJupiterAspectInterpretation(
    aspect="Opposition",
    hook="Your voice stretches between truth and tale. You seek balance in belief.",
    core_interpretation="You are pulled between detail and doctrine. Integrating both sharpens insight and steadies your message.",
    male_expression="You wrestle with extremes. Finding middle ground brings clarity.",
    female_expression="Your faith and facts may clash. Harmonizing them empowers your convictions.",
    other_expression="You are a mental explorer. Balancing skepticism with optimism grounds your wisdom."
)

mercury_jupiter_aspects = {
    "Conjunct": mercury_conjunct_jupiter,
    "Sextile": mercury_sextile_jupiter,
    "Trine": mercury_trine_jupiter,
    "Square": mercury_square_jupiter,
    "Opposition": mercury_opposite_jupiter
}