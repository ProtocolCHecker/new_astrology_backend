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
    hook="You feel with fire and passion is your first language.",
    core_interpretation="Your emotions are bold, immediate, and hard to hide. You react with intensity and often act before thinking, not because you lack depth, but because your feelings move fast. You're fiercely protective and full of desire, but your growth comes from learning how to channel that emotional fire without burning yourself or others.",
    male_expression="You're instinctive and passionate, always ready to protect or pursue. Softening your reactions deepens your strength.",
    female_expression="You express love and anger with equal honesty, direct, intense, and real. Nuance helps you stay powerful without overwhelm.",
    other_expression="You live emotionally in motion. Your courage is raw and it evolves when you pause before you leap."
)

# Sextile
moon_mars_sextile = MoonMarsAspectInterpretation(
    aspect="Sextile",
    hook="You feel it, you move and emotion flows into action with purpose.",
    core_interpretation="You have a healthy and natural link between what you feel and what you do. You're passionate without being reckless, responsive without being reactive. You express emotion with clarity and act on your instincts in constructive ways, making you both engaging and emotionally effective.",
    male_expression="You're warm and action oriented, emotional but grounded. People feel your sincerity and drive.",
    female_expression="You respond quickly and with care and your emotions have a spark, not a sting.",
    other_expression="You live close to your instincts and trust your feelings. Others feel safe in your passion because it's focused, not forced."
)

# Trine
moon_mars_trine = MoonMarsAspectInterpretation(
    aspect="Trine",
    hook="You move from the heart and passion flows through you with ease.",
    core_interpretation="With Moon trine Mars, your emotional life and willpower support each other naturally. You act on your feelings with confidence and grace, rarely second guessing yourself. Others see you as emotionally strong, passionate, and smooth under pressure. This aspect gives you inner balance and your fire rarely burns out of control.",
    male_expression="You're grounded and magnetic, leading with heart and decisiveness. People trust your calm fire.",
    female_expression="You radiate courage and compassion and acting with warmth and purpose. Emotion becomes your strength.",
    other_expression="Your instincts are steady and your reactions graceful. Passion, for you, is a steady current and not a storm."
)

# Square
moon_mars_square = MoonMarsAspectInterpretation(
    aspect="Square",
    hook="You feel like a storm, bold, fast, and hard to hold back.",
    core_interpretation="With Moon square Mars, your emotions are powerful but often volatile. You may react before understanding your own feelings, leading to conflict or impulsive choices. You care deeply and want to make an impact and but the challenge is slowing down enough to respond rather than explode. With self awareness, your fire becomes focused, not flammable.",
    male_expression="You're intense and expressive, but your emotions often run ahead of your clarity. Strength grows when you pause to reflect.",
    female_expression="You love hard and fight harder, but inner peace comes when you stop defending every feeling.",
    other_expression="You're driven by emotion, and that can either fuel growth or chaos. Your edge sharpens when you learn to aim before you strike."
)

# Opposition
moon_mars_opp = MoonMarsAspectInterpretation(
    aspect="Opposition",
    hook="You wrestle between tenderness and tension, the heart wants calm, the will wants fire.",
    core_interpretation="You're often pulled between emotional sensitivity and assertive action. You may find that relationships stir up emotional intensity or that you're drawn to people who mirror your inner fire. Conflict becomes a mirror, showing you what you haven't yet owned in yourself. Growth comes when you stop projecting your passion and learn to express it with clarity and compassion.",
    male_expression="You're passionate and intense, often feeling torn between protecting and provoking. Real power comes from self honesty.",
    female_expression="You feel deeply but may fight to be heard or understood. Peace comes when you claim your feelings without turning them into a battle.",
    other_expression="You grow through contrast between reaction and reflection. Your strength shows when you lead with emotion, not through it."
)

# Store all in a dictionary
moon_mars_aspects = {
    "Conjunction": moon_mars_conj,
    "Sextile": moon_mars_sextile,
    "Trine": moon_mars_trine,
    "Square": moon_mars_square,
    "Opposition": moon_mars_opp
}
