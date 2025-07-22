class SaturnVenusAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
saturn_venus_conj = SaturnVenusAspectInterpretation(
    aspect="Conjunction",
    hook="Your love runs deep and builds slow.",
    core_interpretation="You approach relationships with the patience of a master craftsman, understanding that real love requires time to develop its full beauty. Your connections may start cautiously, but they grow into something unshakeable because you invest in quality over quantity.",
    male_expression="You show love through consistent actions rather than grand gestures, building trust brick by brick. Your loyalty runs so deep that once you commit, you become an unbreakable foundation for those you care about.",
    female_expression="You guard your heart carefully but love with incredible depth when you finally open up. Your relationships mature like fine wine, becoming richer and more precious with each passing year.",
    other_expression="You transform love into something lasting and meaningful, preferring one deep connection over many shallow ones. Your emotional discipline creates space for relationships that can weather any storm."
)

# Sextile
saturn_venus_sextile = SaturnVenusAspectInterpretation(
    aspect="Sextile",
    hook="Love flows through your steady hands.",
    core_interpretation="You have a gift for creating harmony between your heart and your values, building relationships that feel both passionate and secure. Your approach to love combines warmth with wisdom, making others feel cherished and safe in your presence.",
    male_expression="You express affection through thoughtful consistency, showing up in ways that truly matter. Your romantic gestures feel genuine because they're rooted in deep understanding of what your partner needs.",
    female_expression="You create beautiful spaces for love to flourish, blending practicality with tenderness in everything you do. Your caring nature shines through reliable acts of service and gentle attention.",
    other_expression="You bring structure to your relationships without suffocating their natural flow, creating a container where love can grow safely. Your balanced approach to affection makes others feel both free and cherished."
)

# Trine
saturn_venus_trine = SaturnVenusAspectInterpretation(
    aspect="Trine",
    hook="Your heart beats with quiet strength.",
    core_interpretation="You possess an elegant emotional maturity that draws others to you like a magnet, offering love that feels both exciting and reliable. Your natural ability to balance passion with stability creates relationships that are both deeply satisfying and enduring.",
    male_expression="You embody refined strength in love, creating an atmosphere where beauty and substance coexist perfectly. Your appreciation for quality extends to everything you touch, from relationships to creative pursuits.",
    female_expression="You radiate a warm confidence that makes others feel valued and understood in your presence. Your graceful approach to love creates harmony wherever you go, without sacrificing your own needs.",
    other_expression="You effortlessly blend emotional depth with practical wisdom, making love feel both magical and grounded. Your sophisticated approach to relationships inspires others to elevate their own standards."
)

# Square
saturn_venus_square = SaturnVenusAspectInterpretation(
    aspect="Square",
    hook="Love challenges you to grow stronger.",
    core_interpretation="You wrestle with the tension between wanting love and fearing vulnerability, but this inner conflict ultimately teaches you profound lessons about self worth. Your journey with relationships involves learning to trust your own lovability while maintaining healthy boundaries.",
    male_expression="You learn to open your heart through proving your reliability to yourself first, then others. Your cautious approach to love protects you while you develop the confidence to be truly intimate.",
    female_expression="You transform self doubt into self respect through patient work on your relationship patterns. Your sensitivity becomes a strength once you learn to honor your own worth without apology.",
    other_expression="You use relationship challenges as opportunities to build emotional resilience and deeper self understanding. Your most meaningful connections emerge from your willingness to work through difficulties rather than avoid them."
)

# Opposition
saturn_venus_opp = SaturnVenusAspectInterpretation(
    aspect="Opposition",
    hook="Balance teaches you love's true meaning.",
    core_interpretation="You learn about love through experiencing its extremes, discovering how to give without losing yourself and receive without becoming dependent. Your relationships become mirrors that reflect back your deepest values and help you understand what you truly need.",
    male_expression="You master the art of loving without losing your independence, learning to be a partner while remaining whole. Your relationships teach you to balance commitment with personal freedom.",
    female_expression="You discover your own worth through the push and pull of intimate connections, learning to maintain your center while opening your heart. Your partnerships become laboratories for developing authentic self love.",
    other_expression="You develop wisdom about love through experiencing both its challenges and its rewards, becoming a master of healthy relationship dynamics. Your ability to find balance in love inspires others to create more conscious partnerships."
)

saturn_venus_aspects = {
    "Conjunction": saturn_venus_conj,
    "Sextile": saturn_venus_sextile,
    "Trine": saturn_venus_trine,
    "Square": saturn_venus_square,
    "Opposition": saturn_venus_opp
}