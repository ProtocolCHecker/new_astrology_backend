class MarsAscendantAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
mars_conjunct_asc = MarsAscendantAspectInterpretation(
    aspect="Conjunct",
    hook="You show up ready, bold and unapologetically driven.",
    core_interpretation="With Mars conjunct your Ascendant, you come across as assertive, action oriented, and hard to ignore. Your presence is strong, and people feel your willpower before you speak. Whether you express it openly or more subtly, there's a fire that drives you to take charge. Learning when to engage and when to hold your fire helps you lead with presence rather than pressure.",
    male_expression="You act first and ask later and a natural force. Leadership deepens when you master calm as well as courage.",
    female_expression="You lead with boldness and raw energy. When balanced with listening, your strength becomes magnetic.",
    other_expression="Your energy enters the room before your words. You're here to act, just make sure it's not reaction over intention."
)

# Sextile
mars_sextile_asc = MarsAscendantAspectInterpretation(
    aspect="Sextile",
    hook="You move with purpose, assertive but rarely aggressive.",
    core_interpretation="Mars sextile your Ascendant gives you initiative without force, making your drive feel accessible and collaborative. You know how to assert yourself while keeping others at ease and a rare blend of courage and emotional intelligence. People often see you as capable and active, but never overbearing. You lead by example, not domination.",
    male_expression="You're self directed and composed and action flows naturally from confidence, not ego.",
    female_expression="You mix vitality with grace, knowing when to lead and when to inspire. Strength shows in your softness.",
    other_expression="You energize others just by being in motion. Your balanced push helps things move without resistance."
)

# Trine
mars_trine_asc = MarsAscendantAspectInterpretation(
    aspect="Trine",
    hook="You act with ease and your confidence feels natural and true.",
    core_interpretation="With Mars trine your Ascendant, you blend strength and poise in a way that feels effortless. Your actions are often well timed, self assured, and aligned with your identity. You don't need to shout to be heard — people follow your lead because your energy speaks for you. This is quiet power, and it grows when you trust your instincts fully.",
    male_expression="You move like you belong in confidence, calm, and grounded. Others trust your direction.",
    female_expression="You embody presence and assertive without force, strong without harshness. That balance makes you luminous.",
    other_expression="Your actions and identity speak the same language. You don't force momentum and you become it."
)

# Square
mars_square_asc = MarsAscendantAspectInterpretation(
    aspect="Square",
    hook="You face the world head on fierce, fast, and sometimes too raw.",
    core_interpretation="Mars square your Ascendant stirs up inner tension that shows up in how you assert yourself. You're passionate and quick to act, but that same fire can come off as abrupt, aggressive, or misunderstood. The growth here is learning how to own your power without letting it push people away. Once you tame your edge, your drive becomes a powerful tool for focused impact.",
    male_expression="You burn hot and quick to move, quick to clash. Maturity comes when you match force with clarity.",
    female_expression="You lead with intensity and passion, but may feel misread. Real strength comes when you act from centered truth, not reaction.",
    other_expression="You're here to stir momentum, not chaos. When you bring awareness to your impact, your fire becomes transformative."
)

# Opposition
mars_opposite_asc = MarsAscendantAspectInterpretation(
    aspect="Opposition",
    hook="You find your fire through others and challenge teaches you who you are.",
    core_interpretation="With Mars opposite your Ascendant, you're wired to encounter strong personalities that activate your drive or defensiveness. You may attract conflict or competition without meaning to, until you learn to own your assertiveness directly. Relationships become mirrors where you either project your power or learn to integrate it consciously. The goal is learning how to meet others with strength and without making every encounter a battleground.",
    male_expression="You often define yourself in contrast and shaped by challenge. Power grows when you stop giving it away or pushing it outward.",
    female_expression="You meet bold energy in others because it lives in you too. When you claim it, relationships shift from conflict to co creation.",
    other_expression="Your growth comes from friction and learning to assert, not attack. Real strength lives in honest self ownership."
)

# Dictionary of Mars–Ascendant aspect interpretations
mars_ascendant_aspects = {
    "Conjunct": mars_conjunct_asc,
    "Sextile": mars_sextile_asc,
    "Trine": mars_trine_asc,
    "Square": mars_square_asc,
    "Opposition": mars_opposite_asc
}
