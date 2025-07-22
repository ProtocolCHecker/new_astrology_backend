class MercuryVenusAspectInterpretation:
    def __init__(self, relation, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.relation = relation
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunct
mercury_conjunct_venus = MercuryVenusAspectInterpretation(
    relation="Conjunct",
    hook="Your words flow like poetry, graceful, charming, and impossible to ignore.",
    core_interpretation="This combination blends communication with charm, you speak with warmth and wit drawing others in with your poetic expression, but be wary of indecision diluting your authentic voice.",
    male_expression="You woo with words, melding insight with elegance to make your point feel like a love letter.",
    female_expression="You enchant conversations, letting sincerity shine through your every utterance, crafting moments of connection.",
    other_expression="You harmonize logic and emotion, balancing reason with romance to elevate every dialogue."
)

# Sextile
mercury_sextile_venus = MercuryVenusAspectInterpretation(
    relation="Sextile",
    hook="Your charm sparks effortlessly.",
    core_interpretation="This pattern desmonstrate natural charisma and support, your playful banter and thoughtful follow through transform flirty sparks into meaningful bonds.",
    male_expression="You mix humor and depth, stirring smiles and substance in equal measure.",
    female_expression="Your conversation flows with playful insight, lifting spirits and forging genuine rapport.",
    other_expression="You fuse wit and warmth, cultivating joy through words that resonate."
)

# Trine
mercury_trine_venus = MercuryVenusAspectInterpretation(
    relation="Trine",
    hook="Your words flow like a gentle melody, soothing and sincere.",
    core_interpretation="This alignment creates seamless harmony between mind and heart, you express affection with effortless grace, making every exchange both uplifting and authentic.",
    male_expression="You speak truths wrapped in kindness, your honesty feels like a warm embrace.",
    female_expression="Your messages carry gentle conviction, confidence and compassion in every sentence.",
    other_expression="You are a natural peacemaker, your balanced perspective transforms dialogue into connection."
)

# Square
mercury_square_venus = MercuryVenusAspectInterpretation(
    relation="Square",
    hook="Your words have an edge, often stirring the pot.",
    core_interpretation="This tension sparks fiery discourse, you challenge norms with bold expression but watch for reckless remarks that can cut too deep.",
    male_expression="You provoke with sharp wit, pausing before you speak can turn tension into transformative insight.",
    female_expression="Your passion ignites debates, softening your tone ensures your message lands.",
    other_expression="You learn resilience through challenge, grounding your thoughts brings clarity amid the clash."
)

# Opposition
mercury_opposition_venus = MercuryVenusAspectInterpretation(
    relation="Opposition",
    hook="Your mind torns between saying too much and holding back.",
    core_interpretation="This dynamic manifests as push pull dynamics in speech and affection, balancing honesty with tact transforms your tension into meaningful dialogue.",
    male_expression="You alternate between charm and critique, finding equilibrium in listening refines your stance.",
    female_expression="You seek harmony in discourse, pausing before responding lets wisdom temper your words.",
    other_expression="You bridge divides through empathy, merging perspective with persuasion makes your voice resonate."
)

mercury_venus_aspects = {
    "Conjunct": mercury_conjunct_venus,
    "Sextile": mercury_sextile_venus,
    "Trine": mercury_trine_venus,
    "Square": mercury_square_venus,
    "Opposition": mercury_opposition_venus
}
