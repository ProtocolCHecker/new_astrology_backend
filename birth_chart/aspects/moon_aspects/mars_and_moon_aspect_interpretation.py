class MoonMarsAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
moon_mars_conj = MoonMarsAspectInterpretation(
    aspect="Conjunction",
    hook="Your feelings ignite and passion pulses through you.",
    core_interpretation="You act from the heart with fearless energy, and learning patience will make that drive a lasting gift.",
    male_expression="You defend what you love with bold courage and softening your reactions helps you connect deeper.",
    female_expression="Your fierce passion inspires those around you and tempering intensity with tenderness brings harmony.",
    other_expression="Your raw enthusiasm lights up every room and balancing it with calm creates true power."
)

# Sextile
moon_mars_sextile = MoonMarsAspectInterpretation(
    aspect="Sextile",
    hook="Your emotions move with purpose and you feel, then you act.",
    core_interpretation="You channel energy into nurturing action, making you a natural motivator and friend.",
    male_expression="Your warmth drives decisive care and pausing to reflect heightens your impact.",
    female_expression="Your spirited response feels genuine and mixing that with gentle listening strengthens bonds.",
    other_expression="Your intuitive action comforts,excites and balancing feeling with thought fuels your best work."
)

# Trine
moon_mars_trine = MoonMarsAspectInterpretation(
    aspect="Trine",
    hook="Your passion flows effortlessly and strength and sensitivity unite.",
    core_interpretation="You blend courage with compassion so naturally that people trust your lead; inviting others' ideas keeps your spark alive.",
    male_expression="Your confident kindness feels inspiring and embracing new perspectives keeps you fresh.",
    female_expression="Your inner fire warms every interaction and welcoming feedback enriches your journey.",
    other_expression="Your balanced zeal uplifts everyone and sharing responsibility magnifies your flame."
)

# Square
moon_mars_square = MoonMarsAspectInterpretation(
    aspect="Square",
    hook="Your heart and will clash and you learn through the friction.",
    core_interpretation="You feel intensely and sometimes act too quickly, but each pause you take builds stronger self control.",
    male_expression="Your bold reactions can startle, yet every breath you take teaches you calm resilience.",
    female_expression="Your vibrant energy moves mountains and slowing down reveals new paths.",
    other_expression="Your stormy drive forges deep strength and gentle pauses sharpen your aim."
)

# Opposition
moon_mars_opp = MoonMarsAspectInterpretation(
    aspect="Opposition",
    hook="Your desire and need wrestle and balance is your battleground.",
    core_interpretation="You're pulled between comfort and action, and finding middle ground turns conflict into growth.",
    male_expression="Your assertive heart needs a partner to reflect your care; harmony emerges through shared effort.",
    female_expression="Your protective spirit thrives when you honor both giving and receiving; that duality becomes your strength.",
    other_expression="Your dynamic tension guides you and integrating stillness and motion reveals your power."
)

moon_mars_aspects = {
    "Conjunction": moon_mars_conj,
    "Sextile": moon_mars_sextile,
    "Trine": moon_mars_trine,
    "Square": moon_mars_square,
    "Opposition": moon_mars_opp
}
