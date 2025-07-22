class JupiterAscendantAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
jupiter_asc_conj = JupiterAscendantAspectInterpretation(
    aspect="Conjunction",
    hook="You grow as you appear  and  optimism beams from your presence.",
    core_interpretation="With Jupiter conjunct your Ascendant, you naturally radiate generosity and confidence, making you quite appealing to others. However, be mindful of coming across as overly self and assured or indulgent; grounding yourself will help you shine even brighter.",
    male_expression="You are a warm leader, full of enthusiasm and charisma. Embrace humility to truly connect with others.",
    female_expression="Your radiant optimism draws people in, and your kindness is expansive. Just remember to practice moderation to maintain balance.",
    other_expression="Your magnetic presence uplifts those around you. Strengthen your impact with grounded actions."
)

# Sextile
jupiter_asc_sextile = JupiterAscendantAspectInterpretation(
    aspect="Sextile",
    hook="Opportunity and charisma dance gently in your life  and  growth happens naturally.",
    core_interpretation="With Jupiter sextile your Ascendant, you exude approachable confidence and easily build rapport with others. This aspect supports your personal development and enhances your social interactions positively.",
    male_expression="You are an engaging connector, easily approachable, and you grow through your community. Keep nurturing these relationships.",
    female_expression="Your friendly nature helps you blossom through sincere openness. Stay true to this path.",
    other_expression="Your graceful exploration of life helps your maturity unfold gently. Embrace this journey."
)

# Trine
jupiter_asc_trine = JupiterAscendantAspectInterpretation(
    aspect="Trine",
    hook="Your presence hums with potential  and  confidence effortlessly soars.",
    core_interpretation="With Jupiter trine your Ascendant, you possess natural charm and optimism. You inspire others authentically and are well and received without trying too hard, making success come more easily to you.",
    male_expression="You are an effortless influencer, uplifting others with calm confidence. Continue to use this gift wisely.",
    female_expression="Your serene demeanor helps you shine through poised ambition. Keep aiming high.",
    other_expression="Your presence expands through ease and grace. Flow with this promise and embrace your potential."
)

# Square
jupiter_asc_square = JupiterAscendantAspectInterpretation(
    aspect="Square",
    hook="Your ambition strains your reflection  and  tension refines your presence.",
    core_interpretation="With Jupiter square your Ascendant, you may feel friction between your personal aspirations and how you present yourself. Balancing inner confidence with self and awareness is key to avoiding arrogance and achieving your goals.",
    male_expression="As a driven idealist, you learn humility through self and correction. Embrace these lessons for growth.",
    female_expression="Your ambitious nature helps you refine your goals through self and awareness. Keep focusing on this balance.",
    other_expression="Your growth comes through challenges, tempering your presence into authenticity. Embrace this journey."
)

# Opposition
jupiter_asc_opp = JupiterAscendantAspectInterpretation(
    aspect="Opposition",
    hook="Your self mirrors your beliefs  and  relationships become your stage for growth.",
    core_interpretation="With Jupiter opposite your Ascendant, you are encouraged to find balance between how you see yourself and how others perceive you. Growth comes through partnerships, aligning your inner faith with relational perceptions.",
    male_expression="As a reflective companion, you learn about yourself through connection. Cherish these insights.",
    female_expression="Your relational optimism helps you mature by integrating personal and shared visions. Keep nurturing these bonds.",
    other_expression="Your presence evolves through mutual insight. Embrace this mirror of expansion."
)

jupiter_ascendant_aspects = {
    "Conjunction": jupiter_asc_conj,
    "Sextile": jupiter_asc_sextile,
    "Trine": jupiter_asc_trine,
    "Square": jupiter_asc_square,
    "Opposition": jupiter_asc_opp
}
