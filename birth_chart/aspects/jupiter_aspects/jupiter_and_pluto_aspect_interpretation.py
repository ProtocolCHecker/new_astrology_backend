class JupiterPlutoAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Jupiter Conjunct Pluto
jupiter_conjunction_pluto = JupiterPlutoAspectInterpretation(
    aspect="Conjunction",
    hook="Your power expands through vision; belief fuels your transformation.",
    core_interpretation="With this conjunction, you possess profound inner force and resilience, driven by a hunger for growth and deeper meaning. You see opportunities where others see limitations, and your ability to reinvent yourself is exceptional. Pursue your ambitions boldly, confronting authority or convention along the way. Your convictions are intense, and your personal power lies in regenerating what no longer serves you and leading others through transformative change.",
    male_expression="You are a strategic powerhouse, pursuing success through inner conviction and insight. Your determination is your strength.",
    female_expression="You are a magnetic reformer, uplifting through purpose and fierce spiritual drive. Your passion is your guide.",
    other_expression="You are an alchemical visionary, fusing belief and intensity to rebuild from the core. Your vision is your gift."
)

# Jupiter Sextile Pluto
jupiter_sextile_pluto = JupiterPlutoAspectInterpretation(
    aspect="Sextile",
    hook="Your empowered growth flows from truth, depth, and inner clarity.",
    core_interpretation="This harmonious aspect blesses you with an intuitive understanding of cycles, change, and personal empowerment. You are driven by a vision of betterment, not only for yourself but for others, and you are adept at channeling your insights into action. Your growth path is rarely superficial; you are attracted to deep truths and can become a quiet authority in your domain. Embrace your skills in managing resources, navigating crises, and regenerating what seems lost.",
    male_expression="You are a perceptive strategist, leading by example and grounded in integrity. Your integrity is your strength.",
    female_expression="You are an insightful builder, nurturing growth through precision and purpose. Your precision is your guide.",
    other_expression="You are a transformative planner, envisioning renewal and making it real. Your vision is your power."
)

# Jupiter Trine Pluto
jupiter_trine_pluto = JupiterPlutoAspectInterpretation(
    aspect="Trine",
    hook="Your effortless evolution  and  your beliefs renew and empower naturally.",
    core_interpretation="With this trine, your capacity for influence and expansion is innate and well balanced. You are attuned to life's deeper undercurrents and have a gift for channeling your ideals into tangible, meaningful outcomes. Your path toward success is subtle but strong, guided by instinct, intelligence, and a deep desire to make things better. Embrace your natural authority and inner discipline to create lasting impact, often behind the scenes or through mentorship and reform.",
    male_expression="You are a quiet force, building a legacy through steady insight and idealism. Your steadiness is your strength.",
    female_expression="You are an empowered healer, using depth and clarity to uplift others. Your clarity is your guide.",
    other_expression="You are a transformational sage, merging power and wisdom with quiet ease. Your wisdom is your gift."
)

# Jupiter Square Pluto
jupiter_square_pluto = JupiterPlutoAspectInterpretation(
    aspect="Square",
    hook="Your relentless ambition meets the limits of control  and  your beliefs demand transformation.",
    core_interpretation="This tense aspect sharpens your hunger for growth and power but often brings friction or extremes in its pursuit. You may feel compelled to prove yourself or challenge systems that restrict your vision. While this can produce incredible results, it demands vigilance; unchecked ambition or ideological rigidity can lead to burnout or conflict. Embrace the challenge of directing your intense energy toward constructive reform, learning the difference between inspired authority and coercive force.",
    male_expression="You are a driven reformer, battling systems to reshape the world. Your drive is your strength, but balance is key.",
    female_expression="You are a restless achiever, seeking truth through confrontation and renewal. Your restlessness is your guide to growth.",
    other_expression="You are a relentless force, transforming pressure into visionary power. Your relentlessness is your path to success."
)

# Jupiter Opposition Pluto
jupiter_opposition_pluto = JupiterPlutoAspectInterpretation(
    aspect="Opposition",
    hook="Your inner world wrestles with outer forces  and  belief and power face off.",
    core_interpretation="This opposition creates a dynamic push pull between expansive ideals and transformational pressure. You may swing between trusting your inner vision and feeling dominated by external systems or expectations. Authority figures can challenge your growth, or you may resist surrendering to a larger process. Through this tension, you develop a sharpened perspective and deep resilience. Embrace the balance to channel your intensity into meaningful reform, aligning personal power with collective purpose.",
    male_expression="You are a polarizing leader, challenging norms to reclaim belief and integrity. Your challenge is your strength, leading to profound impact.",
    female_expression="You are an awakened seeker, learning to channel conflict into growth. Your awakening is your guide to empowerment.",
    other_expression="You are a radical alchemist, integrating control and surrender through belief. Your radicalism is your path to transformation."
)

# Create a dictionary to store all Jupiter Pluto aspect interpretations
jupiter_pluto_aspects = {
    "Conjunction": jupiter_conjunction_pluto,
    "Sextile": jupiter_sextile_pluto,
    "Trine": jupiter_trine_pluto,
    "Square": jupiter_square_pluto,
    "Opposition": jupiter_opposition_pluto
}
