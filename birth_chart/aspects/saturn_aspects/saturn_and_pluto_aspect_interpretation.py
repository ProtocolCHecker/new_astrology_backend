class SaturnPlutoAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
saturn_pluto_conj = SaturnPlutoAspectInterpretation(
    aspect="Conjunction",
    hook="You harness discipline as a source of power, rebuilding with resolve.",
    core_interpretation="You unite structure and transformation, giving you immense willpower and the capacity to rebuild. This often comes through trials that demand self mastery and deep introspection, teaching you resilience and strength.",
    male_expression="You are commanding and strategic, reshaping your environment with determination. It's important to guard against rigidity and allow flexibility to foster growth and adaptability.",
    female_expression="You are steely yet profoundly transformative, balancing control with compassion. This balance helps you create meaningful change and inspire those around you.",
    other_expression="You are an architect of renewal, reviving what's broken with persistent force. This ability makes you a powerful agent of change, capable of turning challenges into opportunities."
)

# Sextile
saturn_pluto_sextile = SaturnPlutoAspectInterpretation(
    aspect="Sextile",
    hook="Your resolve burns with quiet power, guiding transformation.",
    core_interpretation="You have the ability to transform methodically and with integrity, supporting deep change through disciplined effort. This aspect allows you to execute transformations without overwhelming force, making your evolution feel natural and sustained.",
    male_expression="You are focused and steadfast, navigating change with humility and determination. This trait makes you a reliable and respected figure, capable of inspiring confidence in others.",
    female_expression="You are an intentional transformer, evolving systems step by step with grace and wisdom. This ability makes you a trusted and influential figure, admired for your sense of purpose and responsibility.",
    other_expression="You have subtle power in action, reshaping without drama. This balance of traits makes you a respected and successful individual, capable of creating meaningful change."
)

# Trine
saturn_pluto_trine = SaturnPlutoAspectInterpretation(
    aspect="Trine",
    hook="Change flows through your structure, empowering evolution.",
    core_interpretation="You have an effortless blend of discipline and regeneration, enabling quiet resilience and empowering metamorphosis. This aspect makes your transformations feel natural and sustained, helping you grow and adapt with ease.",
    male_expression="You are resolute yet adaptable, building lasting transformation with determination and grace. This trait makes you a respected and influential figure, capable of inspiring change and progress.",
    female_expression="You are a calming force of change, reforming with grace and wisdom. This ability makes you a trusted and admired figure, capable of creating meaningful and lasting transformations.",
    other_expression="You are a harmonious transformer, evolving through steady and structured growth. This balance of traits makes you a successful and respected individual, capable of turning visions into reality."
)

# Square
saturn_pluto_square = SaturnPlutoAspectInterpretation(
    aspect="Square",
    hook="You are pressed by power and limits, finding breakthroughs in barriers.",
    core_interpretation="You experience intense friction between control and transformation, creating internal conflict that can fuel growth. This aspect teaches you to release destructive rigidity and embrace profound empowerment, turning challenges into opportunities for personal development.",
    male_expression="You are driven and intense, learning depth by confronting inner walls with courage and determination. This journey helps you build resilience and transformative willpower, leading to personal growth and fulfillment.",
    female_expression="You are forceful but may feel conflicted, with strength that surfaces through confrontation and perseverance. This process of facing and overcoming challenges helps you refine your goals and achieve them with greater confidence.",
    other_expression="You experience pressure borne alchemy, evolving by breaking and rebuilding with resilience and determination. This dynamic of facing and resolving tensions helps you develop a more robust and successful character."
)

# Opposition
saturn_pluto_opp = SaturnPlutoAspectInterpretation(
    aspect="Opposition",
    hook="Your structures are tested by deep urges, learning power through reflection.",
    core_interpretation="You balance control with surrender, often mirrored in relationships, teaching that true power emerges from integrating boundaries with transformative depth. This aspect helps you find strength and empowerment through self awareness and growth.",
    male_expression="You are a reflective strategist, growing by balancing authority and vulnerability with wisdom and grace. This balance makes you a respected and trusted figure, capable of providing both emotional and practical support.",
    female_expression="You are intensely aware of power dynamics, finding strength in conscious yielding and adaptability. This trait makes you a successful and admired figure, capable of navigating challenges with grace and determination.",
    other_expression="You are a polarizing transformer, becoming whole by reconciling structure with introspection and growth. This process of understanding and integrating different aspects of yourself helps you grow into a well rounded and successful individual."
)

saturn_pluto_aspects = {
    "Conjunction": saturn_pluto_conj,
    "Sextile": saturn_pluto_sextile,
    "Trine": saturn_pluto_trine,
    "Square": saturn_pluto_square,
    "Opposition": saturn_pluto_opp
}
