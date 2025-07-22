class SaturnMoonAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
saturn_moon_conj = SaturnMoonAspectInterpretation(
    aspect="Conjunction",
    hook="Your heart carries a weight that builds emotional strength.",
    core_interpretation="You bring a deep seriousness to your emotions and a need for self sufficiency. Often stemming from early lessons that emotional expression must be disciplined, you tend toward emotional caution or reserve. You learn resilience through solitude and structure, but it's important to acknowledge your emotional needs and build trusted spaces to feel and heal.",
    male_expression="You are stoic but sensitive, learning strength in vulnerability. Embracing your emotional side will help you connect more deeply with others and find greater fulfillment in your relationships.",
    female_expression="You are composed and caring, blossoming when you trust your emotional wisdom. This journey of self discovery will help you express your feelings more freely and build stronger connections with those around you.",
    other_expression="You are a guarded nurturer, building emotional depth through disciplined openness. This process of learning to trust and express your emotions will enhance your ability to care for others and yourself."
)

# Sextile
saturn_moon_sextile = SaturnMoonAspectInterpretation(
    aspect="Sextile",
    hook="Your feelings blend with discipline, creating a soft and steady presence.",
    core_interpretation="You blend emotional maturity with nurturing, creating reliability in relationships. You offer quiet stability and thoughtful care, balancing empathy with responsibility. Your emotional life is structured yet supportive, making you a calm and dependable presence in others' lives.",
    male_expression="You are steady and supportive, showing love through consistency. This trait makes you a reliable and trusted partner, capable of providing both emotional and practical support.",
    female_expression="You are gentle yet grounded, caring deeply in practical and trustworthy ways. This balance of traits makes you a nurturing and dependable figure, admired for your ability to provide both emotional and tangible support.",
    other_expression="You are a balanced caregiver, offering comfort and reliability in emotional exchange. This ability to provide both emotional and practical care makes you a valued and trusted presence in the lives of those around you."
)

# Trine
saturn_moon_trine = SaturnMoonAspectInterpretation(
    aspect="Trine",
    hook="Your heart and habits align, fostering ease in emotional integrity.",
    core_interpretation="You reflect harmonious emotional strength and discipline, feeling naturally supported by your own inner structure. This allows you to express care responsibly, combining sensitivity with integrity. You are seen as an emotionally mature and reliable companion.",
    male_expression="You are emotionally sure and steady, with a presence that is calming. This trait makes you a grounding and reassuring figure, capable of providing both emotional and practical support.",
    female_expression="You are warm and wise, leading with caring conviction. This balance of traits makes you a nurturing and respected figure, admired for your ability to provide both emotional and tangible care.",
    other_expression="You are a secure emotive presence, balancing feeling with solid support. This ability to provide both emotional and practical care makes you a valued and trusted figure in the lives of those around you."
)

# Square
saturn_moon_square = SaturnMoonAspectInterpretation(
    aspect="Square",
    hook="Your feelings challenge your fears, building emotional strength.",
    core_interpretation="You experience tension between emotional need and inner restraint, often linked to experiences where feelings were discouraged. This aspect can produce emotional inhibition or self criticism, but it also drives growth through learning subtlety, self compassion, and trust in your emotional experience despite inner walls.",
    male_expression="You are sensitive yet guarded, growing by feeling and expressing softly. This journey of emotional exploration will help you build resilience and a stronger sense of self, ultimately leading to personal growth.",
    female_expression="You are cautious but caring, learning to share vulnerable spaces. This process of facing and overcoming emotional challenges will help you refine your ability to care for others and yourself, leading to greater fulfillment in your relationships.",
    other_expression="You have a tension trained heart, softening through emotional courage. This dynamic of facing and resolving emotional tensions will help you develop a more robust and resilient character, capable of providing both emotional and practical support."
)

# Opposition
saturn_moon_opp = SaturnMoonAspectInterpretation(
    aspect="Opposition",
    hook="You seek comfort outside yourself, learning balance through others.",
    core_interpretation="You often reflect emotional needs onto others, leading to cycles of dependency or withdrawal. This dynamic encourages self awareness around authority and nurturing patterns, with integration coming through owning your emotional needs and partnering with trusted figures to build mature emotional foundations.",
    male_expression="You are a relational rock, learning to support and be supported. This balance of giving and receiving emotional care will help you build stronger and more fulfilling relationships.",
    female_expression="You are a reflective nurturer, growing through mutual emotional grounding. This process of understanding and integrating your emotional needs will help you develop a more robust and resilient character, capable of providing both emotional and practical support.",
    other_expression="You are a mirror of emotions, gaining clarity through shared support. This dynamic of understanding and integrating your emotional needs will help you grow into a well rounded and successful individual, capable of providing both emotional and practical care."
)

saturn_moon_aspects = {
    "Conjunction": saturn_moon_conj,
    "Sextile": saturn_moon_sextile,
    "Trine": saturn_moon_trine,
    "Square": saturn_moon_square,
    "Opposition": saturn_moon_opp
}
