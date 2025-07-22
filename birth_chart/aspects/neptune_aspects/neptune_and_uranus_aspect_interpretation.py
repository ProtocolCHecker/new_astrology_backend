class NeptuneUranusAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
neptune_uranus_conj = NeptuneUranusAspectInterpretation(
    aspect="Conjunction",
    hook="Your mind rides wild waves and innovation flows through imagination.",
    core_interpretation="You spark fresh ideas instinctively and people feel energized by you. Grounding each flash with a small plan helps your creativity last.",
    male_expression="Your inventive spark amazes everyone. Writing down one action step turns dreams into reality.",
    female_expression="Your original thoughts feel magical to many. Mapping out a quick outline brings them into focus.",
    other_expression="Your visionary energy leads change naturally. A simple routine sustains your inspiration."
)

# Sextile
neptune_uranus_sextile = NeptuneUranusAspectInterpretation(
    aspect="Sextile",
    hook="Your thoughts dance with innovation and intuition meets progress.",
    core_interpretation="You mix creativity and logic smoothly, and people trust your fresh perspective. Jotting a quick note for each idea keeps them from slipping away.",
    male_expression="Your clever insights spark curiosity in others. A short new idea list helps you build on each thought.",
    female_expression="Your bright concepts open minds instantly. A quick sketch or outline makes your vision clear.",
    other_expression="Your creative flow uplifts every room. Capturing each spark in a few words gives it staying power."
)

# Trine
neptune_uranus_trine = NeptuneUranusAspectInterpretation(
    aspect="Trine",
    hook="Your soul hums in creative sync and genius feels effortless.",
    core_interpretation="You access unique insights with ease and people follow your lead. Turning those insights into small routines keeps your gifts active.",
    male_expression="Your natural innovation inspires trust. Blocking out time each day for brainstorming brings your ideas to life.",
    female_expression="Your flow of ideas feels intuitive and right. Dedicating a few minutes to refine each thought keeps you grounded.",
    other_expression="Your inspired mind guides change. Linking vision to action makes your creativity real."
)

# Square
neptune_uranus_square = NeptuneUranusAspectInterpretation(
    aspect="Square",
    hook="Your vision jolts against routine and tension births new paths.",
    core_interpretation="You challenge norms fearlessly, and that clash makes you grow. Stepping back for a moment of calm turns disruption into purposeful change.",
    male_expression="Your boundary breaking ideas thrill people. A brief breathing break refocuses your energy.",
    female_expression="Your rebellious creativity excites and surprises. A short grounding ritual restores your balance.",
    other_expression="Your inventive tension fuels progress. Pausing and reflecting channels your spark effectively."
)

# Opposition
neptune_uranus_opp = NeptuneUranusAspectInterpretation(
    aspect="Opposition",
    hook="Your ideals and reality play tug of war and harmony reveals your vision.",
    core_interpretation="You switch between big dreams and daily needs, and blending both creates real magic. Checking in with someone you trust keeps you balanced.",
    male_expression="Your futuristic outlook inspires others, but pairing it with clear tasks keeps you moving forward. Asking a friend for feedback makes your plan stronger.",
    female_expression="Your vision feels grand and freeing, yet practical steps turn it into reality. Sharing your ideas ensures they're grounded.",
    other_expression="Your dual perspective guides you deeply. Talking it through helps merge dream and detail."
)

neptune_uranus_aspects = {
    "Conjunction": neptune_uranus_conj,
    "Sextile": neptune_uranus_sextile,
    "Trine": neptune_uranus_trine,
    "Square": neptune_uranus_square,
    "Opposition": neptune_uranus_opp
}
