class UranusPlutoAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
uranus_pluto_conj = UranusPlutoAspectInterpretation(
    aspect="Conjunction",
    hook="You're built for deep disruption.",
    core_interpretation="You're wired for transformation that doesn't just touch the surface and it rewrites you from the inside out. Change doesn't scare you because, on some level, you know you came here to create it.",
    male_expression="You carry a force that shakes structures and starting with your own. Your power lies in embracing the breakdown as the beginning of something truer.",
    female_expression="You evolve through cycles of intense personal growth, often driven by an instinct to break what no longer serves. Your healing becomes a roadmap for others.",
    other_expression="You're a catalyst, even when you don't mean to be. Your presence alone often signals that something is about to shift and for the better, through the fire."
)

# Sextile
uranus_pluto_sextile = UranusPlutoAspectInterpretation(
    aspect="Sextile",
    hook="You upgrade from the inside, quietly but powerfully.",
    core_interpretation="You bring transformation with intention, not chaos and shifting patterns in a way that feels precise and deeply grounded. Your strength is knowing when to act and how to pivot without losing control.",
    male_expression="You know how to innovate without shocking the system. You rebuild with strategy and purpose, making you quietly influential.",
    female_expression="You change from the roots up, often without others noticing until everything is different. Your process is intuitive, your power is subtle but real.",
    other_expression="You work best behind the scenes of transformation and less flash, more depth. You change the game not by force, but by design."
)

# Trine
uranus_pluto_trine = UranusPlutoAspectInterpretation(
    aspect="Trine",
    hook="You evolve with grace and gravity.",
    core_interpretation="Transformation flows through you in a natural rhythm, helping you navigate change with both vision and strength. You have a way of turning personal evolution into quiet leadership.",
    male_expression="You inspire change not by demanding it, but by living it. People sense your depth and trust your direction.",
    female_expression="You carry power with calm and your shifts are deep, but they never feel forced. You make transformation look like a natural part of life.",
    other_expression="You don't just adapt and you refine. Your evolution is steady, your growth feels inevitable, and others often follow your lead without even realizing it."
)

# Square
uranus_pluto_square = UranusPlutoAspectInterpretation(
    aspect="Square",
    hook="You grow through collision, not comfort.",
    core_interpretation="You're built to break through walls and especially the ones you didn't know were there. Your inner tension may feel overwhelming at times, but it's what fuels your most powerful transformations.",
    male_expression="You've been tested by change that felt more like crisis and but each storm taught you how to rebuild stronger. Your resilience is your revolution.",
    female_expression="You carry intensity in your soul, and it doesn't always come gently. But you're learning how to harness that fire and use it to create something lasting.",
    other_expression="You've had to burn parts of yourself down to find what's real. That journey hasn't been easy, but it's made you someone who cannot be shaken."
)

# Opposition
uranus_pluto_opp = UranusPlutoAspectInterpretation(
    aspect="Opposition",
    hook="Your evolution plays out in high contrast.",
    core_interpretation="You often meet external forces that challenge your inner power, pulling you between the need to break free and the pull of what holds you together. The lesson is learning to create change without destroying your own center.",
    male_expression="You see your own strength most clearly through conflict and especially when someone else pushes your limits. Growth means learning to build instead of just breaking.",
    female_expression="You attract experiences that test your power. It's through facing them that you learn how to hold your ground and own your transformation.",
    other_expression="You evolve through contrast and through the push pull between freedom and control. Your greatest breakthroughs come when you find your own rhythm between the two."
)

# Store all Uranus–Pluto aspect interpretations
uranus_pluto_aspects = {
    "Conjunction": uranus_pluto_conj,
    "Sextile": uranus_pluto_sextile,
    "Trine": uranus_pluto_trine,
    "Square": uranus_pluto_square,
    "Opposition": uranus_pluto_opp
}
