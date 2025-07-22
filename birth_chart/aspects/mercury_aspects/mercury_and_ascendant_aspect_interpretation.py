class MercuryAscendantAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Mercury Conjunct Ascendant
mercury_conjunct_ascendant = MercuryAscendantAspectInterpretation(
    aspect="Conjunct",
    hook="You arrive with curiosity. Your mind races ahead before your feet even touch the ground.",
    core_interpretation="You speak and move with remarkable agility. Your swift wit draws people in, though you must guard against blurting before you think.",
    male_expression="You lead conversations with confidence. Practice listening as intently as you speak.",
    female_expression="Your expressiveness charms the room. Ground yourself to temper any restless energy.",
    other_expression="You shine as a lively storyteller. Finding moments of stillness helps your message land."
)

# Mercury Sextile Ascendant
mercury_sextile_ascendant = MercuryAscendantAspectInterpretation(
    aspect="Sextile",
    hook="Your words open doors. Smooth, engaging, and always on point.",
    core_interpretation="You are granted effortless charm in communication. You know precisely how to connect, yet you thrive when you also pause to listen.",
    male_expression="You negotiate with ease. Remember, your greatest strength lies in thoughtful pauses.",
    female_expression="You articulate with grace. Balancing speaking and silence deepens your rapport.",
    other_expression="You're a natural connector. Honoring others' voices amplifies your own."
)

# Mercury Trine Ascendant
mercury_trine_ascendant = MercuryAscendantAspectInterpretation(
    aspect="Trine",
    hook="You speak as naturally as you breathe. Every phrase feels inspired.",
    core_interpretation="You are blessed with seamless self-expression. Your ideas flow with confidence, and you inspire trust when you temper ease with depth.",
    male_expression="You tell stories that captivate. Stretch yourself by exploring new perspectives.",
    female_expression="Your presence feels magnetic. Inviting fresh challenges keeps your spark alive.",
    other_expression="You shine as an intuitive communicator. Embracing complexity enriches your flow."
)

# Mercury Square Ascendant
mercury_square_ascendant = MercuryAscendantAspectInterpretation(
    aspect="Square",
    hook="Your mouth runs ahead of your message. You're mastering the art of mindful speech.",
    core_interpretation="Your Ascendant stirs tension between thought and delivery. As you learn to align presence and purpose, your words gain power without friction.",
    male_expression="You challenge others with sharp insight. Softening your tone widens your influence.",
    female_expression="You think on your feet. Grounding self-trust steadies your voice.",
    other_expression="You grow through honest feedback. Balancing intensity with patience empowers your truth."
)

# Mercury Opposite Ascendant
mercury_opposite_ascendant = MercuryAscendantAspectInterpretation(
    aspect="Opposition",
    hook="Your mirror talks back. You define yourself in every dialogue.",
    core_interpretation="You are drawn into dynamic exchanges. Owning reflections from others refines your voice and fuels authentic connection.",
    male_expression="You thrive on debate. Owning your stance brings clarity to collisions.",
    female_expression="You seek feedback in conversation. Centering your own vision strengthens your expression.",
    other_expression="You learn through reflection. Balancing give and take enriches every exchange."
)

mercury_ascendant_aspects = {
    "Conjunct": mercury_conjunct_ascendant,
    "Sextile": mercury_sextile_ascendant,
    "Trine": mercury_trine_ascendant,
    "Square": mercury_square_ascendant,
    "Opposition": mercury_opposite_ascendant
}