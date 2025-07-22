class JupiterAscendantAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
jupiter_conjunction_ascendant = JupiterAscendantAspectInterpretation(
    aspect="Conjunction",
    hook="You grow as you appear  and  optimism beams from your presence.",
    core_interpretation="With Jupiter conjunct Ascendant, you have a buoyant and generous persona, filled with a strong sense of self worth and an adventurous spirit. However, be mindful of overindulgence or an inflated ego; staying grounded will help you make the most of this aspect.",
    male_expression="You are a warm leader, enthusiastic and charismatic. Embrace humility to truly shine and inspire others.",
    female_expression="You are a radiant optimist, drawing others through your expansive kindness. Remember, moderation is key to sustaining your positive energy.",
    other_expression="You have a magnetic presence; your faith in life uplifts those around you. Grounded actions will strengthen your impact."
)

# Sextile
jupiter_sextile_ascendant = JupiterAscendantAspectInterpretation(
    aspect="Sextile",
    hook="Opportunity and charisma dance gently  and  growth happens naturally for you.",
    core_interpretation="Jupiter sextile Ascendant encourages an approachable confidence and easy rapport, supporting your personal development and positive social impression. Your growth feels natural and effortless.",
    male_expression="You are an engaging connector, easy to approach, and you grow through community. Your connections are your strength.",
    female_expression="You are a friendly aspirant, blossoming through sincere openness. Your openness is your path to success.",
    other_expression="You are a graceful explorer; your maturity unfolds through gentle expansion. Your journey is one of continuous growth."
)

# Trine
jupiter_trine_ascendant = JupiterAscendantAspectInterpretation(
    aspect="Trine",
    hook="Your presence hums with potential  and  confidence effortlessly soars.",
    core_interpretation="With Jupiter trine Ascendant, you are endowed with natural charm, optimism, and success oriented energy. You are inspiring and authentic, well received without pushing too hard. Your confidence is your gift.",
    male_expression="You are an effortless influencer, uplifting others with calm confidence. Your calmness is your superpower.",
    female_expression="You are a serene achiever, shining through poised ambition. Your poise sets you apart.",
    other_expression="You are a flowing promise; your presence expands through ease and grace. Your ease is your essence."
)

# Square
jupiter_square_ascendant = JupiterAscendantAspectInterpretation(
    aspect="Square",
    hook="Your ambition strains your reflection  and  tension refines your presence.",
    core_interpretation="Jupiter square Ascendant brings friction between your personal aspirations and outer persona. This challenge urges you to balance inner confidence with grounded self awareness to avoid arrogance. Embrace this tension as it refines your character.",
    male_expression="You are a driven idealist, learning humility through self correction. Your journey is about finding balance.",
    female_expression="You are an ambitious explorer, refining your goals through self awareness. Your self awareness is your guide.",
    other_expression="You experience challenge borne growth; your presence tempers itself into authenticity. Your challenges are your catalysts."
)

# Opposition
jupiter_opposition_ascendant = JupiterAscendantAspectInterpretation(
    aspect="Opposition",
    hook="Your self mirrors your beliefs  and  relationships become your stage for growth.",
    core_interpretation="With Jupiter opposite Ascendant, you are urged to find balance between how you see yourself and how others see you. This aspect encourages growth through partnerships, aligning your inner faith with relational perceptions. Your relationships are your mirrors.",
    male_expression="You are a reflective companion, learning about yourself through connection. Your connections are your teachers.",
    female_expression="You are a relational optimist, maturing by integrating personal and shared visions. Your shared visions are your path to growth.",
    other_expression="You are a mirror of expansion; your presence evolves through mutual insight. Your mutual insights are your wisdom."
)

jupiter_ascendant_aspects = {
    "Conjunction": jupiter_conjunction_ascendant,
    "Sextile": jupiter_sextile_ascendant,
    "Trine": jupiter_trine_ascendant,
    "Square": jupiter_square_ascendant,
    "Opposition": jupiter_opposition_ascendant
}
