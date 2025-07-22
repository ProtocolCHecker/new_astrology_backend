class SunSaturnAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Sun Conjunct Saturn
sun_conjunct_saturn = SunSaturnAspectInterpretation(
    aspect="Conjunct",
    hook="You wear responsibility like a second skin.",
    core_interpretation="You've likely felt the weight of expectations from an early age, making you naturally cautious and sometimes overly critical of yourself. Your greatest gift lies in your ability to build lasting success through patience and determination, but you must learn that your worth isn't something you need to earn.",
    male_expression="You approach life with serious determination and rarely take shortcuts. Your natural discipline becomes your greatest asset once you stop being so hard on yourself.",
    female_expression="You possess an inner strength that others recognize even when you don't see it yourself. Your composed nature and reliability make you someone others naturally turn to for guidance.",
    other_expression="You have an old soul quality that sets you apart, carrying wisdom beyond your years. Your challenge is learning to embrace your own light instead of constantly questioning if you deserve to shine."
)

# Sun Sextile Saturn
sun_sextile_saturn = SunSaturnAspectInterpretation(
    aspect="Sextile",
    hook="You build your dreams with steady hands.",
    core_interpretation="You have a natural ability to balance ambition with practical thinking, making you someone others can depend on completely. You don't need drama or chaos to feel alive – you find deep satisfaction in consistent progress and meaningful work.",
    male_expression="You lead through example rather than grand gestures, earning respect through your reliability and thoughtful actions. Your steady presence reassures others during uncertain times.",
    female_expression="You create stability wherever you go, combining grace with an unshakeable sense of purpose. Your quiet strength becomes a foundation that others can lean on.",
    other_expression="You understand that true success comes from patience and persistence rather than rushing or taking risks. Your measured approach to life creates lasting results that stand the test of time."
)

# Sun Trine Saturn
sun_trine_saturn = SunSaturnAspectInterpretation(
    aspect="Trine",
    hook="Authority flows through you naturally.",
    core_interpretation="You possess an effortless blend of confidence and responsibility that makes leadership feel natural rather than forced. You have the rare ability to inspire others through your integrity and consistent actions rather than empty promises.",
    male_expression="You command respect without needing to demand it, leading through competence and genuine care for others. Your reliability makes you someone others naturally look up to.",
    female_expression="You embody quiet power, showing others what true strength looks like through your actions and decisions. Your wisdom seems to come from a deep, unshakeable place within you.",
    other_expression="You've mastered the art of being both ambitious and grounded, creating success that feels sustainable and meaningful. Your influence on others comes from your authentic way of living rather than trying to impress."
)

# Sun Square Saturn
sun_square_saturn = SunSaturnAspectInterpretation(
    aspect="Square",
    hook="Your inner critic fights your inner champion.",
    core_interpretation="You often feel caught between wanting to express yourself freely and an overwhelming fear that you're not good enough. The key to your growth lies in learning to treat yourself with the same kindness you'd show a good friend – your harshest critic doesn't need to be yourself.",
    male_expression="You push yourself relentlessly but need to learn that strength also means knowing when to be gentle with yourself. Your drive for excellence becomes truly powerful when it's not fueled by selfdoubt.",
    female_expression="You may hold back your natural radiance because you fear judgment, but your beauty lies in embracing your imperfections. Your journey involves learning that you don't need to be perfect to be worthy of love and recognition.",
    other_expression="You carry a deep wound around feeling worthy of success and happiness, but this same wound can become your greatest source of compassion for others. Your healing comes through accepting that you deserve joy simply because you exist."
)

# Sun Opposition Saturn
sun_opposition_saturn = SunSaturnAspectInterpretation(
    aspect="Opposition",
    hook="You see yourself through borrowed eyes.",
    core_interpretation="You tend to give others too much power over how you feel about yourself, constantly measuring your worth against external expectations or criticism. Your liberation comes when you realize that the harshest judge in your life is often the voice in your own head, not the people around you.",
    male_expression="You may find yourself in power struggles where you're either rebelling against authority or becoming overly rigid yourself. Your balance comes through developing your own internal compass for what success means to you.",
    female_expression="You might feel torn between pleasing others and honoring your own needs, but your growth lies in learning that you can be both caring and selfrespecting. Your strength emerges when you stop apologizing for taking up space.",
    other_expression="You see others as either supportive or limiting, but the real work is recognizing how you limit yourself through fear and selfdoubt. Your freedom comes through owning your power instead of giving it away to external circumstances."
)

# Store all Sun–Saturn aspect interpretations
sun_saturn_aspects = {
    "Conjunct": sun_conjunct_saturn,
    "Sextile": sun_sextile_saturn,
    "Trine": sun_trine_saturn,
    "Square": sun_square_saturn,
    "Opposition": sun_opposition_saturn
}