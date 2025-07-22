class JupiterMarsAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Mars Conjunct Jupiter
jupiter_conjunction_mars = JupiterMarsAspectInterpretation(
    aspect="Conjunction",
    hook="You act like the future is already yours  and  bold, unshaken, relentless.",
    core_interpretation="With Mars conjunct Jupiter, you're wired for action with a bold sense of faith in your future. You charge ahead with vision and courage, often achieving great things  and  but if you're not careful, your fire can burn too fast. Learn to pace yourself so your ambition doesn't outrun your endurance.",
    male_expression="You move like a pioneer  and  brave, daring, and always chasing something bigger. But take a breath sometimes; not every battle is worth the charge.",
    female_expression="Your fire is contagious; you lead with inspiration and justice. Still, when you don't slow down, your own needs can vanish in the rush.",
    other_expression="You shine when you're in motion toward a cause. Just remember: passion is powerful, but sustained purpose is what changes the world."
)

# Mars Sextile Jupiter
jupiter_sextile_mars = JupiterMarsAspectInterpretation(
    aspect="Sextile",
    hook="You strike while the stars are smiling  and  your will opens doors.",
    core_interpretation="This aspect gives you natural momentum  and  things seem to click when you act with heart and belief. You attract opportunity not by luck, but by the sincerity in your actions. Just be sure your optimism doesn't lead you to overlook the details that build long term success.",
    male_expression="You lead with optimism and draw others to you effortlessly. Keep pairing action with intention, and your path opens wide.",
    female_expression="Your drive carries grace  and  you act from deep purpose and others feel your warmth. Just stay grounded in your 'why.'",
    other_expression="Your energy is radiant and ethical. You bring ideas to life with integrity, and life tends to reward that kind of spirit."
)

# Mars Trine Jupiter
jupiter_trine_mars = JupiterMarsAspectInterpretation(
    aspect="Trine",
    hook="You grow with every bold move  and  your steps align with grace.",
    core_interpretation="This is a gift: you act when the time is right, and your instincts often lead to success without strain. There's something almost effortless in how your courage meets your higher vision. But don't let ease make you passive  and  the world still needs your active presence.",
    male_expression="You move with purpose and inspire trust  and  people follow your lead because it feels right. But don't forget to stretch yourself beyond what's easy.",
    female_expression="You lead by example, with elegance and conviction. There's strength in your softness, and it moves mountains.",
    other_expression="You flow with life's current, blending drive and wisdom. Success feels natural, but it still requires conscious intention."
)

# Mars Square Jupiter
jupiter_square_mars = JupiterMarsAspectInterpretation(
    aspect="Square",
    hook="You want more, faster  and  the world becomes your battleground for belief.",
    core_interpretation="You're fueled by bold dreams and a relentless hunger to go further, faster. But your biggest wins only come when you learn the power of restraint. If you don't temper your fire, you may find yourself burned by your own ambition.",
    male_expression="You're a force  and  competitive, passionate, unstoppable. But victory means little if ego drives the mission.",
    female_expression="You chase growth like a wildfire  and  fierce and unapologetic. Slow down before your brilliance burns out.",
    other_expression="You're a challenger at heart, but your greatest strength is knowing when to push  and  and when to pause. Discipline makes your fire sustainable."
)

# Mars Opposite Jupiter
jupiter_opposition_mars = JupiterMarsAspectInterpretation(
    aspect="Opposition",
    hook="You chase the horizon  and  caught between impulse and your higher calling.",
    core_interpretation="You often feel stretched between doing too much or not enough  and  between charging forward and stepping back to reflect. There's a deep fire in you, but it needs harmony with your values to shine at its best. When your actions align with your beliefs, you become a visionary with real impact.",
    male_expression="You're brave, noble, and full of potential  and  but torn by inner conflict. When you unite your drive with meaning, you become unstoppable.",
    female_expression="Your fire is spiritual  and  you act for a cause, but often wrestle with balance. When you integrate purpose and passion, you become magnetic.",
    other_expression="You're on a journey of alignment  and  between instinct and integrity. Your true strength lies in walking your talk, even when it's hard."
)

# Create a dictionary to store all Jupiter Mars aspect interpretations
jupiter_mars_aspects = {
    "Conjunction": jupiter_conjunction_mars,
    "Sextile": jupiter_sextile_mars,
    "Trine": jupiter_trine_mars,
    "Square": jupiter_square_mars,
    "Opposition": jupiter_opposition_mars
}
