class SaturnAscendantAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
saturn_asc_conj = SaturnAscendantAspectInterpretation(
    aspect="Conjunction",
    hook="You present restraint  and  your appearance and identity wear the weight of responsibility.",
    core_interpretation="With Saturn conjunct your Ascendant, you have a reserved and serious demeanor. You are cautious in how you present yourself, and your strong sense of duty matures with time.",
    male_expression="You are quietly authoritative, learning confidence through steady self and reliance. Embrace this journey.",
    female_expression="You are composed and conscientious, blossoming as you shed early inhibitions. This growth is your strength.",
    other_expression="You are a solemn shaper of self; your presence strengthens as you own your responsibilities. This is a powerful aspect of your nature."
)

# Sextile
saturn_asc_sextile = SaturnAscendantAspectInterpretation(
    aspect="Sextile",
    hook="You underlay discipline with approachability  and  structure supports your authentic presence.",
    core_interpretation="With Saturn sextile your Ascendant, you exude calm confidence and reliability. Your grounded and mature persona is one that others trust.",
    male_expression="You are steady and reliable, blending warmth with integrity. This balance is a gift to those around you.",
    female_expression="You are balanced and poised, showing up with integrity and grace. Your presence is a source of strength.",
    other_expression="You are a responsible self; your confidence flows through practiced composure. Embrace this aspect of yourself."
)

# Trine
saturn_asc_trine = SaturnAscendantAspectInterpretation(
    aspect="Trine",
    hook="You wear experience with ease  and  maturity balances your demeanor.",
    core_interpretation="With Saturn trine your Ascendant, you possess natural dignity and self and control. You assume leadership with ease and have a respected, grounded presence.",
    male_expression="You are confident and grounded; your presence feels anchored. This stability is a source of strength for you and others.",
    female_expression="You are elegant and self and assured, commanding respect through poise. Your demeanor is a reflection of your inner strength.",
    other_expression="You are a poised figure; your inner discipline manifests quietly in who you are. This is a beautiful aspect of your nature."
)

# Square
saturn_asc_square = SaturnAscendantAspectInterpretation(
    aspect="Square",
    hook="You encounter your own limits  and  tension between who you are and who you become fuels growth.",
    core_interpretation="With Saturn square your Ascendant, you experience friction in self and expression and image. This prompts inner pressure that can lead to self and improvement through overcoming barriers.",
    male_expression="You are reserved yet restless, finding growth through self and discipline. Embrace this journey of self and improvement.",
    female_expression="You are tense and evolving, refining your identity by pushing through boundaries. This process is a source of strength for you.",
    other_expression="You are a tension and refined self; your presence grows stronger through effort. This resilience is a powerful aspect of your nature."
)

# Opposition
saturn_asc_opp = SaturnAscendantAspectInterpretation(
    aspect="Opposition",
    hook="Your identity is tested against others  and  you learn who you are through mirrored limitations.",
    core_interpretation="With Saturn opposite your Ascendant, you reflect inner authority and boundaries through relationships. You learn that self and definition is found in balancing independence and partnership.",
    male_expression="You are reflective in others' eyes; your boundary strength builds through connection. Cherish these insights.",
    female_expression="You are strengthened through relationships, learning about yourself through relational structures. This growth is a source of empowerment.",
    other_expression="You are a relational self and builder; you grow in awareness of self and other interplay. Embrace this journey of mutual growth."
)

saturn_ascendant_aspects = {
    "Conjunction": saturn_asc_conj,
    "Sextile": saturn_asc_sextile,
    "Trine": saturn_asc_trine,
    "Square": saturn_asc_square,
    "Opposition": saturn_asc_opp
}
