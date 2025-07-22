class SunMoonAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Sun Conjunct Moon
sun_conjunct_moon = SunMoonAspectInterpretation(
    aspect="Conjunct",
    hook="My heart learned to be strong before it learned to be soft.",
    core_interpretation="You carry deep emotional wisdom and resilience, but often struggle to trust your own feelings or show vulnerability. Your early experiences taught you to be emotionally selfsufficient, creating a responsible but sometimes lonely approach to caring and being cared for.",
    male_expression="You're emotionally strong and dependable, but may struggle to express tenderness. Your growth comes through learning that vulnerability is strength, not weakness.",
    female_expression="You have incredible emotional depth and endurance, yet may feel guilty for having needs. Your power emerges when you honor your sensitivity as much as your strength.",
    other_expression="You're emotionally wise beyond your years but may feel isolated in your feelings. Your gift is teaching others that true strength includes emotional authenticity."
)

# Sun Sextile Moon
sun_sextile_moon = SunMoonAspectInterpretation(
    aspect="Sextile",
    hook="Your emotions have structure and steady, reliable, and built to last.",
    core_interpretation="You have a natural ability to balance emotional needs with practical realities, creating stable and lasting relationships. Your feelings are grounded and mature, allowing you to be both supportive and boundariesaware in your connections with others.",
    male_expression="You're emotionally steady and trustworthy, offering security to others naturally. Your challenge is allowing spontaneity and playfulness into your emotional world.",
    female_expression="You bring wisdom and stability to your relationships while staying emotionally present. Your growth comes through embracing more emotional flexibility and lightness.",
    other_expression="You're emotionally grounded and create safe spaces for others to feel. Your gift is showing that emotional maturity doesn't mean emotional distance."
)

# Sun Trine Moon
sun_trine_moon = SunMoonAspectInterpretation(
    aspect="Trine",
    hook="Your heart is your foundation and solid, enduring, and unshakeable.",
    core_interpretation="You possess exceptional emotional stability and the ability to nurture others without losing yourself. Your feelings are both deep and practical, creating a natural capacity for longterm commitment and emotional leadership that others find deeply comforting.",
    male_expression="You're emotionally mature and naturally protective, offering others a sense of security. Your challenge is not becoming too rigid in your emotional expressions.",
    female_expression="You have a gift for emotional wisdom and can nurture others while maintaining your own center. Your growth comes through staying open to emotional surprises and changes.",
    other_expression="You're emotionally solid and create lasting bonds with others. Your gift is showing that true emotional security comes from within, not from controlling circumstances."
)

# Sun Square Moon
sun_square_moon = SunMoonAspectInterpretation(
    aspect="Square",
    hook="Your heart and your walls are locked in eternal battle.",
    core_interpretation="You experience ongoing tension between your need for emotional connection and your fear of being hurt or rejected. This creates a pushpull dynamic in relationships where you crave intimacy but may sabotage it through emotional defensiveness or excessive selfprotection.",
    male_expression="You struggle between wanting emotional closeness and fearing vulnerability. Your breakthrough comes when you risk being seen in your tenderness, not just your strength.",
    female_expression="You may feel emotionally guarded even when you want to connect deeply. Your power emerges when you trust that your sensitivity is safe to share with the right people.",
    other_expression="You're caught between craving emotional security and fearing emotional exposure. Your gift is learning that true security comes from authentic connection, not emotional armor."
)

# Sun Opposition Moon
sun_opposition_moon = SunMoonAspectInterpretation(
    aspect="Opposition",
    hook="You're pulled between your heart's needs and the world's demands.",
    core_interpretation="You feel constant tension between your emotional needs and your responsibilities, often sacrificing your feelings for duty or structure. This creates a lifelong journey of learning to honor both your inner world and outer obligations without losing yourself in either extreme.",
    male_expression="You may prioritize responsibility over emotional needs, sometimes appearing cold when you're actually protecting yourself. Your growth comes through integrating duty with emotional authenticity.",
    female_expression="You might swing between being overly nurturing and overly distant, struggling to find emotional balance. Your power lies in honoring both your feelings and your boundaries equally.",
    other_expression="You're learning to balance emotional needs with life's demands. Your gift is showing others that responsibility and emotional depth can coexist beautifully."
)

# Dictionary of all SunMoon aspect interpretations
sun_moon_aspects = {
    "Conjunct": sun_conjunct_moon,
    "Sextile": sun_sextile_moon,
    "Trine": sun_trine_moon,
    "Square": sun_square_moon,
    "Opposition": sun_opposition_moon
}