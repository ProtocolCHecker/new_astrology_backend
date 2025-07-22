class SunVenusAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Sun Conjunct Venus
sun_conjunct_venus = SunVenusAspectInterpretation(
    aspect="Conjunct",
    hook="You're magnetic without even trying.",
    core_interpretation="You naturally draw people to you through your warmth and genuine appreciation for beauty and harmony in all its forms. Your identity is closely tied to being loved and creating pleasant experiences for others, though you may sometimes avoid necessary conflicts to keep the peace.",
    male_expression="You have an effortless charm that opens doors and hearts, but you need to ensure your niceness doesn't become a mask. Your gift is making others feel valued and appreciated just by being yourself.",
    female_expression="You radiate a natural elegance and grace that others find irresistible, though your worth runs much deeper than your ability to please. Your challenge is learning to value yourself as much as you value harmony with others.",
    other_expression="You're a natural diplomat who can find common ground in almost any situation, bringing out the best in people. Your growth comes through balancing your need to be loved with your need to be authentic."
)

# Sun Sextile Venus
sun_sextile_venus = SunVenusAspectInterpretation(
    aspect="Sextile",
    hook="You make life more beautiful wherever you go.",
    core_interpretation="You have a natural talent for creating harmony and bringing out the beauty in people and situations around you. Your gentle approach to life allows you to build meaningful relationships while maintaining your own sense of self without losing yourself in others.",
    male_expression="You connect with others through genuine warmth and interest, creating relationships based on mutual respect and affection. Your diplomatic skills help you navigate social situations with grace and effectiveness.",
    female_expression="You embody a perfect balance of strength and softness, drawing people close while maintaining your own boundaries. Your natural sense of style and harmony influences others in positive ways.",
    other_expression="You're gifted at finding the sweet spot between giving and receiving, creating relationships that feel both supportive and balanced. Your presence brings a sense of ease and beauty to any environment."
)

# Sun Trine Venus
sun_trine_venus = SunVenusAspectInterpretation(
    aspect="Trine",
    hook="Love flows through you like sunlight.",
    core_interpretation="You express affection and appreciation so naturally that others feel genuinely valued in your presence. Your ability to see and celebrate beauty creates an atmosphere where relationships and creativity can flourish effortlessly.",
    male_expression="You embody the perfect gentleman, treating others with genuine respect and kindness that feels authentic rather than performative. Your natural charm and warmth make you someone people genuinely enjoy being around.",
    female_expression="You radiate a confident femininity that celebrates both inner and outer beauty without vanity or insecurity. Your selflove is so genuine that it gives others permission to love themselves too.",
    other_expression="You're a natural creator of beauty and harmony, whether through art, relationships, or simply your way of moving through the world. Your gift is making others feel seen and appreciated for who they truly are."
)

# Sun Square Venus
sun_square_venus = SunVenusAspectInterpretation(
    aspect="Square",
    hook="You want love but fear losing yourself in it.",
    core_interpretation="You struggle with balancing your need for affection and approval with your need to maintain your own identity and values. This tension can make you alternate between being overly accommodating and suddenly asserting yourself in ways that surprise others.",
    male_expression="You may find yourself trying too hard to be liked, sometimes compromising your authentic self for acceptance. Your growth comes through learning that real charm comes from genuine confidence, not peoplepleasing.",
    female_expression="You battle between wanting to be beautiful and lovable while also wanting to be respected for your substance and strength. Your breakthrough happens when you realize you don't have to choose between being attractive and being authentic.",
    other_expression="You're learning that true harmony comes from honest expression rather than keeping everyone happy at your own expense. Your challenge is finding ways to maintain relationships while honoring your own needs and values."
)

# Sun Opposition Venus
sun_opposition_venus = SunVenusAspectInterpretation(
    aspect="Opposition",
    hook="You see your worth reflected in others' eyes.",
    core_interpretation="You tend to define your value through your relationships and how others respond to you, creating a dynamic where you give away your power to those you love. Your journey involves learning to appreciate yourself independently of external validation or romantic partnerships.",
    male_expression="You may find yourself swinging between being overly focused on pleasing partners and asserting your independence too strongly. Your balance comes through developing selfworth that doesn't depend on others' approval.",
    female_expression="You might lose yourself in relationships or put others' needs so far above your own that you forget what you actually want. Your healing comes through learning to love yourself as much as you love others.",
    other_expression="You're discovering that healthy relationships require you to show up as a whole person rather than molding yourself to fit others' expectations. Your growth happens when you stop seeking completion through others and start creating it within yourself."
)

# Store all Sun–Venus aspect interpretations
sun_venus_aspects = {
    "Conjunct": sun_conjunct_venus,
    "Sextile": sun_sextile_venus,
    "Trine": sun_trine_venus,
    "Square": sun_square_venus,
    "Opposition": sun_opposition_venus
}