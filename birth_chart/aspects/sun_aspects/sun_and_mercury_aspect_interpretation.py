class SunMercuryAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Sun Conjunct Mercury
sun_conjunct_mercury = SunMercuryAspectInterpretation(
    aspect="Conjunct",
    hook="I think, therefore I shine  and my mind and identity speak in unison.",
    core_interpretation="You have a brilliant fusion of mind and identity that makes you a natural communicator and quick thinker. While you excel at expressing yourself, you sometimes struggle with truly listening because your mind is always racing ahead.",
    male_expression="You're clever and assertive, using logic to define who you are. Learning the power of quiet observation will unlock deeper wisdom.",
    female_expression="You're lively and articulate, blending mental strength with natural warmth. Your growth comes from trusting your own voice, not just your knowledge.",
    other_expression="You're mentally radiant and express your authenticity through thought. You feel most alive when sharing ideas, learning, and thinking aloud with others."
)

# Sun Sextile Mercury
sun_sextile_mercury = SunMercuryAspectInterpretation(
    aspect="Sextile",
    hook="Your thoughts flow like golden honey  and sweet, smooth, and irresistible.",
    core_interpretation="You have a natural gift for communication that feels effortless and charming, making complex topics accessible with perfect timing. However, you sometimes avoid deeper conversations in favor of keeping things pleasant and smooth.",
    male_expression="You communicate with natural ease and charm, making others feel comfortable. Your challenge is diving deeper into uncomfortable truths when necessary.",
    female_expression="You have a graceful way with words that draws people in naturally. Your power grows when you're willing to speak difficult truths with the same elegance.",
    other_expression="You express yourself with natural flow and warmth. Your gift is making others feel heard while sharing your own authentic perspective."
)

# Sun Trine Mercury
sun_trine_mercury = SunMercuryAspectInterpretation(
    aspect="Trine",
    hook="Your mind is your crown jewel  and polished, brilliant, and impossible to ignore.",
    core_interpretation="You possess exceptional clarity in thinking and expressing yourself with both intelligence and confidence. While this gift serves you well, you might take your mental abilities for granted and need to push yourself toward more challenging territory.",
    male_expression="You think and speak with natural authority and clarity. Your growth comes from challenging yourself intellectually rather than coasting on natural talent.",
    female_expression="You express your intelligence with grace and confidence that inspires others. Your journey involves using your mental gifts to tackle bigger, more meaningful challenges.",
    other_expression="You have a brilliant mind that works in perfect harmony with who you are. Your potential unlocks when you use these gifts to explore uncharted mental territories."
)

# Sun Square Mercury
sun_square_mercury = SunMercuryAspectInterpretation(
    aspect="Square",
    hook="Your mind and ego are locked in an eternal wrestling match  and and that's your secret weapon.",
    core_interpretation="You experience internal tension between what you think and how you want to be seen, creating a dynamic but sometimes exhausting mental landscape. This inner conflict pushes you to develop unique perspectives and original thinking that others find fascinating.",
    male_expression="You wrestle with self doubt about your ideas, but this struggle creates original thinking. Your breakthrough comes when you stop fighting yourself and start listening.",
    female_expression="You sometimes question your own intelligence unnecessarily, yet your mind works in wonderfully unique ways. Embracing your different thinking style is your superpower.",
    other_expression="You have a restless, questioning mind that sometimes feels at odds with itself. This internal tension is actually the source of your most creative insights."
)

# Sun Opposition Mercury
sun_opposition_mercury = SunMercuryAspectInterpretation(
    aspect="Opposition",
    hook="You see both sides of everything  and a gift that can feel like a curse.",
    core_interpretation="You have an exceptional ability to understand multiple perspectives, which creates internal conflict about what you truly believe. While this can lead to indecision, it also gives you remarkable objectivity and skill at mediating between different people and ideas.",
    male_expression="You excel at seeing all sides but struggle with decisive action. Your strength emerges when you learn to trust your gut alongside your analytical mind.",
    female_expression="You have a gift for understanding others' perspectives that sometimes overshadows your own voice. Your power lies in honoring your own truth while remaining open to others.",
    other_expression="You naturally balance different viewpoints but may lose yourself in the process. Your challenge is maintaining your own perspective while embracing your gift for understanding others."
)

# Dictionary of all Sun Mercury aspect interpretations
sun_mercury_aspects = {
    "Conjunct": sun_conjunct_mercury,
    "Sextile": sun_sextile_mercury,
    "Trine": sun_trine_mercury,
    "Square": sun_square_mercury,
    "Opposition": sun_opposition_mercury
}