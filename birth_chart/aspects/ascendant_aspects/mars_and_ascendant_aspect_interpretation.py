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
    hook="You don't knock and you kick doors open. Your energy *is* your first impression.",
    core_interpretation="Your presence is electric and people feel you before they see you, which is powerful yet raw, as you might intimidate the timid and attract those who crave intensity, but be cautious not to mistake aggression for strength or burn out before learning strategy.",
    male_expression="You're told you're ‘too much' and but your fire is your gift. Channel it, don't smother it.",
    female_expression="Society calls you ‘bossy' when you lead. Fuck that. Own your command and just temper it with wisdom.",
    other_expression="You're a human lightning bolt. Learn to ground yourself, or you'll keep striking the wrong targets."
)

# Sextile
mars_sextile_asc = MarsAscendantAspectInterpretation(
    aspect="Sextile",
    hook="You move through resistance like heat through metal and smooth, unstoppable, but never brutal.",
    core_interpretation="You've got the rare gift of assertiveness without abrasiveness, as people trust your drive because it doesn't bulldoze and it invites, but beware that your ease can make you lazy about deeper courage, for comfort isn't growth.",
    male_expression="You persuade without pushing and a natural leader. But don't let charm replace conviction.",
    female_expression="Your strength is velvet and wrapped steel. Use it to uplift, not just adapt.",
    other_expression="You disarm barriers effortlessly, so now challenge yourself to break a few when it matters."
)

# Trine
mars_trine_asc = MarsAscendantAspectInterpretation(
    aspect="Trine",
    hook="Your confidence isn't loud and it's absolute. People feel your strength before you flex it.",
    core_interpretation="Life hands you victories others fight for, as your energy flows seamlessly, which is a trap because you might avoid necessary battles, mistaking luck for skill, but real power comes from knowing when to choose the fight, not just winning the easy ones.",
    male_expression="You're the calm in the storm and but storms shape souls. Step into chaos sometimes.",
    female_expression="Grace is your armor, but don't let it shield you from your own rage. It's valid too.",
    other_expression="You're a natural winner, so now learn to lose and it'll teach you more than victory ever could."
)

# Square
mars_square_asc = MarsAscendantAspectInterpretation(
    aspect="Square",
    hook="You're a live wire and sparks fly when you enter a room, but so do tempers.",
    core_interpretation="Your energy is a weapon you haven't fully mastered, as you provoke reactions without trying and some crave your fire, others fear it, so the work is to stop blaming others for ‘misreading' you and instead hone your edge and don't just swing it wildly.",
    male_expression="You're called ‘aggressive' when you're just passionate, but dig deeper and are you listening, or just waiting to strike?",
    female_expression="Your anger terrifies people. Good. Now learn to wield it like a scalpel, not a sledgehammer.",
    other_expression="You're a walking challenge, which is power and if you stop apologizing for it and start directing it."
)

# Opposition
mars_opposite_asc = MarsAscendantAspectInterpretation(
    aspect="Opposition",
    hook="Your rivals are your mirrors and every clash shows you a piece of yourself you've disowned.",
    core_interpretation="You attract battles because you need them, as the people who trigger you are here to teach you about your own suppressed power, so stop projecting your fight onto others, own your fury and it's your untapped leadership.",
    male_expression="You call others ‘competitive' and but you're the one who can't stand losing. Lean into that hunger.",
    female_expression="You magnetize strong personalities because you refuse to admit your own strength. Time to meet your match and in the mirror.",
    other_expression="Your ‘enemies' are your best teachers. Thank them and then surpass them."
)

# Dictionary of Mars–Ascendant aspect interpretations
mars_ascendant_aspects = {
    "Conjunct": mars_conjunct_asc,
    "Sextile": mars_sextile_asc,
    "Trine": mars_trine_asc,
    "Square": mars_square_asc,
    "Opposition": mars_opposite_asc
}
