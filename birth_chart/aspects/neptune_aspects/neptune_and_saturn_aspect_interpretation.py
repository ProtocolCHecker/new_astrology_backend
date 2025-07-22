class NeptuneSaturnAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
neptune_saturn_conj = NeptuneSaturnAspectInterpretation(
    aspect="Conjunction",
    hook="You dream with discipline and carry visions that want to be built.",
    core_interpretation="You carry both longing and structure inside you. You're here to give shape to the invisible, to build what others only imagine. When doubt rises, it's your inner faith that holds you steady.",
    male_expression="You're a grounded visionary. You build carefully, with quiet purpose, and your strength grows when your ideals are practiced, not just imagined.",
    female_expression="You bring softness to structure. You shape dreams into something others can touch, and your power deepens as you stay connected to your inner truth.",
    other_expression="You are a sacred builder. The things you imagine aren't fleeting and they're waiting for your hands to give them form."
)

# Sextile
neptune_saturn_sextile = NeptuneSaturnAspectInterpretation(
    aspect="Sextile",
    hook="You bring the unseen into form with steady grace.",
    core_interpretation="You have a gentle talent for blending your ideals with what's real. Your creativity is quiet but focused, and you have a gift for turning imagination into something meaningful and lasting.",
    male_expression="You lead with softness and strength. People trust you because your compassion comes with consistency.",
    female_expression="You carry your purpose like a lantern. You move through life with heart and hands aligned.",
    other_expression="You harmonize care with structure. Your presence creates space for things to become real and beautiful at the same time."
)

# Trine
neptune_saturn_trine = NeptuneSaturnAspectInterpretation(
    aspect="Trine",
    hook="You move like a dream with roots. Calm, grounded, and full of quiet power.",
    core_interpretation="You hold a natural flow between what you imagine and what you create. There's a grace to how you work and an ease that helps others feel safe while you build something meaningful and true.",
    male_expression="You create with confidence and calm. Your stability feels soft, and your ideas carry weight without needing force.",
    female_expression="You are grace in motion. You carry your truth with subtle power, and your life becomes a sanctuary for what matters most.",
    other_expression="You live as a bridge between longing and reality. The world softens in your presence and begins to take shape."
)

# Square
neptune_saturn_square = NeptuneSaturnAspectInterpretation(
    aspect="Square",
    hook="You wrestle with dreams that resist form but refuse to leave you.",
    core_interpretation="Part of you longs to surrender while another part insists on control. This inner tension teaches you to stay with the discomfort of uncertainty, and eventually, to find steady ground in what you believe and especially when no one else sees it yet.",
    male_expression="You build in the fog. Your doubts have shaped your strength, and every time you try again, you learn something real about faith.",
    female_expression="You rise from contradiction. Even when the world feels unclear, you move forward with a courage that comes from feeling deeply.",
    other_expression="You're a sculptor of uncertainty. In the tension between real and imagined, you find the shape of your truth."
)

# Opposition
neptune_saturn_opp = NeptuneSaturnAspectInterpretation(
    aspect="Opposition",
    hook="You stand between what is and what could be, pulled by both and shaped by the space between.",
    core_interpretation="Life pulls you between surrender and responsibility, between trust and structure. In relationships and choices, you're asked again and again to hold that tension. And over time, you learn how to stay rooted without losing your softness.",
    male_expression="You walk a narrow path between control and letting go. Your growth comes through learning which is needed, and when.",
    female_expression="You hold the paradox with grace. You're learning to feel safe in your vision, even when the ground shifts.",
    other_expression="You are a mirror between form and feeling. The more you honor both, the more you discover your unique way of shaping the world."
)

neptune_saturn_aspects = {
    "Conjunction": neptune_saturn_conj,
    "Sextile": neptune_saturn_sextile,
    "Trine": neptune_saturn_trine,
    "Square": neptune_saturn_square,
    "Opposition": neptune_saturn_opp
}
