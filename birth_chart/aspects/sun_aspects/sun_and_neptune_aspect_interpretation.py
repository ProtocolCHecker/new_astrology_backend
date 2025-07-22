class SunNeptuneAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Sun Conjunct Neptune
sun_conjunct_neptune = SunNeptuneAspectInterpretation(
    aspect="Conjunct",
    hook="I build bridges between dreams and reality and architect of the impossible.",
    core_interpretation="You have the rare ability to give structure to your dreams and make the intangible tangible through disciplined creativity. However, you may struggle with periods of disillusionment when reality clashes with your ideals, creating cycles of inspiration followed by harsh selfcriticism.",
    male_expression="You're a visionary with practical skills, but may become overly critical when dreams don't manifest quickly. Your power lies in patient dedication to meaningful work.",
    female_expression="You can manifest beautiful dreams through steady effort, yet may doubt your intuitive gifts when they conflict with logic. Your strength comes from trusting both vision and discipline.",
    other_expression="You're learning to honor both your spiritual longings and earthly responsibilities. Your gift is showing others that dreams need structure to become real."
)

# Sun Sextile Neptune
sun_sextile_neptune = SunNeptuneAspectInterpretation(
    aspect="Sextile",
    hook="Your dreams have backbone and inspired visions with solid foundations.",
    core_interpretation="You naturally blend imagination with practicality, creating sustainable approaches to your ideals and spiritual pursuits. Your disciplined approach to creativity or service allows you to make meaningful contributions while staying grounded in reality.",
    male_expression="You're able to pursue your ideals through consistent action without losing sight of practical needs. Your challenge is not becoming too methodical in your spiritual approach.",
    female_expression="You bring wisdom and structure to your intuitive gifts, making them accessible to others. Your growth comes through trusting the mystery alongside your planning.",
    other_expression="You're a practical mystic who can organize inspiration into meaningful action. Your gift is showing that spiritual growth requires both vision and commitment."
)

# Sun Trine Neptune
sun_trine_neptune = SunNeptuneAspectInterpretation(
    aspect="Trine",
    hook="You turn water into wine and effortlessly transforming dreams into form.",
    core_interpretation="You have exceptional ability to manifest your spiritual and creative visions through patient, dedicated work. Your approach to idealism is mature and sustainable, allowing you to create lasting beauty or meaning without losing touch with practical realities.",
    male_expression="You're naturally gifted at bringing dreams into reality through disciplined effort. Your challenge is not becoming complacent about your natural ability to manifest.",
    female_expression="You have a graceful way of weaving spirituality into daily life and work. Your growth comes through pushing beyond comfortable manifestations to bigger visions.",
    other_expression="You're blessed with the ability to make the mystical practical. Your gift is creating tangible beauty and meaning that inspires others to believe in their own dreams."
)

# Sun Square Neptune
sun_square_neptune = SunNeptuneAspectInterpretation(
    aspect="Square",
    hook="Your dreams and duties wage war and caught between what is and what could be.",
    core_interpretation="You experience constant tension between your spiritual ideals and the harsh demands of reality, creating periods of deep disillusionment or escapism. This struggle can lead to either rigid materialism or impractical dreaming, but ultimately teaches you to find sacred meaning within life's limitations.",
    male_expression="You may swing between crushing your dreams with harsh reality or escaping into fantasy. Your breakthrough comes through finding the divine within discipline itself.",
    female_expression="You might feel torn between your spiritual calling and practical obligations, sometimes sacrificing one for the other. Your power emerges when you see both as sacred paths.",
    other_expression="You're learning that limitations can be the birthplace of creativity, not its enemy. Your gift is transforming spiritual crisis into grounded wisdom."
)

# Sun Opposition Neptune
sun_opposition_neptune = SunNeptuneAspectInterpretation(
    aspect="Opposition",
    hook="You live between two worlds and the solid and the sublime, forever seeking balance.",
    core_interpretation="You feel pulled between concrete responsibilities and transcendent longings, often experiencing them as mutually exclusive forces. This creates a lifelong journey of learning to honor both your need for structure and your spiritual nature without sacrificing either completely.",
    male_expression="You may alternate between being overly practical and overly idealistic, struggling to integrate both sides. Your growth comes through seeing discipline as a spiritual practice.",
    female_expression="You might feel you must choose between material security and spiritual fulfillment. Your power lies in discovering that true abundance includes both worldly wisdom and divine connection.",
    other_expression="You're bridging the gap between matter and spirit through lived experience. Your gift is showing others that true mastery includes both earthly competence and heavenly vision."
)

# Dictionary of all SunNeptune aspect interpretations
sun_neptune_aspects = {
    "Conjunct": sun_conjunct_neptune,
    "Sextile": sun_sextile_neptune,
    "Trine": sun_trine_neptune,
    "Square": sun_square_neptune,
    "Opposition": sun_opposition_neptune
}