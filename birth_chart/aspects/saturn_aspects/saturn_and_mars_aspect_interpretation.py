class SaturnMarsAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
saturn_mars_conj = SaturnMarsAspectInterpretation(
    aspect="Conjunction",
    hook="You build resilience through life's challenges.",
    core_interpretation="You blend ambition with restraint, making you disciplined and methodical. Your persistence often leads to significant accomplishments, and while you may face delays or frustrations, these experiences ultimately build your stamina and strategic approach to life.",
    male_expression="You are steadfast and stoic, turning setbacks into strength. It's important for you to ease self pressure and recognize that growth comes from both effort and self compassion.",
    female_expression="You are persistent and grounded, overcoming obstacles with care. Remember to soften your approach occasionally to let warmth and joy into your life, enhancing your journey.",
    other_expression="You are a quiet powerhouse, acting with patience and purpose. Your strength grows when you discipline your impulses, allowing you to achieve your goals with grace."
)

# Sextile
saturn_mars_sextile = SaturnMarsAspectInterpretation(
    aspect="Sextile",
    hook="Your grit is guided by wisdom and care.",
    core_interpretation="You have a harmonious blend of drive and discipline, making you reliable and efficient. You initiate projects and follow through with patience, and your work ethic is widely admired.",
    male_expression="You are a practical initiator, acting with both courage and caution. This balance makes you a dependable leader, capable of inspiring confidence in those around you.",
    female_expression="You are organized and motivated, flowing between setup and execution with ease. This ability allows you to achieve your goals while maintaining harmony in your personal and professional life.",
    other_expression="You are a measured mover, with progress that is steady and purposeful. Your direction is always refined, ensuring that your efforts lead to meaningful outcomes."
)

# Trine
saturn_mars_trine = SaturnMarsAspectInterpretation(
    aspect="Trine",
    hook="Your intentions are framed by structure.",
    core_interpretation="You have a natural synergy between energy and form, making you self disciplined and efficient. Your efforts feel sustainable, and you excel in long term initiatives or leadership roles.",
    male_expression="You are composed and capable, with strength that comes without strain. This natural ease in leadership roles allows you to inspire confidence and respect in others.",
    female_expression="You are resilient and poised, acting with steady confidence. This trait makes you a respected figure, capable of achieving your goals with elegance and determination.",
    other_expression="You are structured and kinetic, driving forward in balance. Your purpose meets execution effortlessly, ensuring that your endeavors are both ambitious and well grounded."
)

# Square
saturn_mars_square = SaturnMarsAspectInterpretation(
    aspect="Square",
    hook="Your drive meets obstacles, forging resilience.",
    core_interpretation="You face friction between impulse and limitation, often encountering setbacks or internal blocks. While this can lead to frustration, it also builds character and resilience, teaching you the value of patience and perseverance.",
    male_expression="You are driven but may feel frustrated at times, learning power through patience and inner calm. This journey helps you build resilience and transformative willpower, ultimately leading to personal growth.",
    female_expression="You are strong but may feel restrained, with endurance that strengthens through emotional insight. This process of facing and overcoming challenges helps you refine your goals and achieve them with greater confidence.",
    other_expression="You cultivate mastery through tension, learning to temper your spark with structure. This dynamic of facing and resolving tensions helps you develop a more robust and resilient character."
)

# Opposition
saturn_mars_opp = SaturnMarsAspectInterpretation(
    aspect="Opposition",
    hook="Your push meets resistance, teaching balance.",
    core_interpretation="You balance action with restriction, often facing conflicts where ambition meets boundaries. This dynamic teaches you to own your drive consciously, using challenges as guides rather than obstacles.",
    male_expression="You are firm but may be reactive, growing by integrating inner and outer demands. This ability to balance different aspects of yourself helps you pursue your goals with a clear and grounded approach.",
    female_expression="You are determined yet cautious, finding empowerment through conscious courage. This balance ensures that your ambitions are pursued with a sense of responsibility and foresight, leading to meaningful accomplishments.",
    other_expression="You are a reflective warrior, using conflict as a mirror for mature action. This process of understanding and integrating different aspects of yourself helps you grow into a well rounded and successful individual."
)

# Dictionary of all aspects
saturn_mars_aspects = {
    "Conjunction": saturn_mars_conj,
    "Sextile": saturn_mars_sextile,
    "Trine": saturn_mars_trine,
    "Square": saturn_mars_square,
    "Opposition": saturn_mars_opp
}
