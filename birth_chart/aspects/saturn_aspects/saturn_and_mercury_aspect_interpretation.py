class SaturnMercuryAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
saturn_mercury_conj = SaturnMercuryAspectInterpretation(
    aspect="Conjunction",
    hook="Your thoughts are measured and deliberate.",
    core_interpretation="You think deeply and focus on details, communicating with discipline and precision. While you may struggle with self criticism or hesitation in expression, your ability to master complex subjects and communicate clearly will earn you respect and authority.",
    male_expression="You are analytical and methodical, with intellectual precision that earns respect. It's important to soften your self scrutiny and allow yourself the space to grow and make mistakes.",
    female_expression="You are thoughtful and articulate, with a voice that is measured and resonant. Balancing your rigor with warmth will help you connect more deeply with others and express your ideas more freely.",
    other_expression="Your mind and structure are aligned, finding clarity through constraint. Learning to speak freely within the boundaries you've built will enhance your ability to communicate effectively."
)

# Sextile
saturn_mercury_sextile = SaturnMercuryAspectInterpretation(
    aspect="Sextile",
    hook="Your mind connects insight with structure.",
    core_interpretation="You have a helpful balance between thought and discipline, giving you organizational clarity and steady attention. Your thoughtful communication and effective planning make you excel in teaching, writing, or research.",
    male_expression="You are an organized thinker, with communication that is always considered and useful. This trait makes you a reliable source of information and guidance, respected for your clarity and insight.",
    female_expression="You are clear and concise, blending insight with integrity in your expression. This ability allows you to communicate complex ideas effectively, making you a trusted and influential voice.",
    other_expression="You are a balanced scholar, with words that emerge from wisdom. Your strength grows as you speak with purpose, making your ideas both impactful and respected."
)

# Trine
saturn_mercury_trine = SaturnMercuryAspectInterpretation(
    aspect="Trine",
    hook="You speak with quiet authority and solid conviction.",
    core_interpretation="You have an ease between intellect and integrity, making your thoughts well ordered, realistic, and wise. You communicate with clarity and maturity, and your ideas often carry quiet influence.",
    male_expression="You are a measured communicator, with words that inspire trust and action. Your ability to convey ideas thoughtfully and clearly makes you a respected and effective leader.",
    female_expression="You are grounded and eloquent, confident without needing to overpower. This trait allows you to express your ideas with grace and conviction, earning you admiration and respect.",
    other_expression="You have a harmonious voice, with intellect grounded by experience. Your ability to speak firmly without rigidity makes your communication both impactful and authentic."
)

# Square
saturn_mercury_square = SaturnMercuryAspectInterpretation(
    aspect="Square",
    hook="Your mind faces barriers, testing your logic and patience.",
    core_interpretation="You experience friction between thought and structure, which may lead to self doubt or mental resistance. While you think deeply, you might feel blocked or overly critical of your ideas. Learning to pause, organize, and refine your thoughts will cultivate strong intellectual discipline.",
    male_expression="You are a critical thinker, with tension that fuels eventual mental mastery. Embracing this challenge will help you develop resilience and a deeper understanding of your own mind.",
    female_expression="You are focused but cautious, learning to trust your voice through reflection. This journey will help you find confidence in your ideas and express them more freely.",
    other_expression="You face intellectual challenges, with progress that builds through mental perseverance. This process will strengthen your mind and enhance your ability to communicate effectively."
)

# Opposition
saturn_mercury_opp = SaturnMercuryAspectInterpretation(
    aspect="Opposition",
    hook="Your thoughts balance between structure and freedom, finding clarity in tension.",
    core_interpretation="You experience a dialogue between rigid structure and free thought, which can feel like a internal conflict. Integrating disciplined thinking with creative expression will transform this opposition into a healing perspective.",
    male_expression="You are reflective but may feel resistant, growing through bridging logic and intuition. This balance will help you communicate more effectively and connect deeply with others.",
    female_expression="You are structured and insightful, with strength in balancing restraint with openness. This trait allows you to express your ideas with both clarity and creativity.",
    other_expression="You are a polarized thinker, with unity forming through conscious integration of mind and maturity. This process will help you develop a well rounded and influential voice."
)

saturn_mercury_aspects = {
    "Conjunction": saturn_mercury_conj,
    "Sextile": saturn_mercury_sextile,
    "Trine": saturn_mercury_trine,
    "Square": saturn_mercury_square,
    "Opposition": saturn_mercury_opp
}
