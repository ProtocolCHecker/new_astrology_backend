class SunJupiterAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Sun Conjunct Jupiter
sun_conjunct_jupiter = SunJupiterAspectInterpretation(
    aspect="Conjunct",
    hook="You radiate larger than life energy that lights up rooms.",
    core_interpretation="You possess an infectious optimism and natural magnetism that draws opportunities and people to you like a magnet, though your challenge lies in channeling this abundant energy wisely. Your enthusiasm and generous spirit inspire others to dream bigger, but you're learning that true leadership means following through on your grand visions with practical action.",
    male_expression="You're the eternal optimist who bounces back from setbacks with inspiring resilience, though you sometimes promise more than you can deliver. Your gift lies in your ability to see possibilities others miss, but your growth comes from tempering enthusiasm with realistic planning.",
    female_expression="You uplift everyone around you with your radiant faith in life's possibilities, inspiring others to believe in themselves and their dreams. Your challenge is learning to ground your expansive visions in concrete steps that turn inspiration into lasting achievement.",
    other_expression="You're a natural visionary whose identity is fueled by meaning and possibility, but you're discovering that true expansion requires both courage and discipline. Your greatest impact comes when you balance your gift for inspiration with accountability to your commitments."
)

# Sun Sextile Jupiter
sun_sextile_jupiter = SunJupiterAspectInterpretation(
    aspect="Sextile",
    hook="Doors open and hearts warm in your presence.",
    core_interpretation="You have a natural gift for bringing out the best in situations and people, combining confidence with genuine care in a way that creates trust and opportunity. Your moral compass and positive outlook make you a natural mentor who others seek out for guidance and encouragement.",
    male_expression="You lead by example with quiet strength and unwavering principles, earning respect through your integrity rather than demanding it. Your supportive nature and wisdom make you the person others turn to when they need both encouragement and honest guidance.",
    female_expression="You radiate grace and wisdom that draws people into your circle of light, creating spaces where others feel safe to grow and dream. Your ability to see the potential in everyone makes you a natural teacher and healer in whatever field you choose.",
    other_expression="You're a natural bridge builder who helps others see possibilities they couldn't imagine alone, sharing your light in ways that multiply rather than diminish it. Your growth comes through recognizing that your gift for uplifting others is itself a form of sacred service."
)

# Sun Trine Jupiter
sun_trine_jupiter = SunJupiterAspectInterpretation(
    aspect="Trine",
    hook="Fortune favors you with effortless grace.",
    core_interpretation="You move through life with a blessed ease that seems to attract good fortune and genuine affection from others, possessing a philosophical wisdom that helps you stay positive even during challenges. Your gift is your ability to find meaning and joy in life's journey, though you're learning not to take your natural advantages for granted.",
    male_expression="You embody dignified strength and approachable wisdom, drawing respect without having to fight for it. Your challenge is pushing yourself to fulfill your deeper potential rather than coasting on your natural charm and good fortune.",
    female_expression="You carry yourself with warm dignity that makes others feel valued and hopeful in your presence, inspiring trust through your authentic joy in life. Your faith in goodness becomes a beacon that helps others navigate their own difficult times.",
    other_expression="You walk through life with an optimistic balance that makes even ordinary moments feel meaningful, but you're discovering that your greatest growth comes from actively sharing your gifts rather than simply enjoying them. Your presence alone can transform situations, but purposeful action multiplies your impact."
)

# Sun Square Jupiter
sun_square_jupiter = SunJupiterAspectInterpretation(
    aspect="Square",
    hook="Your fire burns bright and sometimes burns out.",
    core_interpretation="You dream big and feel deeply, but your enthusiasm sometimes leads you to overextend yourself financially, emotionally, or energetically. Your generous heart and bold vision are real gifts, but you're learning that sustainable success requires pacing yourself and setting realistic boundaries.",
    male_expression="You're the adventurous dreamer who wants to experience everything life has to offer, but you're discovering that saying no to some opportunities allows you to fully succeed at others. Your growth comes through learning to channel your expansive energy with focused discipline.",
    female_expression="You approach life with idealistic fervor and boundless enthusiasm, but you're learning that true wisdom sometimes means moderating your giving and dreaming. Your maturity brings the grace to discern between opportunities that serve your highest good and those that simply feed your ego.",
    other_expression="You're a bold visionary who believes anything is possible, but you're discovering that turning dreams into reality requires both inspiration and practical planning. Your journey involves learning to balance your magnificent enthusiasm with grounded accountability."
)

# Sun Opposition Jupiter
sun_opposition_jupiter = SunJupiterAspectInterpretation(
    aspect="Opposition",
    hook="You find yourself through grand mirrors of possibility.",
    core_interpretation="You discover who you are through your relationships with big ideas, inspiring people, and meaningful causes, but you're learning to maintain your center while reaching for the stars. Your identity gets wrapped up in your beliefs and visions, and you're discovering how to stay true to yourself while growing beyond your current limitations.",
    male_expression="You're driven by enthusiastic hope and big dreams, but you're learning that chasing external validation of your worth leads to endless searching. Your maturity comes from cultivating inner faith that doesn't depend on outside accomplishments or recognition.",
    female_expression="You're magnetically drawn to growth and expansion, often stretching yourself through relationships and causes that inspire you. Your journey involves learning to define your own center while still remaining open to the transformative power of connection.",
    other_expression="You balance personal expression with universal reach, finding your identity through giving, learning, and bridging the gap between individual dreams and collective vision. Your greatest wisdom emerges from integrating your personal truth with your desire to serve something greater than yourself."
)

# Store all Sun–Jupiter interpretations in a dictionary
sun_jupiter_aspects = {
    "Conjunct": sun_conjunct_jupiter,
    "Sextile": sun_sextile_jupiter,
    "Trine": sun_trine_jupiter,
    "Square": sun_square_jupiter,
    "Opposition": sun_opposition_jupiter
}