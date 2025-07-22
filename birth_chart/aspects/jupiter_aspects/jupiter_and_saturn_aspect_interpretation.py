class JupiterSaturnAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Jupiter Conjunct Saturn
jupiter_conjunction_saturn = JupiterSaturnAspectInterpretation(
    aspect="Conjunction",
    hook="You build your dreams like cathedrals  and  slow, strong, and meant to last.",
    core_interpretation="With Jupiter conjunct Saturn, you carry both vision and structure  and  and you know that one without the other isn't enough. You dream big, but you also respect the rules of time, effort, and strategy. When you trust your pace, success becomes more than luck  and  it becomes legacy.",
    male_expression="You're the steady architect  and  ambitious, but anchored. You climb with purpose, and people trust your steps.",
    female_expression="You build grace into everything you do. Your calm focus makes even the wildest dream feel possible.",
    other_expression="You're wired for endurance  and  someone who plants seeds with patience. Your path may be slow, but it's solid."
)

# Jupiter Sextile Saturn
jupiter_sextile_saturn = JupiterSaturnAspectInterpretation(
    aspect="Sextile",
    hook="You balance your reach with roots  and  and that's your quiet advantage.",
    core_interpretation="This aspect blesses you with a natural rhythm between caution and growth. You know how to think big without floating away from what's real. People see you as trustworthy because your vision has weight  and  and your plans tend to hold up under pressure.",
    male_expression="You lead with calm clarity  and  grounded in wisdom but never afraid to expand. Others rely on your steady optimism.",
    female_expression="You plan with heart and act with strategy. Your strength is your ability to dream without losing direction.",
    other_expression="You move with wise timing  and  intuitive and methodical. That blend helps you build what others only imagine."
)

# Jupiter Trine Saturn
jupiter_trine_saturn = JupiterSaturnAspectInterpretation(
    aspect="Trine",
    hook="You trust time  and  and time tends to trust you back.",
    core_interpretation="With this harmonious aspect, you combine hope and maturity in a way that feels effortless. You're the type of person others come to for guidance, because your judgment feels both expansive and grounded. Success may come steadily rather than explosively  and  but it comes with integrity.",
    male_expression="You carry old soul wisdom  and  someone who grows quietly into lasting influence. You build futures with grace.",
    female_expression="You lead from the middle ground  and  hopeful but practical, visionary but humble. Your path is trustworthy.",
    other_expression="You're a bridge between ambition and patience. When you walk your truth steadily, you teach others how to do the same."
)

# Jupiter Square Saturn
jupiter_square_saturn = JupiterSaturnAspectInterpretation(
    aspect="Square",
    hook="You live in tension  and  between dreaming big and doubting deeply.",
    core_interpretation="This square creates friction between your hopes and your fears. Part of you wants to fly, but another part questions the wings. That conflict can hold you back  and  or make you incredibly strong, depending on how you face it. When you stop seeing doubt as failure, you begin to build with real depth.",
    male_expression="You carry weight with your vision  and  sometimes too much. But once you stop proving yourself and start trusting yourself, you rise.",
    female_expression="You work twice as hard to believe in your dreams  and  and that makes your success deeply earned. Keep moving even when it's slow.",
    other_expression="You're a builder shaped by contrast. The pressure is real, but so is your power to grow from it."
)

# Jupiter Opposition Saturn
jupiter_opposition_saturn = JupiterSaturnAspectInterpretation(
    aspect="Opposition",
    hook="You stretch between freedom and control  and  always balancing what you want with what feels safe.",
    core_interpretation="This aspect pulls you between expansion and restraint, often making you question when to leap and when to hold back. You might doubt your timing or feel blocked by fear just as you're ready to grow. But once you stop seeing your inner conflict as a flaw, you begin to understand both risk and responsibility in powerful ways.",
    male_expression="You toggle between bold and careful  and  and that tension becomes wisdom, if you let it teach you.",
    female_expression="You crave possibility but need structure to feel safe. When those sides learn to work together, you're unstoppable.",
    other_expression="You're learning to harmonize faith and discipline. It's not easy, but it makes you a wiser, more intentional force in the world."
)

# Create a dictionary to store all Jupiter Saturn aspect interpretations
jupiter_saturn_aspects = {
    "Conjunction": jupiter_conjunction_saturn,
    "Sextile": jupiter_sextile_saturn,
    "Trine": jupiter_trine_saturn,
    "Square": jupiter_square_saturn,
    "Opposition": jupiter_opposition_saturn
}
