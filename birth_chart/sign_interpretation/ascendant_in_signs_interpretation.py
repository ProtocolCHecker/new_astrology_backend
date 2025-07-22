class AscendantSignInterpretation:
    def __init__(self, sign, hook, core_interpretation, male_expression, female_expression, other_expression):
        self.sign = sign
        self.hook = hook
        self.core_interpretation = core_interpretation
        self.male_expression = male_expression
        self.female_expression = female_expression
        self.other_expression = other_expression


aries_ascendant = AscendantSignInterpretation(
    sign="Aries",
    hook="You charge forward with instinctive confidence.",
    core_interpretation="Your presence radiates bold energy that naturally takes initiative and embraces challenges without hesitation. While your direct approach inspires action, your growth comes from balancing spontaneity with thoughtful timing.",
    male_expression="Your assertive energy and competitive spirit make you a natural leader who thrives on autonomy and fresh challenges.",
    female_expression="Your fiery presence breaks expectations, showing how strength and femininity can coexist with authentic power.",
    other_expression="You redefine courage by embracing raw authenticity that defies conventional labels and limitations."
)

taurus_ascendant = AscendantSignInterpretation(
    sign="Taurus",
    hook="You ground every space with steady presence.",
    core_interpretation="Your calm, reliable nature creates an aura of stability that others instinctively trust and appreciate. While you value comfort and routine, your evolution involves embracing change as an opportunity for deeper security.",
    male_expression="Your quiet strength and practical approach make you a rock for those who earn your loyalty.",
    female_expression="Your nurturing energy and sensual grace create spaces where beauty and comfort naturally flourish.",
    other_expression="You embody earthy wisdom by moving through life at your own purposeful rhythm."
)

gemini_ascendant = AscendantSignInterpretation(
    sign="Gemini",
    hook="You engage the world with curious charm.",
    core_interpretation="Your quick wit and adaptable nature make you fascinating company who can converse on countless topics. While your mental agility is a gift, your depth emerges when you balance observation with meaningful connection.",
    male_expression="Your intellectual humor and playful banter make you the life of any gathering.",
    female_expression="Your expressive eyes and lively conversation reveal a mind that's constantly making connections.",
    other_expression="You demonstrate how identity can be fluid yet coherent through your multifaceted self expression."
)

cancer_ascendant = AscendantSignInterpretation(
    sign="Cancer",
    hook="You sense the emotional currents around you.",
    core_interpretation="Your intuitive presence creates safe spaces where others feel understood on a soul level. While your protective nature serves others well, your power grows when you honor your own emotional needs equally.",
    male_expression="Your quiet empathy and steadfast loyalty redefine strength as emotional availability.",
    female_expression="Your nurturing instincts create warmth that makes any place feel like home.",
    other_expression="You show how sensitivity can be both armor and superpower in navigating the world."
)

leo_ascendant = AscendantSignInterpretation(
    sign="Leo",
    hook="You illuminate every room you enter.",
    core_interpretation="Your radiant confidence and natural charisma command attention while inspiring others to shine. True leadership emerges when you balance self expression with creating space for others' light.",
    male_expression="Your regal presence and generous spirit make you a born leader who elevates everyone around you.",
    female_expression="Your magnetic warmth and creative flair turn ordinary moments into celebrations of life.",
    other_expression="You demonstrate how authentic self love can be revolutionary rather than egotistical."
)

virgo_ascendant = AscendantSignInterpretation(
    sign="Virgo",
    hook="You perceive what others overlook.",
    core_interpretation="Your analytical mind and attentive nature make you exceptionally skilled at improving systems and serving needs. Your wisdom deepens when you apply your discerning eye with self compassion as much as you do to external details.",
    male_expression="Your quiet competence and practical intelligence make you invaluable in any endeavor.",
    female_expression="Your graceful precision and healing presence bring order to chaos with elegant efficiency.",
    other_expression="You show how mindfulness can be both an art form and a service to the world."
)

libra_ascendant = AscendantSignInterpretation(
    sign="Libra",
    hook="You harmonize every interaction.",
    core_interpretation="Your diplomatic charm and aesthetic sense create beautiful connections and environments effortlessly. Your growth comes from balancing others' needs with your own truth to create genuine harmony.",
    male_expression="Your refined manners and fair minded approach make you a natural peacemaker and connector.",
    female_expression="Your elegant presence and social grace bring people together through shared appreciation.",
    other_expression="You demonstrate how balance can be dynamic rather than static in relationships."
)

scorpio_ascendant = AscendantSignInterpretation(
    sign="Scorpio",
    hook="You perceive beneath the surface.",
    core_interpretation="Your intense presence and penetrating insight create an aura of mystery that draws others in. Your power amplifies when you transform suspicion into discernment and control into authentic vulnerability.",
    male_expression="Your quiet intensity and emotional depth make you a formidable yet loyal presence.",
    female_expression="Your magnetic mystery and psychological insight reveal truths others avoid seeing.",
    other_expression="You show how boundaries can be permeable yet strong in navigating intimacy."
)

sagittarius_ascendant = AscendantSignInterpretation(
    sign="Sagittarius",
    hook="You seek horizons beyond the obvious.",
    core_interpretation="Your optimistic spirit and philosophical mind naturally explore life's bigger questions and adventures. Your wisdom grows when you balance your love of freedom with the depth found in committed exploration.",
    male_expression="Your adventurous energy and blunt honesty make you an inspiring truth teller.",
    female_expression="Your free spirited laughter and intellectual curiosity open minds wherever you roam.",
    other_expression="You demonstrate how identity can be both rooted and expansive simultaneously."
)

capricorn_ascendant = AscendantSignInterpretation(
    sign="Capricorn",
    hook="You build foundations that last.",
    core_interpretation="Your disciplined presence and long term vision create structures that stand the test of time. Your maturity blossoms when you balance achievement with emotional connection and self acceptance.",
    male_expression="Your quiet authority and relentless work ethic command respect through actions.",
    female_expression="Your poised resilience and practical wisdom make you a natural leader and strategist.",
    other_expression="You show how tradition can be honored while still evolving beyond limitations."
)

aquarius_ascendant = AscendantSignInterpretation(
    sign="Aquarius",
    hook="You envision what others can't imagine.",
    core_interpretation="Your innovative mind and unconventional perspective naturally challenge the status quo. Your impact deepens when you balance your futuristic vision with present moment human connection.",
    male_expression="Your intellectual edge and humanitarian ideals make you a catalyst for change.",
    female_expression="Your quirky brilliance and independent spirit inspire others to embrace their uniqueness.",
    other_expression="You demonstrate how individuality and community can coexist beautifully."
)

pisces_ascendant = AscendantSignInterpretation(
    sign="Pisces",
    hook="You feel what others ignore.",
    core_interpretation="Your compassionate presence and artistic sensitivity tune into life's subtle undercurrents. Your spiritual power emerges when you balance empathy with healthy boundaries and grounded expression.",
    male_expression="Your soulful eyes and creative spirit reveal depths rarely expressed in words.",
    female_expression="Your ethereal grace and emotional wisdom make you a natural healer and muse.",
    other_expression="You show how fluidity can be both mystical and grounded in daily life."
)


ascendant_signs = {
    "Aries": aries_ascendant,
    "Taurus": taurus_ascendant,
    "Gemini": gemini_ascendant,
    "Cancer": cancer_ascendant,
    "Leo": leo_ascendant,
    "Virgo": virgo_ascendant,
    "Libra": libra_ascendant,
    "Scorpio": scorpio_ascendant,
    "Sagittarius": sagittarius_ascendant,
    "Capricorn": capricorn_ascendant,
    "Aquarius": aquarius_ascendant,
    "Pisces": pisces_ascendant
}