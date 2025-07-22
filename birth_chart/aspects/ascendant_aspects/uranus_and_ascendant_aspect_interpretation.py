class UranusAscendantAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
uranus_asc_conj = UranusAscendantAspectInterpretation(
    aspect="Conjunction",
    hook="You wear originality as armor  and  your identity is shaped by independence.",
    core_interpretation="With Uranus conjunct Ascendant, you are fiercely individual and unpredictable, with a magnetic presence that draws attention. Your unique spirit sets you apart, making you a natural rebel. Embrace your distinctiveness as it is your strength.",
    male_expression="You are a rebellious maverick, thriving in unconventional ways while remaining charismatic. Your charm lies in your uniqueness.",
    female_expression="You are electric and free and spirited, standing out with bold originality. Your boldness is inspiring to others.",
    other_expression="You are an authentic anarchist, standing apart by being unapologetically yourself. Your authenticity is your power."
)

# Sextile
uranus_asc_sext = UranusAscendantAspectInterpretation(
    aspect="Sextile",
    hook="Your uniqueness connects smoothly  and  creativity without friction.",
    core_interpretation="Uranus sextile Ascendant allows your originality to shine effortlessly. You have an inventive and open and minded charisma that is both exciting and approachable. Your creativity is a bridge to others.",
    male_expression="You are innovative and sociable, expressing your eccentricity with charm. Your ideas can captivate and engage those around you.",
    female_expression="You are a creative catalyst, drawing others in with your quirky warmth. Your warmth makes your uniqueness accessible.",
    other_expression="You are a playful visionary, integrating your uniqueness into your self and presentation. Your vision is infectious and inviting."
)

# Trine
uranus_asc_trine = UranusAscendantAspectInterpretation(
    aspect="Trine",
    hook="You evolve naturally  and  being different feels natural and balanced.",
    core_interpretation="With Uranus trine Ascendant, you experience a harmonious flow between your identity and originality. You are effortlessly progressive and authentically intriguing. Your authenticity is effortless and inspiring.",
    male_expression="You are forward and thinking and poised, finding change to be natural and easy. Your adaptability is a source of strength.",
    female_expression="You are a subtle trendsetter, inspiring others through your graceful uniqueness. Your subtlety is your signature.",
    other_expression="You are a fluid nonconformist, experiencing authenticity as easily as breathing. Your fluidity is your essence."
)

# Square
uranus_asc_square = UranusAscendantAspectInterpretation(
    aspect="Square",
    hook="You clash with conformity  and  friction fuels your evolution.",
    core_interpretation="Uranus square Ascendant creates tension between your drive for freedom and the need for social acceptance. This restlessness pushes you to break molds despite resistance. Embrace this tension as it fuels your growth.",
    male_expression="You are a restless innovator, learning to navigate rebellion with care. Your journey is about finding balance.",
    female_expression="You are boldly independent, growing through creative conflict. Your conflicts are stepping stones to your evolution.",
    other_expression="You are a dynamic disruptor, evolving by challenging both yourself and others. Your challenges are your catalysts."
)

# Opposition
uranus_asc_opp = UranusAscendantAspectInterpretation(
    aspect="Opposition",
    hook="Your reflection is radical  and  you meet change through others.",
    core_interpretation="With Uranus opposite Ascendant, your individuality is highlighted through relationships. You see your unique traits reflected in others, learning to balance freedom with connection. Your relationships are mirrors to your soul.",
    male_expression="You are a reflective rebel, discovering yourself through partnership contrasts. These contrasts are your guides.",
    female_expression="You are a charged mirror, learning belonging by embracing differences. Your differences are your gifts.",
    other_expression="You are a relational raver, finding your identity through mirrored contrasts. These contrasts are your path to self and discovery."
)

uranus_ascendant_aspects = {
    "Conjunction": uranus_asc_conj,
    "Sextile": uranus_asc_sext,
    "Trine": uranus_asc_trine,
    "Square": uranus_asc_square,
    "Opposition": uranus_asc_opp
}
