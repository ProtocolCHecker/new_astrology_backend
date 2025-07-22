class PlutoSaturnAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
pluto_saturn_conj = PlutoSaturnAspectInterpretation(
    aspect="Conjunction",
    hook="You rebuild from the bones out.",
    core_interpretation="You carry a quiet strength that reshapes you from the inside. Life has taught you to endure and evolve at once. You don't just survive  and  you emerge remade, again and again.",
    male_expression="You move through life like tectonic force  and  slow, deliberate, but capable of complete reconstruction. What collapses under pressure in others becomes blueprint in your hands. You lead not through noise, but through gravity.",
    female_expression="Your resilience runs marrow deep. You've met endings and chosen to rise, not in spite of them but because of them. You don't just hold power  and  you embody the wisdom of survival turned structure.",
    other_expression="Within you, destruction and construction breathe as one. Every loss becomes a threshold. You're not afraid to start again, because you understand that everything real begins underground."
)

# Sextile
pluto_saturn_sextile = PlutoSaturnAspectInterpretation(
    aspect="Sextile",
    hook="You shape change with steady hands.",
    core_interpretation="You bring discipline to deep change. Your growth isn't loud, but it leaves lasting marks. You move with intention, building from what others avoid.",
    male_expression="You work like a sculptor: shaping from shadow, carving from pressure. There's a precision to your depth  and  you don't just feel transformation, you steer it with a craftsman's resolve.",
    female_expression="You move with quiet power, knowing that real change is never rushed. Through patience and deep reflection, you guide others  and  and yourself  and  through terrain that demands courage.",
    other_expression="Your presence is grounding, even in upheaval. You know that healing can be designed, and you build it slowly  and  piece by piece, layer by layer  and  until what stands is true."
)

# Trine
pluto_saturn_trine = PlutoSaturnAspectInterpretation(
    aspect="Trine",
    hook="You turn pressure into grace.",
    core_interpretation="Your strength is fluid but grounded. You move through change with quiet confidence, shaping what matters most without force. You build from a place of deep knowing.",
    male_expression="You carry gravitas without weight. Change moves through you smoothly, like water carving stone. Others trust your quiet force  and  you don't demand control; you embody it.",
    female_expression="You balance depth and form with natural elegance. What feels like pressure to others feels like rhythm to you. You create, rebuild, and restructure with a grace born from inner strength.",
    other_expression="You are the still point in the storm  and  not because you resist change, but because you've befriended it. What you touch transforms, not with noise, but with lasting impact."
)

# Square
pluto_saturn_square = PlutoSaturnAspectInterpretation(
    aspect="Square",
    hook="You grow where others break.",
    core_interpretation="Tension lives inside you, but it sharpens you. You've learned to rebuild from strain, and each struggle carves deeper self trust. You turn friction into foundation.",
    male_expression="You've wrestled with your own resistance, broken walls you once built to feel safe. Life keeps demanding more of you  and  and somehow, you keep rising, more defined, more deliberate, more real.",
    female_expression="You've had to fight to become yourself  and  not against the world, but against the fear of being too much or too powerful. Through tension, you've claimed your space and your strength.",
    other_expression="You were not handed ease, but you were handed depth. Through every inner quake, you've sculpted a truer self  and  one that doesn't flinch at pressure, but meets it with vision."
)

# Opposition
pluto_saturn_opp = PlutoSaturnAspectInterpretation(
    aspect="Opposition",
    hook="You hold power between opposites.",
    core_interpretation="Your growth lives in contrast. Others reflect your need for control or your fear of change  and  and through them, you learn balance. Real power comes when you stop fighting yourself.",
    male_expression="You've lived at both ends  and  rigidity and chaos, control and collapse. But your wisdom comes from recognizing these aren't enemies, just mirrors. You grow when you stop choosing sides.",
    female_expression="You carry intensity and structure in tension  and  drawn to power, yet wary of it. Relationships teach you how to soften control and let your strength breathe.",
    other_expression="You've been stretched between containment and eruption. And yet, in this stretch, you've built something rare: the ability to hold contradiction and still act with purpose."
)

pluto_saturn_aspects = {
    "Conjunction": pluto_saturn_conj,
    "Sextile": pluto_saturn_sextile,
    "Trine": pluto_saturn_trine,
    "Square": pluto_saturn_square,
    "Opposition": pluto_saturn_opp
}
