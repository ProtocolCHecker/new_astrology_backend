class JupiterMoonAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Jupiter Conjunct Moon
jupiter_conjunction_moon = JupiterMoonAspectInterpretation(
    aspect="Conjunction",
    hook="Your heart expands with generosity  and  joy is your native tongue.",
    core_interpretation="With the Moon conjunct Jupiter, your emotional responsiveness blends with abundance, optimism, and a deep desire to nurture through meaning. You are warm, forgiving, and emotionally generous, often the first to offer comfort and encouragement. Your emotional intelligence is paired with intuitive wisdom and a natural sense of humor that makes you beloved and trusted. Embrace your innate belief in goodness and fairness, but be mindful of boundaries to avoid coming across as preachy.",
    male_expression="You are kind and passionate, offering emotional leadership and support with grand conviction. Be mindful of over giving or moralizing to maintain balance.",
    female_expression="You are nurturing, wise, and deeply intuitive, exuding emotional generosity and fairness. Remember to receive as well as give to sustain your energy.",
    other_expression="You are an emotional philosopher, giving love like sunlight and insight like water. You uplift others with heart centered truth, making a profound impact."
)

# Jupiter Sextile Moon
jupiter_sextile_moon = JupiterMoonAspectInterpretation(
    aspect="Sextile",
    hook="Your emotions speak in open tones  and  honest, kind, and quietly lucky.",
    core_interpretation="With the Moon sextile Jupiter, you have a steady emotional tone that radiates warmth, tolerance, and openness. You are emotionally balanced, naturally optimistic, and drawn to meaningful experiences. Your inner world is rich and uplifting, inspiring comfort in others simply by being present. Embrace your ability to find perspective in emotional challenges and share this insight with humor and grace.",
    male_expression="You are steady hearted and open minded, bringing calm perspective to emotional moments. Your gentle uplifting nature is a gift to those around you.",
    female_expression="You are naturally generous and wise, offering emotional guidance without pressure. Your love for making others feel seen and safe is your strength.",
    other_expression="You are a peaceful nurturer, connecting through authentic joy and spiritual compassion. Your confidence radiates through feeling and empathy."
)

# Jupiter Trine Moon
jupiter_trine_moon = JupiterMoonAspectInterpretation(
    aspect="Trine",
    hook="Your feelings flow with faith  and  joy isn't just a mood, it's your philosophy.",
    core_interpretation="With the Moon trine Jupiter, you are blessed with emotional grace, intuitive confidence, and a spirit that naturally attracts positivity. Your optimism is innate, and you believe in the goodness of life and people, magnetizing fortunate relationships and emotional fulfillment. You are deeply empathetic and quick to forgive, yet wise enough to maintain perspective. Embrace your love for humor, culture, storytelling, and teaching, guided by your expansive inner moral compass.",
    male_expression="You are emotionally strong and wise, trusting life and teaching others to trust as well. Your calming, uplifting effect on others is a testament to your strength.",
    female_expression="You are gracefully expansive, embracing your feelings with self belief and intuitive power. You are often a joyful mentor or matriarch, inspiring those around you.",
    other_expression="You are an empathic beacon, radiating heart centered leadership and emotional intelligence. You live love as a worldview, touching lives deeply."
)

# Jupiter Square Moon
jupiter_square_moon = JupiterMoonAspectInterpretation(
    aspect="Square",
    hook="Your feelings stretch wide  and  sometimes too far to stay grounded.",
    core_interpretation="With the Moon square Jupiter, you experience emotional intensity and a deep desire to give, belong, and believe. You are incredibly generous of spirit but may struggle with overpromising or unrealistic expectations. You want emotional connection, often to a fault, and may idealize people or causes before facing reality. Embrace maturity by tempering hope with wisdom, becoming an inspiring supporter and moral hearted caregiver.",
    male_expression="You are emotionally big hearted but can be easily overwhelmed, often overextending in support of others. Learning emotional realism will help you find balance.",
    female_expression="You are intensely giving and nurturing, seeking depth but wary of emotional overdrive. Your growth comes from self containment and self care.",
    other_expression="You are an emotional idealist, swinging between joyful highs and heartfelt disappointment. Learning to love without losing your center is your journey."
)

# Jupiter Opposite Moon
jupiter_opposition_moon = JupiterMoonAspectInterpretation(
    aspect="Opposition",
    hook="Your emotions mirror the sky  and  infinite, inspiring, and in search of balance.",
    core_interpretation="With the Moon opposite Jupiter, you seek deep belonging yet crave emotional freedom and adventure. You may feel conflicted between nurturing others and pursuing your own growth, or between loyalty and your belief in possibility. You are emotionally generous, sometimes to your own detriment, giving too much in hopes of being loved or understood. Embrace the key to discerning between heartfelt intuition and exaggerated emotional projection, becoming a wise and open hearted guide.",
    male_expression="You are spiritually generous but emotionally stretched, learning to give without losing yourself. Your strength comes from self honesty and self awareness.",
    female_expression="You are an expansive nurturer, giving love deeply but needing clear boundaries. Balancing your desire to protect with your need to grow is your path to fulfillment.",
    other_expression="You are emotionally visionary, feeling the call of the heart and the horizon. Your evolution comes through harmonizing empathy and independence, creating a balanced and fulfilling life."
)

# Create a dictionary to store all Jupiter Moon aspect interpretations
jupiter_moon_aspects = {
    "Conjunction": jupiter_conjunction_moon,
    "Sextile": jupiter_sextile_moon,
    "Trine": jupiter_trine_moon,
    "Square": jupiter_square_moon,
    "Opposition": jupiter_opposition_moon
}