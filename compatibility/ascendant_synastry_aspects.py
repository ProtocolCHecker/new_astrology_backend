class AscendantSynastryAspects:
    def __init__(self):
        self.aspects = {
            "Ascendant Conjunction Sun": "You instantly feel energized and seen when you're together. Their presence amplifies your authenticity and confidence in a very natural way.",
            "Ascendant Opposition Sun": "You're drawn to their warmth yet may project your ideals onto them, creating intense attraction that risks overshadowing your own identity. This can feel exciting but may leave you questioning who's shining brightest.",
            "Ascendant Trine Sun": "You experience effortless harmony and mutual encouragement in expressing yourselves. Their optimism and your natural flair blend to uplift both of you.",
            "Ascendant Sextile Sun": "You feel a gentle spark of support when they're around, nudging you to be your best version. This easy connection lets you assist each other without feeling overwhelmed.",
            "Ascendant Square Sun": "You may sense a clash between their style and how you wish to present yourself, stirring inner tension around authenticity. Embrace this challenge as an invitation to refine your self-expression.",

            "Ascendant Conjunction Moon": "You feel deeply nurtured and understood emotionally by them, as if your feelings are mirrored. This creates a comforting bond where you can reveal your vulnerabilities safely.",
            "Ascendant Opposition Moon": "You're drawn to their emotional depth but may encounter old family patterns that surface unexpectedly. This can feel supportive yet triggering if you're unprepared for intimacy.",
            "Ascendant Trine Moon": "You find emotional support flows naturally between you, creating a soothing sense of belonging. Their caring responses perfectly echo your need for acceptance.",
            "Ascendant Sextile Moon": "You sense a gentle emotional rapport that helps you relax and open up. This easy exchange allows you both to feel at home in each other's company.",
            "Ascendant Square Moon": "You might feel unsettled by their emotional intensity, clashing with how you want to show up socially. This tension invites you to balance your need for space with their desire for closeness.",

            "Ascendant Conjunction Mercury": "You click mentally and feel genuinely heard in conversation with them. Their communication style aligns with yours, making ideas flow effortlessly.",
            "Ascendant Opposition Mercury": "You're intrigued by their different viewpoint, which can spark lively debate but also misunderstandings. This dynamic challenges you to listen and articulate your needs more clearly.",
            "Ascendant Trine Mercury": "You experience smooth intellectual rapport that feels intuitive and enlightening. Their insights complement your natural curiosity without any strain.",
            "Ascendant Sextile Mercury": "You enjoy a subtle encouragement to share thoughts and broaden your perspective. This connection helps you polish your communication gracefully.",
            "Ascendant Square Mercury": "You may feel misunderstood or challenged by their way of thinking, stirring friction in how you wish to present yourself. This aspect pushes you to clarify your boundaries and speak up.",

            "Ascendant Conjunction Venus": "You feel irresistibly attractive in their eyes and deeply appreciated. Their affection highlights your charm and makes you glow with self-worth.",
            "Ascendant Opposition Venus": "You're drawn to their beauty and grace but risk losing yourself in an idealized romance. Stay mindful of balancing your needs with your admiration for them.",
            "Ascendant Trine Venus": "You savor a harmonious blend of attraction and mutual admiration that feels effortless. Their aesthetic sensibilities enhance your natural appeal joyfully.",
            "Ascendant Sextile Venus": "You sense a gentle warmth in how they value and support you. This easy rapport allows you both to feel confident in your attractiveness.",
            "Ascendant Square Venus": "You might face tension between your personal style and their tastes, creating minor disagreements over values. Use this to develop a richer appreciation for each other's differences.",

            "Ascendant Conjunction Mars": "You feel invigorated by their presence and notice a strong physical chemistry. Their assertiveness inspires you to stand tall and embrace your desires.",
            "Ascendant Opposition Mars": "You're magnetically drawn into exciting push-and-pull, yet their intensity may sometimes feel overwhelming. Learn to assert your boundaries to keep the spark healthy.",
            "Ascendant Trine Mars": "You enjoy a seamless flow of energy and motivation that lifts you both into action. Their drive amplifies your confidence and adventurous spirit effortlessly.",
            "Ascendant Sextile Mars": "You receive a subtle boost of encouragement from their dynamic energy. This support helps you both assert yourselves with grace and clarity.",
            "Ascendant Square Mars": "You may feel pressured by their forceful energy, sparking conflicts about how you want to present yourself. This challenge invites you to find strength in compromise and self-respect.",

            "Ascendant Conjunction Jupiter": "You feel a joyful expansion and optimism when you're together. Their faith in you helps you embrace new possibilities and grow in confidence.",
            "Ascendant Opposition Jupiter": "You might see them as a mentor figure whose ideals inspire you yet sometimes feel preachy. Aim to absorb their wisdom without feeling judged or overwhelmed.",
            "Ascendant Trine Jupiter": "You experience a natural flow of encouragement and shared vision for growth. Their positivity aligns with your authentic self, making you feel supported.",
            "Ascendant Sextile Jupiter": "You sense a friendly nudge towards broader horizons and self-improvement. This easy rapport fosters mutual growth and discovery.",
            "Ascendant Square Jupiter": "You may feel judged by their high expectations, stirring insecurity about your self-expression. This prompts you to balance your aspirations with healthy self-compassion.",

            "Ascendant Conjunction Saturn": "You feel grounded and taken seriously in their presence, as if your goals matter to them. Their structured guidance can support your maturation but may also feel restrictive at times.",
            "Ascendant Opposition Saturn": "You might experience a teacher-student dynamic where their critique feels heavy. Use this to build resilience and define your authentic boundaries.",
            "Ascendant Trine Saturn": "You find reliable support and practical wisdom flowing between you, helping you both achieve your aims. Their steadiness complements your drive in a balanced partnership.",
            "Ascendant Sextile Saturn": "You receive gentle encouragement to take responsibility and mature gracefully. This aspect fosters mutual respect and steady growth.",
            "Ascendant Square Saturn": "You may feel limited by their cautious nature, clashing with your desire for spontaneous self-expression. Embrace this tension as a chance to refine your focus and discipline.",

            "Ascendant Conjunction Uranus": "You feel thrilled and alive in their company, as they spark your originality. Their unpredictable flair pushes you to break free from old habits creatively.",
            "Ascendant Opposition Uranus": "You're drawn to their excitement yet may be unsettled by their inconsistency. Balancing freedom with stability is key to enjoying this electrifying bond.",
            "Ascendant Trine Uranus": "You experience a natural encouragement to express your true uniqueness together. Their innovative spirit harmonizes with your desire for authenticity without chaos.",
            "Ascendant Sextile Uranus": "You sense a playful invitation to experiment and grow independently. This gentle current of innovation supports your mutual authenticity.",
            "Ascendant Square Uranus": "You may feel disrupted by their sudden changes, challenging your need for a coherent public image. This tension can spark growth if you embrace flexibility.",

            "Ascendant Conjunction Neptune": "You feel a dreamy, soulful connection that elevates your creative side. Yet you should watch for blurred boundaries that might cloud reality.",
            "Ascendant Opposition Neptune": "You're enchanted by their elusive charm, but this may lead to idealization or confusion about their true motives. Keep open communication to stay grounded.",
            "Ascendant Trine Neptune": "You enjoy an inspiring, intuitive rapport that nurtures your imagination. Their subtle empathy complements your authentic presentation beautifully.",
            "Ascendant Sextile Neptune": "You receive a gentle touch of spiritual connection that deepens your mutual understanding. This supportive flow helps you explore creative and emotional depths safely.",
            "Ascendant Square Neptune": "You may feel uncertain or misled by their shifting messages, clashing with your desire for clear self-expression. Embrace honest dialogue to dispel illusions.",

            "Ascendant Conjunction Pluto": "You feel profoundly transformed by their intense presence and power. Their depth helps you confront hidden aspects of yourself, though it may feel overwhelming at times.",
            "Ascendant Opposition Pluto": "You're drawn to their magnetic power yet may resist feeling controlled or manipulated. Navigating this potent pull invites you to claim your personal power consciously.",
            "Ascendant Trine Pluto": "You experience a seamless flow of empowerment and regeneration together. Their transformative energy supports your growth into a more powerful self.",
            "Ascendant Sextile Pluto": "You sense a subtle yet profound invitation to evolve and deepen your self-awareness. This supportive aspect helps you harness inner strength gently.",
            "Ascendant Square Pluto": "You may feel pressured by their intense drive, sparking power struggles about your self-presentation. This challenge encourages you to assert your boundaries and transform your approach.",

            "Ascendant Conjunction Medium Coeli": "You feel your authentic self beautifully enhances their professional image, making you an inspiring partner in their public life. Together you can shine in social or career contexts.",
            "Ascendant Opposition Medium Coeli": "You might sense a tension between who you naturally are and what their ambitions require. Balancing authenticity with professional demands helps you both thrive.",
            "Ascendant Trine Medium Coeli": "You experience a natural synergy between your personal style and their career goals, boosting their reputation and your confidence. This harmonious link supports mutual success.",
            "Ascendant Sextile Medium Coeli": "You have an easy opportunity to align your presentation with their aspirations, enhancing both your images. A little initiative from you can yield significant professional rewards for you both.",
            "Ascendant Square Medium Coeli": "You may feel restricted by their professional expectations, clashing with your genuine self-expression. This friction invites you to innovate ways to honor your authenticity within their career vision.",

            "Ascendant Conjunction Ascendant": "You instantly recognize your shared approach to life and feel a comforting sense of understanding. This alignment makes social and personal interaction flow smoothly.",
            "Ascendant Opposition Ascendant": "You mirror each other's strengths and weaknesses, creating dynamic tension that can spark growth. Embracing these differences can lead you both to deeper self-awareness.",
            "Ascendant Square Ascendant": "You might experience friction in how you instinctively present yourselves, causing misunderstandings. Working through this challenge can teach you respect for each other's pace and style.",
            "Ascendant Trine Ascendant": "You share a natural harmony in how you approach the world, making interactions feel effortless. This ease fosters collaboration and mutual comfort in any setting.",
            "Ascendant Sextile Ascendant": "You enjoy a subtle support in each other's self-expression, finding common ground without overpowering each other. This aspect gently encourages cooperation and mutual respect."
        }

    def get_aspect_interpretation(self, aspect_name):
        return self.aspects.get(aspect_name, "Aspect interpretation not found.")

    def add_aspect(self, aspect_name, interpretation):
        self.aspects[aspect_name] = interpretation

    def remove_aspect(self, aspect_name):
        if aspect_name in self.aspects:
            del self.aspects[aspect_name]
