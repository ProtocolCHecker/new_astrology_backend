class SunUranusAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Sun Conjunct Uranus
sun_conjunct_uranus = SunUranusAspectInterpretation(
    aspect="Conjunct",
    hook="You break every mold they try to fit you in.",
    core_interpretation="You have an electric need to be authentically yourself, even when it makes others uncomfortable or challenges the status quo. Your independence isn't just a preference – it's essential to your survival, and you'll resist any attempt to box you in or make you conform to expectations.",
    male_expression="You naturally challenge authority and conventional thinking, but need to channel your rebellious energy constructively. Your boldness inspires others, though you must learn when to pick your battles.",
    female_expression="You refuse to dim your uniqueness to make others comfortable, living by your own rules rather than society's expectations. Your authenticity gives others permission to be themselves too.",
    other_expression="You're wired to disrupt and awaken, but your challenge is doing so without isolating yourself from meaningful connections. Your gift is showing others that being different is not just okay – it's necessary."
)

# Sun Sextile Uranus
sun_sextile_uranus = SunUranusAspectInterpretation(
    aspect="Sextile",
    hook="You bring fresh air to every room you enter.",
    core_interpretation="You have a natural talent for introducing new ideas and perspectives without creating chaos or resistance from others. Your progressive thinking feels approachable rather than threatening, making you an effective bridge between old ways and new possibilities.",
    male_expression="You lead change through collaboration rather than confrontation, making innovation feel accessible to everyone. Your openmindedness creates space for others to evolve alongside you.",
    female_expression="You embody a refreshing blend of wisdom and forwardthinking that draws people to you naturally. Your ability to see potential in everyone helps others discover their own uniqueness.",
    other_expression="You're a natural reformer who updates traditions without destroying their value, helping communities grow and adapt. Your gift is making progress feel exciting rather than scary."
)

# Sun Trine Uranus
sun_trine_uranus = SunUranusAspectInterpretation(
    aspect="Trine",
    hook="Your uniqueness flows like music.",
    core_interpretation="You express your individuality with such natural grace that others are inspired rather than intimidated by your originality. You have an effortless ability to embrace change and help others see the beauty in being different.",
    male_expression="You radiate confidence in your uniqueness, encouraging others to express their authentic selves without fear. Your innovative spirit feels contagious and uplifting rather than disruptive.",
    female_expression="You embody freedom and authenticity in a way that makes others feel safe to explore their own individuality. Your presence alone gives people permission to be more themselves.",
    other_expression="You're a natural catalyst for positive change, helping others evolve simply by being authentically yourself. Your gift is making transformation feel joyful and natural rather than forced."
)

# Sun Square Uranus
sun_square_uranus = SunUranusAspectInterpretation(
    aspect="Square",
    hook="You rebel against your own shadow.",
    core_interpretation="You feel torn between wanting recognition and rejecting any attempts to control or define you, creating an internal war that can make you appear unpredictable. Your challenge is learning that true freedom comes from conscious choice, not automatic rebellion against everything.",
    male_expression="You have explosive bursts of independence that can push people away, but your growth lies in channeling this energy purposefully. Your power emerges when you choose your battles instead of fighting everything on principle.",
    female_expression="You struggle with fitting into roles that others expect while honoring your need to be wildly authentic. Your breakthrough comes when you realize you can be both connected and free.",
    other_expression="You're fighting a battle between your need for acceptance and your need for complete autonomy, but integration brings wisdom. Your healing happens when you stop seeing every boundary as a cage."
)

# Sun Opposition Uranus
sun_opposition_uranus = SunUranusAspectInterpretation(
    aspect="Opposition",
    hook="You find yourself in every rebel you meet.",
    core_interpretation="You tend to attract people who mirror your own unconventional nature, creating relationships that feel both magnetic and unstable. Your lesson involves learning that you can be uniquely yourself without having to choose between belonging and freedom.",
    male_expression="You're drawn to intensity and change but may swing between craving stability and running from it. Your balance comes through conscious selfawareness rather than reactive choices.",
    female_expression="You see your own wild spirit reflected in others, which both excites and challenges you to define yourself clearly. Your growth happens when you stop projecting your rebellion onto others.",
    other_expression="You're learning that true individuality doesn't require separation from others but rather conscious choice about how you connect. Your wholeness comes through embracing both your need for uniqueness and your need for relationship."
)

# Store all Sun–Uranus aspect interpretations
sun_uranus_aspects = {
    "Conjunct": sun_conjunct_uranus,
    "Sextile": sun_sextile_uranus,
    "Trine": sun_trine_uranus,
    "Square": sun_square_uranus,
    "Opposition": sun_opposition_uranus
}