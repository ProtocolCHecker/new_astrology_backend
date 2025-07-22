class UranusMarsAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
uranus_mars_conj = UranusMarsAspectInterpretation(
    aspect="Conjunction",
    hook="You move like a spark ready to ignite.",
    core_interpretation="Your energy is intense, unpredictable, and bold and you act on instinct and often shake things up without meaning to. When you learn to direct that fire, you become unstoppable, but without focus, you may burn through situations too fast.",
    male_expression="You act fast and live on impulse, often surprising even yourself. With just a bit more pause, your boldness can become a true superpower.",
    female_expression="You're electric in motion and people feel your presence and intensity. The challenge is learning when to unleash your force and when to hold steady.",
    other_expression="You carry a kind of wild momentum, like you were born to stir change into action. Learning control doesn't dull your power and it helps you wield it."
)

# Sextile
uranus_mars_sextile = UranusMarsAspectInterpretation(
    aspect="Sextile",
    hook="Your instincts know when to strike.",
    core_interpretation="You combine courage with creativity in a way that makes your actions feel natural, yet refreshing. You're quick to respond to opportunity, and your bravery often opens doors not just for you, but for others too.",
    male_expression="You act with a kind of casual brilliance, finding smart shortcuts and creative ways forward. People trust your sense of timing and vision.",
    female_expression="Your strength comes wrapped in originality and you move with purpose but never predictably. Others admire how naturally you handle change.",
    other_expression="You energize your environment by acting with inspiration rather than force. You don't just react and you innovate, often without even trying."
)

# Trine
uranus_mars_trine = UranusMarsAspectInterpretation(
    aspect="Trine",
    hook="You turn action into art.",
    core_interpretation="You take bold steps without hesitation, and somehow it just works. Your way of acting is so aligned with your inner truth that breakthroughs feel less like struggle and more like rhythm.",
    male_expression="You're a natural trailblazer, often ahead of your time but never out of place. People follow your lead because it just makes sense.",
    female_expression="You're quietly daring and your courage flows with such grace that people don't realize how bold you truly are. Change doesn't scare you and it energizes you.",
    other_expression="You're at your best when moving forward. Action feels aligned, smooth, and full of purpose, even when it breaks the mold."
)

# Square
uranus_mars_square = UranusMarsAspectInterpretation(
    aspect="Square",
    hook="You're wired for breakthroughs and but not without friction.",
    core_interpretation="You often feel like you're about to explode from within, especially when you're told to wait, slow down, or follow rules that don't make sense. Your challenge is learning how to use your force without letting it use you.",
    male_expression="You act fast, think faster, and can get frustrated with anything that feels like a block. Your true strength lies in learning how to channel your fire without letting it burn bridges.",
    female_expression="You're fierce, impulsive, and full of creative tension and it can be overwhelming, but it's also your edge. Mastering timing is your path to power.",
    other_expression="You move between chaos and clarity, often disrupting things before you even realize it. But your tension is fuel and when aimed wisely, it creates lasting change."
)

# Opposition
uranus_mars_opp = UranusMarsAspectInterpretation(
    aspect="Opposition",
    hook="Your power gets tested through others.",
    core_interpretation="You attract situations and and people and that push your buttons and challenge your need for freedom. Conflict isn't always a setback here; sometimes it's exactly what shows you what you're truly capable of.",
    male_expression="You're not afraid of confrontation, but it often mirrors something deeper you're trying to resolve. Real strength comes when you stop reacting and start choosing.",
    female_expression="You meet powerful energy through others and whether in passion or in challenge. It's in those moments of contrast that you rise to your most empowered self.",
    other_expression="You evolve through tension in relationships and situations that test your limits. These moments aren't roadblocks and they're wake up calls that spark your next leap."
)

# Store all Uranus–Mars aspect interpretations
uranus_mars_aspects = {
    "Conjunction": uranus_mars_conj,
    "Sextile": uranus_mars_sextile,
    "Trine": uranus_mars_trine,
    "Square": uranus_mars_square,
    "Opposition": uranus_mars_opp
}
