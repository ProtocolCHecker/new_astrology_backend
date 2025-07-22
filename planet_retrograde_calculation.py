class PlanetRetrogradeInterpretation:
    def __init__(self, planet, hook, core_interpretation,
                 male_expression, female_expression, other_expression):
        self.planet = planet
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Mercury Retrograde
mercury_retro = PlanetRetrogradeInterpretation(
    planet="Mercury",
    hook="Your mind works backwards to move forward.",
    core_interpretation="You naturally pause before speaking and prefer to think things through completely before making decisions. This gives you a unique ability to catch details others miss and communicate with unusual depth when you're ready.",
    male_expression="You process information slowly but thoroughly, often finding solutions others overlook through your careful review process.",
    female_expression="You express yourself with deliberate thoughtfulness, preferring meaningful conversations over quick exchanges that lack substance."
)

# Venus Retrograde
venus_retro = PlanetRetrogradeInterpretation(
    planet="Venus",
    hook="You love from the inside out.",
    core_interpretation="You develop feelings slowly and value emotional depth over surface attraction, often revisiting past relationships to understand your true desires. Your approach to love and money is unconventional but deeply authentic once you trust yourself.",
    male_expression="You guard your heart carefully, needing time to truly open up, but when you do, your affection runs incredibly deep.",
    female_expression="You question social expectations about beauty and relationships, creating your own standards based on what genuinely resonates with your soul."
)

# Mars Retrograde
mars_retro = PlanetRetrogradeInterpretation(
    planet="Mars",
    hook="Your fire burns inward before it blazes.",
    core_interpretation="You hold back your natural impulses, preferring to build energy internally before taking action, which can make you seem passive but actually makes you more strategic. Your anger and drive work differently than others, requiring patience with your own timing.",
    male_expression="You strategize extensively before acting, sometimes frustrating others with your delays, but your eventual moves are usually well-calculated.",
    female_expression="You channel your ambition quietly, working behind the scenes to achieve goals while others might not even realize how determined you are."
)

# Jupiter Retrograde
jupiter_retro = PlanetRetrogradeInterpretation(
    planet="Jupiter",
    hook="You grow by looking within, not outward.",
    core_interpretation="You question traditional beliefs and create your own philosophy through personal experience rather than accepting what others teach you. Your luck comes from internal wisdom rather than external opportunities, making your success more sustainable but slower to develop.",
    male_expression="You develop faith through skepticism, needing to test beliefs personally before embracing them as your truth.",
    female_expression="You seek meaning through introspection, often finding your greatest insights during quiet moments rather than through formal education."
)

# Saturn Retrograde
saturn_retro = PlanetRetrogradeInterpretation(
    planet="Saturn",
    hook="You build your rules from scratch.",
    core_interpretation="You resist external authority and prefer to create your own structure and discipline, though this can lead to self-doubt about your capabilities. Your relationship with responsibility is complex, but you ultimately develop stronger foundations by questioning what others simply accept.",
    male_expression="You challenge traditional paths to success, creating your own methods even if others don't understand or approve of your approach.",
    female_expression="You struggle with self-imposed standards that are often harsher than what anyone else would place on you, but this drives exceptional personal growth."
)

# Uranus Retrograde
uranus_retro = PlanetRetrogradeInterpretation(
    planet="Uranus",
    hook="Your revolution happens in private first.",
    core_interpretation="You process change internally before expressing your uniqueness to the world, making you seem conventional on the surface while harboring deep desire for freedom. Your innovations come from quiet rebellion rather than dramatic announcements.",
    male_expression="You develop your individuality privately, surprising others when you finally reveal how different your thinking really is.",
    female_expression="You question societal expectations silently, building confidence in your authentic self before sharing your unconventional views with others."
)

# Neptune Retrograde
neptune_retro = PlanetRetrogradeInterpretation(
    planet="Neptune",
    hook="Your dreams need reality checks.",
    core_interpretation="You have powerful intuition but struggle to trust it, often dismissing your psychic impressions as imagination rather than valuable guidance. Your spiritual path requires grounding your visions in practical reality rather than escaping into fantasy.",
    male_expression="You question your intuitive hunches even when they're usually right, needing concrete evidence before trusting your inner knowing.",
    female_expression="You have vivid inner experiences but doubt their significance, gradually learning to honor your mystical insights as valid wisdom."
)

# Pluto Retrograde
pluto_retro = PlanetRetrogradeInterpretation(
    planet="Pluto",
    hook="Your power works in shadows.",
    core_interpretation="You transform yourself from the inside out, working through deep psychological changes privately before others notice your evolution. Your ability to regenerate and reinvent yourself is profound but happens through internal work rather than external drama.",
    male_expression="You process intense emotions privately, emerging from personal crises fundamentally changed but rarely showing others the depth of your transformation.",
    female_expression="You work through power dynamics internally, developing genuine strength by facing your shadows rather than projecting them onto others."
)

planet_retrograde = {
    "Mercury": mercury_retro,
    "Venus": venus_retro,
    "Mars": mars_retro,
    "Jupiter": jupiter_retro,
    "Saturn": saturn_retro,
    "Uranus": uranus_retro,
    "Neptune": neptune_retro,
    "Pluto": pluto_retro
}