class UranusNeptuneAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
uranus_neptune_conj = UranusNeptuneAspectInterpretation(
    aspect="Conjunction",
    hook="You dream of a future no one's built yet.",
    core_interpretation="You're tuned into deep, collective shifts and seeing what could be before the rest of the world catches on. Your challenge is to stay rooted while channeling such vast, spiritual and creative energy into something real.",
    male_expression="You carry a vision that blends freedom with compassion, but grounding it into something practical gives it power. You're not here to follow trends and you're here to spark them.",
    female_expression="You hold a quiet knowing of how things could change for the better. Your voice matters most when you trust that your dream can shape real movement.",
    other_expression="You stand at the crossroads of inspiration and rebellion, bringing forward ideas the world isn't quite ready for. Still, your role is to dream them into being."
)

# Sextile
uranus_neptune_sextile = UranusNeptuneAspectInterpretation(
    aspect="Sextile",
    hook="Your dreams adapt to the times.",
    core_interpretation="You move between innovation and imagination with grace, often inspiring change through subtle shifts rather than loud revolutions. Your strength is in knowing how to nudge the world forward, one inspired idea at a time.",
    male_expression="You innovate with empathy, showing others how change can be gentle and meaningful. You're not here to shake things up and you're here to guide them naturally.",
    female_expression="You feel your way into progress, blending emotional insight with visionary thinking. People often look to you as a quiet source of hope and originality.",
    other_expression="You bring the future into the present through kindness and creativity. Your impact comes from your ability to harmonize what's real with what's possible."
)

# Trine
uranus_neptune_trine = UranusNeptuneAspectInterpretation(
    aspect="Trine",
    hook="You turn intuition into innovation.",
    core_interpretation="You carry a natural harmony between your vision of the future and your inner sense of wisdom. Your creativity feels cosmic, yet personal and flowing in ways that can awaken others just by being expressed.",
    male_expression="You think big and dream deep, often offering ideas that feel both futuristic and spiritually grounded. You make progress feel poetic.",
    female_expression="Your creativity comes from somewhere beyond words, yet your ability to express it is clear and resonant. You're a quiet revolution in motion.",
    other_expression="You embody peaceful progress and transforming spaces, ideas, and people through your seamless blend of intuition and imagination."
)

# Square
uranus_neptune_square = UranusNeptuneAspectInterpretation(
    aspect="Square",
    hook="You fight with your own dreams to find your truth.",
    core_interpretation="You live in the tension between what is and what could be and pushing yourself to break illusions while still holding onto hope. This inner friction can feel confusing, but it's what gives your ideas their power to change things.",
    male_expression="You question everything, especially your ideals. That discomfort sharpens your vision and just make sure you don't lose faith while fighting for clarity.",
    female_expression="Your inner world is full of contrast and spiritual longing meets a need for personal reinvention. You're learning how to build something lasting from your inner chaos.",
    other_expression="You're here to expose what no longer works and rebuild with vision. The pressure you feel isn't a flaw and it's the spark of real transformation."
)

# Opposition
uranus_neptune_opp = UranusNeptuneAspectInterpretation(
    aspect="Opposition",
    hook="You reflect the world's growing pains.",
    core_interpretation="You experience the clash between innovation and illusion through relationships and cultural dynamics, often sensing collective shifts before they fully surface. Your journey is about balancing personal clarity with collective confusion.",
    male_expression="You see what others avoid, often through what life mirrors back to you. Your power lies in helping others wake up, without losing yourself in their haze.",
    female_expression="You often find your vision sharpened through contrast and especially with people who challenge or question your dreams. What feels like conflict is often your path to deeper insight.",
    other_expression="You're wired to evolve through contrast and reflection, picking up on the undercurrents of change. Your gift is turning dissonance into direction."
)

# Store all Uranus–Neptune aspect interpretations
uranus_neptune_aspects = {
    "Conjunction": uranus_neptune_conj,
    "Sextile": uranus_neptune_sextile,
    "Trine": uranus_neptune_trine,
    "Square": uranus_neptune_square,
    "Opposition": uranus_neptune_opp
}
