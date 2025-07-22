class VenusAscendantAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
venus_asc_conj = VenusAscendantAspectInterpretation(
    aspect="Conjunction",
    hook="You attract without trying.",
    core_interpretation="There's something about you and your smile, your style, your presence and that draws people in. You naturally make others feel good, but your real growth lies in building depth beneath that charm.",
    male_expression="You give off warmth and style that people gravitate toward. Just be sure your confidence grows from within, not just from how others respond to you.",
    female_expression="You radiate beauty in the way you carry yourself and it's part of who you are. The key is remembering that your value goes far beyond your looks.",
    other_expression="You've got that unspoken glow that makes people take notice. But your greatest strength comes from blending outer grace with inner truth."
)

# Sextile
venus_asc_sext = VenusAscendantAspectInterpretation(
    aspect="Sextile",
    hook="You make people feel at ease around you.",
    core_interpretation="You naturally put people in a good mood and your presence is soft, inviting, and sincere. You bring harmony without effort, and your ability to connect helps open doors wherever you go.",
    male_expression="You come across as easy to talk to, and people often feel drawn to your vibe. Your quiet magnetism makes you someone people want to be around.",
    female_expression="You bring both beauty and kindness into a room, and others feel safe to open up with you. Your charm is real because it comes from a good place.",
    other_expression="You carry yourself with grace and approachability. Your charm isn't loud and it flows, creating space for genuine connection."
)

# Trine
venus_asc_trine = VenusAscendantAspectInterpretation(
    aspect="Trine",
    hook="Your beauty feels effortless and real.",
    core_interpretation="You move through the world with a natural sense of style and harmony, making social situations smoother and relationships easier. There's a quiet grace about you that puts others at ease.",
    male_expression="You're refined, confident, and naturally tuned in to what feels right. Your style never feels forced and it reflects who you are.",
    female_expression="You bring warmth and elegance just by being yourself. Your authenticity is what makes your beauty magnetic.",
    other_expression="You carry a calm, harmonious energy that others notice without you having to say a word. You don't just look good and you feel good to be around."
)

# Square
venus_asc_square = VenusAscendantAspectInterpretation(
    aspect="Square",
    hook="You wrestle with how you're seen.",
    core_interpretation="You may struggle between wanting to be liked and wanting to be real. This tension pushes you to get clear about your values and and to build confidence that isn't based on appearance alone.",
    male_expression="You may rely too much on charm to smooth things over, but it doesn't always feel true. Real strength comes when you show up as your whole self.",
    female_expression="You can feel torn between expressing your softness and being taken seriously. Learning to be both beautiful and bold is your path to peace.",
    other_expression="There's tension in how you present yourself and sometimes polished, sometimes raw. But through that conflict, you find a style that's truly your own."
)

# Opposition
venus_asc_opp = VenusAscendantAspectInterpretation(
    aspect="Opposition",
    hook="Others reflect your beauty back to you.",
    core_interpretation="You often see your value through how others respond to you, especially in close relationships. The journey here is learning to feel beautiful and lovable from the inside, not just through attention or approval.",
    male_expression="You learn who you are by how people treat you and but real growth begins when you stop relying on their gaze to define your worth.",
    female_expression="Relationships teach you what kind of love and presence you truly want to embody. You're here to balance your need for closeness with your need to be fully seen.",
    other_expression="Your charm often draws strong reactions from others and good and bad. Every mirror you meet is a chance to claim your beauty on your own terms."
)

# Store all Venus–Ascendant aspect interpretations
venus_ascendant_aspects = {
    "Conjunction": venus_asc_conj,
    "Sextile": venus_asc_sext,
    "Trine": venus_asc_trine,
    "Square": venus_asc_square,
    "Opposition": venus_asc_opp
}
