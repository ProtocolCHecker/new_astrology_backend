class JupiterMercuryAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Mercury Conjunct Jupiter
jupiter_conjunction_mercury = JupiterMercuryAspectInterpretation(
    aspect="Conjunction",
    hook="Your mind dreams in widescreen  and  thoughts soar beyond the horizon of facts.",
    core_interpretation="With Mercury conjunct Jupiter, your intellect blends seamlessly with expansive vision. You think big, speak boldly, and seek meaning in every idea. You are a natural teacher, storyteller, or philosopher, always curious and sharing. Your words are optimistic and inspiring, though sometimes exaggerated. Embrace your enthusiasm and generosity of thought, but remember to ground your ideas in details.",
    male_expression="You are a charismatic thinker, speaking with confidence and breadth. While you may overpromise or overtalk, your aim is always to inspire. Your confidence is infectious.",
    female_expression="You are a wise and visionary communicator, bridging intellect with idealism. Grounding your ideas in detail will help you follow through. Your wisdom is your guide.",
    other_expression="You have a cosmic mind, connecting dots between disciplines, cultures, and truths. Your imagination thrives when anchored in practice. Your vision is your gift."
)

# Mercury Sextile Jupiter
jupiter_sextile_mercury = JupiterMercuryAspectInterpretation(
    aspect="Sextile",
    hook="You speak the language of growth  and  ideas are seeds, and you're always planting.",
    core_interpretation="Mercury sextile Jupiter offers you a graceful link between communication and philosophy. You have a natural ease in teaching, writing, and storytelling, making complex ideas accessible. You are intellectually curious and optimistic, always looking to broaden perspectives. Your mental agility and hunger for understanding make you a tolerant and fair minded thinker. Embrace your role as a wise advisor and open hearted communicator.",
    male_expression="You are mentally adventurous and fair, enjoying sharing ideas across cultures or disciplines. You help others see the bigger picture. Your curiosity is your strength.",
    female_expression="You are thoughtful and encouraging, uplifting others through your words and understanding. You are often drawn to education or global learning. Your encouragement is your power.",
    other_expression="You are an intellectual bridge builder, seeing unity in diversity. You communicate with warmth, wisdom, and future minded grace. Your vision is your compass."
)

# Mercury Trine Jupiter
jupiter_trine_mercury = JupiterMercuryAspectInterpretation(
    aspect="Trine",
    hook="Your thoughts flow like rivers of gold  and  what you speak, you believe into being.",
    core_interpretation="With Mercury trine Jupiter, you possess clear thinking, an elevated perspective, and optimistic communication. You have a natural eloquence and a mind that harmonizes detail with vision. You are often admired for your wisdom and open mindedness. Embrace your talent for teaching, writing, and mentoring, particularly in philosophy, spirituality, or global affairs. Your good judgment and forward thinking mindset attract fortune.",
    male_expression="You are calmly confident and expansive in thought, communicating from a place of clarity and belief. You are a wise teacher or guide. Your clarity is your superpower.",
    female_expression="You are a warm and visionary communicator, speaking with purpose, grace, and moral clarity. You may find a calling in education or justice. Your purpose is your guide.",
    other_expression="You are a harmonious mind soul channel, bringing ideas to life through insight and inspiration. You live to illuminate truth. Your insight is your gift."
)

# Mercury Square Jupiter
jupiter_square_mercury = JupiterMercuryAspectInterpretation(
    aspect="Square",
    hook="You speak in fireworks  and  brilliant, loud, sometimes too soon.",
    core_interpretation="Mercury square Jupiter fuels a restless and exuberant mind that leaps to conclusions and thrives on mental adventure. You are animated and outspoken, swinging between sharp critique and grand optimism. Your ideas are big, sometimes too big to fully ground, and you may promise more than you can deliver. Embrace the challenge of pacing your thought process and integrating detail with vision. Your enthusiasm is your strength, but grounding it will make you even more compelling.",
    male_expression="You are a bold thinker, leaping into ideas with gusto. Be mindful of overconfidence and cultivate intellectual discipline. Your boldness is your power.",
    female_expression="You are expressive and passionate, speaking with conviction. You may waver between critique and belief, but you find power in balance. Your passion is your guide.",
    other_expression="You are an unfiltered philosopher, thriving on mental friction but growing through grounded truth. Learn to speak with both fire and care. Your growth is your journey."
)

# Mercury Opposite Jupiter
jupiter_opposition_mercury = JupiterMercuryAspectInterpretation(
    aspect="Opposition",
    hook="Your words stretch across oceans  and  sometimes you forget where the shore is.",
    core_interpretation="This opposition challenges the balance between detail and meaning, fact and faith. You often fluctuate between skepticism and idealism, swinging from highly logical to swept up in grand ideas. You can be a compelling speaker but may struggle with consistency or focus. Embrace your gift for synthesizing wide ranging ideas and learn to filter and refine them. Your journey involves integrating both perspectives into a coherent and wise voice.",
    male_expression="You are thoughtful but restless, stretching your mental limits and testing your intellectual ground. Commit to clarity and find your strength.",
    female_expression="You express paradox, dancing between faith and fact. You gain power when rooted in discernment and a steady voice. Your discernment is your guide.",
    other_expression="You are a seeker of meaning, walking the edge between insight and excess. Flourish when your inner contradictions become creative synthesis. Your synthesis is your gift."
)

# Create a dictionary to store all Jupiter Mercury aspect interpretations
jupiter_mercury_aspects = {
    "Conjunction": jupiter_conjunction_mercury,
    "Sextile": jupiter_sextile_mercury,
    "Trine": jupiter_trine_mercury,
    "Square": jupiter_square_mercury,
    "Opposition": jupiter_opposition_mercury
}
