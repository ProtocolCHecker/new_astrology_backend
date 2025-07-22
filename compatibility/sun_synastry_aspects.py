class SunSynastryAspects:
    def __init__(self):
        self.aspects = {
            # Sun-Sun Aspects
            "Sun Conjunction Sun": "You mirror each other's essence—same values, same spark. Instant recognition, but may lack growth if you're *too* similar. Comfortable but watch for stagnation.",
            "Sun Opposition Sun": "You're drawn to each other's polar energies—yin to yang. Thrilling at first, but long-term requires embracing differences, not just tolerating them.",
            "Sun Trine Sun": "You align effortlessly—mutual respect, shared purpose. A rare 'soul tribe' vibe where being together feels like coming home.",
            "Sun Sextile Sun": "You gently enhance each other—no drama, just steady support. A low-key but enduring bond built on mutual appreciation.",
            "Sun Square Sun": "Your egos clash—competing visions, stubborn standoffs. Friction forces growth if you're willing to adapt, not dominate.",

            # Sun-Moon Aspects
            "Sun Conjunction Moon": "You fulfill each other—the Sun person's light nourishes the Moon person's emotions. A heart-and-soul bond, but risks codependency if boundaries blur.",
            "Sun Opposition Moon": "You trigger each other's needs—the Sun person's logic vs. the Moon person's moods. A push-pull that teaches balance between ego and emotion.",
            "Sun Trine Moon": "You harmonize like sunlight on water—natural emotional flow. The Sun person uplifts, the Moon person nurtures. A sanctuary bond.",
            "Sun Sextile Moon": "You soften each other's edges—gentle emotional support without smothering. A safe space to grow at your own pace.",
            "Sun Square Moon": "Your needs war—the Sun person's bluntness hurts, the Moon person's sensitivity frustrates. A crash course in emotional intelligence.",

            # Sun-Ascendant Aspects
            "Sun Conjunction Ascendant": "You see each other clearly—the Sun person embodies the Ascendant person's ideal self. Magnetic, but risks projection ('You're perfect! ...Wait, you're not?').",
            "Sun Opposition Ascendant": "You're karmic mirrors—the Sun person reflects what the Ascendant person seeks in partnership. Romantic potential, but requires seeing beyond the fantasy.",
            "Sun Trine Ascendant": "You bring out each other's best—the Sun person's confidence elevates the Ascendant person's charm. A naturally charismatic duo.",
            "Sun Sextile Ascendant": "You polish each other's shine—subtle boosts to charisma and self-assurance. A 'power couple' potential with minimal effort.",
            "Sun Square Ascendant": "Your personas clash—the Sun person's authenticity jars the Ascendant person's social mask. Growth comes through embracing realness over image.",

            # Sun-Mercury Aspects
            "Sun Conjunction Mercury": "You speak the same language—the Mercury person articulates the Sun person's soul. Mental chemistry so strong it's almost psychic.",
            "Sun Opposition Mercury": "You debate passionately—the Mercury person challenges, the Sun person defends. Stimulating if you love sparring, exhausting if not.",
            "Sun Trine Mercury": "You inspire each other's minds—ideas flow, conversations spark. A bond that thrives on shared curiosity and wit.",
            "Sun Sextile Mercury": "You gently sharpen each other's thoughts—no pressure, just playful mental nudges. A low-pressure meeting of minds.",
            "Sun Square Mercury": "Your communication fractures—the Mercury person nitpicks, the Sun person takes it personally. Requires patience and thicker skin.",

            # Sun-Mars Aspects
            "Sun Conjunction Mars": "You ignite each other—electric chemistry, shared drive. Passionate but volatile if egos collide.",
            "Sun Opposition Mars": "You're fire and flint—sparks fly (in bed *and* arguments). A love-hate dynamic that never bores.",
            "Sun Trine Mars": "You fight *for* each other, not against—unstoppable teamwork. A bond that thrives on shared goals and mutual respect.",
            "Sun Sextile Mars": "You motivate without pressure—the Mars person's drive complements the Sun person's vision. A quietly powerful duo.",
            "Sun Square Mars": "Your tempers clash—power struggles, explosive makeups. A crucible for learning healthy conflict.",

            # Sun-Jupiter Aspects
            "Sun Conjunction Jupiter": "You amplify each other's light—the Jupiter person's optimism magnifies the Sun person's radiance. A bond that feels *lucky*.",
            "Sun Opposition Jupiter": "Your beliefs clash—the Jupiter person preaches, the Sun person resists. Growth comes through debating, not dismissing.",
            "Sun Trine Jupiter": "You expand each other's worlds—adventure, wisdom, shared joy. A bond that makes life feel bigger.",
            "Sun Sextile Jupiter": "You nudge each other toward growth—gentle but meaningful encouragement. A partnership that elevates over time.",
            "Sun Square Jupiter": "Your philosophies war—one's optimism feels naive, the other's realism seems cynical. A test of open-mindedness.",

            # Sun-Saturn Aspects
            "Sun Conjunction Saturn": "You balance each other—the Saturn person's discipline grounds the Sun person's fire. A slow-burn but enduring bond.",
            "Sun Opposition Saturn": "Your rhythms clash—the Saturn person restricts, the Sun person rebels. A tension that teaches patience and timing.",
            "Sun Trine Saturn": "You build legacies together—the Saturn person's wisdom guides the Sun person's ambition. A rock-solid foundation.",
            "Sun Sextile Saturn": "You grow steadily—no shortcuts, just mutual support through life's tests. A bond that deepens with time.",
            "Sun Square Saturn": "Your needs conflict—the Saturn person's caution feels like rejection to the Sun person. A lesson in trust and perseverance.",

            # Sun-Venus Aspects
            "Sun Conjunction Venus": "You adore each other—the Venus person's affection makes the Sun person glow. A warm, loving bond that thrives on mutual appreciation.",
            "Sun Opposition Venus": "You love differently—the Venus person's harmony clashes with the Sun person's ego. A tension that refines your love languages.",
            "Sun Trine Venus": "You romance effortlessly—shared joy, natural affection. A bond that makes love feel easy and right.",
            "Sun Sextile Venus": "You gently sweeten each other's lives—small gestures, steady devotion. A quietly nurturing love.",
            "Sun Square Venus": "Your values clash—one's independence threatens the other's need for closeness. Requires compromise, not ultimatums.",

            # Sun-Neptune Aspects
            "Sun Conjunction Neptune": "You idealize each other—a dreamy, soulful bond. Beware: the pedestal is high, and the fall hurts.",
            "Sun Opposition Neptune": "Your realities diverge—the Neptune person fantasizes, the Sun person demands truth. A test of boundaries and clarity.",
            "Sun Trine Neptune": "You transcend together—artistic, spiritual, or psychic synergy. A bond that defies logic.",
            "Sun Sextile Neptune": "You inspire each other's magic—subtle but profound creative or spiritual growth. A softly luminous connection.",
            "Sun Square Neptune": "Your visions clash—one's idealism feels delusional to the other. Requires grounding in truth, not just hope.",

            # Sun-Uranus Aspects
            "Sun Conjunction Uranus": "You electrify each other—unpredictable, thrilling, but unstable. A bond that refuses to be boxed in.",
            "Sun Opposition Uranus": "Your needs war—freedom vs. commitment. Exhilarating if you embrace the tension, exhausting if not.",
            "Sun Trine Uranus": "You revolutionize each other—growth through rebellion. A bond that thrives on authenticity, not tradition.",
            "Sun Sextile Uranus": "You nudge each other awake—gentle but irreversible shifts toward individuality. A quietly transformative match.",
            "Sun Square Uranus": "Your energies explode—sudden breakups, shocking revelations. A test of adaptability and trust.",

            # Sun-Pluto Aspects
            "Sun Conjunction Pluto": "You transform each other—obsessive, intense, irrevocable. A bond that leaves no one unchanged.",
            "Sun Opposition Pluto": "Your power struggles are epic—control vs. surrender. A crucible for shadow work and rebirth.",
            "Sun Trine Pluto": "You evolve together—facing darkness, emerging stronger. A bond built on unshakable trust and depth.",
            "Sun Sextile Pluto": "You gently unmask each other—no forced drama, just steady empowerment. A resilient, deepening connection.",
            "Sun Square Pluto": "Your demons dance—jealousy, manipulation, or psychological games. The ultimate test of integrity.",

            # Sun-Medium Coeli Aspects
            "Sun Conjunction Medium Coeli": "You elevate each other's destiny—the Sun person's radiance propels the MC person's career. A power duo with shared ambition.",
            "Sun Opposition Medium Coeli": "Your priorities clash—personal joy vs. professional demands. Requires balancing love and legacy.",
            "Sun Trine Medium Coeli": "You rise together—the Sun person's confidence amplifies the MC person's success. A naturally supportive power dynamic.",
            "Sun Sextile Medium Coeli": "You nudge each other toward influence—strategic, gradual growth. A bond that thrives on mutual respect.",
            "Sun Square Medium Coeli": "Your paths conflict—the Sun person's needs disrupt the MC person's reputation. A test of loyalty vs. ambition."
        }

    def get_aspect_interpretation(self, aspect_name):
        return self.aspects.get(aspect_name, "Aspect interpretation not found.")

    def add_aspect(self, aspect_name, interpretation):
        self.aspects[aspect_name] = interpretation

    def remove_aspect(self, aspect_name):
        if aspect_name in self.aspects:
            del self.aspects[aspect_name]