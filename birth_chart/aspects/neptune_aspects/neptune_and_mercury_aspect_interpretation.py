class NeptuneMercuryAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
neptune_mercury_conj = NeptuneMercuryAspectInterpretation(
    aspect="Conjunction",
    hook="Your words drift like mist and each phrase carries emotion.",
    core_interpretation="You speak in a way that feels poetic and touching, and people remember what you say. Adding a key takeaway to each talk helps your beautiful ideas stick.",
    male_expression="Your gentle voice comforts and inspires. Summarizing your main point makes your insights easier to follow.",
    female_expression="Your soft spoken thoughts feel like a warm hug. Highlighting one clear message anchors your vision.",
    other_expression="Your heartfelt talk uplifts listeners. Pairing emotion with a simple fact gives it power."
)

# Sextile
neptune_mercury_sextile = NeptuneMercuryAspectInterpretation(
    aspect="Sextile",
    hook="Your mind drifts into inspiration and ideas flow in color.",
    core_interpretation="You connect imagination and clarity in conversation, making chats feel alive. Tying each story to one concrete tip keeps everyone on track.",
    male_expression="Your vivid stories spark curiosity. Ending with a clear action step makes them memorable.",
    female_expression="Your intuitive ideas open hearts and minds. Following each with a simple example brings them home.",
    other_expression="Your creative mind delights listeners. Grounding it with a quick summary boosts impact."
)

# Trine
neptune_mercury_trine = NeptuneMercuryAspectInterpretation(
    aspect="Trine",
    hook="Your thoughts paint poetry and insight flows naturally.",
    core_interpretation="You blend sense and spirit so smoothly that people feel both informed and inspired. Keeping each point brief adds extra punch to your words.",
    male_expression="Your balanced ideas charm audiences. Trimming to one strong sentence highlights your wisdom.",
    female_expression="Your graceful talk feels healing. Condensing your message makes it unforgettable.",
    other_expression="Your harmonious speech resonates deeply. Pairing clarity with feeling makes it stick."
)

# Square
neptune_mercury_square = NeptuneMercuryAspectInterpretation(
    aspect="Square",
    hook="Your mind wanders between dream and detail and tension sparks insight.",
    core_interpretation="You dance between big visions and small facts, and pausing to jot key points brings clarity. A quick note of your main idea keeps your talks focused.",
    male_expression="Your creative leaps surprise and inspire. Writing a short outline helps others follow along.",
    female_expression="Your playful thoughts delight listeners. Pinning down a few bullets grounds your flow.",
    other_expression="Your mental dance excites the mind. A brief outline anchors your imagination."
)

# Opposition
neptune_mercury_opp = NeptuneMercuryAspectInterpretation(
    aspect="Opposition",
    hook="Your heart questions your head and balance is your art.",
    core_interpretation="You bridge emotion and logic in conversation, giving your words real depth. Inviting others to weigh in keeps your ideas balanced.",
    male_expression="Your caring insight shines when you let others share feedback. Asking questions makes your talks richer.",
    female_expression="Your dreamy logic feels vivid and true. Pausing for others' thoughts ensures you stay grounded.",
    other_expression="Your dual view guides listeners deeply. Opening the floor to dialogue seals the connection."
)

neptune_mercury_aspects = {
    "Conjunction": neptune_mercury_conj,
    "Sextile": neptune_mercury_sextile,
    "Trine": neptune_mercury_trine,
    "Square": neptune_mercury_square,
    "Opposition": neptune_mercury_opp
}
