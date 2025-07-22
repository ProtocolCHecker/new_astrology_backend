class VenusPlutoAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
venus_pluto_conj = VenusPlutoAspectInterpretation(
    aspect="Conjunction",
    hook="Your love has gravity  and   it changes you from the inside out.",
    core_interpretation="When you love, you go all in. Your connections are never casual and  they're intense, magnetic, and transformative. Through love, you meet your shadow and your power.",
    male_expression="You love with your whole being and  sometimes to the edge of control. Healing comes when you stop trying to possess what's meant to move.",
    female_expression="You dive deep in love, craving union that touches the soul. But you grow most when you learn to stay whole within connection.",
    other_expression="You are a portal to depth. Love is your crucible and  burning away illusion and forging emotional truth."
)

# Sextile
venus_pluto_sextile = VenusPlutoAspectInterpretation(
    aspect="Sextile",
    hook="Your presence carries quiet depth  and   you change others without trying.",
    core_interpretation="You love with subtle intensity and emotional insight. There's a quiet power in how you connect and  tender yet transformative, gentle yet profound.",
    male_expression="You express loyalty and emotional depth with grace. Others feel seen and changed by your attention.",
    female_expression="Your love heals softly. You see into others without needing to control or fix them.",
    other_expression="You're a quiet catalyst. You nurture growth by simply showing up fully and  with honesty, presence, and care."
)

# Trine
venus_pluto_trine = VenusPlutoAspectInterpretation(
    aspect="Trine",
    hook="Love transforms you with ease  and   depth flows like a current.",
    core_interpretation="Your emotional power is smooth and graceful. You know how to love deeply without losing balance and  and your relationships evolve naturally, without force.",
    male_expression="You bring magnetism and composure into love, offering intensity with emotional clarity.",
    female_expression="You love deeply but not desperately. Your ability to hold space for others brings transformation.",
    other_expression="Your love is medicine and  strong, soothing, and steady. You change lives simply by being real."
)

# Square
venus_pluto_square = VenusPlutoAspectInterpretation(
    aspect="Square",
    hook="You crave love that cracks you open.",
    core_interpretation="Love awakens your inner fire and  and sometimes your inner fears. Power struggles, jealousy, and intensity may arise, but through these challenges, you learn to love without losing yourself.",
    male_expression="You desire devotion and intensity, but must face your own fears of loss or control to grow.",
    female_expression="You feel deeply and fight fiercely and  for connection, for truth. Balance comes from turning that passion inward, too.",
    other_expression="Your love is a forge and  unrefined, potent, and transformative. Every rupture is a chance to rebuild something truer."
)

# Opposition
venus_pluto_opp = VenusPlutoAspectInterpretation(
    aspect="Opposition",
    hook="Others reflect your emotional intensity  and   love becomes your mirror.",
    core_interpretation="Your relationships hold up a mirror to your desires, fears, and power. Through attraction and resistance, you learn to meet yourself more fully and love with integrity.",
    male_expression="You seek deep bonds, but grow most when you release control and let others be whole too.",
    female_expression="You feel intensely and love completely and  but you evolve when you stop projecting and start integrating.",
    other_expression="Love is a mirror, and you are both the reflection and the seer. Your heart learns truth through contrast and clarity."
)

# Store all Venus–Pluto aspects
venus_pluto_aspects = {
    "Conjunction": venus_pluto_conj,
    "Sextile": venus_pluto_sextile,
    "Trine": venus_pluto_trine,
    "Square": venus_pluto_square,
    "Opposition": venus_pluto_opp
}
