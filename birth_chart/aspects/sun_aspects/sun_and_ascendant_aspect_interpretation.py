class SunAscendantAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Sun Conjunct Ascendant
sun_conjunct_asc = SunAscendantAspectInterpretation(
    aspect="Conjunct",
    hook="You command attention the moment you walk in.",
    core_interpretation="You possess a magnetic presence that naturally draws people's eyes and respect, but this gift comes with the responsibility of learning when to shine and when to step back. Your identity and how others see you are perfectly aligned, making you a natural leader who others instinctively follow and trust.",
    male_expression="You project strength and confidence effortlessly, though you're learning that true leadership includes lifting others up. Your challenge is balancing your natural authority with genuine humility and openness to feedback.",
    female_expression="You radiate self possession and inspire others through your authentic confidence, but you're discovering that vulnerability can be just as powerful as strength. Your presence alone motivates people to believe in themselves.",
    other_expression="You were born to stand out and make an impact, but your greatest growth comes from using your visibility to serve something greater than yourself. Your authentic self expression becomes a beacon for others finding their own way."
)

# Sun Sextile Ascendant
sun_sextile_asc = SunAscendantAspectInterpretation(
    aspect="Sextile",
    hook="Your warmth opens hearts and doors.",
    core_interpretation="You have a gift for making others feel comfortable and inspired in your presence, combining confidence with approachability in a way that feels completely natural. People trust you because your outer expression perfectly matches your inner sincerity, creating opportunities wherever you go.",
    male_expression="You lead through enthusiasm and genuine care, making others want to follow your vision rather than feeling forced to. Your strength lies in bringing out the best in people through your own positive energy.",
    female_expression="You carry yourself with graceful confidence that puts others at ease while inspiring them to reach higher. Your natural charm opens doors, but it's your authenticity that keeps them open.",
    other_expression="You shine in ways that illuminate others rather than overshadowing them, creating win win situations wherever you go. Your ability to collaborate while maintaining your individuality makes you invaluable in any group."
)

# Sun Trine Ascendant
sun_trine_asc = SunAscendantAspectInterpretation(
    aspect="Trine",
    hook="Grace flows through everything you do.",
    core_interpretation="You move through life with an effortless elegance that makes even ordinary moments feel special, possessing a natural magnetism that draws opportunities and admirers alike. Your challenge is recognizing the value of your gifts and using them purposefully rather than taking them for granted.",
    male_expression="You embody refined confidence that others find both inspiring and approachable, though you may need to push yourself beyond your comfort zone to fully develop your potential. Your natural charm can open any door, but your character determines where you go.",
    female_expression="You radiate a luminous quality that makes others feel uplifted in your presence, creating harmony wherever you go. Your elegance and warmth build bridges between people and inspire them to see the beauty in themselves.",
    other_expression="You're a natural performer who shines brightest when sharing your gifts with others, turning every interaction into an opportunity for mutual inspiration. Your presence alone can transform the energy of any room or situation."
)

# Sun Square Ascendant
sun_square_asc = SunAscendantAspectInterpretation(
    aspect="Square",
    hook="Your intensity burns bright and sometimes overwhelms.",
    core_interpretation="You feel a constant tension between who you are inside and how the world receives you, often coming across as more forceful or intimidating than you intend. Your journey involves learning to channel your powerful energy in ways that invite others in rather than pushing them away.",
    male_expression="You project strength so intensely that others may feel challenged by your presence, even when you're trying to be friendly. Your growth comes from developing emotional intelligence and learning to modulate your powerful energy.",
    female_expression="You have strong opinions and aren't afraid to express them, but you're learning that being right isn't always as important as being heard. Your boldness is a gift that needs to be wrapped in understanding and patience.",
    other_expression="You burn with an inner fire that can either illuminate or overwhelm, depending on how consciously you direct it. Your most meaningful relationships form with those who appreciate your intensity and help you refine its expression."
)

# Sun Opposition Ascendant
sun_opposition_asc = SunAscendantAspectInterpretation(
    aspect="Opposition",
    hook="You discover yourself through others' eyes.",
    core_interpretation="You come alive through meaningful connections and partnerships, finding your truest self reflected in the people you love and work with closely. Your gift lies in creating deep, transformative relationships, though you're learning to maintain your identity even within intimate bonds.",
    male_expression="You thrive in partnerships where you can both support and be supported, discovering your strength through vulnerability and connection. Your growth comes from learning to stand confidently alone while still cherishing togetherness.",
    female_expression="You have a natural ability to bring out the best in others through your empathetic presence and genuine interest in their wellbeing. Your challenge is remembering your own worth exists independently of others' validation.",
    other_expression="You're a natural mirror who helps others see themselves more clearly, but you're learning that your own reflection is just as valuable. Your deepest wisdom emerges from balancing your gift for connection with strong self awareness."
)

# Dictionary of all Sun Ascendant aspects
sun_ascendant_aspects = {
    "Conjunct": sun_conjunct_asc,
    "Sextile": sun_sextile_asc,
    "Trine": sun_trine_asc,
    "Square": sun_square_asc,
    "Opposition": sun_opposition_asc
}