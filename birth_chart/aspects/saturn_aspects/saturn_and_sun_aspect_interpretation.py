class SaturnSunAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
saturn_sun_conj = SaturnSunAspectInterpretation(
    aspect="Conjunction",
    hook="You stand tall through structure, tempering your will with reality.",
    core_interpretation="You bring authority, discipline, and serious ambition to your endeavors. While you may face early limitations or self criticism, these experiences ultimately foster mature perseverance and a strong sense of responsibility, helping you achieve your goals.",
    male_expression="You are a steadfast leader, gaining strength through patience and integrity. This journey of self discovery and growth helps you build resilience and a stronger sense of self, ultimately leading to personal fulfillment.",
    female_expression="You are a disciplined achiever, blossoming as you own your worth through action. This process of recognizing and embracing your strengths helps you build confidence and achieve your goals with grace and determination.",
    other_expression="You are a centered authority, building confidence from responsible effort. This balance of traits makes you a respected and successful individual, capable of inspiring trust and respect in others."
)

# Sextile
saturn_sun_sextile = SaturnSunAspectInterpretation(
    aspect="Sextile",
    hook="Your ambition is shaped with grace, growing confidence with structure.",
    core_interpretation="You have disciplined growth and vocational competence, allowing your ambition to flow with practicality. This aspect helps you achieve long term success with a grounded and steady approach, making your endeavors both meaningful and fulfilling.",
    male_expression="You are quietly confident, building steadily toward your goals with determination and grace. This trait makes you a reliable and respected figure, capable of achieving your objectives with integrity and responsibility.",
    female_expression="You are a balanced careerist, combining purpose with responsibility in a way that earns admiration and trust. This ability allows you to pursue your goals with a sense of duty and commitment, making you a successful and influential figure.",
    other_expression="You are a purpose aligned builder, achieving through measured authority and a sense of responsibility. This balance of traits makes you a respected and trusted individual, capable of turning visions into reality."
)

# Trine
saturn_sun_trine = SaturnSunAspectInterpretation(
    aspect="Trine",
    hook="You shine through consistency, with identity flowing with integrity.",
    core_interpretation="You have natural maturity and self control, granting ease in leadership and planning. This aspect gives you quiet confidence grounded in discipline, making your endeavors both successful and fulfilling.",
    male_expression="You are a calm architect, embodying steady strength and determination. This trait makes you a respected and influential figure, capable of inspiring confidence and trust in others.",
    female_expression="You are a composed example, leading with integrity and grace in a way that earns admiration and respect. This ability makes you a trusted and successful individual, capable of achieving your goals with responsibility and commitment.",
    other_expression="You have a sustained presence, shining through reliable authority and a sense of duty. This balance of traits makes you a respected and admired figure, capable of turning visions into reality with grace and determination."
)

# Square
saturn_sun_square = SaturnSunAspectInterpretation(
    aspect="Square",
    hook="You push against walls, finding growth in internal resistance.",
    core_interpretation="You often face self doubt or conflict with authority, but this friction fosters resilience and self discipline. Through these challenges, you develop clarity of purpose and the strength to overcome obstacles, ultimately leading to personal growth and fulfillment.",
    male_expression="You are determined but may feel self critical, succeeding through persistent effort and perseverance. This journey of facing and overcoming challenges helps you build resilience and a stronger sense of self, leading to personal growth and fulfillment.",
    female_expression="You are driven yet cautious, maturing by asserting your worth despite obstacles with courage and determination. This process of recognizing and embracing your strengths helps you achieve your goals with greater confidence and grace.",
    other_expression="You have a tested spirit, forging identity through pressure and humility. This dynamic of facing and resolving tensions helps you develop a more robust and resilient character, capable of inspiring trust and respect in others."
)

# Opposition
saturn_sun_opp = SaturnSunAspectInterpretation(
    aspect="Opposition",
    hook="Your reflection is authority, learning balance between self and structure.",
    core_interpretation="You experience tension between self expression and external expectations, often projecting authority onto others. This aspect teaches you to integrate personal ambition with committed relationships, finding a balance that leads to growth and fulfillment.",
    male_expression="You are a reflective leader, growing through balancing autonomy with cooperation and a sense of responsibility. This journey helps you build resilience and a stronger sense of self, ultimately leading to personal growth and fulfillment.",
    female_expression="You are a self aware achiever, finding power in mutual accountability and a sense of duty. This balance of traits makes you a respected and successful individual, capable of inspiring trust and respect in others.",
    other_expression="You are a relational authority, evolving through mirrored responsibility and a sense of commitment. This process of understanding and integrating different aspects of yourself helps you grow into a well rounded and successful individual."
)

saturn_sun_aspects = {
    "Conjunction": saturn_sun_conj,
    "Sextile": saturn_sun_sextile,
    "Trine": saturn_sun_trine,
    "Square": saturn_sun_square,
    "Opposition": saturn_sun_opp
}
