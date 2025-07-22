class MarsUranusAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

mars_uranus_conj = MarsUranusAspectInterpretation(
    aspect="Conjunct",
    hook="You shatter molds with electric courage rules bend before your will",
    core_interpretation="You are a fearless trailblazer whose drive for freedom sparks innovation grounding that impulse will turn brilliance into lasting impact",
    male_expression="You charge with fearless originality learn to pair impulse with strategy to avoid misfires",
    female_expression="You blaze your own path with daring grace honor moments of pause to refine your edge",
    other_expression="You fuse passion with invention finding structure for your sparks is your greatest mastery"
)

mars_uranus_sextile = MarsUranusAspectInterpretation(
    aspect="Sextile",
    hook="Your instinct is electric you pivot on a dime and light up every room",
    core_interpretation="You are a nimble creativity and swift adaptability focus your energy so that every flash of insight builds toward meaningful change",
    male_expression="You bring visionary energy to the group stay rooted to turn ideas into reality",
    female_expression="You innovate with effortless flair balance spontaneity with followthrough to see results",
    other_expression="You catalyze progress with bright impulses channeling that buzz into purpose sharpens your power"
)

mars_uranus_trine = MarsUranusAspectInterpretation(
    aspect="Trine",
    hook="Your energy flows like lightning original vibrant and free",
    core_interpretation="You blend seamless boldness with authentic insight making you a natural pioneer remain grounded so your sparks dont burn out too soon",
    male_expression="You lead with calm innovation your steady confidence makes change feel effortless",
    female_expression="You energize with graceful originality embrace discipline to give your ideas wings",
    other_expression="You harmonize action and invention steady rhythm transforms flashes into breakthroughs"
)

mars_uranus_square = MarsUranusAspectInterpretation(
    aspect="Square",
    hook="You clash with every boundary your impulse is raw electric and urgent",
    core_interpretation="You fuel restless rebellion and sudden outbursts learning to channel that volatile energy into constructive invention is your path to growth",
    male_expression="You rebel with explosive force practice patience to turn friction into fuel",
    female_expression="You charge ahead when provoked softening your edge can prevent selfsabotage",
    other_expression="You forge resilience in the spark of conflict grounding your brilliance tames the storm"
)

mars_uranus_opp = MarsUranusAspectInterpretation(
    aspect="Opposition",
    hook="You dance with chaos every clash awakens your authentic self",
    core_interpretation="You highlight tension between your will and the unpredictable mastering timing and inner calm will transform disruption into creative breakthroughs",
    male_expression="You thrive on challenge selfawareness will guide your bold innovations",
    female_expression="You ignite growth through relational sparks finding balance amid chaos empowers you",
    other_expression="You meld opposing forces into dynamic energy embracing stillness reveals where to strike next"
)

mars_uranus_aspects = {
    "Conjunct": mars_uranus_conj,
    "Sextile": mars_uranus_sextile,
    "Trine": mars_uranus_trine,
    "Square": mars_uranus_square,
    "Opposition": mars_uranus_opp
}
