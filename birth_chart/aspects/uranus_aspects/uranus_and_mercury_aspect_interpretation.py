class UranusMercuryAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
uranus_mercury_conj = UranusMercuryAspectInterpretation(
    aspect="Conjunction",
    hook="Your mind moves like lightning.",
    core_interpretation="Your thoughts come in flashes and fast, unexpected, and often brilliant. You think differently by nature, and while that's a gift, your challenge is learning to organize your insights before acting on them.",
    male_expression="You generate ideas at a speed most people can't follow. If you give your thoughts structure, they can truly revolutionize the way others think too.",
    female_expression="You bring original insights that feel electrifying, but staying grounded helps others actually receive your message. When you focus, your genius becomes transformative.",
    other_expression="You have a rare mental spark that sees patterns others miss. Your growth comes when you learn to pace your expression without dimming your brilliance."
)

# Sextile
uranus_mercury_sextile = UranusMercuryAspectInterpretation(
    aspect="Sextile",
    hook="You think differently and and make it sound easy.",
    core_interpretation="Your ideas are inventive and fresh, and you share them in ways that others can understand and appreciate. You blend originality with clarity, often becoming a bridge between the future and the present.",
    male_expression="You're someone who drops unexpected wisdom into everyday conversation. People listen because what you say just makes sense and even when it's way ahead of its time.",
    female_expression="You bring out new ways of thinking with charm and fluidity. Others feel inspired and empowered by the way you share your thoughts.",
    other_expression="Your brilliance doesn't shout and it flows. You help others see things from a new angle without needing to force the change."
)

# Trine
uranus_mercury_trine = UranusMercuryAspectInterpretation(
    aspect="Trine",
    hook="Your mind flows with genius.",
    core_interpretation="You naturally blend logic with intuition, creating ideas that are both smart and inspiring. You often say exactly what needs to be heard, without even realizing the impact you have.",
    male_expression="You speak from a place of clarity and insight, and your ideas ripple out in ways that spark change. Your intelligence feels effortless, but it runs deep.",
    female_expression="You express complex thoughts in ways that feel graceful and clear. You may not even notice how often others look to you for a fresh perspective.",
    other_expression="Your way of thinking is fluid, future minded, and surprisingly relatable. You uplift conversations just by bringing your true thoughts forward."
)

# Square
uranus_mercury_square = UranusMercuryAspectInterpretation(
    aspect="Square",
    hook="Your thoughts never stop and but neither does the pressure.",
    core_interpretation="Your mind is intense and fast, often filled with ideas that seem to clash with how others think. That friction can spark genius, but only when you slow down enough to turn your chaos into clarity.",
    male_expression="You speak your mind with force, sometimes before the thought is fully formed. Your power comes when you learn to filter without silencing your truth.",
    female_expression="Your ideas race and your voice can carry a charge and sometimes too strong, sometimes just right. You're learning how to express your mind without burning out.",
    other_expression="You often feel torn between wanting to express your ideas and fearing they'll be misunderstood. But when you learn to center yourself, your voice becomes unforgettable."
)

# Opposition
uranus_mercury_opp = UranusMercuryAspectInterpretation(
    aspect="Opposition",
    hook="Others light up your thinking.",
    core_interpretation="You learn the most through dynamic conversations and clashes of perspective. Sometimes you resist what others say, but often those moments reveal the most about your own way of thinking.",
    male_expression="You attract mental opposites and people who challenge and stretch your thoughts. If you listen as much as you speak, your ideas will grow even stronger.",
    female_expression="You reflect and react to the mental energy of others. When you're open to dialogue, your insights become even more impactful.",
    other_expression="You thrive in exchange and whether through conversation or confrontation. Your growth happens in moments when you allow your mind to stretch beyond your first instinct."
)

# Store all Uranus–Mercury aspect interpretations
uranus_mercury_aspects = {
    "Conjunction": uranus_mercury_conj,
    "Sextile": uranus_mercury_sextile,
    "Trine": uranus_mercury_trine,
    "Square": uranus_mercury_square,
    "Opposition": uranus_mercury_opp
}
