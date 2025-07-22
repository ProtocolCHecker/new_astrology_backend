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
    hook="You carry a weight of responsibility that shapes your presence.",
    core_interpretation="You come across as reserved and serious, with a cautious approach to how you present yourself. Over time, you'll find that this sense of duty becomes a strength, allowing you to mature gracefully.",
    male_expression="You exude a quiet authority, and as you grow, you'll learn to gain confidence through steady self reliance. Your reserved nature may initially seem like a barrier, but it ultimately becomes a source of strength and respect from others.",
    female_expression="You are composed and conscientious, and as you navigate life, you'll blossom by shedding early inhibitions. Your serious demeanor is not a limitation but a foundation for building genuine connections and trust.",
    other_expression="You shape yourself with solemnity, and your presence strengthens as you embrace responsibility. This journey of self discovery and growth is marked by a deepening sense of self assurance and integrity."
)

# Sextile
saturn_asc_sextile = SaturnAscendantAspectInterpretation(
    aspect="Sextile",
    hook="Your discipline is underlaid with approachability.",
    core_interpretation="You possess a calm confidence and reliability in how you express yourself. This grounded maturity makes you someone others naturally trust.",
    male_expression="You are steady and reliable, blending warmth with integrity in a way that others find reassuring. Your ability to balance discipline with approachability makes you a pillar of support in both personal and professional settings.",
    female_expression="You are balanced and poised, showing up with integrity and grace that others admire. Your presence is both calming and inspiring, making you a natural leader and a trusted confidant.",
    other_expression="You are responsible and confident, with a practiced composure that flows naturally. This balance of traits allows you to navigate life's challenges with a sense of calm and assurance, making you a steady force in any situation."
)

# Trine
saturn_asc_trine = SaturnAscendantAspectInterpretation(
    aspect="Trine",
    hook="You wear your experiences with ease.",
    core_interpretation="You have a natural dignity and self control that make it easy for you to assume leadership roles. Your presence is respected and grounded, making you a figure of quiet authority.",
    male_expression="You are confident and grounded, with a presence that feels anchored and secure. This natural ease in leadership roles allows you to inspire confidence in others, making you a reliable and respected figure in any group.",
    female_expression="You are elegant and self assured, commanding respect through your poise and grace. Your ability to carry yourself with dignity and self control makes you a natural leader, admired for your composure and strength.",
    other_expression="You are a poised figure, and your inner discipline manifests quietly in who you are. This inherent sense of self assurance and control allows you to navigate life with a sense of purpose and integrity, earning the respect of those around you."
)

# Square
saturn_asc_square = SaturnAscendantAspectInterpretation(
    aspect="Square",
    hook="You face your limits head on.",
    core_interpretation="You experience friction in how you express yourself and present to the world, but this tension prompts growth. By overcoming barriers, you find paths to self improvement.",
    male_expression="You may feel reserved yet restless, but you find growth through self discipline and perseverance. This internal struggle is not a setback but a catalyst for developing resilience and a stronger sense of self.",
    female_expression="You are tense and evolving, refining your identity by pushing through boundaries. Each challenge you face is an opportunity to redefine yourself and emerge with greater clarity and strength.",
    other_expression="You refine yourself through tension, and your presence grows stronger with effort. This journey of overcoming obstacles shapes you into a more resilient and self assured individual, capable of handling life's complexities with grace."
)

# Opposition
saturn_asc_opp = SaturnAscendantAspectInterpretation(
    aspect="Opposition",
    hook="Your identity is tested through others.",
    core_interpretation="You learn about your own authority and boundaries through your relationships. Balancing independence and partnership teaches you self definition.",
    male_expression="You see yourself reflected in others' eyes, and your strength builds through these connections. This dynamic helps you understand your own boundaries and authority, fostering a deeper sense of self awareness and growth.",
    female_expression="You are strengthened through relationships, learning about yourself through relational structures. These interactions provide valuable insights into your own identity and help you build a stronger, more independent self.",
    other_expression="You build yourself through relationships, growing in awareness of how you interact with others. This process of self discovery through connections allows you to develop a more nuanced understanding of yourself and your place in the world."
)

saturn_ascendant_aspects = {
    "Conjunction": saturn_asc_conj,
    "Sextile": saturn_asc_sextile,
    "Trine": saturn_asc_trine,
    "Square": saturn_asc_square,
    "Opposition": saturn_asc_opp
}
