class NeptuneAscendantAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
neptune_asc_conj = NeptuneAscendantAspectInterpretation(
    aspect="Conjunction",
    hook="Your feelings drift like a soft mist and empathy and imagination flow together.",
    core_interpretation="You feel emotions very deeply and can sense what others need. Simple self care routines help you stay balanced and happy.",
    male_expression="You pick up on people's emotions easily and offer comfort without a word. Taking breaks to recharge keeps your heart from getting overwhelmed.",
    female_expression="Your intuition and kindness create a safe space for everyone around you. Remember to set gentle limits so you don't give all your energy away.",
    other_expression="Your caring nature lifts others up in quiet, powerful ways. Pairing a bit of “you time” with your giving side keeps you healthy."
)

# Sextile
neptune_asc_sextile = NeptuneAscendantAspectInterpretation(
    aspect="Sextile",
    hook="You feel with gentle grace and kindness and insight go hand in hand.",
    core_interpretation="You comfort people naturally, and your warm presence is a gift. Taking a few moments each day to reflect makes your care even stronger.",
    male_expression="Your soft touch and understanding way heal others easily. A short pause now and then helps you stay clear headed.",
    female_expression="Your caring words and actions bring calm to any situation. Setting small personal rituals keeps your empathy from draining you.",
    other_expression="Your ability to listen and respond with warmth makes you unforgettable. Balancing that with quiet reflection keeps your spirit bright."
)

# Trine
neptune_asc_trine = NeptuneAscendantAspectInterpretation(
    aspect="Trine",
    hook="Your heart whispers in dreams and your sensitivity feels natural.",
    core_interpretation="You connect with people on a deep level without trying. Adding simple daily habits helps you share your warmth without getting lost in others' problems.",
    male_expression="Your gentle strength makes others feel safe and heard. Keeping a small routine of your own keeps your heart open and steady.",
    female_expression="Your tender support and easy kindness inspire trust. A little solitude now and then refills your emotional well.",
    other_expression="Your caring presence brings peace wherever you go. Pairing that with “me time” makes your compassion lasting."
)

# Square
neptune_asc_square = NeptuneAscendantAspectInterpretation(
    aspect="Square",
    hook="Your emotions can feel blurry and tension calls you to find clarity.",
    core_interpretation="You swing between strong feelings and daydreams, which can be confusing. Taking short breaks to ground yourself helps turn that tension into creative energy.",
    male_expression="Your big heart sometimes leaves you drained and simple grounding exercises bring calm. A few deep breaths can sharpen your focus.",
    female_expression="Your dreamy compassion can drift without direction and short rituals keep you centered. A walk outside helps you see things clearly.",
    other_expression="Your emotional ups and downs fuel your art and empathy. Small pauses turn that power into purpose."
)

# Opposition
neptune_asc_opp = NeptuneAscendantAspectInterpretation(
    aspect="Opposition",
    hook="Your heart sees itself in others and relationships reflect your feelings.",
    core_interpretation="You learn about your own needs through your closest bonds. Balancing giving and receiving makes every connection stronger.",
    male_expression="You mirror your partner's emotions and grow from it. Asking for support in return keeps your heart from emptying out.",
    female_expression="You feel others' pain as deeply as your own and learn from it. Letting people care for you too builds healthier bonds.",
    other_expression="Your shared empathy teaches you about your own limits. Mutual support helps your kindness stay alive."
)

neptune_asc_aspects = {
    "Conjunction": neptune_asc_conj,
    "Sextile": neptune_asc_sextile,
    "Trine": neptune_asc_trine,
    "Square": neptune_asc_square,
    "Opposition": neptune_asc_opp
}
