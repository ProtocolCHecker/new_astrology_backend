class UranusAscendantAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
uranus_asc_conj = UranusAscendantAspectInterpretation(
    aspect="Conjunction",
    hook="You were never meant to blend in.",
    core_interpretation="You carry a presence that's hard to ignore and unpredictable, bold, and unmistakably original. People may not always understand you, but you were never here to follow anyone else's script.",
    male_expression="You walk into a room and shake things up without saying a word. Being different isn't your act and it's your truth, and that truth sets you apart.",
    female_expression="Your look, your vibe, your energy and it all says ‘I'm not here to fit in, I'm here to be real.' Others may project their discomfort onto you, but deep down they wish they had your courage.",
    other_expression="You don't wear your identity like a costume and it's alive, changing, and completely your own. You challenge norms simply by existing as yourself, and that's your quiet revolution."
)

# Sextile
uranus_asc_sextile = UranusAscendantAspectInterpretation(
    aspect="Sextile",
    hook="Your difference draws people in.",
    core_interpretation="You express your uniqueness in a way that feels playful and light, making others feel like they have permission to be more themselves. You're not here to provoke and you're here to inspire by simply being you.",
    male_expression="You mix charm with originality in a way that makes people curious about your story. Your vibe says ‘different' without ever needing to shout.",
    female_expression="You glow with an inviting kind of originality and one that feels approachable, not intimidating. Your creativity is part of your everyday way of being.",
    other_expression="You make being unconventional feel easy and fun, often becoming a source of inspiration without even realizing it. People feel freer just by being around you."
)

# Trine
uranus_asc_trine = UranusAscendantAspectInterpretation(
    aspect="Trine",
    hook="Being yourself feels effortless.",
    core_interpretation="You don't force originality and it flows through you with grace. You come across as effortlessly different in a way that others find refreshing, even uplifting.",
    male_expression="You lead by example without trying to lead at all. Your steady originality makes people rethink what it means to be authentic.",
    female_expression="You're the kind of different that feels elegant and natural, like it was always meant to be that way. People admire how comfortable you are in your own skin.",
    other_expression="You bring a quiet kind of freedom to the world around you. Just by being fully yourself, you invite others to explore what that might mean for them too."
)

# Square
uranus_asc_square = UranusAscendantAspectInterpretation(
    aspect="Square",
    hook="You struggle with being too much and or not enough.",
    core_interpretation="You often feel torn between wanting to be true to yourself and the pressure to tone it down to be accepted. This push pull can lead to sudden shifts in how you present yourself, but it's also the spark behind your personal growth.",
    male_expression="You've probably been told you're ‘too intense' or ‘too much.' But those raw edges are where your real magic lives and you're just learning how to own them.",
    female_expression="You may have grown up feeling like you had to choose between fitting in and being yourself. The truth is, your power lies in finding your own way and no compromise needed.",
    other_expression="You're wired for change, but that change can feel like conflict and especially with yourself. You grow every time you learn how to stay true without needing to burn it all down."
)

# Opposition
uranus_asc_opp = UranusAscendantAspectInterpretation(
    aspect="Opposition",
    hook="Others reflect your wild side back to you.",
    core_interpretation="You discover your individuality through the relationships and contrasts you experience with others. It's like looking in a mirror that shows you parts of yourself you didn't know were there and sometimes thrilling, sometimes unsettling.",
    male_expression="You attract people who challenge you to be more yourself, even when it feels uncomfortable. Those relationships are not distractions and they're lessons.",
    female_expression="You often meet people who seem completely different, but they reveal truths you've been hiding from yourself. Through them, you learn who you really are.",
    other_expression="Your identity gets shaped through the contrasts and connections you experience. Each person you meet becomes a chance to either break free or break open and and sometimes both."
)

# Store all Uranus–Ascendant aspect interpretations
uranus_ascendant_aspects = {
    "Conjunction": uranus_asc_conj,
    "Sextile": uranus_asc_sextile,
    "Trine": uranus_asc_trine,
    "Square": uranus_asc_square,
    "Opposition": uranus_asc_opp
}
