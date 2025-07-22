class VenusMarsAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
venus_mars_conj = VenusMarsAspectInterpretation(
    aspect="Conjunction",
    hook="You love with fire and touch with passion. Your chemistry is unmistakable.",
    core_interpretation="You blend desire and affection into magnetic intensity, craving excitement in every connection. Channel that heat creatively to avoid impulsive restlessness.",
    male_expression="You pursue romance with bold confidence. Learn to honor emotional nuance as much as you embrace passion.",
    female_expression="Your passion leads the way. Make space for tenderness to balance your vibrant energy.",
    other_expression="You fuse attraction and action seamlessly. Finding healthy outlets for your creativity keeps your spark alive."
)

# Sextile
venus_mars_sextile = VenusMarsAspectInterpretation(
    aspect="Sextile",
    hook="Your desire and charm dance in harmony.",
    core_interpretation="You warm charisma and assertive grace, letting you initiate relationships with ease. Remember to maintain boundaries so your spark doesn't overwhelm.",
    male_expression="You engage with affectionate boldness. Your sincere warmth draws others in, but stay mindful of their pace.",
    female_expression="You lead with sensual confidence. Softening your approach at times helps deepen bonds.",
    other_expression="You strike the perfect balance of give and take. Letting your creativity guide interactions enhances your allure."
)

# Trine
venus_mars_trine = VenusMarsAspectInterpretation(
    aspect="Trine",
    hook="Your heart and will flow together. Attraction feels effortless.",
    core_interpretation="You with a natural blend of passion and harmony, so your relationships feel both exciting and balanced. Stay open to new expressions of beauty and desire.",
    male_expression="You express affection with confident ease. Your smooth grace inspires trust.",
    female_expression="You harmonize passion and pleasure. Embrace fresh creative outlets to keep your energy vibrant.",
    other_expression="You create beauty through dynamic connection. Your effortless style uplifts everyone around you."
)

# Square
venus_mars_square = VenusMarsAspectInterpretation(
    aspect="Square",
    hook="Your passion blazes like wildfire. Sometimes too hot, too fast.",
    core_interpretation="You spark intense desire and occasional friction in love, pushing you to learn patience and healthy boundaries. Transforming that heat into constructive expression leads to deeper fulfillment.",
    male_expression="You dive headfirst into romance. Pausing to listen will temper impulsiveness.",
    female_expression="Your desire burns bright. Softening your approach can turn tension into tenderness.",
    other_expression="You navigate stormy waters of love. Balance your drive with compassion to find steadiness."
)

# Opposition
venus_mars_opp = VenusMarsAspectInterpretation(
    aspect="Opposition",
    hook="Your passion pulls you two ways.",
    core_interpretation="You highlight a dance between attraction and assertion, showing you where you project and where you yearn. Integrating both sides brings harmony and mutual respect in your relationships.",
    male_expression="You spark dynamic chemistry. Seeking self awareness helps you unite desire with connection.",
    female_expression="You find intensity in contrast. Balancing giving and receiving refines your power.",
    other_expression="You grow through mirrored passions. Embracing reflection deepens your emotional mastery."
)

# Store all interpretations
venus_mars_aspects = {
    "Conjunction": venus_mars_conj,
    "Sextile": venus_mars_sextile,
    "Trine": venus_mars_trine,
    "Square": venus_mars_square,
    "Opposition": venus_mars_opp
}