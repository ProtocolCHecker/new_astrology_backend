class UranusMoonAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
uranus_moon_conj = UranusMoonAspectInterpretation(
    aspect="Conjunction",
    hook="Your emotions spark like lightning and unpredictable and alive.",
    core_interpretation="You feel in flashes of insight, and learning steady rhythms brings your brilliance to full bloom.",
    male_expression="Your sudden empathy surprises and awakens and finding grounding anchors your gifts.",
    female_expression="Your spontaneous care delights and steady routines sustain your intuition.",
    other_expression="Your emotional breakthroughs guide you and balancing spark with stillness nurtures growth."
)

# Sextile
uranus_moon_sext = UranusMoonAspectInterpretation(
    aspect="Sextile",
    hook="You feel with flair and emotional freedom flows easily.",
    core_interpretation="Your authentic self shines through every mood, and weaving in small routines keeps that freedom vibrant.",
    male_expression="Your originality comforts others and simple rituals help you recharge.",
    female_expression="Your inventive warmth heals and little anchors ground your spirit.",
    other_expression="Your unique energy uplifts all and steady habits sustain your spark."
)

# Trine
uranus_moon_trine = UranusMoonAspectInterpretation(
    aspect="Trine",
    hook="You ride emotional currents and insight and feeling harmonize.",
    core_interpretation="You balance intuition and stability so gracefully that your presence feels both fresh and comforting.",
    male_expression="Your fluid empathy inspires trust and inviting stability strengthens your flow.",
    female_expression="Your creative caring uplifts and gentle routines amplify your gifts.",
    other_expression="Your harmonious energy guides many and anchoring your vision ensures lasting impact."
)

# Square
uranus_moon_square = UranusMoonAspectInterpretation(
    aspect="Square",
    hook="Your heart rebels and tension births your authenticity.",
    core_interpretation="You break old patterns fiercely, and weaving in moments of calm makes your evolution sustainable.",
    male_expression="Your restless compassion drives change and pausing grounds your efforts.",
    female_expression="Your passionate independence inspires and restful pauses restore your strength.",
    other_expression="Your inner revolution empowers and balance tempers your fire into purpose."
)

# Opposition
uranus_moon_opp = UranusMoonAspectInterpretation(
    aspect="Opposition",
    hook="Your emotions reflect in chaos and others mirror your evolution.",
    core_interpretation="Your relationships push you to grow, and honoring both freedom and closeness deepens your heart.",
    male_expression="Your dynamic care challenges norms and mutual support anchors your journey.",
    female_expression="Your relational spark ignites growth and balanced give and take fuels your path.",
    other_expression="Your shared transformations guide you and interdependence enriches your spirit."
)

uranus_moon_aspects = {
    "Conjunction": uranus_moon_conj,
    "Sextile": uranus_moon_sext,
    "Trine": uranus_moon_trine,
    "Square": uranus_moon_square,
    "Opposition": uranus_moon_opp
}
