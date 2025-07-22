class MarsJupiterAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Mars Conjunct Jupiter
mars_jupiter_conj = MarsJupiterAspectInterpretation(
    aspect="Conjunct",
    hook="You leap before you look, driven by fire, faith, and fearlessness.",
    core_interpretation="With Mars conjunct Jupiter, you move through life with bold vision and relentless energy. You crave adventure, growth, and impact, and you're not afraid to take risks to get there. Your enthusiasm is magnetic, but your challenge is learning how to channel it without burning out or overreaching.",
    male_expression="You're courageous and fast moving, a bold explorer of ideas and action. Learn to balance impulse with long term aim.",
    female_expression="You act from vision and purpose, lifting others with your momentum. Pace yourself to protect your energy and direction.",
    other_expression="You're a spirited force, bold, expansive, and always seeking more. Your power grows when you pause with intention."
)

# Mars Sextile Jupiter
mars_jupiter_sextile = MarsJupiterAspectInterpretation(
    aspect="Sextile",
    hook="You act with vision and your strength opens doors and hearts.",
    core_interpretation="With Mars sextile Jupiter, your courage flows with optimism and principle. You're driven by a desire to grow, achieve, and do good, and life tends to meet your effort with opportunity. You're enthusiastic, ethical, and tend to uplift others as you pursue your goals. This aspect supports bold, meaningful action with grounded timing.",
    male_expression="You're assertive and principled, often acting as a force for progress. Confidence with compassion is your strength.",
    female_expression="You blend passion and direction, expressive, purposeful, and warm. Your drive lifts those around you.",
    other_expression="You're a thoughtful doer, moving with heart and meaning. Your boldness is powerful because it's rooted in integrity."
)

# Mars Trine Jupiter
mars_jupiter_trine = MarsJupiterAspectInterpretation(
    aspect="Trine",
    hook="You move like luck walks with you, bold, smooth, and full of purpose.",
    core_interpretation="With Mars trine Jupiter, you act with ease, confidence, and a sense of timing that feels intuitive. Your courage inspires others, and you often find that doors open just as you arrive. This is a fortunate, flowing energy and it brings success when you trust your momentum and lead with purpose.",
    male_expression="You're a natural leader, optimistic, direct, and inspiring. Your charm and confidence open doors.",
    female_expression="You move with rhythm and belief, courageous yet gracious. Others follow your light without resistance.",
    other_expression="You combine strength with faith, and it shows. Your momentum feels guided and it often is."
)

# Mars Square Jupiter
mars_jupiter_square = MarsJupiterAspectInterpretation(
    aspect="Square",
    hook="You want more, faster but your fire needs focus to go the distance.",
    core_interpretation="With Mars square Jupiter, you're passionate, competitive, and hungry for growth but you may rush into things or overpromise. You act big and aim high, but without strategy, your energy can burn hot and quick. The lesson is learning restraint, timing, and how to channel your ambition without letting it run wild.",
    male_expression="You're daring and action packed, but your progress depends on pacing. Learn that some wins come from patience.",
    female_expression="You live boldly, often taking on too much too fast. Ground your vision to turn your spark into mastery.",
    other_expression="You're a firestarter, full of courage and drive. Just be sure you're building something, not just chasing heat."
)

# Mars Opposite Jupiter
mars_jupiter_opp = MarsJupiterAspectInterpretation(
    aspect="Opposition",
    hook="You chase greatness, but must learn when to hold and when to leap.",
    core_interpretation="With Mars opposite Jupiter, you're pulled between taking bold action and overreaching. You want freedom, purpose, and to do something big but sometimes you struggle with direction or restraint. When you align your ambition with clarity, you become an unstoppable force for inspired impact.",
    male_expression="You're full of drive and ideals, but you can burn out chasing too many dreams. Focus brings true victory.",
    female_expression="You're spirited and expansive, with a passion that moves fast. Anchor your actions in purpose, and you rise with power.",
    other_expression="You thrive on momentum, but wisdom is your missing gear. When your movement is intentional, you change lives starting with your own."
)

# Create a dictionary to store all Mars–Jupiter aspect interpretations
mars_jupiter_aspects = {
    "Conjunct": mars_jupiter_conj,
    "Sextile": mars_jupiter_sextile,
    "Trine": mars_jupiter_trine,
    "Square": mars_jupiter_square,
    "Opposition": mars_jupiter_opp
}
