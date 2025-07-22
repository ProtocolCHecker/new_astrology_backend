class JupiterNeptuneAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Jupiter Conjunct Neptune
jupiter_conjunction_neptune = JupiterNeptuneAspectInterpretation(
    aspect="Conjunction",
    hook="You turn faith into dreams  and  and dreams into truth.",
    core_interpretation="With Jupiter conjunct Neptune, your vision is vast and your soul is tuned to something higher. You often feel that life holds deeper meaning, and you're drawn to what inspires, heals, or uplifts. But to live your dreams without being swept away by them, you must learn to tell the difference between true vision and illusion.",
    male_expression="You're the dreamer visionary  and  open hearted, generous, and led by what you believe is possible. But stay grounded or you risk drifting.",
    female_expression="You feel life through your spirit; your empathy runs deep. Just don't lose yourself in the beauty of ideals that aren't rooted.",
    other_expression="You're a channel for inspiration and hope  and  but the world needs your clarity as much as your dreams. Balance them wisely."
)

# Jupiter Sextile Neptune
jupiter_sextile_neptune = JupiterNeptuneAspectInterpretation(
    aspect="Sextile",
    hook="You move with gentle faith  and  your intuition speaks in kindness.",
    core_interpretation="This aspect helps you blend belief and sensitivity in a way that uplifts others without losing yourself. You live with quiet hope and often act as a guide or healer without needing recognition. You tend to trust the flow of life, and when you stay true to that calm wisdom, people find comfort in your presence.",
    male_expression="You believe in the good in others and carry a quiet strength. Your gentleness is your gift, not your weakness.",
    female_expression="You move through the world like a gentle tide  and  soft but purposeful. You guide others through your calm, intuitive strength.",
    other_expression="You're a natural empath  and  someone who heals not with words, but with presence. Stay connected to your inner compass."
)

# Jupiter Trine Neptune
jupiter_trine_neptune = JupiterNeptuneAspectInterpretation(
    aspect="Trine",
    hook="You trust in the beauty of life  and  and life tends to rise to meet that trust.",
    core_interpretation="This aspect blesses you with deep spiritual harmony and a heart tuned to love, art, or meaning. You don't force faith  and  it flows through you, often guiding your path in subtle and beautiful ways. Your ability to believe in goodness is contagious, and you can help others reconnect with wonder just by being yourself.",
    male_expression="You walk with grace  and  a gentle leader who leads by inspiration, not authority. Your optimism is healing.",
    female_expression="You radiate soulful beauty  and  creative, open hearted, and naturally trusting of life's rhythm. That's a rare kind of power.",
    other_expression="You're in tune with life's quiet magic  and  and when you follow that, your impact ripples outward. Just keep listening to what moves you."
)

# Jupiter Square Neptune
jupiter_square_neptune = JupiterNeptuneAspectInterpretation(
    aspect="Square",
    hook="You reach for the ideal  and  but sometimes lose your footing in the clouds.",
    core_interpretation="This square pushes you to dream big, but it also tests your ability to separate fantasy from truth. You may believe so strongly in a vision that you overlook red flags or ignore reality until it crashes down. Yet when you ground your ideals, you can become someone who turns imagination into real change.",
    male_expression="You chase meaning and freedom  and  but without boundaries, your journey can veer off course. Structure helps your spirit shine.",
    female_expression="You dream with intensity and love deeply  and  but you must anchor your hopes or risk heartbreak. Discernment is part of your growth.",
    other_expression="You're learning to build bridges between your vision and what's actually possible. That tension is hard  and  but transformative."
)

# Jupiter Opposite Neptune
jupiter_opposition_neptune = JupiterNeptuneAspectInterpretation(
    aspect="Opposition",
    hook="You crave something higher  and  but life keeps asking what's real.",
    core_interpretation="With this opposition, you're constantly torn between wanting to believe and needing to doubt. You often place your trust in beautiful visions  and  and sometimes get let down. But through that pain, you develop a deeper, wiser faith  and  one that isn't blind, but earned through real experience.",
    male_expression="You reach for higher truth, even when the world disappoints you. That struggle shapes you into someone others turn to for meaning.",
    female_expression="You feel pulled between what is and what could be. When you learn to trust both your heart and your eyes, your wisdom shines.",
    other_expression="You've lived through both faith and disillusionment. The goal isn't perfection  and  it's integration. And you're getting there."
)

# Create a dictionary to store all Jupiter Neptune aspect interpretations
jupiter_neptune_aspects = {
    "Conjunction": jupiter_conjunction_neptune,
    "Sextile": jupiter_sextile_neptune,
    "Trine": jupiter_trine_neptune,
    "Square": jupiter_square_neptune,
    "Opposition": jupiter_opposition_neptune
}
