class JupiterSunAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Jupiter Conjunct Sun
jupiter_conjunction_sun = JupiterSunAspectInterpretation(
    aspect="Conjunct",
    hook="I shine like faith in motion  and  life owes me brightness, and I offer it back tenfold.",
    core_interpretation="The Sun conjunct Jupiter blends ego with expansion, producing a generous, optimistic, and ideal driven personality. These individuals often radiate warmth, confidence, and a larger than life presence. There's an inherent belief that life will work out  and  and often, it does. They're natural inspirers and motivators, believing in their path and in the goodness of others. However, their grand self belief can sometimes tip into overindulgence, procrastination, or unrealistic promises. At their best, they are joyfully expressive, purpose driven, and charismatic leaders. The journey involves pairing their big heartedness with responsibility and grounded follow through.",
    male_expression="Magnetic and magnanimous; leads through optimism and humor. Must learn to temper excess with consistency.",
    female_expression="Radiant and generous; uplifts others through presence and passion. Needs grounding to manage emotional or material overreach.",
    other_expression="Joyful amplifier; embodies faith, play, and potential. Flourishes when purpose is aligned with meaningful action."
)

# Jupiter Sextile Sun
jupiter_sextile_sun = JupiterSunAspectInterpretation(
    aspect="Sextile",
    hook="My path opens where others hesitate  and  fortune follows faith in action.",
    core_interpretation="Sun sextile Jupiter supports a smooth connection between identity and vision. These people are well liked, generous, and usually possess strong moral character. They approach life with optimism and gratitude, attracting opportunity through their open hearted and easygoing nature. While not forcefully ambitious, they are quietly competent, drawing support and success through integrity and warmth. They tend to have a love for learning, traveling, and broadening horizons  and  and often become natural mentors or community figures.",
    male_expression="Friendly and dependable; leads with honesty and heart. Attracts success through goodwill rather than ego.",
    female_expression="Kind and principled; often seen as a moral compass in her community. Grows through teaching, exploring, and encouraging others.",
    other_expression="Graceful beacon; shines with quiet wisdom and cultural fluency. Lives by inner truth and inspires by example."
)

# Jupiter Trine Sun
jupiter_trine_sun = JupiterSunAspectInterpretation(
    aspect="Trine",
    hook="I thrive with ease  and  fortune is my nature, and joy is my guide.",
    core_interpretation="The Sun trine Jupiter produces a naturally gifted, fortunate, and graceful presence. These individuals often feel 'lucky'  and  and in many cases, they are  and  due to a mindset rooted in trust, generosity, and inner peace. They radiate self assurance and tend to have a strong belief in fairness, ethics, and possibility. They often find themselves in the right place at the right time, supported by both people and fate. While they may lack hard ambition, they excel when sharing their gifts through teaching, creative expression, or spiritual guidance.",
    male_expression="Charismatic and upbeat; inspires through natural leadership and confident ease. Trusts life and brings laughter.",
    female_expression="Wise and welcoming; leads with light and grace. Encourages justice and joy, often drawing others to her warmth.",
    other_expression="Fluent in hope; a natural teacher, nurturer, and cultural translator. Glows from the inside out, often without trying."
)

# Jupiter Square Sun
jupiter_square_sun = JupiterSunAspectInterpretation(
    aspect="Square",
    hook="My light wants to touch the sky  and  but sometimes forgets to check the ground.",
    core_interpretation="Sun square Jupiter drives a thirst for greatness, but often wrestles with overreach, inflated expectations, or inconsistent self discipline. These individuals aim high and love generously  and  but may promise too much, overspend, or underestimate consequences. They are born with big dreams, but must learn to refine their impulses and follow through with maturity. At their best, they're expansive, inspiring, and full of life. When imbalanced, they may struggle with burnout, disillusionment, or lack of focus.",
    male_expression="Bold and optimistic; driven by big ideals but needs structure to make them real. Growth comes through humility and follow through.",
    female_expression="Vivid and visionary; shines with passion but must avoid overextension. Finds strength in balancing faith with realism.",
    other_expression="Inspired performer; thrives on belief in self and cause. Matures by harmonizing bold vision with practical effort."
)

# Jupiter Opposite Sun
jupiter_opposition_sun = JupiterSunAspectInterpretation(
    aspect="Opposition",
    hook="My ego dances with expansion  and  torn between striving and surrendering.",
    core_interpretation="Sun opposite Jupiter creates a dynamic tension between self expression and philosophical growth. These people feel pulled between doing and dreaming  and  between personal identity and collective ideals. They may swing from confident highs to existential questioning, often seeking meaning through experience, travel, or belief systems. They're big hearted and idealistic but must learn balance  and  otherwise they risk becoming preachy, scattered, or unrealistic. The key is to ground their quest for truth in the lived self, not just the imagined one.",
    male_expression="Morally driven and passionate; seeks purpose through big gestures. Learns to contain fire without dimming light.",
    female_expression="Warm and expansive; deeply invested in values and fairness. Must guard against giving too much or losing herself in ideals.",
    other_expression="Bright idealist; balances internal callings with outer roles. Evolves through reconciling personal goals with universal truths."
)

# Create a dictionary to store all Jupiter Sun aspect interpretations
jupiter_sun_aspects = {
    "Conjunction": jupiter_conjunction_sun,
    "Sextile": jupiter_sextile_sun,
    "Trine": jupiter_trine_sun,
    "Square": jupiter_square_sun,
    "Opposition": jupiter_opposition_sun
}