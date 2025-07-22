class SunPlutoAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# sun Conjunct Pluto
sun_conjunct_pluto = SunPlutoAspectInterpretation(
    aspect="Conjunct",
    hook="I forge diamonds from pressure and my strength is earned through fire.",
    core_interpretation="You possess tremendous inner fortitude and the ability to endure and transform through life's most challenging experiences. However, you may struggle with intense control issues and fear of powerlessness, sometimes creating the very crises you're trying to avoid through rigid thinking or behavior.",
    male_expression="You're incredibly resilient but may become overly controlling when threatened. Your power emerges when you learn to trust the process of transformation instead of fighting it.",
    female_expression="You have profound strength and can rebuild from nothing, yet may fear your own intensity. Your gift unfolds when you embrace your power without apology or excessive self-control.",
    other_expression="You're a master of transformation who knows how to survive and thrive through crisis. Your challenge is learning that true security comes from adaptability, not control."
)

# Sun Sextile Pluto
sun_sextile_pluto = SunPlutoAspectInterpretation(
    aspect="Sextile",
    hook="You rebuild wisely and patient transformation with lasting results.",
    core_interpretation="You have a natural ability to work with deep change in structured, sustainable ways, creating lasting transformation without destructive upheaval. Your approach to power and regeneration is methodical and wise, allowing you to build something meaningful from life's challenges.",
    male_expression="You're able to handle intense situations with calm authority and practical wisdom. Your growth comes from not becoming too cautious about embracing necessary changes.",
    female_expression="You transform challenges into opportunities through patient, strategic action. Your power lies in trusting your instincts about when to push forward and when to wait.",
    other_expression="You're a wise architect of change who builds transformation on solid foundations. Your gift is showing others how to evolve without losing what truly matters."
)

# Sun Trine Pluto
sun_trine_pluto = SunPlutoAspectInterpretation(
    aspect="Trine",
    hook="Your power runs deep and steady and unshakeable strength that endures.",
    core_interpretation="You possess natural authority and the ability to handle power responsibly, creating lasting change through disciplined effort and deep insight. Your strength is quiet but profound, and you can rebuild or transform anything you touch with patience and wisdom.",
    male_expression="You're naturally authoritative and can handle crisis with calm competence. Your challenge is not becoming too comfortable with your ability to control difficult situations.",
    female_expression="You have innate wisdom about power dynamics and can create deep change through steady effort. Your growth comes from using your gifts for broader transformation, not just personal security.",
    other_expression="You're blessed with sustainable power that builds rather than destroys. Your gift is demonstrating that true strength comes from inner authority, not external force."
)

# Sun Square Pluto
sun_square_pluto = SunPlutoAspectInterpretation(
    aspect="Square",
    hook="You're caught between order and chaos and forged by the tension between control and surrender.",
    core_interpretation="You experience intense internal pressure between your need for structure and the forces of transformation that constantly challenge your foundations. This creates periods of profound crisis and rebuilding that ultimately teach you that real security comes from inner resilience, not external control.",
    male_expression="You may struggle with authority or become overly rigid when facing change. Your breakthrough comes when you learn to use structure as a tool for transformation, not a shield against it.",
    female_expression="You might swing between excessive control and feeling completely powerless. Your strength emerges when you realize that true power lies in working with change, not against it.",
    other_expression="You're learning that destruction and construction are partners in growth. Your gift is mastering the art of conscious transformation through accepting both order and chaos."
)

# Sun Opposition Pluto
sun_opposition_pluto = SunPlutoAspectInterpretation(
    aspect="Opposition",
    hook="You dance between building and breaking and learning to wield power with wisdom.",
    core_interpretation="You feel pulled between the need for security and stability versus the call for deep transformation and renewal. This creates a lifelong journey of learning when to hold on and when to let go, ultimately teaching you to become a master of both preservation and regeneration.",
    male_expression="You may alternate between rigid control and destructive rebellion against authority. Your growth comes through finding constructive ways to channel your power and need for transformation.",
    female_expression="You might struggle between maintaining stability and embracing necessary change. Your power lies in learning that true security includes the wisdom to evolve and transform.",
    other_expression="You're balancing the forces of creation and destruction in your life. Your gift is learning to be both a builder and a transformer, knowing when each is needed."
)

# Dictionary of all Sun-Pluto aspect interpretations
sun_pluto_aspects = {
    "Conjunct": sun_conjunct_pluto,
    "Sextile": sun_sextile_pluto,
    "Trine": sun_trine_pluto,
    "Square": sun_square_pluto,
    "Opposition": sun_opposition_pluto
}