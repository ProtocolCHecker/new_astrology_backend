class SaturnJupiterAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
saturn_jupiter_conj = SaturnJupiterAspectInterpretation(
    aspect="Conjunction",
    hook="You build your path with both faith and careful steps.",
    core_interpretation="You blend ambition with discipline, offering yourself the potential for structured growth and long term success. Your practical idealism helps you achieve meaningful goals.",
    male_expression="You are a purposeful builder, merging vision with reliability. This balance allows you to pursue your dreams while staying grounded, making you a dependable leader in any endeavor.",
    female_expression="You are a realistic optimist, grounding your dreams in structure. This approach helps you turn aspirations into tangible achievements, earning respect and admiration from those around you.",
    other_expression="You are a balanced achiever, thinking big while acting responsibly. This combination of traits makes you a natural at turning ambitious ideas into successful realities."
)

# Sextile
saturn_jupiter_sextile = SaturnJupiterAspectInterpretation(
    aspect="Sextile",
    hook="You harmonize growth with structure, making progress feel graceful.",
    core_interpretation="You support steady progress and wise planning, where opportunities align with disciplined effort. This leads to mature growth and confidence in your abilities.",
    male_expression="You are a tactful planner, acting with both wisdom and ambition. This duality allows you to navigate challenges with foresight, making you a strategic thinker and effective problem solver.",
    female_expression="You are a strategic dreamer, nurturing your goals with care. This balance of vision and practicality helps you achieve your objectives while maintaining harmony in your personal and professional life.",
    other_expression="You experience harmonious growth, building with both vision and prudence. This approach ensures that your ambitions are met with thoughtful planning, leading to sustained success."
)

# Trine
saturn_jupiter_trine = SaturnJupiterAspectInterpretation(
    aspect="Trine",
    hook="Your ambitions flow with ease as purpose aligns with timing.",
    core_interpretation="You have a natural balance between expansion and restraint, enabling confident leadership and clear direction. Your well paced efforts lead to positive outcomes and a strong reputation.",
    male_expression="You are a confident leader, allowing growth within boundaries. This trait makes you adept at inspiring others while maintaining a sense of order and responsibility.",
    female_expression="You are a graceful trailblazer, gliding between order and aspiration. This ability helps you pursue your goals with elegance and determination, making you a respected figure in any setting.",
    other_expression="You achieve effortless success, combining maturity with optimism. This blend of traits ensures that your endeavors are both ambitious and well grounded, leading to fulfilling achievements."
)

# Square
saturn_jupiter_square = SaturnJupiterAspectInterpretation(
    aspect="Square",
    hook="Your faith meets reality, testing your beliefs and boundaries.",
    core_interpretation="You experience tension between your ideals and limitations, often causing frustration or self doubt. However, this friction also drives growth through perseverance when challenges are met constructively.",
    male_expression="You are driven but cautious, learning through trial and integrity. This journey of overcoming obstacles helps you build resilience and a stronger sense of self, ultimately leading to personal growth.",
    female_expression="You are ambitious yet wary, maturing by asserting boundaries. This process of facing and overcoming challenges helps you refine your goals and achieve them with greater confidence.",
    other_expression="You experience conflict driven maturation, growing stronger through friction. This dynamic of facing and resolving tensions helps you develop a more robust and resilient character."
)

# Opposition
saturn_jupiter_opp = SaturnJupiterAspectInterpretation(
    aspect="Opposition",
    hook="Your limits reflect your potential, showing you both sides of growth.",
    core_interpretation="You balance conservation with expansion, learning to navigate your ambitions with realism. This tension encourages you to find compromise, leading to true and sustainable growth.",
    male_expression="You are a balanced explorer, navigating aspiration with realism. This ability to see and integrate different perspectives helps you pursue your goals with a clear and grounded approach.",
    female_expression="You are a reflective achiever, integrating caution and hope. This balance ensures that your ambitions are pursued with a sense of responsibility and foresight, leading to meaningful accomplishments.",
    other_expression="Your vision is shaped by boundaries, evolving through duality. This process of understanding and integrating different aspects of yourself helps you grow into a well rounded and successful individual."
)

saturn_jupiter_aspects = {
    "Conjunction": saturn_jupiter_conj,
    "Sextile": saturn_jupiter_sextile,
    "Trine": saturn_jupiter_trine,
    "Square": saturn_jupiter_square,
    "Opposition": saturn_jupiter_opp
}
