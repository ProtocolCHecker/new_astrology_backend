class UranusSunAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
uranus_sun_conj = UranusSunAspectInterpretation(
    aspect="Conjunction",
    hook="You were born to break the mold.",
    core_interpretation="You shine brightest when you're free to be yourself and raw, different, and completely untamed. Your path isn't about fitting in; it's about showing others what freedom looks like in human form.",
    male_expression="You live by your own code and expect others to keep up. But real strength comes when you use your individuality to lead, not just shock.",
    female_expression="You're wired for authenticity, no matter the cost. Your presence challenges others to wake up and do the same.",
    other_expression="You walk into rooms like change itself. Your energy shifts things just by being real and and people feel it, whether they're ready or not."
)

# Sextile
uranus_sun_sextile = UranusSunAspectInterpretation(
    aspect="Sextile",
    hook="You make being different look effortless.",
    core_interpretation="You express yourself with a blend of originality and charm, making others feel like it's safe and and even fun and to be a little freer. Your creativity doesn't demand attention; it earns it.",
    male_expression="You bring new ideas to life with style, not force. People listen because your authenticity feels both fresh and relatable.",
    female_expression="You radiate an easy kind of confidence that makes standing out feel natural. Your originality isn't loud, but it is unforgettable.",
    other_expression="You offer the world a smooth, magnetic version of rebellion and one that changes things without needing to clash first."
)

# Trine
uranus_sun_trine = UranusSunAspectInterpretation(
    aspect="Trine",
    hook="You grow by being true to yourself.",
    core_interpretation="Your sense of identity flows with freedom, making it easy for you to evolve without resistance. You move through change with confidence, inspiring others to do the same just by watching you.",
    male_expression="You adapt with ease and bring vision into everything you do. Your quiet self assurance shows people that evolution can be graceful.",
    female_expression="You carry your individuality like light and soft, strong, and constant. Change doesn't throw you off; it lifts you higher.",
    other_expression="You show how being fully yourself can feel stable, not scary. Your gift is moving forward while staying grounded in who you are."
)

# Square
uranus_sun_square = UranusSunAspectInterpretation(
    aspect="Square",
    hook="Your freedom and your identity don't always agree.",
    core_interpretation="You often feel torn between being accepted and being true to who you are. This internal tug of war creates the friction that fuels your biggest breakthroughs and if you're willing to face the discomfort.",
    male_expression="You challenge rules just by existing, but that fight can wear you out if it's constant. Your power grows when you stop needing to prove your difference.",
    female_expression="You can burn hot and especially when you feel boxed in. The key is channeling that intensity into creating something that actually frees you.",
    other_expression="You carry an engine for change, but sometimes it turns on yourself. The growth comes when you learn how to rebel with direction and not just reaction."
)

# Opposition
uranus_sun_opp = UranusSunAspectInterpretation(
    aspect="Opposition",
    hook="You see yourself in the ones who challenge you.",
    core_interpretation="Your growth often shows up through the people who push your buttons the most. These relationships mirror parts of you that are still evolving and and through them, you get closer to your real self.",
    male_expression="You meet your reflection in those who won't let you stay the same. The tension they bring helps you become more of who you actually are.",
    female_expression="You're drawn to people who challenge your sense of identity and and through them, you uncover your truth. Relationship is your revolution.",
    other_expression="You grow through contrast, often learning who you are by seeing who you're not. The freedom you crave often shows up through someone else's mirror."
)

# Store all Uranus–Sun aspect interpretations
uranus_sun_aspects = {
    "Conjunction": uranus_sun_conj,
    "Sextile": uranus_sun_sextile,
    "Trine": uranus_sun_trine,
    "Square": uranus_sun_square,
    "Opposition": uranus_sun_opp
}
