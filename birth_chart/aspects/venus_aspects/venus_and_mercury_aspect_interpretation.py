class VenusMercuryAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
venus_mercury_conj = VenusMercuryAspectInterpretation(
    aspect="Conjunction",
    hook="Your words carry beauty.",
    core_interpretation="You express yourself with grace and charm, often knowing just what to say to create harmony. Your gift is making people feel seen and heard and though learning to share your deeper truths without sugarcoating takes time.",
    male_expression="You speak with a natural polish that draws others in, but the real magic happens when you let go of perfect and get personal.",
    female_expression="You express love through words and presence, often with a soft, poetic rhythm. The journey lies in opening up without hiding behind pleasantries.",
    other_expression="You're a communicator who blends kindness with insight. When your voice becomes as real as it is beautiful, connection deepens."
)

# Sextile
venus_mercury_sextile = VenusMercuryAspectInterpretation(
    aspect="Sextile",
    hook="You connect through kindness.",
    core_interpretation="You're skilled at creating ease in conversation and your words feel inviting, thoughtful, and real. People trust your voice because it blends feeling with clarity, and you often bring people together through how you express yourself.",
    male_expression="You're a bridge builder, someone who knows how to say the right thing without faking it. Your calm, friendly tone helps people open up.",
    female_expression="You speak with emotional intelligence and warmth, often offering support just when it's needed. Your communication is healing, not just helpful.",
    other_expression="You lead with empathy in your speech, offering insight wrapped in kindness. You help others feel understood without losing your own voice."
)

# Trine
venus_mercury_trine = VenusMercuryAspectInterpretation(
    aspect="Trine",
    hook="Your voice flows with ease and grace.",
    core_interpretation="You express love, ideas, and beauty effortlessly and your thoughts often feel like poetry, even in casual conversation. This natural flow makes it easy for you to inspire, connect, and soothe with your words.",
    male_expression="You have a way with words that feels smooth and sincere. Others are drawn to your style because it never feels forced.",
    female_expression="You communicate with warmth and elegance and your words carry not just meaning, but feeling. People listen because you make them feel safe.",
    other_expression="You're naturally articulate and emotionally in tune, making it easy for you to express affection and truth in the same breath."
)

# Square
venus_mercury_square = VenusMercuryAspectInterpretation(
    aspect="Square",
    hook="Your voice wants to please and but also be real.",
    core_interpretation="You feel pulled between saying what others want to hear and what you truly feel. This tension can lead to overthinking or second guessing, but it also sharpens your ability to speak with honesty and care.",
    male_expression="You're witty and clever, but sometimes your words feel stuck between charm and truth. Learning to trust your voice takes courage and but it's worth it.",
    female_expression="You care deeply about being understood, but that can lead to holding back. Your growth comes from finding your rhythm between diplomacy and directness.",
    other_expression="You're learning how to turn inner conflict into thoughtful communication. It's your honesty, not your polish, that will build real connection."
)

# Opposition
venus_mercury_opp = VenusMercuryAspectInterpretation(
    aspect="Opposition",
    hook="You hear yourself in others.",
    core_interpretation="Relationships often teach you how to communicate more authentically. You might find yourself torn between expressing your truth and keeping the peace, but it's through this tension that your voice becomes wiser and more grounded.",
    male_expression="You often attract people who challenge how you communicate, especially in love. These moments help you find a more balanced, honest tone.",
    female_expression="You learn to speak your truth by hearing where it echoes and or clashes and with someone else's. Every conversation becomes a mirror for growth.",
    other_expression="You grow through contrast in communication and learning that your voice matters just as much as theirs. Harmony comes not from agreement, but from honest exchange."
)

# Store all Venus–Mercury aspect interpretations
venus_mercury_aspects = {
    "Conjunction": venus_mercury_conj,
    "Sextile": venus_mercury_sextile,
    "Trine": venus_mercury_trine,
    "Square": venus_mercury_square,
    "Opposition": venus_mercury_opp
}
