class MercuryAscendantAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Mercury Conjunct Ascendant
mercury_conjunct_asc = MercuryAscendantAspectInterpretation(
    aspect="Conjunct",
    hook="You arrive with questions  and  curious eyes, quick wit, and a story always ready.",
    core_interpretation="With Mercury conjunct your Ascendant, you are highly expressive and intellectually active. You come across as sharp and observant, often with a playful spark in your eye. Your communication is rapid and animated, and you likely identify strongly with your verbal abilities. However, be mindful of speaking before thinking or appearing nervous.",
    male_expression="You are talkative and mentally quick, often leading conversations. Remember to balance speaking with listening.",
    female_expression="Your expressiveness and intelligence shine through your charm and cleverness. Stay grounded to manage overthinking.",
    other_expression="You are a lively communicator, blending mental curiosity with personal style. You feel most authentic when speaking your truth with humor."
)

# Mercury Sextile Ascendant
mercury_sextile_asc = MercuryAscendantAspectInterpretation(
    aspect="Sextile",
    hook="Your words open doors  and  smooth, smart, and just the right dose of sparkle.",
    core_interpretation="With Mercury sextile your Ascendant, you have a natural ability to communicate and express yourself with ease. You are socially clever and engaging, knowing how to strike the right tone. You navigate social settings with grace and mental agility, making you persuasive yet approachable.",
    male_expression="You are clever and composed, knowing how to phrase things precisely. Your skills in negotiation or debate are a natural strength.",
    female_expression="You are poised and articulate, often the voice of reason in a group. Your calm energy in conversations is a gift.",
    other_expression="You are a thoughtful connector, reading people well and speaking with style. Communication feels like second nature to you."
)

# Mercury Trine Ascendant
mercury_trine_asc = MercuryAscendantAspectInterpretation(
    aspect="Trine",
    hook="You speak like you breathe  and  fluently, freely, and with a spark of brilliance.",
    core_interpretation="With Mercury trine your Ascendant, you experience effortless harmony between your mind and self and expression. You are a natural communicator, gifted in speech and writing. Your quick wit and curiosity make ideas sound inspiring and accessible, making you a lifelong learner and stimulating companion.",
    male_expression="You are bright and expressive, thriving on intellectual connections. Your storytelling or wordplay is often admired.",
    female_expression="Your charm and quick mind help you connect, heal, or guide through language. You are thoughtful without being rigid.",
    other_expression="You are a harmonious speaker, with your voice and body speaking the same truth. Exchanging ideas with the world makes you feel alive."
)

# Mercury Square Ascendant
mercury_square_asc = MercuryAscendantAspectInterpretation(
    aspect="Square",
    hook="Your mouth runs ahead of your message  and  you're learning to match meaning with delivery.",
    core_interpretation="With Mercury square your Ascendant, you may feel friction between your thoughts and self and presentation. You might often feel misunderstood or find that your words and body language don't always align. Learning to relax into your voice and practice conscious communication is key to becoming a compelling communicator.",
    male_expression="You are edgy and intelligent but may question yourself even while appearing confident. Patience and self and trust will serve you well.",
    female_expression="Your wit is accompanied by self and criticism, often second and guessing how you're perceived. Authentic self and expression will bring you strength.",
    other_expression="You are a challenging communicator, learning to align your message with your presence. Refining your tone without losing your truth will bring you power."
)

# Mercury Opposite Ascendant
mercury_opposite_asc = MercuryAscendantAspectInterpretation(
    aspect="Opposition",
    hook="Your mirror talks back  and  you find yourself in the words you share.",
    core_interpretation="With Mercury opposite your Ascendant, your communication and mental processing thrive in relationships. You define your voice in response to others and seek mental stimulation in your closest connections. Be mindful of projecting thoughts or exaggerating to make a point, as sharp conversational skills are your strength.",
    male_expression="You are persuasive and lively, loving to talk things out. Be careful not to dominate conversations and grow through mental sparring.",
    female_expression="You are relational and expressive, seeking understanding through dialogue. Learn to center your own voice, not just reflect others'.",
    other_expression="You are an interpersonal mirror, speaking to discover and listening to grow. Shared thought and heartfelt discussion bring you clarity."
)

# Create a dictionary to store all Mercury and Ascendant aspect interpretations
mercury_ascendant_aspects = {
    "Conjunct": mercury_conjunct_asc,
    "Sextile": mercury_sextile_asc,
    "Trine": mercury_trine_asc,
    "Square": mercury_square_asc,
    "Opposition": mercury_opposite_asc
}
