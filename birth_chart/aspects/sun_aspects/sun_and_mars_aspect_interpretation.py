class SunMarsAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Sun Conjunct Mars
sun_conjunct_mars = SunMarsAspectInterpretation(
    aspect="Conjunct",
    hook="Your presence commands attention with raw power.",
    core_interpretation="You radiate an intensity that can't be ignored, possessing the courage to go after what you want with unwavering determination. Your challenge lies in learning to channel this fierce energy constructively rather than letting it explode impulsively, because underneath your boldness lies a deep drive to prove your worth to yourself and the world.",
    male_expression="You embody commanding presence and thrive in competitive environments where your direct approach and physical energy can shine. Your strength lies in your ability to take action when others hesitate, though you're learning that sometimes patience serves you better than speed.",
    female_expression="You refuse to play small and lead with passionate conviction, even when others find your intensity intimidating. Your journey involves learning to balance your fierce independence with strategic patience, turning your fire into focused power rather than scattered heat.",
    other_expression="You're driven by an inner fire that demands authentic expression and meaningful action, but you're discovering that your greatest victories come when you align your warrior energy with your deepest truth. Your presence alone can inspire others to find their own courage."
)

# Sun Sextile Mars
sun_sextile_mars = SunMarsAspectInterpretation(
    aspect="Sextile",
    hook="You act with perfect timing and noble purpose.",
    core_interpretation="You possess a natural ability to take action at exactly the right moment, combining courage with wisdom in a way that others deeply respect. Your energy feels trustworthy and inspiring because it's driven by genuine principles rather than ego or impulse.",
    male_expression="You demonstrate leadership through fair play and strategic thinking, earning respect through your competence and integrity. Your natural assertiveness feels supportive rather than threatening, making others want to follow your lead.",
    female_expression="You stand up for what's right with both strength and grace, defending the underdog while building your own confidence through meaningful action. Your energy inspires others to be braver and more authentic in their own lives.",
    other_expression="You channel your drive toward goals that align with your values, making every action feel purposeful and empowering. Your ability to combine passion with principle makes you a natural advocate and leader in whatever field you choose."
)

# Sun Trine Mars
sun_trine_mars = SunMarsAspectInterpretation(
    aspect="Trine",
    hook="Confidence flows through you like liquid fire.",
    core_interpretation="You move through life with an effortless blend of power and grace that makes even difficult challenges look easy, possessing a natural vitality that others find magnetic. Your gift is your ability to act from authentic strength without needing to prove yourself, though you're learning not to underestimate the impact of your natural capabilities.",
    male_expression="You embody steady confidence and masculine grace, excelling in situations that require both physical presence and strategic thinking. Your challenge is recognizing that what feels effortless to you is actually extraordinary to others.",
    female_expression="You radiate self assurance and bold elegance, thriving in situations that combine movement with purpose. Your natural courage and poise inspire others to embrace their own strength and take meaningful risks.",
    other_expression="You feel most alive when your actions align perfectly with your inner truth, creating a harmony between intention and expression that feels both powerful and peaceful. Your presence alone can energize entire situations and inspire others to step into their own power."
)

# Sun Square Mars
sun_square_mars = SunMarsAspectInterpretation(
    aspect="Square",
    hook="Your fire burns hot and demands refinement.",
    core_interpretation="You wrestle with intense energy that sometimes feels too big for your container, learning to transform raw power into purposeful action through experience and maturity. Your greatest strength emerges when you learn to pause between impulse and action, turning your natural intensity into focused determination.",
    male_expression="You carry an edge that can feel intimidating to others, but you're learning that true strength lies in choosing your battles wisely rather than fighting them all. Your intensity becomes your greatest asset when channeled through clear purpose and disciplined response.",
    female_expression="You burn with passionate conviction that others sometimes misinterpret as aggression, but you're discovering that your fire is meant to light the way rather than burn bridges. Your journey involves learning to lead with intention rather than react from emotion.",
    other_expression="You're forged in the fires of challenge and confrontation, developing resilience by testing your limits and learning from your mistakes. Your greatest wisdom comes from understanding that your power is most effective when it serves something greater than your ego."
)

# Sun Opposition Mars
sun_opposition_mars = SunMarsAspectInterpretation(
    aspect="Opposition",
    hook="You discover your power through intense encounters.",
    core_interpretation="You learn about your own strength and courage through relationships and conflicts that mirror your inner fire back to you, often finding yourself in situations that require you to stand up and be counted. Your growth comes from recognizing that the intensity you see in others is actually a reflection of your own untapped power.",
    male_expression="You define yourself through competition and confrontation, gradually learning to own your triggers and use conflict as a catalyst for growth. Your identity becomes clearer when you stop reacting to others and start responding from your own center.",
    female_expression="You discover your authority through challenging relationships and situations that force you to claim your power rather than giving it away. Your strength emerges when you learn to generate your own fire rather than getting caught up in others' drama.",
    other_expression="You thrive in intense one on one dynamics where passion and purpose collide, using resistance as fuel for transformation. Your greatest breakthroughs come when you learn to channel opposition into insight rather than letting it trigger automatic reactions."
)

# Dictionary of all Sun–Mars aspect interpretations
sun_mars_aspects = {
    "Conjunct": sun_conjunct_mars,
    "Sextile": sun_sextile_mars,
    "Trine": sun_trine_mars,
    "Square": sun_square_mars,
    "Opposition": sun_opposition_mars
}