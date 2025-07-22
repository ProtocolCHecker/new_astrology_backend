class MercurySaturnAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunct
mercury_conjunct_saturn = MercurySaturnAspectInterpretation(
    aspect="Conjunct",
    hook="You speak slowly, but you mean every word. Built from truth, tested by time.",
    core_interpretation="This disciplined mental alignment gives you a structured approach to thinking. Trusting your voice while softening self-criticism lets your wisdom shine.",
    male_expression="You deliberate with care. Releasing doubt frees your natural authority.",
    female_expression="Your precision is profound. Allowing imperfection opens your connection.",
    other_expression="You are a mental architect. Owning each phrase makes your ideas endure."
)

# Sextile
mercury_sextile_saturn = MercurySaturnAspectInterpretation(
    aspect="Sextile",
    hook="Your thoughts build bridges. Sturdy, steady, and meant to last.",
    core_interpretation="This harmonious connection makes you a reliable communicator and planner. Pairing structure with flexibility ensures your strategies thrive.",
    male_expression="You speak with quiet confidence. Embracing spontaneity sparks innovation.",
    female_expression="Your clarity guides others. Inviting new perspectives enriches your framework.",
    other_expression="You construct ideas with care. Balancing order and openness fuels success."
)

# Trine
mercury_trine_saturn = MercurySaturnAspectInterpretation(
    aspect="Trine",
    hook="Your mind is a compass. Aligned with reason, guided by principle.",
    core_interpretation="This flowing aspect blesses you with seamless logic and calm expression. Stretching boundaries with new challenges amplifies your growth.",
    male_expression="You embody steady insight. Occasionally shaking things up renews your edge.",
    female_expression="Your wisdom resonates. Embracing fresh ideas deepens your mastery.",
    other_expression="You are a silent pillar. Welcoming change ensures your legacy."
)

# Square
mercury_square_saturn = MercurySaturnAspectInterpretation(
    aspect="Square",
    hook="Your words weigh heavy. You measure every phrase and still doubt.",
    core_interpretation="This challenging aspect stirs self-critique and hesitation. Releasing perfectionism and speaking your truth empowers both you and your listeners.",
    male_expression="You guard your voice. Letting vulnerability in strengthens trust.",
    female_expression="Your caution protects. Stepping into flow invites authenticity.",
    other_expression="You grow by claiming mental space. Bold speech builds confidence."
)

# Opposition
mercury_opposite_saturn = MercurySaturnAspectInterpretation(
    aspect="Opposition",
    hook="Your mind echoes with caution. Torn between truth and silence.",
    core_interpretation="This polar aspect highlights tension between speaking and withholding. Trusting your worth and practicing honest expression turns blocks into bridges.",
    male_expression="You pause before you speak. Embracing flow amplifies your message.",
    female_expression="Your restraint guards you. Allowing vulnerability deepens connection.",
    other_expression="You balance caution with courage. Your strongest voice emerges through openness."
)

mercury_saturn_aspects = {
    "Conjunct": mercury_conjunct_saturn,
    "Sextile": mercury_sextile_saturn,
    "Trine": mercury_trine_saturn,
    "Square": mercury_square_saturn,
    "Opposition": mercury_opposite_saturn
}