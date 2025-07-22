class SunAscendantAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Sun Conjunct Ascendant
sun_conjunct_asc = SunAscendantAspectInterpretation(
    aspect="Conjunct",
    hook="You lead with presence  and  your identity shines the moment you enter a room.",
    core_interpretation="With the Sun conjunct your Ascendant, you have a bold and self and assured personality that naturally takes center stage. You make a strong first impression and are often seen as a leader. Embrace your confidence while balancing it with humility.",
    male_expression="You are charismatic and commanding, projecting strength naturally. Remember to cultivate humility to truly connect with others.",
    female_expression="You are confident and magnetic, often seen as self and possessed or inspiring. Balance your visibility with vulnerability to grow even more.",
    other_expression="You are born to stand out, seeking authenticity through visibility. Align your inner identity with your outer presence to shine."
)

# Sun Sextile Ascendant
sun_sextile_asc = SunAscendantAspectInterpretation(
    aspect="Sextile",
    hook="Your light opens doors  and  expressive, warm, and well and received.",
    core_interpretation="With the Sun sextile your Ascendant, you have a smooth and expressive personality. You are confident without arrogance, naturally liked and respected. Your quiet strength radiates sincerity and approachability.",
    male_expression="You are approachable and enthusiastic, comfortable in your own skin. Channel your leadership with tact to inspire those around you.",
    female_expression="You are gracious and expressive, carrying yourself with calm self and assurance. Your positive presence naturally draws admiration.",
    other_expression="You are a solar diplomat, shining without overpowering. Grow through collaboration while maintaining your individuality."
)

# Sun Trine Ascendant
sun_trine_asc = SunAscendantAspectInterpretation(
    aspect="Trine",
    hook="You move with grace  and  radiant, expressive, and aligned with your path.",
    core_interpretation="With the Sun trine your Ascendant, you experience ease between your identity and expression. You have a regal presence and express yourself with natural grace. Embrace your charisma and sincerity, and use your gifts wisely.",
    male_expression="You are charming and expressive, naturally confident and admired. Seek challenges to stay engaged and continue growing.",
    female_expression="You are elegant and magnetic, with a presence that people trust. Build bridges with your brightness and warmth.",
    other_expression="You are a soulful performer, with your presence aligning with your purpose. You shine brightest when sharing your space with others."
)

# Sun Square Ascendant
sun_square_asc = SunAscendantAspectInterpretation(
    aspect="Square",
    hook="Your light meets friction  and  bold, intense, and sometimes misunderstood.",
    core_interpretation="With the Sun square your Ascendant, you may feel tension between your self and image and how you come across. You might feel misread or misjudged, and could come off as intense. Growth comes from aligning your inner strength with a softer outward expression.",
    male_expression="You are assertive and intense, sometimes clashing with authority. Cultivate emotional intelligence to navigate relationships smoothly.",
    female_expression="You are strong and opinionated, which can be perceived as bold. Understanding how you're perceived will help you grow.",
    other_expression="You are a fierce self and expressor, and others may not always understand you. Learn to match your inner power with outer grace."
)

# Sun Opposition Ascendant
sun_opposition_asc = SunAscendantAspectInterpretation(
    aspect="Opposition",
    hook="You find yourself in others  and  mirrored, relational, and seeking reflection.",
    core_interpretation="With the Sun opposite your Ascendant, you define yourself through relationships. You thrive on personal connections and seek feedback to gain self and awareness. Embrace your gifts in one and on and one dynamics and learn to own your power independently.",
    male_expression="You are relational and reflective, seeking identity through meaningful partnerships. Balance your autonomy with connection to grow.",
    female_expression="You are empathic and responsive, thriving when emotionally mirrored. Affirm yourself outside of relationships to strengthen your sense of self.",
    other_expression="You are a mirror soul, discovering yourself in the gaze of another. Learn to hold your power with and without accompaniment."
)

# Dictionary of all Sun and Ascendant aspects
sun_ascendant_aspects = {
    "Conjunct": sun_conjunct_asc,
    "Sextile": sun_sextile_asc,
    "Trine": sun_trine_asc,
    "Square": sun_square_asc,
    "Opposition": sun_opposition_asc
}
