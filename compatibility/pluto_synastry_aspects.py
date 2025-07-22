class PlutoSynastryAspects:
    def __init__(self):
        self.aspects = {
            "Pluto Conjunction Sun": "You ignite each other's core identity—the Pluto person forces deep evolution, while the Sun person fuels their power. A bond that can feel fated, but power struggles may arise if egos clash.",
            "Pluto Opposition Sun": "Your wills clash—the Pluto person's intensity feels controlling to the Sun person, who may resist being 'transformed.' A battle of dominance that, if navigated, can forge unshakable strength.",
            "Pluto Trine Sun": "You empower each other effortlessly—the Pluto person's depth helps the Sun person rise stronger. A rare, regenerative bond where growth feels destined.",
            "Pluto Sextile Sun": "You gently push each other toward evolution—subtle but profound shifts in self-expression. A supportive, low-drama transformative connection.",
            "Pluto Square Sun": "Your egos collide—the Pluto person's demands feel suffocating, the Sun person's pride triggers control issues. A crucible for growth if both surrender the need to 'win.'",
            "Pluto Conjunction Moon": "You emotionally merge—the Pluto person unearths buried wounds, the Moon person nurtures their intensity. Deeply cathartic but can veer into codependency.",
            "Pluto Opposition Moon": "Your emotional needs war—the Pluto person's depth overwhelms, the Moon person's sensitivity feels 'weak.' A painful but revealing mirror for healing.",
            "Pluto Trine Moon": "You heal each other's past—the Pluto person's insight helps the Moon person release old pain. A soulful, nurturing bond.",
            "Pluto Sextile Moon": "You gently deepen emotional trust—no forced drama, just steady transformation. A safe space for vulnerability.",
            "Pluto Square Moon": "Your emotional styles clash—the Pluto person's intensity feels like manipulation, the Moon person's moods seem irrational. Requires radical honesty.",
            "Pluto Conjunction Ascendant": "You redefine each other—the Pluto person's presence alters how the Ascendant person is perceived. A bond that transforms identity, for better or worse.",
            "Pluto Opposition Ascendant": "Your energies repel at first—the Pluto person's demands feel oppressive, the Ascendant person's authenticity seems 'superficial.' A tension that demands integration.",
            "Pluto Trine Ascendant": "You evolve each other naturally—the Pluto person's depth helps the Ascendant person own their power. A quietly life-changing match.",
            "Pluto Sextile Ascendant": "You nudge each other toward growth—subtle shifts in self-expression that build over time. A supportive, low-intensity transformative bond.",
            "Pluto Square Ascendant": "Your identities clash—the Pluto person pushes change, the Ascendant person resists. A power struggle that forces self-confrontation.",
            "Pluto Conjunction Mercury": "You read each other's minds—the Pluto person exposes hidden truths, the Mercury person articulates their depth. Conversations can feel hypnotic or manipulative.",
            "Pluto Opposition Mercury": "Your thoughts war—the Pluto person's intensity overwhelms, the Mercury person's logic seems shallow. A battle of perspectives that can sharpen both.",
            "Pluto Trine Mercury": "You unlock each other's genius—psychological insight meets razor-sharp communication. A bond that thrives on intellectual depth.",
            "Pluto Sextile Mercury": "You gently deepen each other's thinking—no forced intensity, just gradual 'aha' moments. A mentally stimulating but safe connection.",
            "Pluto Square Mercury": "Your communication fractures—the Pluto person's probing feels invasive, the Mercury person's detachment seems evasive. Requires patience.",
            "Pluto Conjunction Venus": "You obsess over each other—the Pluto person ignites primal desire, the Venus person softens their edge. Passionate but possessive.",
            "Pluto Opposition Venus": "Your love languages clash—the Pluto person craves fusion, the Venus person needs harmony. A tension that breeds either depth or destruction.",
            "Pluto Trine Venus": "You love with terrifying depth—soulmate-level intimacy, unshakable loyalty. A bond that transcends the superficial.",
            "Pluto Sextile Venus": "You deepen each other's capacity for love—gentle but transformative. A romance that grows richer over time.",
            "Pluto Square Venus": "Your desires war—jealousy, control issues, or power plays may erupt. A test of trust and surrender.",
            "Pluto Conjunction Mars": "You electrify each other—the Pluto person's focus meets the Mars person's drive. A powerhouse duo, but explosive if unchecked.",
            "Pluto Opposition Mars": "Your energies clash—the Pluto person's control frustrates, the Mars person's impulsiveness triggers. A dynamic that demands compromise.",
            "Pluto Trine Mars": "You fight for each other, not against—shared intensity fuels unstoppable teamwork. A bond that thrives on challenge.",
            "Pluto Sextile Mars": "You motivate each other subtly—no drama, just steady progress toward shared goals. A quietly potent match.",
            "Pluto Square Mars": "Your wills collide—power struggles, explosive arguments, or dominance games. A crucible for learning healthy conflict.",
            "Pluto Conjunction Jupiter": "You expand through crisis—the Pluto person's depth tempers the Jupiter person's optimism. A bond that thrives on shared philosophy.",
            "Pluto Opposition Jupiter": "Your beliefs war—the Pluto person's skepticism clashes with the Jupiter person's faith. A tension that breeds wisdom if respected.",
            "Pluto Trine Jupiter": "You grow through shared truth—the Pluto person's insight grounds the Jupiter person's vision. A rare, enlightening bond.",
            "Pluto Sextile Jupiter": "You gently broaden each other's horizons—transformation meets opportunity. A supportive, wisdom-building connection.",
            "Pluto Square Jupiter": "Your approaches to growth clash—one's optimism feels naive, the other's depth seems heavy. Requires balance.",
            "Pluto Conjunction Saturn": "You rebuild each other—the Pluto person's destruction meets the Saturn person's discipline. A bond that forges resilience.",
            "Pluto Opposition Saturn": "Your structures war—the Pluto person demands change, the Saturn person resists. A test of patience and timing.",
            "Pluto Trine Saturn": "You transform systems together—the Pluto person's depth strengthens the Saturn person's foundations. A masterclass in lasting growth.",
            "Pluto Sextile Saturn": "You evolve each other steadily—no forced upheavals, just incremental empowerment. A mature, enduring bond.",
            "Pluto Square Saturn": "Your rhythms clash—the Pluto person's urgency frustrates, the Saturn person's caution triggers. A lesson in pacing.",
            "Pluto Conjunction Uranus": "You revolutionize each other—the Pluto person's depth fuels the Uranus person's rebellion. A bond that thrives on chaos.",
            "Pluto Opposition Uranus": "Your freedoms war—the Pluto person's control clashes with the Uranus person's spontaneity. A tension that demands flexibility.",
            "Pluto Trine Uranus": "You disrupt systems together—the Pluto person's insight guides the Uranus person's innovation. A brilliantly subversive match.",
            "Pluto Sextile Uranus": "You nudge each other toward change—gentle but irreversible shifts. A bond that thrives on reinvention.",
            "Pluto Square Uranus": "Your energies explode—unpredictable power struggles or sudden fractures. A test of adaptability.",
            "Pluto Conjunction Neptune": "You dissolve boundaries—the Pluto person's depth merges with the Neptune person's mysticism. A transcendent but confusing bond.",
            "Pluto Opposition Neptune": "Your realities war—the Pluto person's scrutiny clashes with the Neptune person's idealism. A tension between truth and illusion.",
            "Pluto Trine Neptune": "You awaken each other's intuition—a psychic, soul-level connection. A bond that defies logic.",
            "Pluto Sextile Neptune": "You gently deepen each other's spirituality—no forced intensity, just quiet revelation. A mystically enriching match.",
            "Pluto Square Neptune": "Your visions clash—the Pluto person's skepticism wounds, the Neptune person's dreams seem delusional. Requires grounding.",
            "Pluto Conjunction Pluto": "You mirror each other's darkness—a bond of terrifying depth, shared obsessions, or mutual evolution. Not for the faint-hearted.",
            "Pluto Opposition Pluto": "Your shadows war—power struggles, psychological games, or competing transformations. A battle for self-mastery.",
            "Pluto Trine Pluto": "You evolve together seamlessly—a rare, alchemical bond where growth feels inevitable. Unstoppable when united.",
            "Pluto Sextile Pluto": "You nudge each other toward empowerment—subtle but profound shifts in self-awareness. A quietly transformative connection.",
            "Pluto Square Pluto": "Your demons clash—control issues, manipulation, or destructive patterns. A crucible for shadow work.",
            "Pluto Conjunction Medium Coeli": "You redefine each other's legacy—the Pluto person's influence reshapes the MC person's career. A bond that alters destinies.",
            "Pluto Opposition Medium Coeli": "Your ambitions war—the Pluto person's depth disrupts the MC person's public image. A tension between authenticity and success.",
            "Pluto Trine Medium Coeli": "You rise together—the Pluto person's insight elevates the MC person's professional power. A match that thrives on shared ambition.",
            "Pluto Sextile Medium Coeli": "You nudge each other toward influence—subtle but strategic career evolution. A bond built on mutual respect.",
            "Pluto Square Medium Coeli": "Your paths clash—the Pluto person's demands destabilize the MC person's reputation. A test of integrity."
        }

    def get_aspect_interpretation(self, aspect_name):
        return self.aspects.get(aspect_name, "Aspect interpretation not found.")

    def add_aspect(self, aspect_name, interpretation):
        self.aspects[aspect_name] = interpretation

    def remove_aspect(self, aspect_name):
        if aspect_name in self.aspects:
            del self.aspects[aspect_name]