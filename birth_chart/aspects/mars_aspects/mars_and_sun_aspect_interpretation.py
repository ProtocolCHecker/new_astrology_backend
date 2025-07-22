class SunMarsAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

mars_sun_conj = SunMarsAspectInterpretation(
    aspect="Conjunction",
    hook="You burn bright and strike fast your purpose and power move as one",
    core_interpretation="With Sun conjunct Mars you radiate bold energy and instinctive courage always ready to lead When you channel that fire with intention you inspire others if unchecked impatience or conflict may flare up",
    male_expression="You command attention with daring confidence learn to harness your heat to uplift not overpower",
    female_expression="Your passion blazes trails embrace calm reflection to temper any flashes of restlessness",
    other_expression="You fuse identity and action seamlessly finding balance between ego and impulse is your path to growth"
)

mars_sun_sextile = SunMarsAspectInterpretation(
    aspect="Sextile",
    hook="You meet life head on assertive agile and ignited with spark",
    core_interpretation="You are an enterprising spirit and warm confidence that feels natural to others You take initiative with grace though you must guard against stretching yourself too thin",
    male_expression="You lead with approachable energy your blend of courage and care wins long term loyalty",
    female_expression="You step forward with poised enthusiasm remember to pause and recharge your inner flame",
    other_expression="You balance drive and diplomacy your dynamic yet smooth style lights the way"
)

mars_sun_trine = SunMarsAspectInterpretation(
    aspect="Trine",
    hook="Your fire flows steady confident graceful and unwavering",
    core_interpretation="You are an effortless mix of self assurance and action You inspire through calm strength yet you still benefit from challenging yourself to avoid complacency",
    male_expression="You embody composed leadership your quiet courage speaks volumes",
    female_expression="You move with elegant conviction embrace occasional risks to stretch your comfort zone",
    other_expression="You act with purpose and poise letting your passion guide you without disruption"
)

mars_sun_square = SunMarsAspectInterpretation(
    aspect="Square",
    hook="Your will meets friction you grow by fighting to be heard and free",
    core_interpretation="You spark inner tension that can erupt as impatience or conflict pushing you to refine your focus As you learn patience and channel anger constructively you become a powerful catalyst for change",
    male_expression="You charge into challenges pair that fire with self control to turn friction into fuel",
    female_expression="You push boundaries boldly softening your approach can transform clashes into breakthroughs",
    other_expression="You forge identity through conflict mastery comes from directing that energy with clear intent"
)

mars_sun_opp = SunMarsAspectInterpretation(
    aspect="Opposition",
    hook="Your strength is mirrored in conflict you face yourself in every pushback",
    core_interpretation="You highlight tensions between your ego and desires often through clashes with others By owning these reflections and asserting purposefully you learn to harmonize cooperation with self assertion",
    male_expression="You define yourself in competition self awareness will guide that drive toward growth",
    female_expression="You spark intensity in relationships balancing give and take will free your authentic power",
    other_expression="You grow through mirrors of conflict integrating both sides of yourself brings true harmony"
)

sun_mars_aspects = {
    "Conjunction" : mars_sun_conj,
    "Sextile" : mars_sun_sextile,
    "Trine" : mars_sun_trine,
    "Square" : mars_sun_square,
    "Opposition" : mars_sun_opp
}
