class JupiterUranusAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Jupiter Conjunct Uranus
jupiter_conjunction_uranus = JupiterUranusAspectInterpretation(
    aspect="Conjunction",
    hook="The future calls  and  and you answer with vision, freedom, and bold invention.",
    core_interpretation="With Jupiter conjunct Uranus, you are wired for breakthroughs. Your optimism is unconventional, your insights are lightning fast, and your need for growth is intimately tied to innovation. You rebel against limits and are energized by change and progress. Embrace your role as a trendsetter or bold thinker, as your genius lies in spontaneity and authentic expression. You don't follow; you discover.",
    male_expression="You are a restless visionary, following inner sparks rather than tradition. Your restlessness is your strength.",
    female_expression="You are an intuitive rebel, blending insight with freedom in graceful rebellion. Your intuition is your guide.",
    other_expression="You are a paradigm breaker, thriving on originality and belief in better futures. Your originality is your gift."
)

# Jupiter Sextile Uranus
jupiter_sextile_uranus = JupiterUranusAspectInterpretation(
    aspect="Sextile",
    hook="Your intuition opens doors  and  your curiosity keeps them unlocked.",
    core_interpretation="This supportive aspect gives you a spirit of experimentation and a love of learning that expands naturally over time. You are open to unorthodox ideas and likely to follow an unusual path that pays off through your adaptability and openness. Change inspires you, and your vision is future forward. Embrace your role as a practical idealist who blends hope and originality into life enhancing insights.",
    male_expression="You are a progressive realist, blending foresight with grounded action. Your progressiveness is your strength.",
    female_expression="You are an inventive teacher, inspiring through knowledge and uniqueness. Your inventiveness is your gift.",
    other_expression="You are an optimistic innovator, shaping the future by living beyond limits. Your optimism is your compass."
)

# Jupiter Trine Uranus
jupiter_trine_uranus = JupiterUranusAspectInterpretation(
    aspect="Trine",
    hook="Freedom flows where intuition leads.",
    core_interpretation="This trine blesses you with natural openness to synchronicity, new ideas, and sudden opportunities. You sense what's possible, often before anyone else does. Your path is non linear but richly inspired, and your beliefs evolve freely over time. Embrace your uniqueness and encourage it in others, as you are a powerful catalyst for change. Good fortune often follows your boldness, especially when you trust your timing and stay true to your inner compass.",
    male_expression="You are a natural futurist, riding waves of change with clarity. Your clarity is your strength.",
    female_expression="You are a magnetic awakener, uplifting others through creative vision. Your creativity is your gift.",
    other_expression="You are a channel of insight, living freely, learning quickly, and adapting gracefully. Your insight is your guide."
)

# Jupiter Square Uranus
jupiter_square_uranus = JupiterUranusAspectInterpretation(
    aspect="Square",
    hook="Your growth is electric, but stability is a moving target.",
    core_interpretation="This square creates tension between your need for expansion and your craving for disruption. You want to leap into the future but sometimes forget to lay the groundwork. While your ideas are brilliant, your impulsiveness or impatience can lead to rebellion for its own sake. Embrace your radical originality and big picture foresight, learning to pace your breakthroughs and commit to long term growth.",
    male_expression="You are a wild learner, challenging norms with restless energy. Your energy is your strength, but balance is key.",
    female_expression="You are an explosive reformer, turning frustration into vision. Your vision is your guide to transformation.",
    other_expression="You are a bold disruptor, dancing between chaos and creation. Your boldness is your path to innovation."
)

# Jupiter Opposition Uranus
jupiter_opposition_uranus = JupiterUranusAspectInterpretation(
    aspect="Opposition",
    hook="Your vision and your freedom wrestle until something wild and wise emerges.",
    core_interpretation="This aspect reflects a constant negotiation between the need to believe and the urge to break free. You may swing between extreme optimism and sudden rebellion, making consistency a challenge. Still, your unconventional spirit makes you a magnet for growth and transformation. Embrace your role as a daring force for truth, with the power to challenge stagnant systems and inspire collective awakening.",
    male_expression="You are a rebellious believer, testing limits to evolve belief. Your rebellion is your strength, leading to profound insights.",
    female_expression="You are a freedom seeking idealist, exploring life by walking the uncharted. Your idealism is your guide to new horizons.",
    other_expression="You are a radical thinker, stretching beyond norms to create new truths. Your radicalism is your path to enlightenment."
)

# Create a dictionary to store all Jupiter Uranus aspect interpretations
jupiter_uranus_aspects = {
    "Conjunction": jupiter_conjunction_uranus,
    "Sextile": jupiter_sextile_uranus,
    "Trine": jupiter_trine_uranus,
    "Square": jupiter_square_uranus,
    "Opposition": jupiter_opposition_uranus
}
