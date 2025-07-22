class NeptuneJupiterAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
neptune_jup_conj = NeptuneJupiterAspectInterpretation(
    aspect="Conjunction",
    hook="Your hope feels like a warm fog and everyone breathes it in.",
    core_interpretation="You see the good in every situation and bring optimism to those around you. Grounding big ideas in small daily steps makes your positivity last.",
    male_expression="Your upbeat energy lifts people's spirits instantly. Pinning down one clear action each day helps turn your dreams into reality.",
    female_expression="Your bright outlook helps others believe in better days. Setting a simple weekly plan channels your enthusiasm productively.",
    other_expression="Your faith in possibility feels contagious and comforting. Linking your vision to concrete goals ensures they come true."
)

# Sextile
neptune_jup_sextile = NeptuneJupiterAspectInterpretation(
    aspect="Sextile",
    hook="Your soul sings of wonder and curiosity lights your path.",
    core_interpretation="You explore life with gentle excitement and learn quickly from every experience. Writing down one new idea each morning keeps that spark alive.",
    male_expression="Your curious spirit draws people into your world. Jotting quick notes brings your insights into focus.",
    female_expression="Your playful outlook makes every day feel like an adventure. Keeping a simple journal captures your best thoughts.",
    other_expression="Your love of exploration inspires others. A short checklist helps you follow through on your discoveries."
)

# Trine
neptune_jup_trine = NeptuneJupiterAspectInterpretation(
    aspect="Trine",
    hook="Your heart sees possibility everywhere and optimism is your compass.",
    core_interpretation="You face challenges with confidence and turn setbacks into lessons. Pairing that courage with small action steps keeps your journey steady.",
    male_expression="Your hope guides others through hard times. Breaking big goals into bite sized tasks makes them easier to reach.",
    female_expression="Your positive spirit feels like a shelter in storms. Mapping out a few clear tasks helps your confidence grow.",
    other_expression="Your faith in good outcomes uplifts everyone. Steady progress on small steps builds lasting success."
)

# Square
neptune_jup_square = NeptuneJupiterAspectInterpretation(
    aspect="Square",
    hook="Your idealism stretches wide and sometimes it pulls you off balance.",
    core_interpretation="You want to help and believe the best, but you can overextend if you're not careful. Learning to say no sometimes keeps your energy sustainable.",
    male_expression="Your big heart risks burnout when you take on too much. Setting a clear limit on your time prevents exhaustion.",
    female_expression="Your generous spirit may leave you drained without boundaries. Saying “not today” protects your well being.",
    other_expression="Your caring nature teaches you self respect. Balancing kindness with limits keeps you healthy."
)

# Opposition
neptune_jup_opp = NeptuneJupiterAspectInterpretation(
    aspect="Opposition",
    hook="Your dreams and reality dance and finding balance reveals your truth.",
    core_interpretation="You swing between big hopes and practical needs, and blending both makes a grounded, joyful life. Checking in with friends helps you stay on track.",
    male_expression="Your vision is inspiring, but pairing it with clear steps keeps you moving forward. Asking a friend to help you plan makes it stick.",
    female_expression="Your ambition and care pull you different ways; honoring both gives you real power. Sharing your goals with someone boosts accountability.",
    other_expression="Your mix of hope and realism becomes your strength. Talking it out with others clarifies your path."
)

neptune_jupiter_aspects = {
    "Conjunction": neptune_jup_conj,
    "Sextile": neptune_jup_sextile,
    "Trine": neptune_jup_trine,
    "Square": neptune_jup_square,
    "Opposition": neptune_jup_opp
}
