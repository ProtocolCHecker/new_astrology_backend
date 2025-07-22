class MercuryUranusAspectInterpretation:
    def __init__(self, relation, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.relation = relation
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunct
mercury_conjunct_uranus = MercuryUranusAspectInterpretation(
    relation="Conjunct",
    hook="You're a live wire of thought, electric, original, impossible to box in.",
    core_interpretation="This combination fuses intellect with innovation, you think at lightning speed and break molds, when you ground that brilliance your ideas lead revolutions.",
    male_expression="You spark ideas with fearless flair, pairing impulse with focus turns insight into invention.",
    female_expression="You blaze a mental trail, honoring stillness sharpens your inventive edge.",
    other_expression="You channel quantum thinking, balancing flow with form gives your genius shape."
)

# Sextile
mercury_sextile_uranus = MercuryUranusAspectInterpretation(
    relation="Sextile",
    hook="Your ideas light up the room, clever, clear and just off center enough to intrigue.",
    core_interpretation="This pattern grants a sharp inventive mind, you pivot on a dime and inspire breakthroughs, steady follow through turns sparks into lasting progress.",
    male_expression="You bring wit and vision, rooting insights in action magnifies your impact.",
    female_expression="Your intelligence dazzles, grounding spontaneity sustains your momentum.",
    other_expression="You're a catalyst for change, anchoring novelty keeps innovation alive."
)

# Trine
mercury_trine_uranus = MercuryUranusAspectInterpretation(
    relation="Trine",
    hook="Your thoughts move like lightning, quick, clean and impossible to copy.",
    core_interpretation="This alignment offers seamless access to inventive thinking, you see patterns others miss, pairing that clarity with discipline gives your vision wings.",
    male_expression="You articulate fresh perspectives, balancing freedom with focus makes your voice unforgettable.",
    female_expression="You innovate with grace, structuring your insights magnifies their reach.",
    other_expression="You are a natural visionary, merging intuition and logic unleashes your potential."
)

# Square
mercury_square_uranus = MercuryUranusAspectInterpretation(
    relation="Square",
    hook="Your thoughts spark rebellion, disruptive, inspired and sometimes untamed.",
    core_interpretation="This tension fuels restless brilliance and sudden outbursts, you challenge norms but learning pacing prevents your sparks from burning bridges.",
    male_expression="You provoke with bold ideas, tempering intensity with timing turns friction into fuel.",
    female_expression="You clash with convention, softening your edge guides revolution rather than revolt.",
    other_expression="You forge resilience in disruption, channeling energy gives your vision enduring form."
)

# Opposition
mercury_opposition_uranus = MercuryUranusAspectInterpretation(
    relation="Opposition",
    hook="Your mind dances between genius and chaos, an electrifying tension.",
    core_interpretation="This dynamic reflects a dance between tradition and innovation, balancing mental independence with patience transforms flashes of insight into sustained breakthroughs.",
    male_expression="You alternate between conformity and revolt, listening deepens your perspective.",
    female_expression="You thrive on challenge, grounding your radical ideas ensures they land with impact.",
    other_expression="You are a contrarian genius, steady rhythms give your breakthroughs staying power."
)

mercury_uranus_aspects = {
    "Conjunct": mercury_conjunct_uranus,
    "Sextile": mercury_sextile_uranus,
    "Trine": mercury_trine_uranus,
    "Square": mercury_square_uranus,
    "Opposition": mercury_opposition_uranus
}
