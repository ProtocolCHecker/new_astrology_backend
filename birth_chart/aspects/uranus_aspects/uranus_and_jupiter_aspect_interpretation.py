class UranusJupiterAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
uranus_jupiter_conj = UranusJupiterAspectInterpretation(
    aspect="Conjunction",
    hook="You think big and and differently.",
    core_interpretation="You're driven by bold visions and flashes of insight that can completely shift your worldview. You're not here to follow traditional paths and you're here to build your own, fueled by a belief that things really can be better.",
    male_expression="You bring revolution to your beliefs, constantly questioning limits and pushing toward what feels freer and more expansive. Others may not always keep up, but you don't wait for permission.",
    female_expression="Your optimism feels electric, and your ideas often arrive ahead of their time. You're not afraid to break old rules if it means living with more meaning and freedom.",
    other_expression="You dream of change on a big scale, with a spirit that challenges outdated thinking. Your growth comes through following your excitement and even when it surprises others."
)

# Sextile
uranus_jupiter_sextile = UranusJupiterAspectInterpretation(
    aspect="Sextile",
    hook="Your ideas open doors and for you and for others.",
    core_interpretation="You blend imagination and wisdom in a way that leads to steady breakthroughs. You're able to bring new ideas into the world without needing to shock or force them, often inspiring people with your vision for a better future.",
    male_expression="You challenge yourself to grow through curiosity rather than rebellion. Your strength lies in exploring new perspectives without needing to burn the old ones down.",
    female_expression="You bring change with warmth, offering new ways of thinking that uplift rather than divide. People feel safe exploring new territory with you.",
    other_expression="You have a rare ability to turn big ideas into real possibilities. Your influence comes from your openness and your willingness to explore without judgment."
)

# Trine
uranus_jupiter_trine = UranusJupiterAspectInterpretation(
    aspect="Trine",
    hook="You move forward with effortless insight.",
    core_interpretation="Your personal growth feels guided by a deep, intuitive wisdom that seems to know when it's time to leap. You often find yourself in the right place at the right time and because you trust your instincts and welcome what's new.",
    male_expression="You have a natural confidence in your big ideas, and life tends to reward you for trusting them. People admire your easy relationship with change.",
    female_expression="You expand with grace, never forcing your evolution but always moving toward more freedom. Your beliefs lift you, and others, higher.",
    other_expression="You're someone who thrives on progress without pressure. Your growth feels organic, like the universe itself is quietly opening the door for you."
)

# Square
uranus_jupiter_square = UranusJupiterAspectInterpretation(
    aspect="Square",
    hook="Your biggest leaps come through inner tension.",
    core_interpretation="You're constantly pushing against beliefs that feel too tight, and that pressure often drives you to discover more liberating ways of living. The key is learning to follow your vision without becoming rigid in your rebellion.",
    male_expression="You may wrestle with extreme ideals, sometimes leaping before you look. But that restlessness is also what leads to your most powerful growth.",
    female_expression="You've likely felt the friction between being hopeful and being realistic and but this tension is where your transformation lives. It forces you to evolve faster than most.",
    other_expression="You often feel like you're at war with old ways of thinking and even your own. But each challenge is a step toward a more honest and liberated version of you."
)

# Opposition
uranus_jupiter_opp = UranusJupiterAspectInterpretation(
    aspect="Opposition",
    hook="Others challenge your view and and unlock your growth.",
    core_interpretation="You grow the most when you're confronted with different beliefs and ways of thinking. These moments stretch you, showing that freedom doesn't always mean going solo and it can also come from listening and evolving together.",
    male_expression="You attract strong thinkers who test your ideals, and through them, you sharpen your own. Your expansion happens through exchange, not isolation.",
    female_expression="You often meet people who reflect back what you're trying to grow beyond and and that reflection helps you evolve. You find your truth through contrast.",
    other_expression="You're here to bridge differences and make peace with paradox. Your beliefs are always in motion, shaped by the people who challenge and expand them."
)

# Store all Uranus–Jupiter aspect interpretations
uranus_jupiter_aspects = {
    "Conjunction": uranus_jupiter_conj,
    "Sextile": uranus_jupiter_sextile,
    "Trine": uranus_jupiter_trine,
    "Square": uranus_jupiter_square,
    "Opposition": uranus_jupiter_opp
}
