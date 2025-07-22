class NeptuneMarsAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
neptune_mars_conj = NeptuneMarsAspectInterpretation(
    aspect="Conjunction",
    hook="Your drive feels like a soft wave and action flows from feeling.",
    core_interpretation="You follow your heart when you act, making others feel cared for. Setting a clear goal helps your soft strength last through challenges.",
    male_expression="Your gentle energy motivates without force. Writing down one simple aim keeps you focused.",
    female_expression="Your caring actions inspire trust in others. Breaking tasks into steps helps you move forward.",
    other_expression="Your kind will opens doors softly. Linking purpose to small plans makes your spark endure."
)

# Sextile
neptune_mars_sextile = NeptuneMarsAspectInterpretation(
    aspect="Sextile",
    hook="Your energy flows like poetry and purpose and compassion entwine.",
    core_interpretation="You act with kindness and clear intent, making everything feel meaningful. Pairing that with a loose plan ensures your efforts have impact.",
    male_expression="Your caring drive lifts people up. Drafting a quick checklist gives your heart a roadmap.",
    female_expression="Your inspired actions feel natural and true. Noting a few priorities keeps your kindness on track.",
    other_expression="Your soulful movement guides you. A simple framework helps your gifts shine."
)

# Trine
neptune_mars_trine = NeptuneMarsAspectInterpretation(
    aspect="Trine",
    hook="Your actions feel like gentle tides and strength wrapped in softness.",
    core_interpretation="You lead with both heart and calm, and people trust your quiet confidence. Mapping out a few clear milestones makes your softness purposeful.",
    male_expression="Your composed courage draws others to follow. Setting small targets keeps your vision alive.",
    female_expression="Your warm assertiveness comforts and motivates. Defining a short list of goals boosts your impact.",
    other_expression="Your balanced will nurtures progress. Listing easy steps ensures you stay steady."
)

# Square
neptune_mars_square = NeptuneMarsAspectInterpretation(
    aspect="Square",
    hook="Your heart and action sometimes collide and tension shapes your path.",
    core_interpretation="You feel strongly and may act too quickly, but each pause teaches you control. A simple breathing break can turn confusion into clear energy.",
    male_expression="Your blazing compassion can lead to missteps. Pausing for a breath sharpens your next move.",
    female_expression="Your caring intensity pushes you forward. A short walk restores your balance and focus.",
    other_expression="Your fierce kindness forges strength. Gentle pauses refine your purpose."
)

# Opposition
neptune_mars_opp = NeptuneMarsAspectInterpretation(
    aspect="Opposition",
    hook="Your desire dances with your dream and finding rhythm reveals your power.",
    core_interpretation="You're pulled between fantasy and reality, and blending both creates inspired action. Checking in with a friend keeps you grounded.",
    male_expression="Your visionary drive excites people, but clear steps make it real. Asking someone for feedback keeps you honest.",
    female_expression="Your gentle passion inspires others, yet you need firm targets. Sharing your plan with a buddy helps you stay on course.",
    other_expression="Your dynamic vision guides you. Talking it through adds focus to your dreams."
)

neptune_mars_aspects = {
    "Conjunction": neptune_mars_conj,
    "Sextile": neptune_mars_sextile,
    "Trine": neptune_mars_trine,
    "Square": neptune_mars_square,
    "Opposition": neptune_mars_opp
}
