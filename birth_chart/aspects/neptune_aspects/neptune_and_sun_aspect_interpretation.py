class NeptuneSunAspectInterpretation:
    def __init__(self, aspect, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.aspect = aspect
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression

# Conjunction
neptune_sun_conj = NeptuneSunAspectInterpretation(
    aspect="Conjunction",
    hook="Your identity feels woven from dreams and imagination leads your path.",
    core_interpretation="You glow with creative kindness that draws people to you. Turning your big visions into simple daily actions makes your purpose clear.",
    male_expression="Your soft confidence inspires trust in others. Noting one small goal each day grounds your vision.",
    female_expression="Your warm presence lights the way for everyone. Breaking your dreams into steps helps you shine.",
    other_expression="Your gentle charisma heals and uplifts. Linking that to everyday plans keeps your light steady."
)

# Sextile
neptune_sun_sextile = NeptuneSunAspectInterpretation(
    aspect="Sextile",
    hook="Your spirit sparkles with subtle magic and kindness shapes your world.",
    core_interpretation="You inspire through quiet grace and make others feel cared for. Adding a simple habit to express your creativity keeps that magic alive.",
    male_expression="Your calm warmth comforts people around you. Scheduling a few minutes each day for a creative project keeps you energized.",
    female_expression="Your gentle glow brightens any room. Setting aside a little time for your passions keeps your spirit strong.",
    other_expression="Your soft leadership feels nurturing to all. Pairing it with small steps brings your vision into form."
)

# Trine
neptune_sun_trine = NeptuneSunAspectInterpretation(
    aspect="Trine",
    hook="Your heart and purpose dance and compassion feels like destiny.",
    core_interpretation="You lead with both care and clarity, making your approach feel natural. Writing down one clear intention each morning helps you bring your dreams into focus.",
    male_expression="Your genuine kindness builds trust and respect. Noting a simple action plan keeps your path clear.",
    female_expression="Your intuitive drive steers others with ease. A short checklist turns inspiration into reality.",
    other_expression="Your harmonious self uplifts many. Charting a few steps each day brings your goals to life."
)

# Square
neptune_sun_square = NeptuneSunAspectInterpretation(
    aspect="Square",
    hook="Your ego and dreams sometimes clash and tension sparks your evolution.",
    core_interpretation="You juggle between what's real and what's possible, which drives growth. Taking a brief pause to reflect brings calm and clarity to your next move.",
    male_expression="Your visionary heart may feel torn by everyday duties. Pausing for a quick journal entry helps you reconnect with purpose.",
    female_expression="Your imaginative spirit tests limits in reality. Stepping away for a short walk refreshes your outlook.",
    other_expression="Your internal push pull builds wisdom. A moment of stillness reveals your true direction."
)

# Opposition
neptune_sun_opp = NeptuneSunAspectInterpretation(
    aspect="Opposition",
    hook="Your self mirrors your vision and balance reveals your essence.",
    core_interpretation="You find yourself through your big dreams, and honoring both helps you stay grounded. Asking a friend for honest feedback keeps you on track.",
    male_expression="Your compassionate leadership grows when you care for yourself. Letting others share in your vision makes it stronger.",
    female_expression="Your nurturing purpose thrives on mutual support. Inviting others' help strengthens your resolve.",
    other_expression="Your mirrored journey teaches you self awareness. Sharing your goals makes them more real and reachable."
)

neptune_sun_aspects = {
    "Conjunction": neptune_sun_conj,
    "Sextile": neptune_sun_sextile,
    "Trine": neptune_sun_trine,
    "Square": neptune_sun_square,
    "Opposition": neptune_sun_opp
}
